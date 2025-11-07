---
url: https://hl7.org/fhir/R4/patient-version-maps.html
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
  * **R3/R4 Conversions**


This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/patient-version-maps.html) [R4B](http://hl7.org/fhir/R4B/patient-version-maps.html) **R4** [R3](http://hl7.org/fhir/STU3/patient-version-maps.html)
  * [Content](https://hl7.org/fhir/R4/patient.html)
  * [Examples](https://hl7.org/fhir/R4/patient-examples.html)
  * [Detailed Descriptions](https://hl7.org/fhir/R4/patient-definitions.html)
  * [Mappings](https://hl7.org/fhir/R4/patient-mappings.html)
  * [Profiles & Extensions](https://hl7.org/fhir/R4/patient-profiles.html)
  * [Operations](https://hl7.org/fhir/R4/patient-operations.html)
  * [R3 Conversions](https://hl7.org/fhir/R4/patient-version-maps.html#)


##  8.1.18 Resource Patient - R3/R4 Conversions [](https://hl7.org/fhir/R4/patient-version-maps.html#8.1.18 "link to here")
[Patient Administration ![](https://hl7.org/fhir/R4/external.png)](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group |  [Maturity Level](https://hl7.org/fhir/R4/versions.html#maturity): N/A |  [Standards Status](https://hl7.org/fhir/R4/versions.html#std-process): Informative |  [Security Category](https://hl7.org/fhir/R4/security.html#SecPrivConsiderations): Patient |  [Compartments](https://hl7.org/fhir/R4/compartmentdefinition.html): [Patient](https://hl7.org/fhir/R4/compartmentdefinition-patient.html), [Practitioner](https://hl7.org/fhir/R4/compartmentdefinition-practitioner.html), [RelatedPerson](https://hl7.org/fhir/R4/compartmentdefinition-relatedperson.html)  
---|---|---|---|---  
R3 : R4 Conversion maps for Patient.
Functional status for this map: 16 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid. ([see documentation)](https://hl7.org/fhir/R4/r3maps.html)
###  8.1.18.1 R3 to R4 [](https://hl7.org/fhir/R4/patient-version-maps.html#8.1.18.1 "link to here")
```
map "http://hl7.org/fhir/StructureMap/Patient3to4" = "R3 to R4 Conversions for Patient"

uses "http://hl7.org/fhir/3.0/StructureDefinition/Patient" alias PatientR3 as source
uses "http://hl7.org/fhir/StructureDefinition/Patient" alias Patient as target

imports "http://hl7.org/fhir/StructureMap/*3to4"

group Patient(source src : PatientR3, target tgt : Patient) extends DomainResource <<type+>> {
  src.identifier -> tgt.identifier;
  src.active -> tgt.active;
  src.name -> tgt.name;
  src.telecom -> tgt.telecom;
  src.gender -> tgt.gender;
  src.birthDate -> tgt.birthDate;
  src.deceased : boolean as vs -> tgt.deceased = create('boolean') as vt then boolean(vs, vt);
  src.deceased : dateTime as vs -> tgt.deceased = create('dateTime') as vt then dateTime(vs, vt);
  src.address -> tgt.address;
  src.maritalStatus -> tgt.maritalStatus;
  src.multipleBirth : boolean as vs -> tgt.multipleBirth = create('boolean') as vt then boolean(vs, vt);
  src.multipleBirth : integer as vs -> tgt.multipleBirth = create('integer') as vt then integer(vs, vt);
  src.photo -> tgt.photo;
  src.contact as vs0 -> tgt.contact as vt0 then contact(vs0, vt0);
  src.animal as vs0 -> tgt.extension as vt0 then animal(vs0, vt0);
  src.communication as vs0 -> tgt.communication as vt0 then communication(vs0, vt0);
  src.generalPractitioner -> tgt.generalPractitioner;
  src.managingOrganization -> tgt.managingOrganization;
  src.link as vs0 -> tgt.link as vt0 then link(vs0, vt0);
}

group contact(source src, target tgt) extends BackboneElement {
  src.relationship -> tgt.relationship;
  src.name -> tgt.name;
  src.telecom -> tgt.telecom;
  src.address -> tgt.address;
  src.gender -> tgt.gender;
  src.organization -> tgt.organization;
  src.period -> tgt.period;
}

group animal(source src, target tgt) extends Element {
  src -> tgt.url = 'http://hl7.org/fhir/StructureDefinition/patient-animal' "animal";
  src.species as vs ->  tgt.extension as ext,  ext.url = 'species',  ext.value = vs;
  src.breed as vs ->  tgt.extension as ext,  ext.url = 'breed',  ext.value = vs;
  src.genderStatus as vs ->  tgt.extension as ext,  ext.url = 'genderStatus',  ext.value = vs;
}

group communication(source src, target tgt) extends BackboneElement {
  src.language -> tgt.language;
  src.preferred -> tgt.preferred;
}

group link(source src, target tgt) extends BackboneElement {
  src.other -> tgt.other;
  src.type -> tgt.type;
}



```

###  8.1.18.2 R4 to R3 [](https://hl7.org/fhir/R4/patient-version-maps.html#8.1.18.2 "link to here")
```
map "http://hl7.org/fhir/StructureMap/Patient4to3" = "R4 to R3 Conversion for Patient"

uses "http://hl7.org/fhir/StructureDefinition/Patient" alias Patient as source
uses "http://hl7.org/fhir/3.0/StructureDefinition/Patient" alias PatientR3 as target

imports "http://hl7.org/fhir/StructureMap/*4to3"

group Patient(source src : Patient, target tgt : PatientR3) extends DomainResource <<type+>> {
  src.identifier -> tgt.identifier;
  src.active -> tgt.active;
  src.name -> tgt.name;
  src.telecom -> tgt.telecom;
  src.gender -> tgt.gender;
  src.birthDate -> tgt.birthDate;
  src.deceased : boolean as vs -> tgt.deceased = create('boolean') as vt then boolean(vs, vt);
  src.deceased : dateTime as vs -> tgt.deceased = create('dateTime') as vt then dateTime(vs, vt);
  src.address -> tgt.address;
  src.maritalStatus -> tgt.maritalStatus;
  src.multipleBirth : boolean as vs -> tgt.multipleBirth = create('boolean') as vt then boolean(vs, vt);
  src.multipleBirth : integer as vs -> tgt.multipleBirth = create('integer') as vt then integer(vs, vt);
  src.photo -> tgt.photo;
  src.contact as vs0 -> tgt.contact as vt0 then contact(vs0, vt0);
  src.extension as vs0 where url = 'http://hl7.org/fhir/StructureDefinition/patient-animal' -> tgt.animal as vt0 then animal(vs0, vt0) "animal";
  src.communication as vs0 -> tgt.communication as vt0 then communication(vs0, vt0);
  src.generalPractitioner -> tgt.generalPractitioner;
  src.managingOrganization -> tgt.managingOrganization;
  src.link as vs0 -> tgt.link as vt0 then link(vs0, vt0);
}

group contact(source src, target tgt) extends BackboneElement {
  src.relationship -> tgt.relationship;
  src.name -> tgt.name;
  src.telecom -> tgt.telecom;
  src.address -> tgt.address;
  src.gender -> tgt.gender;
  src.organization -> tgt.organization;
  src.period -> tgt.period;
}

group animal(source src, target tgt) {
  src.extension as ext where url = 'species' then {
    ext.value as vs0 -> tgt.species = vs0 "species2";
  } "species";
  src.extension as ext where url = 'breed' then {
    ext.value as vs0 -> tgt.breed = vs0 "breed";
  } "breed";
  src.extension as ext where url = 'genderStatus' then {
    ext.value as vs0 -> tgt.genderStatus = vs0 "genderStatus";
  } "genderStatus";
}

group communication(source src, target tgt) extends BackboneElement {
  src.language -> tgt.language;
  src.preferred -> tgt.preferred;
}

group link(source src, target tgt) extends BackboneElement {
  src.other -> tgt.other;
  src.type -> tgt.type;
}



```

###  8.1.18.3 R4 Validation Errors [](https://hl7.org/fhir/R4/patient-version-maps.html#8.1.18.3 "link to here")
<p>No validation errors - all conversions are clean</p>
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:36+1100. [QA Page](https://hl7.org/fhir/R4/qa.html)   
Links: [Search ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/search.cfm) | [Version History](https://hl7.org/fhir/R4/history.html) | [Table of Contents](https://hl7.org/fhir/R4/toc.html) | [Credits](https://hl7.org/fhir/R4/credits.html) | [Compare to R3 ![](https://hl7.org/fhir/R4/external.png)](https://www.fhir.org/perl/htmldiff.pl?oldfile=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fpatient-version-maps.html&newfile=http%3A%2F%2Fhl7.org%2Ffhir%2FR4%2Fpatient-version-maps.html) | [![CC0](https://hl7.org/fhir/R4/cc0.png)](https://hl7.org/fhir/R4/license.html) | [Propose a change ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir-issues)
