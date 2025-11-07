---
url: https://hl7.org/fhir/R4/patient-mappings.html
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


  * [![](https://hl7.org/fhir/R4/administration.jpg) Administration](https://hl7.org/fhir/R4/administration-module.html)
  * [Patient](https://hl7.org/fhir/R4/patient.html)
  * **Mappings**


This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/patient-mappings.html) [R4B](http://hl7.org/fhir/R4B/patient-mappings.html) **R4** [R3](http://hl7.org/fhir/STU3/patient-mappings.html) [R2](http://hl7.org/fhir/DSTU2/patient-mappings.html)
  * [Content](https://hl7.org/fhir/R4/patient.html)
  * [Examples](https://hl7.org/fhir/R4/patient-examples.html)
  * [Detailed Descriptions](https://hl7.org/fhir/R4/patient-definitions.html)
  * [Mappings](https://hl7.org/fhir/R4/patient-mappings.html#)
  * [Profiles & Extensions](https://hl7.org/fhir/R4/patient-profiles.html)
  * [Operations](https://hl7.org/fhir/R4/patient-operations.html)
  * [R3 Conversions](https://hl7.org/fhir/R4/patient-version-maps.html)


##  8.1.15 Resource Patient - Mappings [](https://hl7.org/fhir/R4/patient-mappings.html#8.1.15 "link to here")
[Patient Administration ![](https://hl7.org/fhir/R4/external.png)](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group |  [Maturity Level](https://hl7.org/fhir/R4/versions.html#maturity): N/A |  [Standards Status](https://hl7.org/fhir/R4/versions.html#std-process): Informative |  [Security Category](https://hl7.org/fhir/R4/security.html#SecPrivConsiderations): Patient |  [Compartments](https://hl7.org/fhir/R4/compartmentdefinition.html): [Patient](https://hl7.org/fhir/R4/compartmentdefinition-patient.html), [Practitioner](https://hl7.org/fhir/R4/compartmentdefinition-practitioner.html), [RelatedPerson](https://hl7.org/fhir/R4/compartmentdefinition-relatedperson.html)  
---|---|---|---|---  
Mappings:
[FiveWs Pattern Mapping](https://hl7.org/fhir/R4/patient-mappings.html#w5)
[HL7 v2 Mapping](https://hl7.org/fhir/R4/patient-mappings.html#v2)
[LOINC code for the element](https://hl7.org/fhir/R4/patient-mappings.html#loinc)
[CDA (R2)](https://hl7.org/fhir/R4/patient-mappings.html#cda)
[RIM Mapping](https://hl7.org/fhir/R4/patient-mappings.html#rim)
Mappings for the patient resource (see [Mappings to Other Standards](https://hl7.org/fhir/R4/mappings.html) for further information & status).
###  8.1.15.1 FiveWs Pattern Mapping ([http://hl7.org/fhir/fivews ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/fivews.html)) [](https://hl7.org/fhir/R4/patient-mappings.html#w5 "link to here")
**Patient** |   
---|---  
identifier | FiveWs.identifier  
active | FiveWs.status  
###  8.1.15.2 HL7 v2 Mapping ([http://hl7.org/v2 ![](https://hl7.org/fhir/R4/external.png)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185)) [](https://hl7.org/fhir/R4/patient-mappings.html#v2 "link to here")
**Patient** |   
---|---  
identifier | PID-3  
active |   
name | PID-5, PID-9  
telecom | PID-13, PID-14, PID-40  
gender | PID-8  
birthDate | PID-7  
deceased[x] | PID-30 (bool) and PID-29 (datetime)  
address | PID-11  
maritalStatus | PID-16  
multipleBirth[x] | PID-24 (bool), PID-25 (integer)  
photo | OBX-5 - needs a profile  
contact |   
relationship | NK1-7, NK1-3  
name | NK1-2  
telecom | NK1-5, NK1-6, NK1-40  
address | NK1-4  
gender | NK1-15  
organization | NK1-13, NK1-30, NK1-31, NK1-32, NK1-41  
period |   
communication |   
language | PID-15, LAN-2  
preferred | PID-15  
generalPractitioner | PD1-4  
managingOrganization |   
link |   
other | PID-3, MRG-1  
type |   
###  8.1.15.3 LOINC code for the element ([http://loinc.org ![](https://hl7.org/fhir/R4/external.png)](http://loinc.org)) [](https://hl7.org/fhir/R4/patient-mappings.html#loinc "link to here")
**Patient** |   
---|---  
identifier |   
active |   
name |   
telecom |   
gender |   
birthDate | 21112-8  
deceased[x] |   
address |   
maritalStatus |   
multipleBirth[x] |   
photo |   
contact |   
relationship |   
name |   
telecom |   
address |   
gender |   
organization |   
period |   
communication |   
language |   
preferred |   
generalPractitioner |   
managingOrganization |   
link |   
other |   
type |   
###  8.1.15.4 CDA (R2) ([http://hl7.org/v3/cda ![](https://hl7.org/fhir/R4/external.png)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7)) [](https://hl7.org/fhir/R4/patient-mappings.html#cda "link to here")
**Patient** | ClinicalDocument.recordTarget.patientRole  
---|---  
identifier | .id  
active | n/a  
name | .patient.name  
telecom | .telecom  
gender | .patient.administrativeGenderCode  
birthDate | .patient.birthTime  
deceased[x] | n/a  
address | .addr  
maritalStatus | .patient.maritalStatusCode  
multipleBirth[x] | n/a  
photo | n/a  
contact | n/a  
relationship | n/a  
name | n/a  
telecom | n/a  
address | n/a  
gender | n/a  
organization | n/a  
period | n/a  
communication | patient.languageCommunication  
language | .languageCode  
preferred | .preferenceInd  
generalPractitioner | n/a  
managingOrganization | .providerOrganization  
link | n/a  
other | n/a  
type | n/a  
###  8.1.15.5 RIM Mapping ([http://hl7.org/v3 ![](https://hl7.org/fhir/R4/external.png)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=186)) [](https://hl7.org/fhir/R4/patient-mappings.html#rim "link to here")
**Patient** | Patient[classCode=PAT]  
---|---  
identifier | id  
active | statusCode  
name | name  
telecom | telecom  
gender | player[classCode=PSN|ANM and determinerCode=INSTANCE]/administrativeGender  
birthDate | player[classCode=PSN|ANM and determinerCode=INSTANCE]/birthTime  
deceased[x] | player[classCode=PSN|ANM and determinerCode=INSTANCE]/deceasedInd, player[classCode=PSN|ANM and determinerCode=INSTANCE]/deceasedTime  
address | addr  
maritalStatus | player[classCode=PSN]/maritalStatusCode  
multipleBirth[x] | player[classCode=PSN|ANM and determinerCode=INSTANCE]/multipleBirthInd, player[classCode=PSN|ANM and determinerCode=INSTANCE]/multipleBirthOrderNumber  
photo | player[classCode=PSN|ANM and determinerCode=INSTANCE]/desc  
contact | player[classCode=PSN|ANM and determinerCode=INSTANCE]/scopedRole[classCode=CON]  
relationship | code  
name | name  
telecom | telecom  
address | addr  
gender | player[classCode=PSN|ANM and determinerCode=INSTANCE]/administrativeGender  
organization | scoper  
period | effectiveTime  
communication | LanguageCommunication  
language | player[classCode=PSN|ANM and determinerCode=INSTANCE]/languageCommunication/code  
preferred | preferenceInd  
generalPractitioner | subjectOf.CareEvent.performer.AssignedEntity  
managingOrganization | scoper  
link | outboundLink  
other | id  
type | typeCode  
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:36+1100. [QA Page](https://hl7.org/fhir/R4/qa.html)   
Links: [Search ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/search.cfm) | [Version History](https://hl7.org/fhir/R4/history.html) | [Table of Contents](https://hl7.org/fhir/R4/toc.html) | [Credits](https://hl7.org/fhir/R4/credits.html) | [Compare to R3 ![](https://hl7.org/fhir/R4/external.png)](https://www.fhir.org/perl/htmldiff.pl?oldfile=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fpatient-mappings.html&newfile=http%3A%2F%2Fhl7.org%2Ffhir%2FR4%2Fpatient-mappings.html) | [![CC0](https://hl7.org/fhir/R4/cc0.png)](https://hl7.org/fhir/R4/license.html) | [Propose a change ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir-issues)
