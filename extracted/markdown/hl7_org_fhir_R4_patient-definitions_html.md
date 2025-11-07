---
url: https://hl7.org/fhir/R4/patient-definitions.html
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
  * **Detailed Descriptions**


This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/patient-definitions.html) [R4B](http://hl7.org/fhir/R4B/patient-definitions.html) **R4** [R3](http://hl7.org/fhir/STU3/patient-definitions.html) [R2](http://hl7.org/fhir/DSTU2/patient-definitions.html)
  * [Content](https://hl7.org/fhir/R4/patient.html)
  * [Examples](https://hl7.org/fhir/R4/patient-examples.html)
  * [Detailed Descriptions](https://hl7.org/fhir/R4/patient-definitions.html#)
  * [Mappings](https://hl7.org/fhir/R4/patient-mappings.html)
  * [Profiles & Extensions](https://hl7.org/fhir/R4/patient-profiles.html)
  * [Operations](https://hl7.org/fhir/R4/patient-operations.html)
  * [R3 Conversions](https://hl7.org/fhir/R4/patient-version-maps.html)


##  8.1.14 Resource Patient - Detailed Descriptions [](https://hl7.org/fhir/R4/patient-definitions.html#8.1.14 "link to here")
[Patient Administration ![](https://hl7.org/fhir/R4/external.png)](http://www.hl7.org/Special/committees/pafm/index.cfm) Work Group |  [Maturity Level](https://hl7.org/fhir/R4/versions.html#maturity): [N](https://hl7.org/fhir/R4/versions.html#std-process) |  [Normative](https://hl7.org/fhir/R4/versions.html#std-process "Standard Status") (from v4.0.0) |  [Security Category](https://hl7.org/fhir/R4/security.html#SecPrivConsiderations): Patient |  [Compartments](https://hl7.org/fhir/R4/compartmentdefinition.html): [Patient](https://hl7.org/fhir/R4/compartmentdefinition-patient.html), [Practitioner](https://hl7.org/fhir/R4/compartmentdefinition-practitioner.html), [RelatedPerson](https://hl7.org/fhir/R4/compartmentdefinition-relatedperson.html)  
---|---|---|---|---  
Detailed Descriptions for the elements in the Patient resource.
**Patient**  
---  
Element Id | Patient  
Definition |  Demographics and other administrative information about an individual or animal receiving care or other health-related services.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [DomainResource](https://hl7.org/fhir/R4/domainresource.html)  
Requirements |  Tracking patient is the center of the healthcare process.  
Alternate Names | SubjectOfCare Client Resident  
**Patient.identifier**  
Element Id | Patient.identifier  
Definition |  An identifier for this patient.  
Note | This is a business identifier, not a resource identifier (see [discussion](https://hl7.org/fhir/R4/resource.html#identifiers))  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [Identifier](https://hl7.org/fhir/R4/datatypes.html#Identifier)  
Requirements |  Patients are almost always assigned specific numerical identifiers.  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
**Patient.active**  
Element Id | Patient.active  
Definition |  Whether this patient record is in active use. Many systems use this property to mark as non-current patients, such as those that have not been seen for a period of time based on an organization's business rules. It is often used to filter patient lists to exclude inactive patients Deceased patients may also be marked as inactive for the same reasons, but may be active for some time after death.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [boolean](https://hl7.org/fhir/R4/datatypes.html#boolean)  
[Is Modifier](https://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true (Reason: This element is labelled as a modifier because it is a status element that can indicate that a record should not be treated as valid)  
Meaning if Missing | This resource is generally assumed to be active if no value is provided for the active element  
Requirements |  Need to be able to mark a patient record as not to be used because it was created in error.  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
Comments |  If a record is inactive, and linked to an active record, then future patient/record updates should occur on the other patient.  
**Patient.name**  
Element Id | Patient.name  
Definition |  A name associated with the individual.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [HumanName](https://hl7.org/fhir/R4/datatypes.html#HumanName)  
Requirements |  Need to be able to track the patient by multiple names. Examples are your official name and a partner name.  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
Comments |  A patient may have multiple names with different uses or applicable periods. For animals, the name is a "HumanName" in the sense that is assigned and used by humans and has the same patterns.  
**Patient.telecom**  
Element Id | Patient.telecom  
Definition |  A contact detail (e.g. a telephone number or an email address) by which the individual may be contacted.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [ContactPoint](https://hl7.org/fhir/R4/datatypes.html#ContactPoint)  
Requirements |  People have (primary) ways to contact them in some way such as phone, email.  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
Comments |  A Patient may have multiple ways to be contacted with different uses or applicable periods. May need to have options for contacting the person urgently and also to help with identification. The address might not go directly to the individual, but may reach another party that is able to proxy for the patient (i.e. home phone, or pet owner's phone).  
**Patient.gender**  
Element Id | Patient.gender  
Definition |  Administrative Gender - the gender that the patient is considered to have for administration and record keeping purposes.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Terminology Binding](https://hl7.org/fhir/R4/terminologies.html) |  [AdministrativeGender](https://hl7.org/fhir/R4/valueset-administrative-gender.html) ([Required](https://hl7.org/fhir/R4/terminologies.html#required))  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [code](https://hl7.org/fhir/R4/datatypes.html#code)  
Requirements |  Needed for identification of the individual, in combination with (at least) name and birth date.  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
Comments |  The gender might not match the biological sex as determined by genetics or the individual's preferred identification. Note that for both humans and particularly animals, there are other legitimate possibilities than male and female, though the vast majority of systems and contexts only support male and female. Systems providing decision support or enforcing business rules should ideally do this on the basis of Observations dealing with the specific sex or gender aspect of interest (anatomical, chromosomal, social, etc.) However, because these observations are infrequently recorded, defaulting to the administrative gender is common practice. Where such defaulting occurs, rule enforcement should allow for the variation between administrative and biological, chromosomal and other gender aspects. For example, an alert about a hysterectomy on a male should be handled as a warning or overridable error, not a "hard" error. See the Patient Gender and Sex section for additional information about communicating patient gender and sex.  
**Patient.birthDate**  
Element Id | Patient.birthDate  
Definition |  The date of birth for the individual.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [date](https://hl7.org/fhir/R4/datatypes.html#date)  
Requirements |  Age of the individual drives many clinical processes.  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
Comments |  At least an estimated year should be provided as a guess if the real DOB is unknown There is a standard extension "patient-birthTime" available that should be used where Time is required (such as in maternity/infant care systems).  
LOINC Code | 21112-8  
**Patient.deceased[x]**  
Element Id | Patient.deceased[x]  
Definition |  Indicates if the individual is deceased or not.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Type](https://hl7.org/fhir/R4/datatypes.html) |  [boolean](https://hl7.org/fhir/R4/datatypes.html#boolean)|[dateTime](https://hl7.org/fhir/R4/datatypes.html#dateTime)  
[x] Note | See [Choice of Data Types](https://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x]  
[Is Modifier](https://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true (Reason: This element is labeled as a modifier because once a patient is marked as deceased, the actions that are appropriate to perform on the patient may be significantly different.)  
Requirements |  The fact that a patient is deceased influences the clinical process. Also, in human communication and relation management it is necessary to know whether the person is alive.  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
Comments |  If there's no value in the instance, it means there is no statement on whether or not the individual is deceased. Most systems will interpret the absence of a value as a sign of the person being alive.  
**Patient.address**  
Element Id | Patient.address  
Definition |  An address for the individual.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [Address](https://hl7.org/fhir/R4/datatypes.html#Address)  
Requirements |  May need to keep track of patient addresses for contacting, billing or reporting requirements and also to help with identification.  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
Comments |  Patient may have multiple addresses with different uses or applicable periods.  
**Patient.maritalStatus**  
Element Id | Patient.maritalStatus  
Definition |  This field contains a patient's most recent marital (civil) status.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Terminology Binding](https://hl7.org/fhir/R4/terminologies.html) |  [MaritalStatus](https://hl7.org/fhir/R4/valueset-marital-status.html) ([Extensible](https://hl7.org/fhir/R4/terminologies.html#extensible))  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](https://hl7.org/fhir/R4/datatypes.html#CodeableConcept)  
Requirements |  Most, if not all systems capture it.  
**Patient.multipleBirth[x]**  
Element Id | Patient.multipleBirth[x]  
Definition |  Indicates whether the patient is part of a multiple (boolean) or indicates the actual birth order (integer).  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Type](https://hl7.org/fhir/R4/datatypes.html) |  [boolean](https://hl7.org/fhir/R4/datatypes.html#boolean)|[integer](https://hl7.org/fhir/R4/datatypes.html#integer)  
[x] Note | See [Choice of Data Types](https://hl7.org/fhir/R4/formats.html#choice) for further information about how to use [x]  
Requirements |  For disambiguation of multiple-birth children, especially relevant where the care provider doesn't meet the patient, such as labs.  
Comments |  Where the valueInteger is provided, the number is the birth number in the sequence. E.g. The middle birth in triplets would be valueInteger=2 and the third born would have valueInteger=3 If a boolean value was provided for this triplets example, then all 3 patient records would have valueBoolean=true (the ordering is not indicated).  
**Patient.photo**  
Element Id | Patient.photo  
Definition |  Image of the patient.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [Attachment](https://hl7.org/fhir/R4/datatypes.html#Attachment)  
Requirements |  Many EHR systems have the capability to capture an image of the patient. Fits with newer social media usage too.  
Comments |  Guidelines:
  * Use id photos, not clinical photos.
  * Limit dimensions to thumbnail.
  * Keep byte count low to ease resource updates.

  
**Patient.contact**  
Element Id | Patient.contact  
Definition |  A contact party (e.g. guardian, partner, friend) for the patient.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
Requirements |  Need to track people you can contact about the patient.  
Comments |  Contact covers all kinds of contact parties: family members, business contacts, guardians, caregivers. Not applicable to register pedigree and family ties beyond use of having contact.  
Invariants |  | **Defined on this element**  
---  
**pat-1** |  [Rule](https://hl7.org/fhir/R4/conformance-rules.html#rule) | SHALL at least contain a contact's details or a reference to an organization | name.exists() or telecom.exists() or address.exists() or organization.exists()  
**Patient.contact.relationship**  
Element Id | Patient.contact.relationship  
Definition |  The nature of the relationship between the patient and the contact person.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
[Terminology Binding](https://hl7.org/fhir/R4/terminologies.html) |  [Patient Contact Relationship ](https://hl7.org/fhir/R4/valueset-patient-contactrelationship.html) ([Extensible](https://hl7.org/fhir/R4/terminologies.html#extensible))  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](https://hl7.org/fhir/R4/datatypes.html#CodeableConcept)  
Requirements |  Used to determine which contact person is the most relevant to approach, depending on circumstances.  
**Patient.contact.name**  
Element Id | Patient.contact.name  
Definition |  A name associated with the contact person.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [HumanName](https://hl7.org/fhir/R4/datatypes.html#HumanName)  
Requirements |  Contact persons need to be identified by name, but it is uncommon to need details about multiple other names for that contact person.  
**Patient.contact.telecom**  
Element Id | Patient.contact.telecom  
Definition |  A contact detail for the person, e.g. a telephone number or an email address.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [ContactPoint](https://hl7.org/fhir/R4/datatypes.html#ContactPoint)  
Requirements |  People have (primary) ways to contact them in some way such as phone, email.  
Comments |  Contact may have multiple ways to be contacted with different uses or applicable periods. May need to have options for contacting the person urgently, and also to help with identification.  
**Patient.contact.address**  
Element Id | Patient.contact.address  
Definition |  Address for the contact person.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [Address](https://hl7.org/fhir/R4/datatypes.html#Address)  
Requirements |  Need to keep track where the contact person can be contacted per postal mail or visited.  
**Patient.contact.gender**  
Element Id | Patient.contact.gender  
Definition |  Administrative Gender - the gender that the contact person is considered to have for administration and record keeping purposes.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Terminology Binding](https://hl7.org/fhir/R4/terminologies.html) |  [AdministrativeGender](https://hl7.org/fhir/R4/valueset-administrative-gender.html) ([Required](https://hl7.org/fhir/R4/terminologies.html#required))  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [code](https://hl7.org/fhir/R4/datatypes.html#code)  
Requirements |  Needed to address the person correctly.  
**Patient.contact.organization**  
Element Id | Patient.contact.organization  
Definition |  Organization on behalf of which the contact is acting or for which the contact is working.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Type](https://hl7.org/fhir/R4/datatypes.html) |  [Reference](https://hl7.org/fhir/R4/references.html#Reference)([Organization](https://hl7.org/fhir/R4/organization.html))  
Requirements |  For guardians or business related contacts, the organization is relevant.  
Invariants |  | **Affect this element**  
---  
**pat-1** |  [Rule](https://hl7.org/fhir/R4/conformance-rules.html#rule) | SHALL at least contain a contact's details or a reference to an organization | name.exists() or telecom.exists() or address.exists() or organization.exists()  
**Patient.contact.period**  
Element Id | Patient.contact.period  
Definition |  The period during which this contact person or organization is valid to be contacted relating to this patient.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [Period](https://hl7.org/fhir/R4/datatypes.html#Period)  
**Patient.communication**  
Element Id | Patient.communication  
Definition |  A language which may be used to communicate with the patient about his or her health.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
Requirements |  If a patient does not speak the local language, interpreters may be required, so languages spoken and proficiency are important things to keep track of both for patient and other persons of interest.  
Comments |  If no language is specified, this _implies_ that the default local language is spoken. If you need to convey proficiency for multiple modes, then you need multiple Patient.Communication associations. For animals, language is not a relevant field, and should be absent from the instance. If the Patient does not speak the default local language, then the Interpreter Required Standard can be used to explicitly declare that an interpreter is required.  
**Patient.communication.language**  
Element Id | Patient.communication.language  
Definition |  The ISO-639-1 alpha 2 code in lower case for the language, optionally followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in upper case; e.g. "en" for English, or "en-US" for American English versus "en-EN" for England English.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 1..1  
[Terminology Binding](https://hl7.org/fhir/R4/terminologies.html) |  [Common Languages](https://hl7.org/fhir/R4/valueset-languages.html) ([Preferred](https://hl7.org/fhir/R4/terminologies.html#preferred) but limited to [All Languages](https://hl7.org/fhir/R4/valueset-all-languages.html))  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](https://hl7.org/fhir/R4/datatypes.html#CodeableConcept)  
Requirements |  Most systems in multilingual countries will want to convey language. Not all systems actually need the regional dialect.  
Comments |  The structure aa-BB with this exact casing is one the most widely used notations for locale. However not all systems actually code this but instead have it as free text. Hence CodeableConcept instead of code as the data type.  
**Patient.communication.preferred**  
Element Id | Patient.communication.preferred  
Definition |  Indicates whether or not the patient prefers this language (over other languages he masters up a certain level).  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [boolean](https://hl7.org/fhir/R4/datatypes.html#boolean)  
Requirements |  People that master multiple languages up to certain level may prefer one or more, i.e. feel more confident in communicating in a particular language making other languages sort of a fall back method.  
Comments |  This language is specifically identified for communicating healthcare information.  
**Patient.generalPractitioner**  
Element Id | Patient.generalPractitioner  
Definition |  Patient's nominated care provider.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
[Type](https://hl7.org/fhir/R4/datatypes.html) |  [Reference](https://hl7.org/fhir/R4/references.html#Reference)([Organization](https://hl7.org/fhir/R4/organization.html) | [Practitioner](https://hl7.org/fhir/R4/practitioner.html) | [PractitionerRole](https://hl7.org/fhir/R4/practitionerrole.html))  
Alternate Names | careProvider  
Comments |  This may be the primary care provider (in a GP context), or it may be a patient nominated care manager in a community/disability setting, or even organization that will provide people to perform the care provider roles. It is not to be used to record Care Teams, these should be in a CareTeam resource that may be linked to the CarePlan or EpisodeOfCare resources. Multiple GPs may be recorded against the patient for various reasons, such as a student that has his home GP listed along with the GP at university during the school semesters, or a "fly-in/fly-out" worker that has the onsite GP also included with his home GP to remain aware of medical issues. Jurisdictions may decide that they can profile this down to 1 if desired, or 1 per type.  
**Patient.managingOrganization**  
Element Id | Patient.managingOrganization  
Definition |  Organization that is the custodian of the patient record.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..1  
[Type](https://hl7.org/fhir/R4/datatypes.html) |  [Reference](https://hl7.org/fhir/R4/references.html#Reference)([Organization](https://hl7.org/fhir/R4/organization.html))  
Requirements |  Need to know who recognizes this patient record, manages and updates it.  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
Comments |  There is only one managing organization for a specific patient record. Other organizations will have their own Patient record, and may use the Link property to join the records together (or a Person resource which can include confidence ratings for the association).  
**Patient.link**  
Element Id | Patient.link  
Definition |  Link to another patient resource that concerns the same actual patient.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 0..*  
[Is Modifier](https://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true (Reason: This element is labeled as a modifier because it might not be the main Patient resource, and the referenced patient should be used instead of this Patient record. This is when the link.type value is 'replaced-by')  
Requirements |  There are multiple use cases:
  * Duplicate patient records due to the clerical errors associated with the difficulties of identifying humans consistently, and
  * Distribution of patient information across multiple servers.

  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
Comments |  There is no assumption that linked patient records have mutual links.  
**Patient.link.other**  
Element Id | Patient.link.other  
Definition |  The other patient resource that the link refers to.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 1..1  
[Type](https://hl7.org/fhir/R4/datatypes.html) |  [Reference](https://hl7.org/fhir/R4/references.html#Reference)([Patient](https://hl7.org/fhir/R4/patient.html) | [RelatedPerson](https://hl7.org/fhir/R4/relatedperson.html))  
[Hierarchy](https://hl7.org/fhir/R4/references.html#circular) | This reference may point back to the same instance (including transitively)  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
Comments |  Referencing a RelatedPerson here removes the need to use a Person record to associate a Patient and RelatedPerson as the same individual.  
**Patient.link.type**  
Element Id | Patient.link.type  
Definition |  The type of link between this patient resource and another patient resource.  
[Cardinality](https://hl7.org/fhir/R4/conformance-rules.html#cardinality) | 1..1  
[Terminology Binding](https://hl7.org/fhir/R4/terminologies.html) |  [LinkType](https://hl7.org/fhir/R4/valueset-link-type.html) ([Required](https://hl7.org/fhir/R4/terminologies.html#required))  
[Type](https://hl7.org/fhir/R4/datatypes.html) | [code](https://hl7.org/fhir/R4/datatypes.html#code)  
[Summary](https://hl7.org/fhir/R4/search.html#summary) | true  
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:36+1100. [QA Page](https://hl7.org/fhir/R4/qa.html)   
Links: [Search ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/search.cfm) | [Version History](https://hl7.org/fhir/R4/history.html) | [Table of Contents](https://hl7.org/fhir/R4/toc.html) | [Credits](https://hl7.org/fhir/R4/credits.html) | [Compare to R3 ![](https://hl7.org/fhir/R4/external.png)](https://www.fhir.org/perl/htmldiff.pl?oldfile=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fpatient-definitions.html&newfile=http%3A%2F%2Fhl7.org%2Ffhir%2FR4%2Fpatient-definitions.html) | [![CC0](https://hl7.org/fhir/R4/cc0.png)](https://hl7.org/fhir/R4/license.html) | [Propose a change ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir-issues)
