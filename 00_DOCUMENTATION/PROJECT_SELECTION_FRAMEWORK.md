# FHIR R4 Project Selection Framework

**Version**: 1.0
**Date**: November 8, 2025
**Author**: Symphony Corp
**Purpose**: Guide for selecting and filtering FHIR R4 URLs for specific healthcare projects

---

## Executive Summary

This framework provides a systematic approach to selecting FHIR R4 documentation URLs for different healthcare projects. It includes detailed configurations for two reference projects (Andor Health System and WHIO APCD) and templates for custom projects. The framework ensures that each project gets precisely the documentation it needs while minimizing unnecessary crawling costs.

---

## Table of Contents

1. [Project Analysis Template](#project-analysis-template)
2. [Andor Health System (Provider-Focused)](#andor-health-system-provider-focused)
3. [WHIO APCD (Payer-Focused)](#whio-apcd-payer-focused)
4. [Custom Project Configuration](#custom-project-configuration)
5. [Query Design for BM25 Scoring](#query-design-for-bm25-scoring)
6. [Filtering Pattern Strategies](#filtering-pattern-strategies)
7. [Validation Checklist](#validation-checklist)
8. [Common Project Types](#common-project-types)

---

## Project Analysis Template

Before configuring URL selection for any project, complete this analysis:

### 1. Project Scope Definition

```yaml
project_analysis:
  name: "Project Name"
  type: "provider|payer|hybrid|research|vendor"
  focus: "Primary business domain"

  stakeholders:
    primary: "Who will use this documentation"
    secondary: "Who else needs access"

  use_cases:
    - "Primary use case 1"
    - "Primary use case 2"
    - "Secondary use case"

  timeline:
    start: "YYYY-MM-DD"
    go_live: "YYYY-MM-DD"
    documentation_needed_by: "YYYY-MM-DD"
```

### 2. Resource Requirements

```yaml
required_resources:
  # Core business objects
  essential:
    - Patient
    - Organization
    - Practitioner

  # Supporting resources
  important:
    - Location
    - Encounter

  # Nice to have
  optional:
    - Schedule
    - Slot
```

### 3. Implementation Guide Dependencies

```yaml
implementation_guides:
  required:
    - name: "US Core"
      version: "6.1.0"
      reason: "Baseline US requirements"

  recommended:
    - name: "QI-Core"
      version: "6.0.0"
      reason: "Quality reporting"
```

### 4. Technical Requirements

```yaml
technical_requirements:
  apis:
    - "RESTful FHIR"
    - "Bulk Data Export"
    - "SMART on FHIR"

  operations:
    - "$export"
    - "$everything"
    - "$validate"

  search_parameters:
    - "_id"
    - "_lastUpdated"
    - "patient"
```

---

## Andor Health System (Provider-Focused)

### Project Overview

**Name**: Andor Health System
**Type**: Provider/Clinical
**Focus**: EHR integration with Epic for clinical data exchange

### Business Context

Andor Health System is implementing a comprehensive clinical data platform that needs to:
- Exchange patient data with Epic EHR systems
- Support quality measure reporting
- Enable bulk data exports for analytics
- Provide real-time clinical decision support

### Resource Selection

#### Essential Resources (Must Have)

```yaml
clinical_resources:
  demographics:
    - Patient
    - Practitioner
    - PractitionerRole
    - Organization
    - Location

  encounters:
    - Encounter
    - EpisodeOfCare
    - Account

  clinical_data:
    - Observation
    - Condition
    - Procedure
    - DiagnosticReport
    - DocumentReference

  medications:
    - Medication
    - MedicationRequest
    - MedicationDispense
    - MedicationAdministration
    - MedicationStatement

  care_coordination:
    - CarePlan
    - CareTeam
    - Goal
    - ReferralRequest
```

#### Quality Reporting Resources

```yaml
quality_resources:
  - Measure
  - MeasureReport
  - Library
  - GuidanceResponse
```

#### Supporting Resources

```yaml
supporting_resources:
  scheduling:
    - Schedule
    - Slot
    - Appointment
    - AppointmentResponse

  clinical_reasoning:
    - PlanDefinition
    - ActivityDefinition
    - RequestGroup

  terminology:
    - CodeSystem
    - ValueSet
    - ConceptMap
    - NamingSystem
```

### Implementation Guides

```yaml
andor_implementation_guides:
  us_core:
    url: "http://hl7.org/fhir/us/core/STU6.1/"
    version: "6.1.0"
    priority: "required"
    resources:
      - US Core Patient Profile
      - US Core Practitioner Profile
      - US Core Organization Profile
      - US Core Encounter Profile
      - US Core Observation Profiles

  qi_core:
    url: "http://hl7.org/fhir/us/qicore/STU6/"
    version: "6.0.0"
    priority: "required"
    purpose: "Quality measurement and reporting"

  davinci_deqm:
    url: "https://build.fhir.org/ig/HL7/davinci-deqm/STU3/"
    version: "3.1.0"
    priority: "recommended"
    purpose: "Data exchange for quality measures"

  davinci_atr:
    url: "http://hl7.org/fhir/us/davinci-atr/STU1/"
    version: "1.0.0"
    priority: "optional"
    purpose: "Patient attribution"

  bulk_fhir:
    url: "https://hl7.org/fhir/uv/bulkdata/STU2/"
    version: "2.0.0"
    priority: "required"
    purpose: "Bulk data export for analytics"
```

### BM25 Query Configuration

```python
ANDOR_BM25_QUERIES = [
    # Clinical focus
    "patient practitioner organization encounter observation condition procedure",
    "diagnostic report medication request administration clinical data",

    # Quality reporting
    "quality measure reporting measurereport library qi-core",
    "clinical quality measures CQM performance",

    # US Core specific
    "US Core implementation guide profiles extensions",
    "US Core patient practitioner organization vital signs",

    # Bulk operations
    "bulk data export operation async pattern group export",
    "$export operation bulk fhir ndjson",

    # Care coordination
    "care plan care team coordination referral",
    "episode of care clinical pathways"
]
```

### URL Filtering Patterns

```yaml
andor_url_patterns:
  include:
    # Core R4 resources
    - "*/fhir/R4/patient*.html"
    - "*/fhir/R4/practitioner*.html"
    - "*/fhir/R4/organization*.html"
    - "*/fhir/R4/observation*.html"
    - "*/fhir/R4/condition*.html"
    - "*/fhir/R4/procedure*.html"
    - "*/fhir/R4/medication*.html"
    - "*/fhir/R4/diagnosticreport*.html"
    - "*/fhir/R4/encounter*.html"

    # Modules
    - "*/fhir/R4/clinical-module.html"
    - "*/fhir/R4/diagnostics-module.html"
    - "*/fhir/R4/medications-module.html"
    - "*/fhir/R4/workflow-module.html"

    # Implementation guides
    - "*/fhir/us/core/*"
    - "*/fhir/us/qicore/*"
    - "*/davinci-deqm/*"
    - "*/bulkdata/*"

    # Operations
    - "*/fhir/R4/operation*.html"
    - "*/fhir/R4/operations.html"

  exclude:
    # Non-relevant domains
    - "*/fhir/R4/claim*.html"
    - "*/fhir/R4/coverage*.html"
    - "*/fhir/R4/explanationofbenefit*.html"

    # Version-specific exclusions
    - "*/fhir/R5/*"
    - "*/fhir/R4B/*"
    - "*ballot*"
    - "*snapshot*"

    # Low-value content
    - "*-questionnaire.html"
    - "*-spreadsheet.xml"
    - "*.xsd"
    - "*.sch"
```

### Expected URL Distribution

```yaml
andor_expected_urls:
  total: 400-600
  breakdown:
    resources: 180-220
    modules: 40-50
    implementation_guides: 80-120
    valuesets: 80-100
    operations: 20-30
    examples: 20-40  # Selective
```

---

## WHIO APCD (Payer-Focused)

### Project Overview

**Name**: WHIO All-Payer Claims Database
**Type**: Payer/Financial
**Focus**: Claims processing and member management similar to Blue Button

### Business Context

WHIO APCD is implementing an all-payer claims database that needs to:
- Process claims from multiple payers
- Generate Explanations of Benefits
- Manage member coverage and eligibility
- Support CARIN Blue Button requirements
- Enable data sharing with CMS

### Resource Selection

#### Essential Resources (Must Have)

```yaml
payer_resources:
  member_management:
    - Patient
    - RelatedPerson
    - Person
    - Group

  coverage:
    - Coverage
    - CoverageEligibilityRequest
    - CoverageEligibilityResponse
    - EnrollmentRequest
    - EnrollmentResponse

  claims:
    - Claim
    - ClaimResponse
    - ExplanationOfBenefit

  financial:
    - PaymentNotice
    - PaymentReconciliation
    - Invoice
    - Account

  provider:
    - Organization
    - Practitioner
    - PractitionerRole
    - OrganizationAffiliation
```

#### Supporting Resources

```yaml
payer_supporting:
  contracts:
    - Contract
    - InsurancePlan

  risk:
    - RiskAssessment
    - DetectedIssue

  communication:
    - Communication
    - CommunicationRequest

  documents:
    - DocumentReference
    - DocumentManifest
```

### Implementation Guides

```yaml
whio_implementation_guides:
  carin_bb:
    url: "http://hl7.org/fhir/us/carin-bb/"
    priority: "required"
    purpose: "Blue Button 2.0 implementation"
    profiles:
      - CARIN BB Patient Profile
      - CARIN BB Coverage Profile
      - CARIN BB ExplanationOfBenefit Profile

  davinci_pdex:
    url: "http://hl7.org/fhir/us/davinci-pdex/"
    priority: "recommended"
    purpose: "Payer data exchange"

  davinci_pas:
    url: "http://hl7.org/fhir/us/davinci-pas/"
    priority: "optional"
    purpose: "Prior authorization"

  davinci_crd:
    url: "http://hl7.org/fhir/us/davinci-crd/"
    priority: "optional"
    purpose: "Coverage requirements discovery"
```

### BM25 Query Configuration

```python
WHIO_BM25_QUERIES = [
    # Payer focus
    "coverage claim explanation of benefit payer insurance",
    "claim response adjudication payment financial",

    # Member management
    "patient member beneficiary enrollment eligibility",
    "coverage eligibility request response subscriber",

    # Blue Button specific
    "CARIN Blue Button consumer directed exchange",
    "patient access API member portal",

    # All-payer database
    "all-payer claims database APCD reporting",
    "claims aggregation analytics population health",

    # Financial operations
    "payment reconciliation invoice billing",
    "prior authorization coverage determination"
]
```

### URL Filtering Patterns

```yaml
whio_url_patterns:
  include:
    # Core payer resources
    - "*/fhir/R4/coverage*.html"
    - "*/fhir/R4/explanationofbenefit*.html"
    - "*/fhir/R4/claim*.html"
    - "*/fhir/R4/patient*.html"
    - "*/fhir/R4/organization*.html"

    # Financial module
    - "*/fhir/R4/financial-module.html"
    - "*/fhir/R4/administration-module.html"

    # CARIN specific
    - "*/carin*"
    - "*/blue-button*"

    # DaVinci IGs
    - "*/davinci-pdex/*"
    - "*/davinci-pas/*"

  exclude:
    # Clinical resources (not primary focus)
    - "*/fhir/R4/observation*.html"
    - "*/fhir/R4/procedure*.html"
    - "*/fhir/R4/medication*.html"
    - "*/fhir/R4/diagnosticreport*.html"

    # Clinical modules
    - "*/fhir/R4/clinical-module.html"
    - "*/fhir/R4/diagnostics-module.html"
    - "*/fhir/R4/medications-module.html"
```

### Expected URL Distribution

```yaml
whio_expected_urls:
  total: 200-350
  breakdown:
    resources: 120-150
    modules: 20-30
    implementation_guides: 40-60
    valuesets: 40-60
    operations: 10-20
    examples: 10-20  # Minimal
```

---

## Custom Project Configuration

### Template Structure

```yaml
# configs/custom_project.yml
project:
  name: "Your Project Name"
  type: "provider|payer|hybrid|research|vendor"
  focus: "Specific domain focus"
  description: "Detailed project description"

# Resources to prioritize
required_resources:
  - Resource1
  - Resource2

preferred_resources:
  - Resource3
  - Resource4

# Implementation guides needed
implementation_guides:
  - name: "IG Name"
    url_pattern: "*pattern*"
    priority: "required|recommended|optional"

# BM25 scoring queries
bm25_queries:
  - "query 1 with relevant terms"
  - "query 2 with domain keywords"
  - "query 3 with resource names"

# URL filtering patterns
filter_patterns:
  include:
    - "*/positive/pattern/*"
  exclude:
    - "*/negative/pattern/*"

# Scoring configuration
scoring:
  score_threshold: 0.3  # Minimum score to include
  category_weights:
    resource: 1.0
    module: 0.8
    implementation: 0.9
    valueset: 0.6
    example: 0.4

# Depth assignment
depth_strategy:
  resource: 0
  module: 1
  implementation: 1
  valueset: 1
  example: 2

# URL limits
max_urls:
  total: 500
  per_category:
    resource: 200
    module: 50
    implementation: 100
    valueset: 100
    example: 50
```

### Project Type Templates

#### Research Project

```yaml
project:
  name: "Clinical Research Platform"
  type: "research"
  focus: "Clinical trials and research data"

required_resources:
  - ResearchStudy
  - ResearchSubject
  - Consent
  - Observation
  - Patient

bm25_queries:
  - "research study clinical trial protocol"
  - "consent research subject enrollment"
  - "observation measurement outcome"
```

#### Laboratory Integration

```yaml
project:
  name: "Laboratory System Integration"
  type: "provider"
  focus: "Lab orders and results"

required_resources:
  - ServiceRequest
  - DiagnosticReport
  - Observation
  - Specimen
  - Task

bm25_queries:
  - "laboratory diagnostic report specimen"
  - "service request lab order result"
  - "observation component reference range"
```

#### Pharmacy System

```yaml
project:
  name: "Pharmacy Management System"
  type: "provider"
  focus: "Medication dispensing and management"

required_resources:
  - Medication
  - MedicationRequest
  - MedicationDispense
  - MedicationAdministration
  - MedicationStatement

bm25_queries:
  - "medication prescription dispensing pharmacy"
  - "medication request dosage administration"
  - "drug interaction allergy contraindication"
```

---

## Query Design for BM25 Scoring

### Effective Query Principles

#### 1. Use Domain Terminology

```python
# Good: Uses specific FHIR terminology
queries = [
    "patient demographics administrative resource",
    "observation vital signs measurement clinical"
]

# Poor: Too generic
queries = [
    "data information system",
    "medical records health"
]
```

#### 2. Include Resource Names

```python
# Include exact resource names
queries = [
    "Patient Practitioner Organization Location",
    "Coverage ExplanationOfBenefit Claim ClaimResponse"
]
```

#### 3. Layer Specificity

```python
# Layer from general to specific
queries = [
    # General domain
    "healthcare clinical data exchange",

    # Specific resources
    "patient encounter observation procedure",

    # Implementation details
    "US Core profile extension search parameter",

    # Technical specifics
    "RESTful API bundle transaction operation"
]
```

#### 4. Include Synonyms

```python
# Include common synonyms and abbreviations
queries = [
    "explanation of benefit EOB claim adjudication",
    "practitioner provider physician clinician doctor",
    "medication drug prescription pharmaceutical"
]
```

### Query Optimization Strategies

#### Test Query Effectiveness

```python
def test_query_effectiveness(query: str, sample_urls: List[dict]) -> float:
    """
    Test how well a query matches intended URLs
    """
    from rank_bm25 import BM25Okapi

    # Create corpus from URL metadata
    corpus = [f"{url['title']} {url['description']}" for url in sample_urls]
    tokenized_corpus = [doc.lower().split() for doc in corpus]

    # Initialize BM25
    bm25 = BM25Okapi(tokenized_corpus)

    # Score query
    query_tokens = query.lower().split()
    scores = bm25.get_scores(query_tokens)

    # Calculate effectiveness metrics
    avg_score = np.mean(scores)
    max_score = np.max(scores)
    above_threshold = sum(1 for s in scores if s > 0.3)

    return {
        'average_score': avg_score,
        'max_score': max_score,
        'matches_above_0.3': above_threshold,
        'effectiveness': above_threshold / len(sample_urls)
    }
```

#### Iterative Refinement

```python
# Start with base query
base_query = "patient clinical data"

# Test and refine
refinements = [
    "patient clinical data observation",  # Add specific resource
    "patient clinical data observation vital signs",  # Add domain term
    "patient clinical data US Core observation vital signs"  # Add IG
]

# Test each refinement
for query in refinements:
    effectiveness = test_query_effectiveness(query, sample_urls)
    print(f"Query: {query}")
    print(f"Effectiveness: {effectiveness['effectiveness']:.2%}")
```

---

## Filtering Pattern Strategies

### Pattern Design Principles

#### 1. Start Broad, Then Narrow

```yaml
patterns:
  # Level 1: Broad category
  - "*/fhir/R4/*"

  # Level 2: Specific resources
  - "*/fhir/R4/patient*.html"

  # Level 3: Specific pages
  - "*/fhir/R4/patient-examples.html"
```

#### 2. Use Wildcards Effectively

```yaml
patterns:
  # Match any patient-related page
  - "*patient*"

  # Match patient resource specifically
  - "*/patient.html"

  # Match patient profiles
  - "*-patient-*.html"
```

#### 3. Combine Inclusion and Exclusion

```yaml
filter_patterns:
  # Include clinical resources
  include:
    - "*/fhir/R4/observation*.html"
    - "*/fhir/R4/condition*.html"

  # But exclude examples unless high score
  exclude:
    - "*-example*.html"  # Excluded unless score > 0.8
```

### Common Pattern Templates

#### Resource-Specific Patterns

```yaml
# Patient-related
patient_patterns:
  - "*/patient.html"           # Main resource
  - "*/patient-*.html"          # Profiles and extensions
  - "*-patient-*.html"          # IG-specific profiles
  - "*/StructureDefinition-*patient*.html"  # Formal definitions

# Observation-related
observation_patterns:
  - "*/observation.html"
  - "*/observation-*.html"
  - "*/vitalsigns.html"         # Specific profile
  - "*/observation-profiles.html"
```

#### Module Patterns

```yaml
module_patterns:
  clinical:
    - "*clinical-module*.html"
    - "*clinical-*.html"

  financial:
    - "*financial-module*.html"
    - "*billing*.html"
    - "*payment*.html"

  administrative:
    - "*administration-module*.html"
    - "*scheduling*.html"
    - "*workflow*.html"
```

#### Implementation Guide Patterns

```yaml
ig_patterns:
  us_core:
    - "*/us/core/*"
    - "*us-core-*.html"
    - "*/StructureDefinition-us-core-*.html"

  carin:
    - "*/carin/*"
    - "*carin-bb-*.html"
    - "*blue-button*.html"

  davinci:
    - "*/davinci-*/*"
    - "*davinci-*.html"
```

---

## Validation Checklist

### Pre-Selection Validation

- [ ] **Project scope clearly defined**
  - [ ] Stakeholders identified
  - [ ] Use cases documented
  - [ ] Timeline established

- [ ] **Resources identified**
  - [ ] Essential resources listed
  - [ ] Supporting resources considered
  - [ ] Dependencies mapped

- [ ] **Implementation guides selected**
  - [ ] Required IGs identified
  - [ ] Versions specified
  - [ ] Compatibility verified

### Configuration Validation

- [ ] **BM25 queries tested**
  - [ ] Queries match intended resources
  - [ ] Effectiveness score > 0.5
  - [ ] No redundant queries

- [ ] **Patterns validated**
  - [ ] Include patterns tested
  - [ ] Exclude patterns reviewed
  - [ ] No conflicting patterns

- [ ] **Thresholds appropriate**
  - [ ] Score threshold tested (0.3-0.5 typical)
  - [ ] Category weights sum to reasonable total
  - [ ] URL limits realistic

### Post-Selection Validation

- [ ] **URL distribution reviewed**
  - [ ] Total URLs within expected range
  - [ ] Category breakdown reasonable
  - [ ] High-priority resources included

- [ ] **Coverage complete**
  - [ ] All required resources present
  - [ ] Implementation guides covered
  - [ ] No critical gaps

- [ ] **Cost estimates acceptable**
  - [ ] Time estimate reasonable
  - [ ] Token usage within budget
  - [ ] ROI justifiable

### Quality Assurance

- [ ] **Sample review completed**
  - [ ] Random sample of 20 URLs reviewed
  - [ ] Relevance confirmed
  - [ ] False positives < 10%

- [ ] **Comparison performed**
  - [ ] Compared with manual selection
  - [ ] Differences analyzed
  - [ ] Improvements identified

---

## Common Project Types

### Quick Reference Configuration

| Project Type | Focus | Key Resources | Typical URLs | Depth Strategy |
|-------------|-------|---------------|--------------|----------------|
| **Provider EHR** | Clinical data | Patient, Observation, Medication | 400-600 | 0-1 for resources |
| **Payer System** | Claims/coverage | Coverage, EOB, Claim | 200-350 | 0 for most |
| **Laboratory** | Diagnostics | ServiceRequest, DiagnosticReport | 150-250 | 0-1 selective |
| **Pharmacy** | Medications | Medication*, Immunization | 100-200 | 0-1 for resources |
| **Quality Reporting** | Measures | Measure, MeasureReport | 100-150 | 1 for most |
| **Research Platform** | Studies | ResearchStudy, Consent | 150-200 | 0-1 selective |
| **Public Health** | Population | Immunization, Observation | 200-300 | 0-1 for resources |
| **Dental** | Dental claims | Claim, Patient, Practitioner | 100-150 | 0 for most |

### Recommended Configurations by Use Case

#### Startup/MVP

```yaml
# Minimal viable configuration
project:
  name: "MVP Healthcare Platform"

max_urls:
  total: 100-150

focus_on:
  - Core resources only
  - Skip examples
  - Depth 0 for all
```

#### Enterprise Integration

```yaml
# Comprehensive enterprise configuration
project:
  name: "Enterprise Health System"

max_urls:
  total: 800-1200

focus_on:
  - All relevant resources
  - Multiple IGs
  - Depth 0-2 based on scoring
```

#### Specialty System

```yaml
# Focused specialty configuration
project:
  name: "Cardiology Practice System"

max_urls:
  total: 200-300

focus_on:
  - Specific clinical resources
  - Relevant observations
  - Depth 0-1 selective
```

---

## Appendix: Configuration Examples

### Minimal Configuration

```yaml
# configs/minimal.yml
project:
  name: "Basic FHIR Implementation"

required_resources:
  - Patient
  - Observation

bm25_queries:
  - "patient observation basic fhir"

score_threshold: 0.5
max_urls:
  total: 50
```

### Comprehensive Configuration

See full examples in:
- `configs/andor_crawl_config.yml` - Provider-focused
- `configs/whio_crawl_config.yml` - Payer-focused
- `configs/research_crawl_config.yml` - Research-focused
- `configs/laboratory_crawl_config.yml` - Lab-focused

---

**Document Version**: 1.0
**Last Updated**: November 8, 2025
**Next Review**: February 8, 2026

---

*For implementation details, see PRE_CRAWL_METHODOLOGY.md*
*For usage instructions, see URL_DISCOVERY_GUIDE.md*