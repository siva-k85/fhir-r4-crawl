#!/bin/bash
#
# FHIR R4 Pre-Crawl Pipeline Orchestrator
# Version: 1.0
# Date: November 10, 2025
# Author: Symphony Corp
#
# Purpose: Orchestrate complete pre-crawl workflow for FHIR R4 projects
#
# Usage:
#   bash scripts/integrate_pre_crawl.sh andor
#   bash scripts/integrate_pre_crawl.sh whio
#   bash scripts/integrate_pre_crawl.sh both
#   bash scripts/integrate_pre_crawl.sh andor --dry-run --limit 500
#

set -euo pipefail  # Exit on error, undefined vars, pipe failures

# ============================================================================
# CONFIGURATION
# ============================================================================

# Parse arguments
PROJECT="${1:-both}"
DRY_RUN=false
RESUME_FROM=""
LIMIT=0
CONTINUE_ON_ERROR=false

shift || true  # Remove first argument (project)

# Parse flags
for arg in "$@"; do
    case $arg in
        --dry-run)
            DRY_RUN=true
            ;;
        --resume-from=*)
            RESUME_FROM="${arg#*=}"
            ;;
        --limit=*)
            LIMIT="${arg#*=}"
            ;;
        --continue-on-error)
            CONTINUE_ON_ERROR=true
            ;;
    esac
done

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging
LOG_FILE="outputs/pipeline.log"
mkdir -p outputs logs

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1" | tee -a "$LOG_FILE"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$LOG_FILE"
}

log_stage() {
    echo "" | tee -a "$LOG_FILE"
    echo -e "${BLUE}========================================${NC}" | tee -a "$LOG_FILE"
    echo -e "${BLUE}$1${NC}" | tee -a "$LOG_FILE"
    echo -e "${BLUE}========================================${NC}" | tee -a "$LOG_FILE"
}

run_command() {
    local cmd="$1"
    local stage="$2"

    if [[ "$DRY_RUN" == true ]]; then
        echo "[DRY RUN] $cmd"
        return 0
    fi

    log_info "Running: $cmd"
    if eval "$cmd" 2>&1 | tee -a "$LOG_FILE"; then
        log_info "✓ $stage completed successfully"
        return 0
    else
        local exit_code=$?
        log_error "✗ $stage failed with exit code $exit_code"

        if [[ "$CONTINUE_ON_ERROR" == false ]]; then
            log_error "Pipeline stopped. Use --continue-on-error to continue on failures."
            exit $exit_code
        else
            log_warn "Continuing despite error (--continue-on-error enabled)"
            return $exit_code
        fi
    fi
}

should_run_stage() {
    local stage="$1"

    if [[ -z "$RESUME_FROM" ]]; then
        return 0  # Run all stages
    fi

    # Define stage order
    local stages=("setup" "discovery" "validation" "categorization" "filtering" "depth" "cost" "summary")

    # Find indices
    local resume_idx=-1
    local current_idx=-1

    for i in "${!stages[@]}"; do
        if [[ "${stages[$i]}" == "$RESUME_FROM" ]]; then
            resume_idx=$i
        fi
        if [[ "${stages[$i]}" == "$stage" ]]; then
            current_idx=$i
        fi
    done

    # Run if current >= resume
    if [[ $current_idx -ge $resume_idx ]]; then
        return 0
    else
        log_info "Skipping stage '$stage' (resuming from '$RESUME_FROM')"
        return 1
    fi
}

# ============================================================================
# PIPELINE STAGES
# ============================================================================

echo "==================================================================" | tee "$LOG_FILE"
echo "FHIR R4 PRE-CRAWL PIPELINE" | tee -a "$LOG_FILE"
echo "==================================================================" | tee -a "$LOG_FILE"
echo "Project: $PROJECT" | tee -a "$LOG_FILE"
echo "Started: $(date)" | tee -a "$LOG_FILE"
echo "==================================================================" | tee -a "$LOG_FILE"

# Stage 0: Setup
if should_run_stage "setup"; then
    log_stage "[Stage 0/7] Setup and Validation"

    # Create directories
    mkdir -p outputs logs

    # Check Python
    if ! command -v python3 &> /dev/null; then
        log_error "Python 3 not found. Please install Python 3.8+"
        exit 1
    fi

    log_info "Python version: $(python3 --version)"

    # Install dependencies
    log_info "Installing dependencies from requirements.txt..."
    run_command "python3 -m pip install -q -r requirements.txt" "Dependency installation"

    # Verify BM25
    if ! python3 -c "from rank_bm25 import BM25Okapi" 2>/dev/null; then
        log_error "BM25 package not installed correctly"
        exit 1
    fi

    log_info "✓ All dependencies installed"
fi

# Stage 1: Discovery
if should_run_stage "discovery"; then
    log_stage "[Stage 1/7] URL Discovery"

    CMD="python3 scripts/pre_crawl_discovery.py \
        -c 02_CONFIGURATION/configs/url_seeding_config.yml \
        -o outputs/discovered_urls.csv"

    if [[ $LIMIT -gt 0 ]]; then
        CMD="$CMD --limit $LIMIT"
    fi

    run_command "$CMD" "URL Discovery"

    # Check output exists
    if [[ ! -f "outputs/discovered_urls.csv" && "$DRY_RUN" == false ]]; then
        log_error "Discovery output not found: outputs/discovered_urls.csv"
        exit 1
    fi
fi

# Stage 2: Validation
if should_run_stage "validation"; then
    log_stage "[Stage 2/7] URL Validation"

    CMD="python3 scripts/validate_urls.py \
        outputs/discovered_urls.csv \
        -o outputs/validated_urls.csv \
        --report outputs/validation_report.md \
        --strict-r4"

    run_command "$CMD" "URL Validation"

    # Check output exists
    if [[ ! -f "outputs/validated_urls.csv" && "$DRY_RUN" == false ]]; then
        log_error "Validation output not found: outputs/validated_urls.csv"
        exit 1
    fi
fi

# Stage 3: Categorization
if should_run_stage "categorization"; then
    log_stage "[Stage 3/7] URL Categorization"

    CMD="python3 scripts/url_categorizer.py \
        --input outputs/validated_urls.csv \
        --output outputs/categorized_urls.csv \
        --format csv \
        --stats"

    run_command "$CMD" "URL Categorization"

    # Check output exists
    if [[ ! -f "outputs/categorized_urls.csv" && "$DRY_RUN" == false ]]; then
        log_error "Categorization output not found: outputs/categorized_urls.csv"
        exit 1
    fi
fi

# Stage 4: Project Filtering
if should_run_stage "filtering"; then
    log_stage "[Stage 4/7] Project Filtering"

    # Determine which projects to filter
    PROJECTS=()
    if [[ "$PROJECT" == "both" ]]; then
        PROJECTS=("andor" "whio")
    else
        PROJECTS=("$PROJECT")
    fi

    # Filter each project
    for proj in "${PROJECTS[@]}"; do
        log_info "Filtering project: $proj"

        CMD="python3 scripts/project_filter.py \
            outputs/categorized_urls.csv \
            -c 02_CONFIGURATION/configs/${proj}_crawl_config.yml \
            -o outputs/${proj}_filtered_urls.csv \
            --stats \
            --json outputs/${proj}_filter_report.json"

        run_command "$CMD" "Project Filtering ($proj)"

        # Check output exists
        if [[ ! -f "outputs/${proj}_filtered_urls.csv" && "$DRY_RUN" == false ]]; then
            log_error "Filter output not found: outputs/${proj}_filtered_urls.csv"
            exit 1
        fi
    done
fi

# Stage 5: Depth Optimization
if should_run_stage "depth"; then
    log_stage "[Stage 5/7] Depth Optimization"

    # Determine which projects to optimize
    PROJECTS=()
    if [[ "$PROJECT" == "both" ]]; then
        PROJECTS=("andor" "whio")
    else
        PROJECTS=("$PROJECT")
    fi

    # Optimize each project
    for proj in "${PROJECTS[@]}"; do
        log_info "Optimizing depths for: $proj"

        CMD="python3 scripts/depth_optimizer.py \
            outputs/${proj}_filtered_urls.csv \
            -c 02_CONFIGURATION/configs/${proj}_crawl_config.yml \
            -o outputs/${proj}_urls_with_depth.csv \
            --stats"

        run_command "$CMD" "Depth Optimization ($proj)"

        # Check output exists
        if [[ ! -f "outputs/${proj}_urls_with_depth.csv" && "$DRY_RUN" == false ]]; then
            log_error "Depth output not found: outputs/${proj}_urls_with_depth.csv"
            exit 1
        fi
    done
fi

# Stage 6: Cost Estimation
if should_run_stage "cost"; then
    log_stage "[Stage 6/7] Cost Estimation"

    # Determine which projects to estimate
    PROJECTS=()
    if [[ "$PROJECT" == "both" ]]; then
        PROJECTS=("andor" "whio")
    else
        PROJECTS=("$PROJECT")
    fi

    # Estimate each project
    for proj in "${PROJECTS[@]}"; do
        log_info "Estimating costs for: $proj"

        CMD="python3 scripts/cost_estimator.py \
            outputs/${proj}_urls_with_depth.csv \
            -o outputs/${proj}_cost_estimate.json \
            --report outputs/${proj}_cost_estimate.md"

        run_command "$CMD" "Cost Estimation ($proj)"

        # Check output exists
        if [[ ! -f "outputs/${proj}_cost_estimate.json" && "$DRY_RUN" == false ]]; then
            log_error "Cost output not found: outputs/${proj}_cost_estimate.json"
            exit 1
        fi
    done
fi

# Stage 7: Summary Report
if should_run_stage "summary"; then
    log_stage "[Stage 7/7] Summary Report Generation"

    SUMMARY_FILE="outputs/pre_crawl_summary.md"

    if [[ "$DRY_RUN" == false ]]; then
        cat > "$SUMMARY_FILE" <<EOF
# FHIR R4 Pre-Crawl Pipeline Summary

**Generated**: $(date)

## Pipeline Configuration
- **Projects**: $PROJECT
- **Discovery Limit**: ${LIMIT:-unlimited}
- **Resume From**: ${RESUME_FROM:-none}

## Results

EOF

        # Add project-specific summaries
        if [[ "$PROJECT" == "both" || "$PROJECT" == "andor" ]]; then
            if [[ -f "outputs/andor_urls_with_depth.csv" ]]; then
                ANDOR_COUNT=$(wc -l < outputs/andor_urls_with_depth.csv | tr -d ' ')
                ANDOR_COUNT=$((ANDOR_COUNT - 1))  # Subtract header

                cat >> "$SUMMARY_FILE" <<EOF
### Andor Health System (Provider)
- **Final URL Count**: $ANDOR_COUNT
- **Cost Estimate**: [outputs/andor_cost_estimate.json](outputs/andor_cost_estimate.json)
- **Depth Distribution**: [outputs/andor_urls_with_depth.csv](outputs/andor_urls_with_depth.csv)
- **Filter Report**: [outputs/andor_filter_report.json](outputs/andor_filter_report.json)

EOF
            fi
        fi

        if [[ "$PROJECT" == "both" || "$PROJECT" == "whio" ]]; then
            if [[ -f "outputs/whio_urls_with_depth.csv" ]]; then
                WHIO_COUNT=$(wc -l < outputs/whio_urls_with_depth.csv | tr -d ' ')
                WHIO_COUNT=$((WHIO_COUNT - 1))  # Subtract header

                cat >> "$SUMMARY_FILE" <<EOF
### WHIO APCD (Payer)
- **Final URL Count**: $WHIO_COUNT
- **Cost Estimate**: [outputs/whio_cost_estimate.json](outputs/whio_cost_estimate.json)
- **Depth Distribution**: [outputs/whio_urls_with_depth.csv](outputs/whio_urls_with_depth.csv)
- **Filter Report**: [outputs/whio_filter_report.json](outputs/whio_filter_report.json)

EOF
            fi
        fi

        cat >> "$SUMMARY_FILE" <<EOF
## Output Files

### Discovery Phase
- [outputs/discovered_urls.csv](outputs/discovered_urls.csv) - All discovered URLs
- [outputs/validated_urls.csv](outputs/validated_urls.csv) - Validated R4-only URLs
- [outputs/validation_report.md](outputs/validation_report.md) - Validation report

### Categorization Phase
- [outputs/categorized_urls.csv](outputs/categorized_urls.csv) - Categorized by FHIR taxonomy

### Project-Specific Outputs
- [outputs/{project}_filtered_urls.csv](outputs/) - Filtered URLs per project
- [outputs/{project}_urls_with_depth.csv](outputs/) - URLs with assigned depths
- [outputs/{project}_cost_estimate.json](outputs/) - Cost estimates (JSON)
- [outputs/{project}_cost_estimate.md](outputs/) - Cost estimates (Markdown)
- [outputs/{project}_filter_report.json](outputs/) - Filter statistics (JSON)

### Logs
- [outputs/pipeline.log](outputs/pipeline.log) - Complete pipeline log

## Commands to Reproduce

\`\`\`bash
# Full pipeline
bash scripts/integrate_pre_crawl.sh $PROJECT

# With options
bash scripts/integrate_pre_crawl.sh $PROJECT --limit ${LIMIT:-500} --resume-from filtering
\`\`\`

---
*Pipeline completed: $(date)*
EOF

        log_info "Summary report written to $SUMMARY_FILE"
    fi
fi

# ============================================================================
# COMPLETION
# ============================================================================

echo "" | tee -a "$LOG_FILE"
echo "==================================================================" | tee -a "$LOG_FILE"
echo -e "${GREEN}✓ PIPELINE COMPLETE${NC}" | tee -a "$LOG_FILE"
echo "==================================================================" | tee -a "$LOG_FILE"
echo "Project: $PROJECT" | tee -a "$LOG_FILE"
echo "Completed: $(date)" | tee -a "$LOG_FILE"
echo "Summary: outputs/pre_crawl_summary.md" | tee -a "$LOG_FILE"
echo "Log: outputs/pipeline.log" | tee -a "$LOG_FILE"
echo "==================================================================" | tee -a "$LOG_FILE"

exit 0
