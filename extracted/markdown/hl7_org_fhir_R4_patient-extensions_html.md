---
url: https://hl7.org/fhir/R4/patient-extensions.html
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
  * [Profile](https://hl7.org/fhir/R4/patient-extensions.html)
  * **Patient HL7 Extensions**


This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/directory.html). Page versions: **R4** [R3](http://hl7.org/fhir/STU3/patient-extensions.html) [R2](http://hl7.org/fhir/DSTU2/patient-extensions.html)
##  8.1.19 Patient HL7 Extensions [](https://hl7.org/fhir/R4/patient-extensions.html#8.1.19 "link to here")
[Patient Administration ![](https://hl7.org/fhir/R4/external.png)](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group |  [Maturity Level](https://hl7.org/fhir/R4/versions.html#maturity): N/A |  [Standards Status](https://hl7.org/fhir/R4/versions.html#levels): Informative |   
---|---|---|---  
Defines common extensions used with or related to the Patient resource 
###  8.1.19.1 Content [](https://hl7.org/fhir/R4/patient-extensions.html#content "link to here")
**Extensions** :   
---  
[patient-mothersMaidenName](https://hl7.org/fhir/R4/extension-patient-mothersmaidenname.html) |  **mothersMaidenName** : Mother's maiden (unmarried) name, commonly collected to help verify patient identity.  
[patient-birthPlace](https://hl7.org/fhir/R4/extension-patient-birthplace.html) |  **birthPlace** : The registered place of birth of the patient. A sytem may use the address.text if they don't store the birthPlace address in discrete elements.  
[patient-birthTime](https://hl7.org/fhir/R4/extension-patient-birthtime.html) |  **birthTime** : The time of day that the Patient was born. This includes the date to ensure that the timezone information can be communicated effectively.  
[patient-nationality](https://hl7.org/fhir/R4/extension-patient-nationality.html) |  **nationality** : The nationality of the patient.  
[patient-citizenship](https://hl7.org/fhir/R4/extension-patient-citizenship.html) |  **citizenship** : The patient's legal status as citizen of a country.  
[patient-cadavericDonor](https://hl7.org/fhir/R4/extension-patient-cadavericdonor.html) |  **cadavericDonor** : Flag indicating whether the patient authorized the donation of body parts after death.  
[patient-congregation](https://hl7.org/fhir/R4/extension-patient-congregation.html) |  **congregation** : A group or place of religious practice that may provide services to the patient.  
[patient-adoptionInfo](https://hl7.org/fhir/R4/extension-patient-adoptioninfo.html) |  **adoptionInfo** : Code indication the adoption status of the patient.  
[patient-disability](https://hl7.org/fhir/R4/extension-patient-disability.html) |  **disability** : Value(s) identifying physical or mental condition(s) that limits a person's movements, senses, or activities.  
[patient-importance](https://hl7.org/fhir/R4/extension-patient-importance.html) |  **importance** : The importance of the patient (e.g. VIP).  
[patient-interpreterRequired](https://hl7.org/fhir/R4/extension-patient-interpreterrequired.html) |  **interpreterRequired** : This Patient requires an interpreter to communicate healthcare information to the practitioner.  
[patient-religion](https://hl7.org/fhir/R4/extension-patient-religion.html) |  **religion** : The patient's professed religious affiliations.  
[patient-relatedPerson](https://hl7.org/fhir/R4/extension-patient-relatedperson.html) |  **relatedPerson** : In some cases a Patient.contact will also be populated as a RelatedPerson resource. This linkage permits the linkage between the 2 resources to be able to accurately indicate a representation of the same individual, and updating details between could be appropriate.  
[patient-genderIdentity](https://hl7.org/fhir/R4/extension-patient-genderidentity.html) |  **genderIdentity** : The gender the patient identifies with. The Patient's gender identity is used as guidance (e.g. for staff) about how to interact with the patient.  
[patient-preferenceType](https://hl7.org/fhir/R4/extension-patient-preferencetype.html) |  **preferenceType** : Indicates what mode of communication the patient prefers to use for the indicated language.  
[patient-animal](https://hl7.org/fhir/R4/extension-patient-animal.html) |  **animal** : This patient is known to be an animal.  
[patient-proficiency](https://hl7.org/fhir/R4/extension-patient-proficiency.html) |  **proficiency** : Proficiency level of the communication.  
###  8.1.19.2 Search Parameters [](https://hl7.org/fhir/R4/patient-extensions.html#search "link to here")
Search parameters defined by this package. See [Searching](https://hl7.org/fhir/R4/search.html) for more information about searching in REST, messaging, and services.
**Name** | **Type** | **Description** | **Paths** | **Source**  
---|---|---|---|---  
age | [number](https://hl7.org/fhir/R4/search.html#number) | Searches for patients based on age as calculated based on current date and date of birth. Deceased patients are excluded from the search. | f:Patient/f:birthDate |  [XML](https://hl7.org/fhir/R4/patient-extensions-Patient-age.xml.html) / [JSON](https://hl7.org/fhir/R4/patient-extensions-Patient-age.json.html)  
birthOrderBoolean | [token](https://hl7.org/fhir/R4/search.html#token) | Search based on whether a patient was part of a multiple birth or not. | f:Patient/f:multipleBirthBoolean | f:Patient/f:multipleBirthInteger |  [XML](https://hl7.org/fhir/R4/patient-extensions-Patient-birthOrderBoolean.xml.html) / [JSON](https://hl7.org/fhir/R4/patient-extensions-Patient-birthOrderBoolean.json.html)  
mothersMaidenName | [string](https://hl7.org/fhir/R4/search.html#string) | Search based on patient's mother's maiden name |  |  [XML](https://hl7.org/fhir/R4/patient-extensions-Patient-mothersMaidenName.xml.html) / [JSON](https://hl7.org/fhir/R4/patient-extensions-Patient-mothersMaidenName.json.html)  
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:36+1100. [QA Page](https://hl7.org/fhir/R4/qa.html)   
Links: [Search ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/search.cfm) | [Version History](https://hl7.org/fhir/R4/history.html) | [Table of Contents](https://hl7.org/fhir/R4/toc.html) | [Credits](https://hl7.org/fhir/R4/credits.html) | [Compare to R3 ![](https://hl7.org/fhir/R4/external.png)](https://www.fhir.org/perl/htmldiff.pl?oldfile=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fpatient-extensions.html&newfile=http%3A%2F%2Fhl7.org%2Ffhir%2FR4%2Fpatient-extensions.html) | [![CC0](https://hl7.org/fhir/R4/cc0.png)](https://hl7.org/fhir/R4/license.html) | [Propose a change ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir-issues)
