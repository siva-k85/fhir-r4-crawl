#!/usr/bin/env python3
"""
Create shortlist of payer-focused FHIR R4 pages
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils import ensure_directory, write_file_lines

# Payer-focused FHIR R4 pages
SHORTLIST_URLS = [
    # Core Resources
    "https://hl7.org/fhir/R4/patient.html",
    "https://hl7.org/fhir/R4/coverage.html",
    "https://hl7.org/fhir/R4/explanationofbenefit.html",

    # Search & Query
    "https://hl7.org/fhir/R4/search.html",
    "https://hl7.org/fhir/R4/searchparameter.html",

    # Data Types & Structure
    "https://hl7.org/fhir/R4/datatypes.html",
    "https://hl7.org/fhir/R4/structuredefinition.html",

    # Terminologies
    "https://hl7.org/fhir/R4/terminologies.html",
    "https://hl7.org/fhir/R4/codesystem.html",
    "https://hl7.org/fhir/R4/valueset.html",
]

RATIONALE_TEXT = """# FHIR R4 Shortlist Rationale

This document explains why each page was selected for the payer-focused FHIR R4 demo.

## Selection Criteria

- **Relevance**: Core to payer operations (claims, coverage, member demographics)
- **Dependencies**: Shared components needed to understand core resources
- **Completeness**: Sufficient context for LLM-based analysis

---

## Core Resources (Payer-Specific)

### 1. Patient
**URL**: https://hl7.org/fhir/R4/patient.html

**Rationale**: Essential for member demographics and identity management. Payers need to:
- Track member enrollment and eligibility
- Link claims to covered individuals
- Manage family relationships for dependent coverage

### 2. Coverage
**URL**: https://hl7.org/fhir/R4/coverage.html

**Rationale**: Represents insurance coverage details including:
- Plan information and benefits
- Subscriber and beneficiary relationships
- Coverage periods and status
- Cost-sharing parameters (deductibles, copays)

### 3. ExplanationOfBenefit
**URL**: https://hl7.org/fhir/R4/explanationofbenefit.html

**Rationale**: Core payer resource representing adjudicated claims:
- Claim details and line items
- Adjudication outcomes (paid, denied, pending)
- Patient financial responsibility
- Provider payments

---

## Search & Query Capabilities

### 4. Search
**URL**: https://hl7.org/fhir/R4/search.html

**Rationale**: Understanding search is critical for:
- Querying patients by ID, name, or date of birth
- Finding coverage by member or plan
- Retrieving claims by patient or date range

### 5. SearchParameter
**URL**: https://hl7.org/fhir/R4/searchparameter.html

**Rationale**: Defines available search parameters for each resource type, enabling:
- Custom search criteria
- Composite searches across multiple fields
- Pagination and result limiting

---

## Data Structure & Types

### 6. DataTypes
**URL**: https://hl7.org/fhir/R4/datatypes.html

**Rationale**: Foundational for understanding:
- How dates, identifiers, and codes are structured
- Address and contact information formats
- Money and quantity representations (critical for claims)

### 7. StructureDefinition
**URL**: https://hl7.org/fhir/R4/structuredefinition.html

**Rationale**: Metadata describing resource structures:
- Element definitions and cardinality
- Data type constraints
- Extensions and profiles (US Core, CARIN)

---

## Terminologies & Value Sets

### 8. Terminologies
**URL**: https://hl7.org/fhir/R4/terminologies.html

**Rationale**: Overview of terminology usage in FHIR:
- How codes and value sets work
- Standard terminologies (SNOMED, LOINC, RxNorm)
- Importance for interoperability

### 9. CodeSystem
**URL**: https://hl7.org/fhir/R4/codesystem.html

**Rationale**: Defines code systems used in payer workflows:
- Diagnosis codes (ICD-10)
- Procedure codes (CPT, HCPCS)
- Administrative codes (claim status, coverage type)

### 10. ValueSet
**URL**: https://hl7.org/fhir/R4/valueset.html

**Rationale**: Collections of codes for specific use cases:
- Coverage types (HMO, PPO, Medicare)
- Claim statuses (active, cancelled, entered-in-error)
- Payment statuses (paid, denied, pending)

---

## Exclusions

The following were deliberately excluded:

- **Other FHIR versions** (R5, R4B, R3, R2): Focus only on R4
- **Provider-focused resources**: Practitioner, Organization, Location
- **Clinical resources**: Observation, Condition, Procedure (not primary payer use cases)
- **Implementation guides**: Too specific; focus on base specification
- **Binary downloads**: No .zip, .tgz files
- **Ballot versions**: Only published R4

---

## Use Case: Dr. Smith's LLM-Powered Demo

This shortlist supports a payer demo where an LLM:

1. **Understands** Patient, Coverage, and EOB resources
2. **Queries** data using search parameters
3. **Interprets** codes and terminologies
4. **Parses** data types and structures correctly

All extracted markdown will be LLM-ready for training or RAG systems.
"""


def main():
    """Create shortlist and rationale"""
    print("═══════════════════════════════════════════════")
    print("  Step 3: Shortlist Creation")
    print("═══════════════════════════════════════════════")
    print("")

    # Ensure directory exists
    ensure_directory("shortlist")

    # Write URLs
    print(f"→ Writing {len(SHORTLIST_URLS)} URLs to shortlist/urls.txt...")
    write_file_lines("shortlist/urls.txt", SHORTLIST_URLS)
    print("  ✓ URLs written")

    # Write rationale
    print("→ Writing rationale to shortlist/rationale.md...")
    with open("shortlist/rationale.md", "w", encoding="utf-8") as f:
        f.write(RATIONALE_TEXT)
    print("  ✓ Rationale written")

    print("")
    print("═══════════════════════════════════════════════")
    print("  ✅ Shortlist created!")
    print("═══════════════════════════════════════════════")
    print("")
    print("Generated files:")
    print("  • shortlist/urls.txt (10 URLs)")
    print("  • shortlist/rationale.md (selection criteria)")
    print("")
    print("Next step:")
    print("  python scripts/04_extract_markdown.py")
    print("")


if __name__ == "__main__":
    main()
