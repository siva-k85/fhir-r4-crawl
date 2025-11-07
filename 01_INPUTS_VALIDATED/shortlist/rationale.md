# FHIR R4 Shortlist Rationale

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
