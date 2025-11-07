---
url: https://hl7.org/fhir/R4/consent.html
title: Unknown
crawled: unknown
depth: 0
---

[![logo fhir](https://hl7.org/fhir/R4/assets/images/fhir-logo-www.png) ](http://hl7.org/fhir)
**Release 4**
[ ![visit the hl7 website](https://hl7.org/fhir/R4/assets/images/hl7-logo.png) ](http://www.hl7.org)
[![Search FHIR](https://hl7.org/fhir/R4/assets/images/search.png)](http://hl7.org/fhir/R4/searchform.html)
[FHIR](https://hl7.org/fhir/R4/index.html)
  * [Home](https://hl7.org/fhir/R4/index.html)
  * [Getting Started](https://hl7.org/fhir/R4/modules.html)
  * [Documentation](https://hl7.org/fhir/R4/documentation.html)
  * [Resources](https://hl7.org/fhir/R4/resourcelist.html)
  * [Profiles](https://hl7.org/fhir/R4/profilelist.html)
  * [Extensions](https://hl7.org/fhir/R4/extensibility-registry.html)
  * [Operations](https://hl7.org/fhir/R4/operationslist.html)
  * [Terminologies](https://hl7.org/fhir/R4/terminologies-systems.html)


  * **Home**


This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/index.html) [R4B](http://hl7.org/fhir/R4B/index.html) **R4** [R3](http://hl7.org/fhir/STU3/index.html) [R2](http://hl7.org/fhir/DSTU2/index.html)
#  0 Welcome to FHIR® [](https://hl7.org/fhir/R4/index.html#0 "link to here")
FHIR is a standard for health care data exchange, published by HL7®.
**First time here?**  
See the [executive summary](https://hl7.org/fhir/R4/summary.html), the [developer's introduction](https://hl7.org/fhir/R4/overview-dev.html), [clinical introduction](https://hl7.org/fhir/R4/overview-clinical.html), or [architect's introduction](https://hl7.org/fhir/R4/overview-arch.html), and then the FHIR [overview / roadmap](https://hl7.org/fhir/R4/overview.html) & [Timelines](https://hl7.org/fhir/R4/versions.html). See also the [open license](https://hl7.org/fhir/R4/license.html) (and don't miss the full [Table of Contents](https://hl7.org/fhir/R4/toc.html) and the [Community Credits](https://hl7.org/fhir/R4/credits.html) or you can [search this specification](https://hl7.org/fhir/R4/search.cfm)). 
**[Technical Corrections](https://hl7.org/fhir/R4/history.html)** : 
  * [**4.0.1** , Oct-30 2019](https://hl7.org/fhir/R4/history.html#v4.0.1): Corrections to invariants & generated conformance resources, and add ANSI Normative Status Notes


**Level 1** Basic framework on which the specification is built
[ Foundation ](https://hl7.org/fhir/R4/foundation-module.html)
[Base Documentation](https://hl7.org/fhir/R4/documentation.html), [XML](https://hl7.org/fhir/R4/xml.html), [JSON](https://hl7.org/fhir/R4/json.html), [Data Types](https://hl7.org/fhir/R4/datatypes.html), [Extensions](https://hl7.org/fhir/R4/extensibility.html)
**Level 2** Supporting implementation and binding to external specifications
[ Implementer Support ](https://hl7.org/fhir/R4/implsupport-module.html)
[Downloads](https://hl7.org/fhir/R4/downloads.html),  
[Version Mgmt](https://hl7.org/fhir/R4/versioning.html),  
[Use Cases](https://hl7.org/fhir/R4/usecases.html),  
[Testing](https://hl7.org/fhir/R4/testing.html)
[ Security & Privacy ](https://hl7.org/fhir/R4/secpriv-module.html)
[Security](https://hl7.org/fhir/R4/security.html),  
[Consent](https://hl7.org/fhir/R4/consent.html),  
[Provenance](https://hl7.org/fhir/R4/provenance.html),  
[AuditEvent](https://hl7.org/fhir/R4/auditevent.html)
[ Conformance ](https://hl7.org/fhir/R4/conformance-module.html)
[StructureDefinition](https://hl7.org/fhir/R4/structuredefinition.html),  
[CapabilityStatement](https://hl7.org/fhir/R4/capabilitystatement.html),  
[ImplementationGuide](https://hl7.org/fhir/R4/implementationguide.html),  
[Profiling](https://hl7.org/fhir/R4/profiling.html)
[ Terminology ](https://hl7.org/fhir/R4/terminology-module.html)
[CodeSystem](https://hl7.org/fhir/R4/codesystem.html),  
[ValueSet](https://hl7.org/fhir/R4/valueset.html),  
[ConceptMap](https://hl7.org/fhir/R4/conceptmap.html),  
[Terminology Svc](https://hl7.org/fhir/R4/terminology-service.html)
[ Exchange ](https://hl7.org/fhir/R4/exchange-module.html)
[REST API](https://hl7.org/fhir/R4/http.html) + [Search](https://hl7.org/fhir/R4/search.html)  
[Documents](https://hl7.org/fhir/R4/documents.html)  
[Messaging](https://hl7.org/fhir/R4/messaging.html)  
[Services](https://hl7.org/fhir/R4/services.html)  
[Databases](https://hl7.org/fhir/R4/storage.html)  

**Level 3** Linking to real world concepts in the healthcare system
[ Administration ](https://hl7.org/fhir/R4/administration-module.html)
[Patient](https://hl7.org/fhir/R4/patient.html), [Practitioner](https://hl7.org/fhir/R4/practitioner.html), [CareTeam](https://hl7.org/fhir/R4/careteam.html), [Device](https://hl7.org/fhir/R4/device.html), [Organization](https://hl7.org/fhir/R4/organization.html), [Location](https://hl7.org/fhir/R4/location.html), [Healthcare Service](https://hl7.org/fhir/R4/healthcareservice.html)
**Level 4** Record-keeping and Data Exchange for the healthcare process
[ Clinical ](https://hl7.org/fhir/R4/clinicalsummary-module.html)
[Allergy](https://hl7.org/fhir/R4/allergyintolerance.html), [Problem](https://hl7.org/fhir/R4/condition.html), [Procedure](https://hl7.org/fhir/R4/procedure.html), [CarePlan](https://hl7.org/fhir/R4/careplan.html)/[Goal](https://hl7.org/fhir/R4/goal.html), [ServiceRequest](https://hl7.org/fhir/R4/servicerequest.html), [Family History](https://hl7.org/fhir/R4/familymemberhistory.html), [RiskAssessment](https://hl7.org/fhir/R4/riskassessment.html), etc. 
[ Diagnostics ](https://hl7.org/fhir/R4/diagnostics-module.html)
[Observation](https://hl7.org/fhir/R4/observation.html), [Report](https://hl7.org/fhir/R4/diagnosticreport.html), [Specimen](https://hl7.org/fhir/R4/specimen.html), [ImagingStudy](https://hl7.org/fhir/R4/imagingstudy.html), [Genomics](https://hl7.org/fhir/R4/genomics.html), [Specimen](https://hl7.org/fhir/R4/specimen.html), [ImagingStudy](https://hl7.org/fhir/R4/imagingstudy.html), etc. 
[ Medications ](https://hl7.org/fhir/R4/medications-module.html)
[Medication](https://hl7.org/fhir/R4/medication.html),  
[Request](https://hl7.org/fhir/R4/medicationrequest.html), [Dispense](https://hl7.org/fhir/R4/medicationdispense.html),  
[Administration](https://hl7.org/fhir/R4/medicationadministration.html),  
[Statement](https://hl7.org/fhir/R4/medicationstatement.html),  
[Immunization](https://hl7.org/fhir/R4/immunization.html), etc. 
[ Workflow ](https://hl7.org/fhir/R4/workflow-module.html)
[Introduction](https://hl7.org/fhir/R4/workflow.html) + [Task](https://hl7.org/fhir/R4/task.html), [Appointment](https://hl7.org/fhir/R4/appointment.html), [Schedule](https://hl7.org/fhir/R4/schedule.html), [Referral](https://hl7.org/fhir/R4/servicerequest.html), [PlanDefinition](https://hl7.org/fhir/R4/plandefinition.html), etc 
[ Financial ](https://hl7.org/fhir/R4/financial-module.html)
[Claim](https://hl7.org/fhir/R4/claim.html), [Account](https://hl7.org/fhir/R4/account.html),  
[Invoice](https://hl7.org/fhir/R4/invoice.html), [ChargeItem](https://hl7.org/fhir/R4/chargeitem.html),   
[Coverage](https://hl7.org/fhir/R4/coverage.html) + Eligibility   
[Request](https://hl7.org/fhir/R4/coverageeligibilityrequest.html) & [Response](https://hl7.org/fhir/R4/coverageeligibilityresponse.html), [ExplanationOfBenefit](https://hl7.org/fhir/R4/explanationofbenefit.html), etc. 
**Level 5** Providing the ability to reason about the healthcare process
[ Clinical Reasoning ](https://hl7.org/fhir/R4/clinicalreasoning-module.html)
[Library](https://hl7.org/fhir/R4/library.html), [PlanDefinition](https://hl7.org/fhir/R4/plandefinition.html) & [GuidanceResponse](https://hl7.org/fhir/R4/guidanceresponse.html), [Measure](https://hl7.org/fhir/R4/measure.html)/[MeasureReport](https://hl7.org/fhir/R4/measurereport.html), etc.
**External Links:**
**Implementation Guides** Specifications based on the FHIR standard
  * [Published by HL7, Affiliates & FHIR Foundation ![](https://hl7.org/fhir/R4/external.png)](http://www.fhir.org/guides/registry)
  * [Other IGs (FHIR Confluence) ![](https://hl7.org/fhir/R4/external.png)](https://confluence.hl7.org/display/FHIR/IGs+from+other+Organizations)

|  **[FHIR Foundation![](https://hl7.org/fhir/R4/external.png)](http://fhir.org)** Enabling health interoperability through FHIR
  * [Community Forum ![](https://hl7.org/fhir/R4/external.png)](http://community.fhir.org/) + [FHIR Chat ![](https://hl7.org/fhir/R4/external.png)](http://chat.fhir.org/)
  * [Public Test Servers & Software ![](https://hl7.org/fhir/R4/external.png)](https://confluence.hl7.org/display/FHIR/Public+Test+Servers)
  * [Blogs that cover FHIR ![](https://hl7.org/fhir/R4/external.png)](https://confluence.hl7.org/display/FHIR/Blogs)
  * [FHIR Confluence ![](https://hl7.org/fhir/R4/external.png)](https://confluence.hl7.org/display/FHIR)

|  **Translations** Note that translations are not always up to date
  * [Russian ![](https://hl7.org/fhir/R4/external.png)](http://fhir-ru.github.io/index.html)
  * [Chinese ![](https://hl7.org/fhir/R4/external.png)](https://github.com/wanghaisheng/fhir-cn/blob/source/README.md)
  * [Japanese ![](https://hl7.org/fhir/R4/external.png)](https://std.jpfhir.jp/)

  
---|---|---  
Note: This specification requires a browser that is SVG compatible (Microsoft Internet Explorer 10+/Edge, Firefox 3.0+, Chrome, or Safari), and uses the browser's session storage to remember which tabs are active.
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:37+1100. [QA Page](https://hl7.org/fhir/R4/qa.html)   
Links: [Search ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/search.cfm) | [Version History](https://hl7.org/fhir/R4/history.html) | [Table of Contents](https://hl7.org/fhir/R4/toc.html) | [Credits](https://hl7.org/fhir/R4/credits.html) | [Compare to R3 ![](https://hl7.org/fhir/R4/external.png)](https://www.fhir.org/perl/htmldiff.pl?oldfile=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Findex.html&newfile=http%3A%2F%2Fhl7.org%2Ffhir%2FR4%2Findex.html) | [![CC0](https://hl7.org/fhir/R4/cc0.png)](https://hl7.org/fhir/R4/license.html) | [Propose a change ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir-issues)
