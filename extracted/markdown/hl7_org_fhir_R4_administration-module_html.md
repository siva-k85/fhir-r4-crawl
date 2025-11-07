---
url: https://hl7.org/fhir/R4/administration-module.html
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


  * **![](https://hl7.org/fhir/R4/administration.jpg)Administration**


This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/administration-module.html) [R4B](http://hl7.org/fhir/R4B/administration-module.html) **R4** [R3](http://hl7.org/fhir/STU3/administration-module.html)
Work Group [Patient Administration ![](https://hl7.org/fhir/R4/external.png)](http://www.hl7.org/Special/committees/pafm/index.cfm) |  [Standards Status](https://hl7.org/fhir/R4/versions.html#std-process): [Informative](https://hl7.org/fhir/R4/versions.html#std-process)  
---|---  
##  8.0 Administration Module [](https://hl7.org/fhir/R4/administration-module.html#8.0 "link to here")
###  8.0.1 Introduction [](https://hl7.org/fhir/R4/administration-module.html#intro "link to here")
The Administrative module covers the base data that is then linked into the other modules for clinical content, finance/billing, workflow, etc.  
It is built on the FHIR technology platform modules. 
Before any clinical data can be recorded, the basic information of the patient must be recorded, and then often the basis of the interaction (such as an encounter). 
###  8.0.2 Index [](https://hl7.org/fhir/R4/administration-module.html#index "link to here")
  * [Patient](https://hl7.org/fhir/R4/patient.html)
  * [RelatedPerson](https://hl7.org/fhir/R4/relatedperson.html)
  * [Person](https://hl7.org/fhir/R4/person.html)
  * [Group](https://hl7.org/fhir/R4/group.html)
  * [Practitioner](https://hl7.org/fhir/R4/practitioner.html)
  * [PractitionerRole](https://hl7.org/fhir/R4/practitionerrole.html)

| 
  * [Organization](https://hl7.org/fhir/R4/organization.html)
  * [Location](https://hl7.org/fhir/R4/location.html)
  * [HealthcareService](https://hl7.org/fhir/R4/healthcareservice.html)
  * [Endpoint](https://hl7.org/fhir/R4/endpoint.html)
  * [Schedule](https://hl7.org/fhir/R4/schedule.html)
  * [Slot](https://hl7.org/fhir/R4/slot.html)

| 
  * [EpisodeOfCare](https://hl7.org/fhir/R4/episodeofcare.html)
  * [Encounter](https://hl7.org/fhir/R4/encounter.html)
  * [Appointment](https://hl7.org/fhir/R4/appointment.html)
  * [AppointmentResponse](https://hl7.org/fhir/R4/appointmentresponse.html)
  * [Account](https://hl7.org/fhir/R4/account.html)
  * [Flag](https://hl7.org/fhir/R4/flag.html)

| 
  * [Device](https://hl7.org/fhir/R4/device.html)
  * [DeviceDefinition](https://hl7.org/fhir/R4/devicedefinition.html)
  * [DeviceMetric](https://hl7.org/fhir/R4/devicemetric.html)
  * [Substance](https://hl7.org/fhir/R4/substance.html)

  
---|---|---|---  
####  8.0.2.1 Patient Registers [](https://hl7.org/fhir/R4/administration-module.html#patient-reg "link to here")
Track people involved in receiving healthcare, the basics nearly everything else references back to 
**Name** | **Aliases** | **Description**  
---|---|---  
[Patient](https://hl7.org/fhir/R4/patient.html) | SubjectOfCare Client Resident | Demographics and other administrative information about an individual or animal receiving care or other health-related services.  
[RelatedPerson](https://hl7.org/fhir/R4/relatedperson.html) |  | Information about a person that is involved in the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.  
[Person](https://hl7.org/fhir/R4/person.html) |  | Demographics and administrative information about a person independent of a specific health-related context.  
[Group](https://hl7.org/fhir/R4/group.html) |  | Represents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization.  
![Image showing the relationship between resources representing people](https://hl7.org/fhir/R4/administration-module-person.png)
> **Implementation Note:** [Patient linking](https://hl7.org/fhir/R4/patient.html#links) should also be considered when evaluating searches with references to other resources. e.g. searching for a patients' conditions for a patient.  
>  At present the specification does not define if the links should be also followed to include conditions that reference the linked patients too. We are currently seeking feedback on this. 
> **Implementation Note:** The Person resource may be used as a centralized register of people that may eventually be involved in healthcare, and could be used as the central core demographics register.  
>  However, the fields/values in Person are duplicated in the other resources, and in many cases the Person resource will be hosted on external systems. 
####  8.0.2.2 Clinical Categorization Resources [](https://hl7.org/fhir/R4/administration-module.html#clinical-reg "link to here")
Most clinical activities occur grouped in some way. Long term care is typically covered by an EpisodeOfCare, whereas short term care is covered by encounters. Account associates the tracking of transactions back to a Patient (or other resource). Flag is just used to highlight a warning or other notification about a patient (or other resource) 
**Name** | **Aliases** | **Description**  
---|---|---  
[EpisodeOfCare](https://hl7.org/fhir/R4/episodeofcare.html) | Case Program Problem | An association between a patient and an organization / healthcare provider(s) during which time encounters may occur. The managing organization assumes a level of responsibility for the patient during this time.  
[Encounter](https://hl7.org/fhir/R4/encounter.html) | Visit | An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.  
[Account](https://hl7.org/fhir/R4/account.html) | Cost center | A financial tool for tracking value accrued for a particular purpose. In the healthcare field, used to track charges for a patient, cost centers, etc.  
[Flag](https://hl7.org/fhir/R4/flag.html) | Barriers to Care, Alert | Prospective warnings of potential issues when providing care to the patient.  
![Image showing the administration interactions](https://hl7.org/fhir/R4/administration-module-interactions.png)
> **Implementation Note:** Resources shown with a dotted box are described in other sections of the specification: `Coverage` and `Claim` are from the [section on Finance](https://hl7.org/fhir/R4/financial-module.html). 
####  8.0.2.3 Service Provider Directory Resources [](https://hl7.org/fhir/R4/administration-module.html#dir-reg "link to here")
Service Provider Directory resources are usually stored in the administration section of applications, and may even be synchronized from external systems. 
**Name** | **Aliases** | **Description**  
---|---|---  
[Organization](https://hl7.org/fhir/R4/organization.html) |  | A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action. Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.  
[Location](https://hl7.org/fhir/R4/location.html) |  | Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated.  
[Practitioner](https://hl7.org/fhir/R4/practitioner.html) |  | A person who is directly or indirectly involved in the provisioning of healthcare.  
[PractitionerRole](https://hl7.org/fhir/R4/practitionerrole.html) |  | A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.  
[HealthcareService](https://hl7.org/fhir/R4/healthcareservice.html) |  | The details of a healthcare service available at a location.  
[Endpoint](https://hl7.org/fhir/R4/endpoint.html) |  | The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.  
![Image showing the provider directory resources](https://hl7.org/fhir/R4/administration-module-prov-dir.png)
####  8.0.2.4 Scheduling and Appointments [](https://hl7.org/fhir/R4/administration-module.html#sched "link to here")
The Scheduling/Appointment resources permit the planning of encounters to occur and follow on with other clinical activities. 
**Name** | **Aliases** | **Description**  
---|---|---  
[Schedule](https://hl7.org/fhir/R4/schedule.html) | Availability | A container for slots of time that may be available for booking appointments.  
[Slot](https://hl7.org/fhir/R4/slot.html) |  | A slot of time on a schedule that may be available for booking appointments.  
[Appointment](https://hl7.org/fhir/R4/appointment.html) |  | A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time. This may result in one or more Encounter(s).  
[AppointmentResponse](https://hl7.org/fhir/R4/appointmentresponse.html) |  | A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.  
![Image showing the scheduling interactions](https://hl7.org/fhir/R4/administration-module-scheduling.png)
####  8.0.2.5 Devices and Substances [](https://hl7.org/fhir/R4/administration-module.html#dev-sub "link to here")
Other assets are often registered in the administration system, and maintained as master files. 
**Name** | **Aliases** | **Description**  
---|---|---  
[Device](https://hl7.org/fhir/R4/device.html) |  | A type of a manufactured item that is used in the provision of healthcare without being substantially changed through that activity. The device may be a medical or non-medical device.  
[DeviceDefinition](https://hl7.org/fhir/R4/devicedefinition.html) |  | The characteristics, operational status and capabilities of a medical-related component of a medical device.  
[DeviceMetric](https://hl7.org/fhir/R4/devicemetric.html) |  | Describes a measurement, calculation or setting capability of a medical device.  
[Substance](https://hl7.org/fhir/R4/substance.html) |  | A homogeneous material with a definite composition.  
###  8.0.3 Security and Privacy [](https://hl7.org/fhir/R4/administration-module.html#secpriv "link to here")
Patient privacy is handled with security labels and tags in the Resource [Meta](https://hl7.org/fhir/R4/resource.html#Meta) property. This is the standard way in which that the FHIR specification provides this supporting information to a sub-system that implements it (which is not defined by FHIR). 
One of the more common use cases is for marking a patient as being a [celebrity](https://hl7.org/fhir/R4/security-labels.html). 
Note that privacy considerations apply to Person, Practitioner and RelatedPerson records in addition to Patient's. 
While Organization, Location, Device and other non-person-identifying records are generally subject to less stringent security precautions, such data must still be protected to avoid safety issues (e.g. someone maliciously changing the ingredients associated with a drug to cause/fail to cause alerts) 
Devices can be linked to Patients. If this occurs, they must be protected as any other patient-linked element 
For more general considerations, see [the Security and Privacy module](https://hl7.org/fhir/R4/secpriv-module.html). 
###  8.0.4 Common Use Cases [](https://hl7.org/fhir/R4/administration-module.html#uses "link to here")
Administration Resources are cornerstone resources that are used by clinical and other domains of the FHIR Standard. 
  * **Managing a Master Record of a Patient and a Person** (e.g. MPI)  
A [Patient](https://hl7.org/fhir/R4/patient.html) resource is used to describe patient demographic information and any updates to it. It can be used to communicate [Patient](https://hl7.org/fhir/R4/patient.html) information to other systems (e.g. other registries, clinical, ancillary and financial systems). Some systems distinguish the Patient Registry (or Client Registry) from the Person Registry. A [Person](https://hl7.org/fhir/R4/person.html) resource is a base for the Person Registry system. The Patient/Person Management use case includes creation, update, as well as merge/unmerge and link/unlink scenarios. 
  * **Managing a Master Record of a Provider and Service Catalogue** (e.g. Provider Registry, Service Directory)  
A [Practitioner](https://hl7.org/fhir/R4/practitioner.html) resource is a base resource for enabling the registry of individuals, related to providing health care services. Other resources, such as [Organization](https://hl7.org/fhir/R4/organization.html), [Location](https://hl7.org/fhir/R4/location.html), [HealthcareService](https://hl7.org/fhir/R4/healthcareservice.html), are creating a complete picture of where, how and by whom the care services are offered to a patient. The resources can be used for managing the master record or as a reference in clinical resources to inform about participants and places for various clinical resources. 
  * **Managing Other Administrative Records**  
The Administration domain of the FHIR standard includes creation and update of [Device](https://hl7.org/fhir/R4/device.html) and [Substance](https://hl7.org/fhir/R4/substance.html) records. Resources can be used for managing a master record or communicating its information to other systems. 
  * **Enabling Patient Profiles, Clinical Reporting and Connecting Clinical Records**  
Administration Resources are referred to by almost all clinical resources. Querying systems, using the references to Administration Resources enables the creation of profiles and reports of various complexities. 
  * **Enabling Clinical Grouping and Financial Reporting**  
Other use cases are included in the roadmap of resources, developed by the Patient Administration group. The roadmap section lists plans and updates of the current work. 


###  8.0.5 Developmental Roadmap [](https://hl7.org/fhir/R4/administration-module.html#roadmap "link to here")
The Patient Administration is currently working through resources that support: 
  * Encounters and Scheduling _(enhance maturity of encounters and further develop in/outpatient scheduling)_
  * Service Provider Directory _(in co-ordination with the Argonaut Provider Directory group)_
  * Financial Management interactions _(account/coverage, then charge item, which links administration to billing)_


Many of the administrative resources are part of the core resources that most systems use first and have formed the basis for most people's first experiences with FHIR.  
However this limited exposure has still to be proven in all contexts, such as veterinary, public health and clinical research. 
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:37+1100. [QA Page](https://hl7.org/fhir/R4/qa.html)   
Links: [Search ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/search.cfm) | [Version History](https://hl7.org/fhir/R4/history.html) | [Table of Contents](https://hl7.org/fhir/R4/toc.html) | [Credits](https://hl7.org/fhir/R4/credits.html) | [Compare to R3 ![](https://hl7.org/fhir/R4/external.png)](https://www.fhir.org/perl/htmldiff.pl?oldfile=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fadministration-module.html&newfile=http%3A%2F%2Fhl7.org%2Ffhir%2FR4%2Fadministration-module.html) | [![CC0](https://hl7.org/fhir/R4/cc0.png)](https://hl7.org/fhir/R4/license.html) | [Propose a change ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir-issues)
