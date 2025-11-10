---
url: https://hl7.org/fhir/R4/auditevent.html
title: auditevent.html
source: official_download
extracted: local_file_conversion
mirror_path: auditevent.html
---

[![logo fhir](./assets/images/fhir-logo-www.png) ](http://hl7.org/fhir)
**Release 4**
[ ![visit the hl7 website](./assets/images/hl7-logo.png) ](http://www.hl7.org)
[![Search FHIR](./assets/images/search.png)](http://hl7.org/fhir/search.cfm)
[FHIR](index.html)
  * [Home](./index.html)
  * [Getting Started](./modules.html)
  * [Documentation](./documentation.html)
  * [Resources](./resourcelist.html)
  * [Profiles](./profilelist.html)
  * [Extensions](./extensibility-registry.html)
  * [Operations](./operationslist.html)
  * [Terminologies](./terminologies-systems.html)


  * [![](secpriv.jpg) Security and Privacy](secpriv-module.html)
  * **AuditEvent**


**This page is part of a downloaded copy of this specification.** This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html)
  * [Content](#)
  * [Examples](auditevent-examples.html)
  * [Detailed Descriptions](auditevent-definitions.html)
  * [Mappings](auditevent-mappings.html)
  * [Profiles & Extensions](auditevent-profiles.html)
  * [R3 Conversions](auditevent-version-maps.html)


#  6.4 Resource AuditEvent - Content [](auditevent.html#6.4 "link to here")
[Security ![](external.png)](http://www.hl7.org/Special/committees/secure/index.cfm) Work Group |  [Maturity Level](versions.html#maturity): 3 |  [Trial Use](versions.html#std-process "Standard Status") |  [Security Category](security.html#SecPrivConsiderations): Not Classified |  [Compartments](compartmentdefinition.html): [Device](compartmentdefinition-device.html), [Patient](compartmentdefinition-patient.html), [Practitioner](compartmentdefinition-practitioner.html)  
---|---|---|---|---  
A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.
##  6.4.1 Scope and Usage [](auditevent.html#scope "link to here")
The audit event is based on the IHE-ATNA Audit record definitions, originally from [RFC 3881 ![](external.png)](http://tools.ietf.org/html/rfc3881), and now managed by DICOM (see [DICOM Part 15 Annex A5 ![](external.png)](http://medical.nema.org/medical/dicom/current/output/html/part15.html#sect_A.5)). 
  * ASTM E2147 – Setup the concept of security audit logs for healthcare including accounting of disclosures
  * IETF RFC 3881 – Defined the Information Model (IETF rule forced this to be informative)
  * DICOM Audit Log Message – Made the information model Normative, defined Vocabulary, Transport Binding, and Schema
  * IHE ATNA – Defines the grouping with secure transport and access controls; and defined specific audit log records for specific IHE transactions.
  * NIST SP800-92 – Shows how to do audit log management and reporting – consistent with our model
  * HL7 PASS – Defined an Audit Service with responsibilities and a query interface for reporting use
  * ISO 27789 – Defined the subset of audit events that an EHR would need 
  * ISO/HL7 10781 EHR System Functional Model Release 2
  * ISO 21089 Trusted End-to-End Information Flows


This resource is managed collaboratively between HL7, DICOM, and IHE. 
The primary purpose of this resource is the maintenance of security audit log information. However, it can also be used for any audit logging needs and simple event-based notification. 
##  6.4.2 Background and Context [](auditevent.html#bnc "link to here")
All actors - such as applications, processes, and services - involved in an auditable event should record an AuditEvent. This will likely result in multiple AuditEvent entries that show whether privacy and security safeguards, such as access control, are properly functioning across an enterprise's system-of-systems. Thus, it is typical to get an auditable event recorded by both the application in a workflow process and the servers that support them. For this reason, duplicate entries are expected, which is helpful because it may aid in the detection of. For example, fewer than expected actors being recorded in a multi-actor process or attributes related to those records being in conflict, which is an indication of a security problem. There may be non-participating actors, such as trusted intermediary, that also detect a security relevant event and thus would record an AuditEvent, such as a trusted intermediary. 
Security relevant events are not limited to communications or RESTful events. They include: 
  * software start-up and shutdown;
  * user login and logout; 
  * access control decisions; 
  * configuration events; 
  * software installation; 
  * policy rules changes; and 
  * manipulation of data that exposes the data to users. 


See the [Audit Event Sub-Type](valueset-audit-event-sub-type.html) vocabulary for guidance on some security relevant events. 
The content of an AuditEvent is intended for use by security system administrators, security and privacy information managers, and records management personnel. This content is not intended to be accessible or used directly by other healthcare users, such as providers or patients, although reports generated from the raw data would be useful. An example is a patient-centric accounting of disclosures or an access report. Servers that provide support for AuditEvent resources would not generally accept update or delete operations on the resources, as this would compromise the integrity of the audit record. Access to the AuditEvent would typically be limited to security, privacy, or other system administration purposes. 
Relationship of AuditEvent and Provenance resources are often (though not exclusively) created by the application responding to the create/read/query/update/delete/execute etc. event. A [Provenance](provenance.html) resource contains overlapping information, but is a record-keeping assertion that gathers information about the context in which the information in a resource "came to be" in its current state, e.g., whether it was created de novo or obtained from another entity in whole, part, or by transformation. Provenance resources are prepared by the application that initiates the create/update of the resource and may be persisted with the AuditEvent target resource. 
##  6.4.3 Resource Content [](auditevent.html#resource "link to here")
  * [Structure](#tabs-struc)
  * [UML](#tabs-uml)
  * [XML](#tabs-xml)
  * [JSON](#tabs-json)
  * [Turtle](#tabs-ttl)
  * [R3 Diff](#tabs-diff)
  * [All](#tabs-all)


**Structure**
[Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") |  [Description & Constraints](formats.html#table "Additional information about the element")[![doco](help16.png)](formats.html#table "Legend for this format")  
---|---|---|---|---  
![.](tbl_spacer.png)![.](icon_resource.png) [AuditEvent](auditevent-definitions.html#AuditEvent "AuditEvent : A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Event record kept for security purposes  
Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.

Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource \(including cannot change the meaning of modifierExtension itself\).")  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](auditevent-definitions.html#AuditEvent.type "AuditEvent.type : Identifier for a family of the event.  For example, a menu item, program, rule, policy, function code, application name or URL. It identifies the performed function.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Coding](datatypes.html#Coding) | Type/identifier of event  
[Audit Event ID](valueset-audit-event-type.html "Type of event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [subtype](auditevent-definitions.html#AuditEvent.subtype "AuditEvent.subtype : Identifier for the category of event.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Coding](datatypes.html#Coding) | More specific type/id for the event  
[Audit Event Sub-Type](valueset-audit-event-sub-type.html "Sub-type of event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [action](auditevent-definitions.html#AuditEvent.action "AuditEvent.action : Indicator for type of action performed during the event that generated the audit.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Type of action performed during the event  
[AuditEventAction](valueset-audit-event-action.html "Indicator for type of action performed during the event that generated the event.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [period](auditevent-definitions.html#AuditEvent.period "AuditEvent.period : The period during which the activity occurred.") |  | 0..1 | [Period](datatypes.html#Period) | When the activity occurred  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [recorded](auditevent-definitions.html#AuditEvent.recorded "AuditEvent.recorded : The time when the event was recorded.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [instant](datatypes.html#instant) | Time when the event was recorded  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [outcome](auditevent-definitions.html#AuditEvent.outcome "AuditEvent.outcome : Indicates whether the event succeeded or failed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Whether the event succeeded or failed  
[AuditEventOutcome](valueset-audit-event-outcome.html "Indicates whether the event succeeded or failed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [outcomeDesc](auditevent-definitions.html#AuditEvent.outcomeDesc "AuditEvent.outcomeDesc : A free text description of the outcome of the event.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Description of the event outcome  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [purposeOfEvent](auditevent-definitions.html#AuditEvent.purposeOfEvent "AuditEvent.purposeOfEvent : The purposeOfUse \(reason\) that was used during the event being recorded.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | The purposeOfUse of the event  
[V3 Value SetPurposeOfUse](v3/PurposeOfUse/vs.html "The reason the activity took place.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [agent](auditevent-definitions.html#AuditEvent.agent "AuditEvent.agent : An actor taking an active role in the event or activity that is logged.") |  | 1..* | [BackboneElement](backboneelement.html) | Actor involved in the event  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](auditevent-definitions.html#AuditEvent.agent.type "AuditEvent.agent.type : Specification of the participation type the user plays when performing the event.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | How agent participated  
[ParticipationRoleType](valueset-participation-role-type.html "The Participation type of the agent to the event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [role](auditevent-definitions.html#AuditEvent.agent.role "AuditEvent.agent.role : The security role that the user was acting under, that come from local codes defined by the access control security system \(e.g. RBAC, ABAC\) used in the local context.") |  | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Agent role in the event  
[SecurityRoleType](valueset-security-role-type.html "What security role enabled the agent to participate in the event.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included."))  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [who](auditevent-definitions.html#AuditEvent.agent.who "AuditEvent.agent.who : Reference to who this agent is that was involved in the event.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  [Reference](references.html#Reference)([PractitionerRole](practitionerrole.html) | [Practitioner](practitioner.html) | [Organization](organization.html) | [Device](device.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Identifier of who  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [altId](auditevent-definitions.html#AuditEvent.agent.altId "AuditEvent.agent.altId : Alternative agent Identifier. For a human, this should be a user identifier text string from authentication system. This identifier would be one known to a common authentication system \(e.g. single sign-on\), if available.") |  | 0..1 | [string](datatypes.html#string) | Alternative User identity  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](auditevent-definitions.html#AuditEvent.agent.name "AuditEvent.agent.name : Human-meaningful name for the agent.") |  | 0..1 | [string](datatypes.html#string) | Human friendly name for the agent  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [requestor](auditevent-definitions.html#AuditEvent.agent.requestor "AuditEvent.agent.requestor : Indicator that the user is or is not the requestor, or initiator, for the event being audited.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [boolean](datatypes.html#boolean) | Whether user is initiator  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [location](auditevent-definitions.html#AuditEvent.agent.location "AuditEvent.agent.location : Where the event occurred.") |  | 0..1 |  [Reference](references.html#Reference)([Location](location.html)) | Where  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [policy](auditevent-definitions.html#AuditEvent.agent.policy "AuditEvent.agent.policy : The policy or plan that authorized the activity being recorded. Typically, a single activity may have multiple applicable policies, such as patient consent, guarantor funding, etc. The policy would also indicate the security token used.") |  | 0..* | [uri](datatypes.html#uri) | Policy that authorized event  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [media](auditevent-definitions.html#AuditEvent.agent.media "AuditEvent.agent.media : Type of media involved. Used when the event is about exporting/importing onto media.") |  | 0..1 | [Coding](datatypes.html#Coding) | Type of media  
[Media Type Code](valueset-dicm-405-mediatype.html "Used when the event is about exporting/importing onto media.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_element.gif) [network](auditevent-definitions.html#AuditEvent.agent.network "AuditEvent.agent.network : Logical network location for application activity, if the activity has a network location.") |  | 0..1 | [BackboneElement](backboneelement.html) | Logical network location for application activity  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [address](auditevent-definitions.html#AuditEvent.agent.network.address "AuditEvent.agent.network.address : An identifier for the network access point of the user device for the audit event.") |  | 0..1 | [string](datatypes.html#string) | Identifier for the network access point of the user device  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [type](auditevent-definitions.html#AuditEvent.agent.network.type "AuditEvent.agent.network.type : An identifier for the type of network access point that originated the audit event.") |  | 0..1 | [code](datatypes.html#code) | The type of network access point  
[AuditEventAgentNetworkType](valueset-network-type.html "The type of network access point of this agent in the audit event.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_datatype.gif) [purposeOfUse](auditevent-definitions.html#AuditEvent.agent.purposeOfUse "AuditEvent.agent.purposeOfUse : The reason \(purpose of use\), specific to this agent, that was used during the event being recorded.") |  | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Reason given for this user  
[V3 Value SetPurposeOfUse](v3/PurposeOfUse/vs.html "The reason the activity took place.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [source](auditevent-definitions.html#AuditEvent.source "AuditEvent.source : The system that is reporting the event.") |  | 1..1 | [BackboneElement](backboneelement.html) | Audit Event Reporter  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [site](auditevent-definitions.html#AuditEvent.source.site "AuditEvent.source.site : Logical source location within the healthcare enterprise network.  For example, a hospital or other provider location within a multi-entity provider group.") |  | 0..1 | [string](datatypes.html#string) | Logical source location within the enterprise  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [observer](auditevent-definitions.html#AuditEvent.source.observer "AuditEvent.source.observer : Identifier of the source where the event was detected.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [Reference](references.html#Reference)([PractitionerRole](practitionerrole.html) | [Practitioner](practitioner.html) | [Organization](organization.html) | [Device](device.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | The identity of source detecting the event  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_datatype.gif) [type](auditevent-definitions.html#AuditEvent.source.type "AuditEvent.source.type : Code specifying the type of source where event originated.") |  | 0..* | [Coding](datatypes.html#Coding) | The type of source where event originated  
[Audit Event Source Type](valueset-audit-source-type.html "Code specifying the type of system that detected and recorded the event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [entity](auditevent-definitions.html#AuditEvent.entity "AuditEvent.entity : Specific instances of data or objects that have been accessed.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..* | [BackboneElement](backboneelement.html) | Data or objects used  
+ Rule: Either a name or a query (NOT both)  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_reference.png) [what](auditevent-definitions.html#AuditEvent.entity.what "AuditEvent.entity.what : Identifies a specific instance of the entity. The reference should be version specific.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  [Reference](references.html#Reference)([Any](resourcelist.html)) | Specific instance of resource  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](auditevent-definitions.html#AuditEvent.entity.type "AuditEvent.entity.type : The type of the object that was involved in this audit event.") |  | 0..1 | [Coding](datatypes.html#Coding) | Type of entity involved  
[Audit event entity type](valueset-audit-entity-type.html "Code for the entity type involved in the audit event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [role](auditevent-definitions.html#AuditEvent.entity.role "AuditEvent.entity.role : Code representing the role the entity played in the event being audited.") |  | 0..1 | [Coding](datatypes.html#Coding) | What role the entity played  
[AuditEventEntityRole](valueset-object-role.html "Code representing the role the entity played in the audit event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [lifecycle](auditevent-definitions.html#AuditEvent.entity.lifecycle "AuditEvent.entity.lifecycle : Identifier for the data life-cycle stage for the entity.") |  | 0..1 | [Coding](datatypes.html#Coding) | Life-cycle stage for the entity  
[ObjectLifecycleEvents](valueset-object-lifecycle-events.html "Identifier for the data life-cycle stage for the entity.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [securityLabel](auditevent-definitions.html#AuditEvent.entity.securityLabel "AuditEvent.entity.securityLabel : Security labels for the identified entity.") |  | 0..* | [Coding](datatypes.html#Coding) | Security labels on the entity  
[SecurityLabels](valueset-security-labels.html "Security Labels from the Healthcare Privacy and Security Classification System.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](auditevent-definitions.html#AuditEvent.entity.name "AuditEvent.entity.name : A name of the entity in the audit event.") |  [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Descriptor for entity  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [description](auditevent-definitions.html#AuditEvent.entity.description "AuditEvent.entity.description : Text that describes the entity in more detail.") |  | 0..1 | [string](datatypes.html#string) | Descriptive text  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [query](auditevent-definitions.html#AuditEvent.entity.query "AuditEvent.entity.query : The query parameters for a query-type entities.") |  [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [base64Binary](datatypes.html#base64Binary) | Query parameters  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [detail](auditevent-definitions.html#AuditEvent.entity.detail "AuditEvent.entity.detail : Tagged value pairs for conveying additional information about the entity.") |  | 0..* | [BackboneElement](backboneelement.html) | Additional Information about the entity  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [type](auditevent-definitions.html#AuditEvent.entity.detail.type "AuditEvent.entity.detail.type : The type of extra detail provided in the value.") |  | 1..1 | [string](datatypes.html#string) | Name of the property  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_choice.gif) [value[x]](auditevent-definitions.html#AuditEvent.entity.detail.value_x_ "AuditEvent.entity.detail.value\[x\] : The  value of the extra detail.") |  | 1..1 |  | Property value  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) valueString |  |  | [string](datatypes.html#string) |   
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) valueBase64Binary |  |  | [base64Binary](datatypes.html#base64Binary) |   
  
[![doco](help16.png) Documentation for this format](formats.html#table "Legend for this format")  
**UML Diagram** ([Legend](formats.html#uml))
AuditEvent (DomainResource)Identifier for a family of the event. For example, a menu item, program, rule, policy, function code, application name or URL. It identifies the performed functiontype : Coding [1..1] « Type of event. (Strength=Extensible)AuditEventID+ »Identifier for the category of eventsubtype : Coding [0..*] « Sub-type of event. (Strength=Extensible)AuditEventSub-Type+ »Indicator for type of action performed during the event that generated the auditaction : code [0..1] « Indicator for type of action performed during the event that generated the event. (Strength=Required)AuditEventAction! »The period during which the activity occurredperiod : Period [0..1]The time when the event was recordedrecorded : instant [1..1]Indicates whether the event succeeded or failedoutcome : code [0..1] « Indicates whether the event succeeded or failed. (Strength=Required)AuditEventOutcome! »A free text description of the outcome of the eventoutcomeDesc : string [0..1]The purposeOfUse (reason) that was used during the event being recordedpurposeOfEvent : CodeableConcept [0..*] « The reason the activity took place. (Strength=Extensible)v3.PurposeOfUse+ »AgentSpecification of the participation type the user plays when performing the eventtype : CodeableConcept [0..1] « The Participation type of the agent to the event. (Strength=Extensible)ParticipationRoleType+ »The security role that the user was acting under, that come from local codes defined by the access control security system (e.g. RBAC, ABAC) used in the local contextrole : CodeableConcept [0..*] « What security role enabled the agent to participate in the event. (Strength=Example)SecurityRoleType?? »Reference to who this agent is that was involved in the eventwho : Reference [0..1] « PractitionerRole|Practitioner|Organization| Device|Patient|RelatedPerson »Alternative agent Identifier. For a human, this should be a user identifier text string from authentication system. This identifier would be one known to a common authentication system (e.g. single sign-on), if availablealtId : string [0..1]Human-meaningful name for the agentname : string [0..1]Indicator that the user is or is not the requestor, or initiator, for the event being auditedrequestor : boolean [1..1]Where the event occurredlocation : Reference [0..1] « Location »The policy or plan that authorized the activity being recorded. Typically, a single activity may have multiple applicable policies, such as patient consent, guarantor funding, etc. The policy would also indicate the security token usedpolicy : uri [0..*]Type of media involved. Used when the event is about exporting/importing onto mediamedia : Coding [0..1] « Used when the event is about exporting/importing onto media. (Strength=Extensible)MediaTypeCode+ »The reason (purpose of use), specific to this agent, that was used during the event being recordedpurposeOfUse : CodeableConcept [0..*] « The reason the activity took place. (Strength=Extensible)v3.PurposeOfUse+ »NetworkAn identifier for the network access point of the user device for the audit eventaddress : string [0..1]An identifier for the type of network access point that originated the audit eventtype : code [0..1] « The type of network access point of this agent in the audit event. (Strength=Required)AuditEventAgentNetworkType! »SourceLogical source location within the healthcare enterprise network. For example, a hospital or other provider location within a multi-entity provider groupsite : string [0..1]Identifier of the source where the event was detectedobserver : Reference [1..1] « PractitionerRole|Practitioner| Organization|Device|Patient|RelatedPerson »Code specifying the type of source where event originatedtype : Coding [0..*] « Code specifying the type of system that detected and recorded the event. (Strength=Extensible)AuditEventSourceType+ »EntityIdentifies a specific instance of the entity. The reference should be version specificwhat : Reference [0..1] « Any »The type of the object that was involved in this audit eventtype : Coding [0..1] « Code for the entity type involved in the audit event. (Strength=Extensible)AuditEventEntityType+ »Code representing the role the entity played in the event being auditedrole : Coding [0..1] « Code representing the role the entity played in the audit event. (Strength=Extensible)AuditEventEntityRole+ »Identifier for the data life-cycle stage for the entitylifecycle : Coding [0..1] « Identifier for the data life-cycle stage for the entity. (Strength=Extensible)ObjectLifecycleEvents+ »Security labels for the identified entitysecurityLabel : Coding [0..*] « Security Labels from the Healthcare Privacy and Security Classification System. (Strength=Extensible)All Security Labels+ »A name of the entity in the audit eventname : string [0..1]Text that describes the entity in more detaildescription : string [0..1]The query parameters for a query-type entitiesquery : base64Binary [0..1]DetailThe type of extra detail provided in the valuetype : string [1..1]The value of the extra detailvalue[x] : Type [1..1] « string|base64Binary »Logical network location for application activity, if the activity has a network locationnetwork[0..1]An actor taking an active role in the event or activity that is loggedagent[1..*]The system that is reporting the eventsource[1..1]Tagged value pairs for conveying additional information about the entitydetail[0..*]Specific instances of data or objects that have been accessedentity[0..*]
**XML Template**
```

<[**AuditEvent**](auditevent-definitions.html#AuditEvent "A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.") xmlns="http://hl7.org/fhir"> [![doco](help.png)](xml.html "Documentation for this format")
 <!-- from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language) -->
 <!-- from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension) -->
 <[**type**](auditevent-definitions.html#AuditEvent.type "Identifier for a family of the event.  For example, a menu item, program, rule, policy, function code, application name or URL. It identifies the performed function.")><!-- **1..1** Coding[](datatypes.html#Coding) Type/identifier of event[](valueset-audit-event-type.html) --></type>
 <[**subtype**](auditevent-definitions.html#AuditEvent.subtype "Identifier for the category of event.")><!-- **0..*** Coding[](datatypes.html#Coding) More specific type/id for the event[](valueset-audit-event-sub-type.html) --></subtype>
 <[**action**](auditevent-definitions.html#AuditEvent.action "Indicator for type of action performed during the event that generated the audit.") value="[code[](datatypes.html#code)]"/><!-- **0..1** Type of action performed during the event[](valueset-audit-event-action.html) -->
 <[**period**](auditevent-definitions.html#AuditEvent.period "The period during which the activity occurred.")><!-- **0..1** Period[](datatypes.html#Period) When the activity occurred[](terminologies.html#unbound) --></period>
 <[**recorded**](auditevent-definitions.html#AuditEvent.recorded "The time when the event was recorded.") value="[instant[](datatypes.html#instant)]"/><!-- **1..1** Time when the event was recorded[](terminologies.html#unbound) -->
 <[**outcome**](auditevent-definitions.html#AuditEvent.outcome "Indicates whether the event succeeded or failed.") value="[code[](datatypes.html#code)]"/><!-- **0..1** Whether the event succeeded or failed[](valueset-audit-event-outcome.html) -->
 <[**outcomeDesc**](auditevent-definitions.html#AuditEvent.outcomeDesc "A free text description of the outcome of the event.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Description of the event outcome[](terminologies.html#unbound) -->
 <[**purposeOfEvent**](auditevent-definitions.html#AuditEvent.purposeOfEvent "The purposeOfUse \(reason\) that was used during the event being recorded.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) The purposeOfUse of the event[](v3/PurposeOfUse/vs.html) --></purposeOfEvent>
 <[**agent**](auditevent-definitions.html#AuditEvent.agent "An actor taking an active role in the event or activity that is logged.")>  <!-- **1..*** Actor involved in the event -->
  <[**type**](auditevent-definitions.html#AuditEvent.agent.type "Specification of the participation type the user plays when performing the event.")><!-- **0..1** CodeableConcept[](datatypes.html#CodeableConcept) How agent participated[](valueset-participation-role-type.html) --></type>
  <[**role**](auditevent-definitions.html#AuditEvent.agent.role "The security role that the user was acting under, that come from local codes defined by the access control security system \(e.g. RBAC, ABAC\) used in the local context.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) Agent role in the event[](valueset-security-role-type.html) --></role>
  <[**who**](auditevent-definitions.html#AuditEvent.agent.who "Reference to who this agent is that was involved in the event.")><!-- **0..1** Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|
    Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) Identifier of who[](terminologies.html#unbound) --></who>
  <[**altId**](auditevent-definitions.html#AuditEvent.agent.altId "Alternative agent Identifier. For a human, this should be a user identifier text string from authentication system. This identifier would be one known to a common authentication system \(e.g. single sign-on\), if available.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Alternative User identity[](terminologies.html#unbound) -->
  <[**name**](auditevent-definitions.html#AuditEvent.agent.name "Human-meaningful name for the agent.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Human friendly name for the agent[](terminologies.html#unbound) -->
  <[**requestor**](auditevent-definitions.html#AuditEvent.agent.requestor "Indicator that the user is or is not the requestor, or initiator, for the event being audited.") value="[boolean[](datatypes.html#boolean)]"/><!-- **1..1** Whether user is initiator[](terminologies.html#unbound) -->
  <[**location**](auditevent-definitions.html#AuditEvent.agent.location "Where the event occurred.")><!-- **0..1** Reference[](references.html#Reference)(Location[](location.html#Location)) Where[](terminologies.html#unbound) --></location>
  <[**policy**](auditevent-definitions.html#AuditEvent.agent.policy "The policy or plan that authorized the activity being recorded. Typically, a single activity may have multiple applicable policies, such as patient consent, guarantor funding, etc. The policy would also indicate the security token used.") value="[uri[](datatypes.html#uri)]"/><!-- **0..*** Policy that authorized event[](terminologies.html#unbound) -->
  <[**media**](auditevent-definitions.html#AuditEvent.agent.media "Type of media involved. Used when the event is about exporting/importing onto media.")><!-- **0..1** Coding[](datatypes.html#Coding) Type of media[](valueset-dicm-405-mediatype.html) --></media>
  <[**network**](auditevent-definitions.html#AuditEvent.agent.network "Logical network location for application activity, if the activity has a network location.")>  <!-- **0..1** Logical network location for application activity -->
   <[**address**](auditevent-definitions.html#AuditEvent.agent.network.address "An identifier for the network access point of the user device for the audit event.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Identifier for the network access point of the user device[](terminologies.html#unbound) -->
   <[**type**](auditevent-definitions.html#AuditEvent.agent.network.type "An identifier for the type of network access point that originated the audit event.") value="[code[](datatypes.html#code)]"/><!-- **0..1** The type of network access point[](valueset-network-type.html) -->
  </network>
  <[**purposeOfUse**](auditevent-definitions.html#AuditEvent.agent.purposeOfUse "The reason \(purpose of use\), specific to this agent, that was used during the event being recorded.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) Reason given for this user[](v3/PurposeOfUse/vs.html) --></purposeOfUse>
 </agent>
 <[**source**](auditevent-definitions.html#AuditEvent.source "The system that is reporting the event.")>  <!-- **1..1** Audit Event Reporter -->
  <[**site**](auditevent-definitions.html#AuditEvent.source.site "Logical source location within the healthcare enterprise network.  For example, a hospital or other provider location within a multi-entity provider group.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Logical source location within the enterprise[](terminologies.html#unbound) -->
  <[**observer**](auditevent-definitions.html#AuditEvent.source.observer "Identifier of the source where the event was detected.")><!-- **1..1** Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|
    Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) The identity of source detecting the event[](terminologies.html#unbound) --></observer>
  <[**type**](auditevent-definitions.html#AuditEvent.source.type "Code specifying the type of source where event originated.")><!-- **0..*** Coding[](datatypes.html#Coding) The type of source where event originated[](valueset-audit-source-type.html) --></type>
 </source>
 <[**entity**](auditevent-definitions.html#AuditEvent.entity "Specific instances of data or objects that have been accessed.")>  <!-- **0..*** Data or objects used -->
  <[**what**](auditevent-definitions.html#AuditEvent.entity.what "Identifies a specific instance of the entity. The reference should be version specific.")><!-- **0..1** Reference[](references.html#Reference)(Any[](resourcelist.html)) Specific instance of resource[](terminologies.html#unbound) --></what>
  <[**type**](auditevent-definitions.html#AuditEvent.entity.type "The type of the object that was involved in this audit event.")><!-- **0..1** Coding[](datatypes.html#Coding) Type of entity involved[](valueset-audit-entity-type.html) --></type>
  <[**role**](auditevent-definitions.html#AuditEvent.entity.role "Code representing the role the entity played in the event being audited.")><!-- **0..1** Coding[](datatypes.html#Coding) What role the entity played[](valueset-object-role.html) --></role>
  <[**lifecycle**](auditevent-definitions.html#AuditEvent.entity.lifecycle "Identifier for the data life-cycle stage for the entity.")><!-- **0..1** Coding[](datatypes.html#Coding) Life-cycle stage for the entity[](valueset-object-lifecycle-events.html) --></lifecycle>
  <[**securityLabel**](auditevent-definitions.html#AuditEvent.entity.securityLabel "Security labels for the identified entity.")><!-- **0..*** Coding[](datatypes.html#Coding) Security labels on the entity[](valueset-security-labels.html) --></securityLabel>
  <[**name**](auditevent-definitions.html#AuditEvent.entity.name "A name of the entity in the audit event.") value="[string[](datatypes.html#string)]"/><!-- **![??](lock.png) 0..1** Descriptor for entity[](terminologies.html#unbound) -->
  <[**description**](auditevent-definitions.html#AuditEvent.entity.description "Text that describes the entity in more detail.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Descriptive text[](terminologies.html#unbound) -->
  <[**query**](auditevent-definitions.html#AuditEvent.entity.query "The query parameters for a query-type entities.") value="[base64Binary[](datatypes.html#base64Binary)]"/><!-- **![??](lock.png) 0..1** Query parameters[](terminologies.html#unbound) -->
  <[**detail**](auditevent-definitions.html#AuditEvent.entity.detail "Tagged value pairs for conveying additional information about the entity.")>  <!-- **0..*** Additional Information about the entity -->
   <[**type**](auditevent-definitions.html#AuditEvent.entity.detail.type "The type of extra detail provided in the value.") value="[string[](datatypes.html#string)]"/><!-- **1..1** Name of the property[](terminologies.html#unbound) -->
   <[**value[x]**](auditevent-definitions.html#AuditEvent.entity.detail.value\[x\] "The  value of the extra detail.")><!-- **1..1** string[](datatypes.html#string)|base64Binary[](datatypes.html#base64Binary) Property value[](terminologies.html#unbound) --></value[x]>
  </detail>
 </entity>
</AuditEvent>

```

**JSON Template**
```

{[![doco](help.png)](json.html "Documentation for this format")
  "resourceType" : "[**AuditEvent**](auditevent-definitions.html#AuditEvent "A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.")",
  // from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language)
  // from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension)
  "type[](auditevent-definitions.html#AuditEvent.type "Identifier for a family of the event.  For example, a menu item, program, rule, policy, function code, application name or URL. It identifies the performed function.")" : { Coding[](datatypes.html#Coding) }, // **R!**  Type/identifier of event[](valueset-audit-event-type.html)
  "subtype[](auditevent-definitions.html#AuditEvent.subtype "Identifier for the category of event.")" : [{ Coding[](datatypes.html#Coding) }], // More specific type/id for the event[](valueset-audit-event-sub-type.html)
  "action[](auditevent-definitions.html#AuditEvent.action "Indicator for type of action performed during the event that generated the audit.")" : "<code[](datatypes.html#code)>", // Type of action performed during the event[](valueset-audit-event-action.html)
  "period[](auditevent-definitions.html#AuditEvent.period "The period during which the activity occurred.")" : { Period[](datatypes.html#Period) }, // When the activity occurred[](terminologies.html#unbound)
  "recorded[](auditevent-definitions.html#AuditEvent.recorded "The time when the event was recorded.")" : "<instant[](datatypes.html#instant)>", // **R!**  Time when the event was recorded[](terminologies.html#unbound)
  "outcome[](auditevent-definitions.html#AuditEvent.outcome "Indicates whether the event succeeded or failed.")" : "<code[](datatypes.html#code)>", // Whether the event succeeded or failed[](valueset-audit-event-outcome.html)
  "outcomeDesc[](auditevent-definitions.html#AuditEvent.outcomeDesc "A free text description of the outcome of the event.")" : "<string[](datatypes.html#string)>", // Description of the event outcome[](terminologies.html#unbound)
  "purposeOfEvent[](auditevent-definitions.html#AuditEvent.purposeOfEvent "The purposeOfUse \(reason\) that was used during the event being recorded.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // The purposeOfUse of the event[](v3/PurposeOfUse/vs.html)
  "agent[](auditevent-definitions.html#AuditEvent.agent "An actor taking an active role in the event or activity that is logged.")" : [{ // **R!**  Actor involved in the event[](terminologies.html#unbound)
    "type[](auditevent-definitions.html#AuditEvent.agent.type "Specification of the participation type the user plays when performing the event.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // How agent participated[](valueset-participation-role-type.html)
    "role[](auditevent-definitions.html#AuditEvent.agent.role "The security role that the user was acting under, that come from local codes defined by the access control security system \(e.g. RBAC, ABAC\) used in the local context.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // Agent role in the event[](valueset-security-role-type.html)
    "who[](auditevent-definitions.html#AuditEvent.agent.who "Reference to who this agent is that was involved in the event.")" : { Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|
    Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) }, // Identifier of who[](terminologies.html#unbound)
    "altId[](auditevent-definitions.html#AuditEvent.agent.altId "Alternative agent Identifier. For a human, this should be a user identifier text string from authentication system. This identifier would be one known to a common authentication system \(e.g. single sign-on\), if available.")" : "<string[](datatypes.html#string)>", // Alternative User identity[](terminologies.html#unbound)
    "name[](auditevent-definitions.html#AuditEvent.agent.name "Human-meaningful name for the agent.")" : "<string[](datatypes.html#string)>", // Human friendly name for the agent[](terminologies.html#unbound)
    "requestor[](auditevent-definitions.html#AuditEvent.agent.requestor "Indicator that the user is or is not the requestor, or initiator, for the event being audited.")" : <boolean[](datatypes.html#boolean)>, // **R!**  Whether user is initiator[](terminologies.html#unbound)
    "location[](auditevent-definitions.html#AuditEvent.agent.location "Where the event occurred.")" : { Reference[](references.html#Reference)(Location[](location.html#Location)) }, // Where[](terminologies.html#unbound)
    "policy[](auditevent-definitions.html#AuditEvent.agent.policy "The policy or plan that authorized the activity being recorded. Typically, a single activity may have multiple applicable policies, such as patient consent, guarantor funding, etc. The policy would also indicate the security token used.")" : ["<uri[](datatypes.html#uri)>"], // Policy that authorized event[](terminologies.html#unbound)
    "media[](auditevent-definitions.html#AuditEvent.agent.media "Type of media involved. Used when the event is about exporting/importing onto media.")" : { Coding[](datatypes.html#Coding) }, // Type of media[](valueset-dicm-405-mediatype.html)
    "network[](auditevent-definitions.html#AuditEvent.agent.network "Logical network location for application activity, if the activity has a network location.")" : { // Logical network location for application activity[](terminologies.html#unbound)
      "address[](auditevent-definitions.html#AuditEvent.agent.network.address "An identifier for the network access point of the user device for the audit event.")" : "<string[](datatypes.html#string)>", // Identifier for the network access point of the user device[](terminologies.html#unbound)
      "type[](auditevent-definitions.html#AuditEvent.agent.network.type "An identifier for the type of network access point that originated the audit event.")" : "<code[](datatypes.html#code)>" // The type of network access point[](valueset-network-type.html)
    },
    "purposeOfUse[](auditevent-definitions.html#AuditEvent.agent.purposeOfUse "The reason \(purpose of use\), specific to this agent, that was used during the event being recorded.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }] // Reason given for this user[](v3/PurposeOfUse/vs.html)
  }],
  "source[](auditevent-definitions.html#AuditEvent.source "The system that is reporting the event.")" : { // **R!**  Audit Event Reporter[](terminologies.html#unbound)
    "site[](auditevent-definitions.html#AuditEvent.source.site "Logical source location within the healthcare enterprise network.  For example, a hospital or other provider location within a multi-entity provider group.")" : "<string[](datatypes.html#string)>", // Logical source location within the enterprise[](terminologies.html#unbound)
    "observer[](auditevent-definitions.html#AuditEvent.source.observer "Identifier of the source where the event was detected.")" : { Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|
    Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) }, // **R!**  The identity of source detecting the event[](terminologies.html#unbound)
    "type[](auditevent-definitions.html#AuditEvent.source.type "Code specifying the type of source where event originated.")" : [{ Coding[](datatypes.html#Coding) }] // The type of source where event originated[](valueset-audit-source-type.html)
  },
  "entity[](auditevent-definitions.html#AuditEvent.entity "Specific instances of data or objects that have been accessed.")" : [{ // Data or objects used[](terminologies.html#unbound)
    "what[](auditevent-definitions.html#AuditEvent.entity.what "Identifies a specific instance of the entity. The reference should be version specific.")" : { Reference[](references.html#Reference)(Any[](resourcelist.html)) }, // Specific instance of resource[](terminologies.html#unbound)
    "type[](auditevent-definitions.html#AuditEvent.entity.type "The type of the object that was involved in this audit event.")" : { Coding[](datatypes.html#Coding) }, // Type of entity involved[](valueset-audit-entity-type.html)
    "role[](auditevent-definitions.html#AuditEvent.entity.role "Code representing the role the entity played in the event being audited.")" : { Coding[](datatypes.html#Coding) }, // What role the entity played[](valueset-object-role.html)
    "lifecycle[](auditevent-definitions.html#AuditEvent.entity.lifecycle "Identifier for the data life-cycle stage for the entity.")" : { Coding[](datatypes.html#Coding) }, // Life-cycle stage for the entity[](valueset-object-lifecycle-events.html)
    "securityLabel[](auditevent-definitions.html#AuditEvent.entity.securityLabel "Security labels for the identified entity.")" : [{ Coding[](datatypes.html#Coding) }], // Security labels on the entity[](valueset-security-labels.html)
    "name[](auditevent-definitions.html#AuditEvent.entity.name "A name of the entity in the audit event.")" : "<string[](datatypes.html#string)>", // **C?** Descriptor for entity[](terminologies.html#unbound)
    "description[](auditevent-definitions.html#AuditEvent.entity.description "Text that describes the entity in more detail.")" : "<string[](datatypes.html#string)>", // Descriptive text[](terminologies.html#unbound)
    "query[](auditevent-definitions.html#AuditEvent.entity.query "The query parameters for a query-type entities.")" : "<base64Binary[](datatypes.html#base64Binary)>", // **C?** Query parameters[](terminologies.html#unbound)
    "detail[](auditevent-definitions.html#AuditEvent.entity.detail "Tagged value pairs for conveying additional information about the entity.")" : [{ // Additional Information about the entity[](terminologies.html#unbound)
      "type[](auditevent-definitions.html#AuditEvent.entity.detail.type "The type of extra detail provided in the value.")" : "<string[](datatypes.html#string)>", // **R!**  Name of the property[](terminologies.html#unbound)
      // value[x]: Property value. One of these 2:
      "valueString[](auditevent-definitions.html#AuditEvent.entity.detail.valueString "The  value of the extra detail.")" : "<string[](datatypes.html#string)>"
      "valueBase64Binary[](auditevent-definitions.html#AuditEvent.entity.detail.valueBase64Binary "The  value of the extra detail.")" : "<base64Binary[](datatypes.html#base64Binary)>"
    }]
  }]
}

```

**Turtle Template**
```

@prefix fhir: <http://hl7.org/fhir/> .[![doco](help.png)](rdf.html "Documentation for this format")


[ a fhir:[**AuditEvent**](auditevent-definitions.html#AuditEvent "A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.");
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource[](resource.html): .id[](resource.html#id), .meta[](resource.html#meta), .implicitRules[](resource.html#implicitRules), and .language[](resource.html#language)
  # from DomainResource[](domainresource.html): .text[](narrative.html#Narrative), .contained[](references.html#contained), .extension[](extensibility.html), and .modifierExtension[](extensibility.html#modifierExtension)
  fhir:AuditEvent.type[](auditevent-definitions.html#AuditEvent.type "Identifier for a family of the event.  For example, a menu item, program, rule, policy, function code, application name or URL. It identifies the performed function.") [ Coding[](datatypes.html#Coding) ]; # 1..1 Type/identifier of event
  fhir:AuditEvent.subtype[](auditevent-definitions.html#AuditEvent.subtype "Identifier for the category of event.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* More specific type/id for the event
  fhir:AuditEvent.action[](auditevent-definitions.html#AuditEvent.action "Indicator for type of action performed during the event that generated the audit.") [ code[](datatypes.html#code) ]; # 0..1 Type of action performed during the event
  fhir:AuditEvent.period[](auditevent-definitions.html#AuditEvent.period "The period during which the activity occurred.") [ Period[](datatypes.html#Period) ]; # 0..1 When the activity occurred
  fhir:AuditEvent.recorded[](auditevent-definitions.html#AuditEvent.recorded "The time when the event was recorded.") [ instant[](datatypes.html#instant) ]; # 1..1 Time when the event was recorded
  fhir:AuditEvent.outcome[](auditevent-definitions.html#AuditEvent.outcome "Indicates whether the event succeeded or failed.") [ code[](datatypes.html#code) ]; # 0..1 Whether the event succeeded or failed
  fhir:AuditEvent.outcomeDesc[](auditevent-definitions.html#AuditEvent.outcomeDesc "A free text description of the outcome of the event.") [ string[](datatypes.html#string) ]; # 0..1 Description of the event outcome
  fhir:AuditEvent.purposeOfEvent[](auditevent-definitions.html#AuditEvent.purposeOfEvent "The purposeOfUse \(reason\) that was used during the event being recorded.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* The purposeOfUse of the event
  fhir:AuditEvent.agent[](auditevent-definitions.html#AuditEvent.agent "An actor taking an active role in the event or activity that is logged.") [ # 1..* Actor involved in the event
    fhir:AuditEvent.agent.type[](auditevent-definitions.html#AuditEvent.agent.type "Specification of the participation type the user plays when performing the event.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 0..1 How agent participated
    fhir:AuditEvent.agent.role[](auditevent-definitions.html#AuditEvent.agent.role "The security role that the user was acting under, that come from local codes defined by the access control security system \(e.g. RBAC, ABAC\) used in the local context.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* Agent role in the event
    fhir:AuditEvent.agent.who[](auditevent-definitions.html#AuditEvent.agent.who "Reference to who this agent is that was involved in the event.") [ Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) ]; # 0..1 Identifier of who
    fhir:AuditEvent.agent.altId[](auditevent-definitions.html#AuditEvent.agent.altId "Alternative agent Identifier. For a human, this should be a user identifier text string from authentication system. This identifier would be one known to a common authentication system \(e.g. single sign-on\), if available.") [ string[](datatypes.html#string) ]; # 0..1 Alternative User identity
    fhir:AuditEvent.agent.name[](auditevent-definitions.html#AuditEvent.agent.name "Human-meaningful name for the agent.") [ string[](datatypes.html#string) ]; # 0..1 Human friendly name for the agent
    fhir:AuditEvent.agent.requestor[](auditevent-definitions.html#AuditEvent.agent.requestor "Indicator that the user is or is not the requestor, or initiator, for the event being audited.") [ boolean[](datatypes.html#boolean) ]; # 1..1 Whether user is initiator
    fhir:AuditEvent.agent.location[](auditevent-definitions.html#AuditEvent.agent.location "Where the event occurred.") [ Reference[](references.html#Reference)(Location[](location.html#Location)) ]; # 0..1 Where
    fhir:AuditEvent.agent.policy[](auditevent-definitions.html#AuditEvent.agent.policy "The policy or plan that authorized the activity being recorded. Typically, a single activity may have multiple applicable policies, such as patient consent, guarantor funding, etc. The policy would also indicate the security token used.") [ uri[](datatypes.html#uri) ], ... ; # 0..* Policy that authorized event
    fhir:AuditEvent.agent.media[](auditevent-definitions.html#AuditEvent.agent.media "Type of media involved. Used when the event is about exporting/importing onto media.") [ Coding[](datatypes.html#Coding) ]; # 0..1 Type of media
    fhir:AuditEvent.agent.network[](auditevent-definitions.html#AuditEvent.agent.network "Logical network location for application activity, if the activity has a network location.") [ # 0..1 Logical network location for application activity
      fhir:AuditEvent.agent.network.address[](auditevent-definitions.html#AuditEvent.agent.network.address "An identifier for the network access point of the user device for the audit event.") [ string[](datatypes.html#string) ]; # 0..1 Identifier for the network access point of the user device
      fhir:AuditEvent.agent.network.type[](auditevent-definitions.html#AuditEvent.agent.network.type "An identifier for the type of network access point that originated the audit event.") [ code[](datatypes.html#code) ]; # 0..1 The type of network access point
    ];
    fhir:AuditEvent.agent.purposeOfUse[](auditevent-definitions.html#AuditEvent.agent.purposeOfUse "The reason \(purpose of use\), specific to this agent, that was used during the event being recorded.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* Reason given for this user
  ], ...;
  fhir:AuditEvent.source[](auditevent-definitions.html#AuditEvent.source "The system that is reporting the event.") [ # 1..1 Audit Event Reporter
    fhir:AuditEvent.source.site[](auditevent-definitions.html#AuditEvent.source.site "Logical source location within the healthcare enterprise network.  For example, a hospital or other provider location within a multi-entity provider group.") [ string[](datatypes.html#string) ]; # 0..1 Logical source location within the enterprise
    fhir:AuditEvent.source.observer[](auditevent-definitions.html#AuditEvent.source.observer "Identifier of the source where the event was detected.") [ Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) ]; # 1..1 The identity of source detecting the event
    fhir:AuditEvent.source.type[](auditevent-definitions.html#AuditEvent.source.type "Code specifying the type of source where event originated.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* The type of source where event originated
  ];
  fhir:AuditEvent.entity[](auditevent-definitions.html#AuditEvent.entity "Specific instances of data or objects that have been accessed.") [ # 0..* Data or objects used
    fhir:AuditEvent.entity.what[](auditevent-definitions.html#AuditEvent.entity.what "Identifies a specific instance of the entity. The reference should be version specific.") [ Reference[](references.html#Reference)(Any[](resourcelist.html)) ]; # 0..1 Specific instance of resource
    fhir:AuditEvent.entity.type[](auditevent-definitions.html#AuditEvent.entity.type "The type of the object that was involved in this audit event.") [ Coding[](datatypes.html#Coding) ]; # 0..1 Type of entity involved
    fhir:AuditEvent.entity.role[](auditevent-definitions.html#AuditEvent.entity.role "Code representing the role the entity played in the event being audited.") [ Coding[](datatypes.html#Coding) ]; # 0..1 What role the entity played
    fhir:AuditEvent.entity.lifecycle[](auditevent-definitions.html#AuditEvent.entity.lifecycle "Identifier for the data life-cycle stage for the entity.") [ Coding[](datatypes.html#Coding) ]; # 0..1 Life-cycle stage for the entity
    fhir:AuditEvent.entity.securityLabel[](auditevent-definitions.html#AuditEvent.entity.securityLabel "Security labels for the identified entity.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* Security labels on the entity
    fhir:AuditEvent.entity.name[](auditevent-definitions.html#AuditEvent.entity.name "A name of the entity in the audit event.") [ string[](datatypes.html#string) ]; # 0..1 Descriptor for entity
    fhir:AuditEvent.entity.description[](auditevent-definitions.html#AuditEvent.entity.description "Text that describes the entity in more detail.") [ string[](datatypes.html#string) ]; # 0..1 Descriptive text
    fhir:AuditEvent.entity.query[](auditevent-definitions.html#AuditEvent.entity.query "The query parameters for a query-type entities.") [ base64Binary[](datatypes.html#base64Binary) ]; # 0..1 Query parameters
    fhir:AuditEvent.entity.detail[](auditevent-definitions.html#AuditEvent.entity.detail "Tagged value pairs for conveying additional information about the entity.") [ # 0..* Additional Information about the entity
      fhir:AuditEvent.entity.detail.type[](auditevent-definitions.html#AuditEvent.entity.detail.type "The type of extra detail provided in the value.") [ string[](datatypes.html#string) ]; # 1..1 Name of the property
      # AuditEvent.entity.detail.value[x][](auditevent-definitions.html#AuditEvent.entity.detail.value\[x\] "The  value of the extra detail.") : 1..1 Property value. One of these 2
        fhir:AuditEvent.entity.detail.valueString[](auditevent-definitions.html#AuditEvent.entity.detail.valueString "The  value of the extra detail.") [ string[](datatypes.html#string) ]
        fhir:AuditEvent.entity.detail.valueBase64Binary[](auditevent-definitions.html#AuditEvent.entity.detail.valueBase64Binary "The  value of the extra detail.") [ base64Binary[](datatypes.html#base64Binary) ]
    ], ...;
  ], ...;
]

```

**Changes since R3**
[AuditEvent](auditevent.html#AuditEvent) |   
---|---  
AuditEvent.action | 
  * Change value set from http://hl7.org/fhir/ValueSet/audit-event-action to http://hl7.org/fhir/ValueSet/audit-event-action|4.0.1

  
AuditEvent.period | 
  * Added Element

  
AuditEvent.outcome | 
  * Change value set from http://hl7.org/fhir/ValueSet/audit-event-outcome to http://hl7.org/fhir/ValueSet/audit-event-outcome|4.0.1

  
AuditEvent.agent.type | 
  * Added Element

  
AuditEvent.agent.role | 
  * Remove Binding `http://hl7.org/fhir/ValueSet/security-role-type` (extensible) 

  
AuditEvent.agent.who | 
  * Added Element

  
AuditEvent.agent.network.type | 
  * Change value set from http://hl7.org/fhir/ValueSet/network-type to http://hl7.org/fhir/ValueSet/network-type|4.0.1

  
AuditEvent.source.observer | 
  * **Added Mandatory Element**

  
AuditEvent.source.type | 
  * Change code system for extensibly bound codes from "http://hl7.org/fhir/security-source-type" to "http://terminology.hl7.org/CodeSystem/security-source-type"

  
AuditEvent.entity.what | 
  * Added Element

  
AuditEvent.entity.role | 
  * Change code system for extensibly bound codes from "http://hl7.org/fhir/object-role" to "http://terminology.hl7.org/CodeSystem/object-role"

  
AuditEvent.entity.detail.value[x] | 
  * Renamed from value to value[x]
  * Add Type string

  
AuditEvent.agent.reference | 
  * deleted

  
AuditEvent.agent.userId | 
  * deleted

  
AuditEvent.source.identifier | 
  * deleted

  
AuditEvent.entity.identifier | 
  * deleted

  
AuditEvent.entity.reference | 
  * deleted

  
See the [Full Difference](diff.html) for further information
This analysis is available as [XML](auditevent.diff.xml) or [JSON](auditevent.diff.json). 
See [R3 <--> R4 Conversion Maps](auditevent-version-maps.html) (status = 8 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)
**Structure**
[Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") |  [Description & Constraints](formats.html#table "Additional information about the element")[![doco](help16.png)](formats.html#table "Legend for this format")  
---|---|---|---|---  
![.](tbl_spacer.png)![.](icon_resource.png) [AuditEvent](auditevent-definitions.html#AuditEvent "AuditEvent : A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Event record kept for security purposes  
Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.

Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource \(including cannot change the meaning of modifierExtension itself\).")  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](auditevent-definitions.html#AuditEvent.type "AuditEvent.type : Identifier for a family of the event.  For example, a menu item, program, rule, policy, function code, application name or URL. It identifies the performed function.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [Coding](datatypes.html#Coding) | Type/identifier of event  
[Audit Event ID](valueset-audit-event-type.html "Type of event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [subtype](auditevent-definitions.html#AuditEvent.subtype "AuditEvent.subtype : Identifier for the category of event.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Coding](datatypes.html#Coding) | More specific type/id for the event  
[Audit Event Sub-Type](valueset-audit-event-sub-type.html "Sub-type of event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [action](auditevent-definitions.html#AuditEvent.action "AuditEvent.action : Indicator for type of action performed during the event that generated the audit.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Type of action performed during the event  
[AuditEventAction](valueset-audit-event-action.html "Indicator for type of action performed during the event that generated the event.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [period](auditevent-definitions.html#AuditEvent.period "AuditEvent.period : The period during which the activity occurred.") |  | 0..1 | [Period](datatypes.html#Period) | When the activity occurred  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [recorded](auditevent-definitions.html#AuditEvent.recorded "AuditEvent.recorded : The time when the event was recorded.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [instant](datatypes.html#instant) | Time when the event was recorded  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [outcome](auditevent-definitions.html#AuditEvent.outcome "AuditEvent.outcome : Indicates whether the event succeeded or failed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | Whether the event succeeded or failed  
[AuditEventOutcome](valueset-audit-event-outcome.html "Indicates whether the event succeeded or failed.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [outcomeDesc](auditevent-definitions.html#AuditEvent.outcomeDesc "AuditEvent.outcomeDesc : A free text description of the outcome of the event.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Description of the event outcome  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [purposeOfEvent](auditevent-definitions.html#AuditEvent.purposeOfEvent "AuditEvent.purposeOfEvent : The purposeOfUse \(reason\) that was used during the event being recorded.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | The purposeOfUse of the event  
[V3 Value SetPurposeOfUse](v3/PurposeOfUse/vs.html "The reason the activity took place.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [agent](auditevent-definitions.html#AuditEvent.agent "AuditEvent.agent : An actor taking an active role in the event or activity that is logged.") |  | 1..* | [BackboneElement](backboneelement.html) | Actor involved in the event  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](auditevent-definitions.html#AuditEvent.agent.type "AuditEvent.agent.type : Specification of the participation type the user plays when performing the event.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | How agent participated  
[ParticipationRoleType](valueset-participation-role-type.html "The Participation type of the agent to the event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [role](auditevent-definitions.html#AuditEvent.agent.role "AuditEvent.agent.role : The security role that the user was acting under, that come from local codes defined by the access control security system \(e.g. RBAC, ABAC\) used in the local context.") |  | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Agent role in the event  
[SecurityRoleType](valueset-security-role-type.html "What security role enabled the agent to participate in the event.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included."))  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [who](auditevent-definitions.html#AuditEvent.agent.who "AuditEvent.agent.who : Reference to who this agent is that was involved in the event.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  [Reference](references.html#Reference)([PractitionerRole](practitionerrole.html) | [Practitioner](practitioner.html) | [Organization](organization.html) | [Device](device.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Identifier of who  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [altId](auditevent-definitions.html#AuditEvent.agent.altId "AuditEvent.agent.altId : Alternative agent Identifier. For a human, this should be a user identifier text string from authentication system. This identifier would be one known to a common authentication system \(e.g. single sign-on\), if available.") |  | 0..1 | [string](datatypes.html#string) | Alternative User identity  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](auditevent-definitions.html#AuditEvent.agent.name "AuditEvent.agent.name : Human-meaningful name for the agent.") |  | 0..1 | [string](datatypes.html#string) | Human friendly name for the agent  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [requestor](auditevent-definitions.html#AuditEvent.agent.requestor "AuditEvent.agent.requestor : Indicator that the user is or is not the requestor, or initiator, for the event being audited.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [boolean](datatypes.html#boolean) | Whether user is initiator  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [location](auditevent-definitions.html#AuditEvent.agent.location "AuditEvent.agent.location : Where the event occurred.") |  | 0..1 |  [Reference](references.html#Reference)([Location](location.html)) | Where  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [policy](auditevent-definitions.html#AuditEvent.agent.policy "AuditEvent.agent.policy : The policy or plan that authorized the activity being recorded. Typically, a single activity may have multiple applicable policies, such as patient consent, guarantor funding, etc. The policy would also indicate the security token used.") |  | 0..* | [uri](datatypes.html#uri) | Policy that authorized event  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [media](auditevent-definitions.html#AuditEvent.agent.media "AuditEvent.agent.media : Type of media involved. Used when the event is about exporting/importing onto media.") |  | 0..1 | [Coding](datatypes.html#Coding) | Type of media  
[Media Type Code](valueset-dicm-405-mediatype.html "Used when the event is about exporting/importing onto media.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_element.gif) [network](auditevent-definitions.html#AuditEvent.agent.network "AuditEvent.agent.network : Logical network location for application activity, if the activity has a network location.") |  | 0..1 | [BackboneElement](backboneelement.html) | Logical network location for application activity  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [address](auditevent-definitions.html#AuditEvent.agent.network.address "AuditEvent.agent.network.address : An identifier for the network access point of the user device for the audit event.") |  | 0..1 | [string](datatypes.html#string) | Identifier for the network access point of the user device  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [type](auditevent-definitions.html#AuditEvent.agent.network.type "AuditEvent.agent.network.type : An identifier for the type of network access point that originated the audit event.") |  | 0..1 | [code](datatypes.html#code) | The type of network access point  
[AuditEventAgentNetworkType](valueset-network-type.html "The type of network access point of this agent in the audit event.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_datatype.gif) [purposeOfUse](auditevent-definitions.html#AuditEvent.agent.purposeOfUse "AuditEvent.agent.purposeOfUse : The reason \(purpose of use\), specific to this agent, that was used during the event being recorded.") |  | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Reason given for this user  
[V3 Value SetPurposeOfUse](v3/PurposeOfUse/vs.html "The reason the activity took place.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [source](auditevent-definitions.html#AuditEvent.source "AuditEvent.source : The system that is reporting the event.") |  | 1..1 | [BackboneElement](backboneelement.html) | Audit Event Reporter  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [site](auditevent-definitions.html#AuditEvent.source.site "AuditEvent.source.site : Logical source location within the healthcare enterprise network.  For example, a hospital or other provider location within a multi-entity provider group.") |  | 0..1 | [string](datatypes.html#string) | Logical source location within the enterprise  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [observer](auditevent-definitions.html#AuditEvent.source.observer "AuditEvent.source.observer : Identifier of the source where the event was detected.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [Reference](references.html#Reference)([PractitionerRole](practitionerrole.html) | [Practitioner](practitioner.html) | [Organization](organization.html) | [Device](device.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | The identity of source detecting the event  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_datatype.gif) [type](auditevent-definitions.html#AuditEvent.source.type "AuditEvent.source.type : Code specifying the type of source where event originated.") |  | 0..* | [Coding](datatypes.html#Coding) | The type of source where event originated  
[Audit Event Source Type](valueset-audit-source-type.html "Code specifying the type of system that detected and recorded the event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [entity](auditevent-definitions.html#AuditEvent.entity "AuditEvent.entity : Specific instances of data or objects that have been accessed.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..* | [BackboneElement](backboneelement.html) | Data or objects used  
+ Rule: Either a name or a query (NOT both)  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_reference.png) [what](auditevent-definitions.html#AuditEvent.entity.what "AuditEvent.entity.what : Identifies a specific instance of the entity. The reference should be version specific.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  [Reference](references.html#Reference)([Any](resourcelist.html)) | Specific instance of resource  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](auditevent-definitions.html#AuditEvent.entity.type "AuditEvent.entity.type : The type of the object that was involved in this audit event.") |  | 0..1 | [Coding](datatypes.html#Coding) | Type of entity involved  
[Audit event entity type](valueset-audit-entity-type.html "Code for the entity type involved in the audit event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [role](auditevent-definitions.html#AuditEvent.entity.role "AuditEvent.entity.role : Code representing the role the entity played in the event being audited.") |  | 0..1 | [Coding](datatypes.html#Coding) | What role the entity played  
[AuditEventEntityRole](valueset-object-role.html "Code representing the role the entity played in the audit event.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [lifecycle](auditevent-definitions.html#AuditEvent.entity.lifecycle "AuditEvent.entity.lifecycle : Identifier for the data life-cycle stage for the entity.") |  | 0..1 | [Coding](datatypes.html#Coding) | Life-cycle stage for the entity  
[ObjectLifecycleEvents](valueset-object-lifecycle-events.html "Identifier for the data life-cycle stage for the entity.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [securityLabel](auditevent-definitions.html#AuditEvent.entity.securityLabel "AuditEvent.entity.securityLabel : Security labels for the identified entity.") |  | 0..* | [Coding](datatypes.html#Coding) | Security labels on the entity  
[SecurityLabels](valueset-security-labels.html "Security Labels from the Healthcare Privacy and Security Classification System.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](auditevent-definitions.html#AuditEvent.entity.name "AuditEvent.entity.name : A name of the entity in the audit event.") |  [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [string](datatypes.html#string) | Descriptor for entity  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [description](auditevent-definitions.html#AuditEvent.entity.description "AuditEvent.entity.description : Text that describes the entity in more detail.") |  | 0..1 | [string](datatypes.html#string) | Descriptive text  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [query](auditevent-definitions.html#AuditEvent.entity.query "AuditEvent.entity.query : The query parameters for a query-type entities.") |  [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [base64Binary](datatypes.html#base64Binary) | Query parameters  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [detail](auditevent-definitions.html#AuditEvent.entity.detail "AuditEvent.entity.detail : Tagged value pairs for conveying additional information about the entity.") |  | 0..* | [BackboneElement](backboneelement.html) | Additional Information about the entity  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [type](auditevent-definitions.html#AuditEvent.entity.detail.type "AuditEvent.entity.detail.type : The type of extra detail provided in the value.") |  | 1..1 | [string](datatypes.html#string) | Name of the property  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_choice.gif) [value[x]](auditevent-definitions.html#AuditEvent.entity.detail.value_x_ "AuditEvent.entity.detail.value\[x\] : The  value of the extra detail.") |  | 1..1 |  | Property value  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) valueString |  |  | [string](datatypes.html#string) |   
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) valueBase64Binary |  |  | [base64Binary](datatypes.html#base64Binary) |   
  
[![doco](help16.png) Documentation for this format](formats.html#table "Legend for this format")  
**UML Diagram** ([Legend](formats.html#uml))
AuditEvent (DomainResource)Identifier for a family of the event. For example, a menu item, program, rule, policy, function code, application name or URL. It identifies the performed functiontype : Coding [1..1] « Type of event. (Strength=Extensible)AuditEventID+ »Identifier for the category of eventsubtype : Coding [0..*] « Sub-type of event. (Strength=Extensible)AuditEventSub-Type+ »Indicator for type of action performed during the event that generated the auditaction : code [0..1] « Indicator for type of action performed during the event that generated the event. (Strength=Required)AuditEventAction! »The period during which the activity occurredperiod : Period [0..1]The time when the event was recordedrecorded : instant [1..1]Indicates whether the event succeeded or failedoutcome : code [0..1] « Indicates whether the event succeeded or failed. (Strength=Required)AuditEventOutcome! »A free text description of the outcome of the eventoutcomeDesc : string [0..1]The purposeOfUse (reason) that was used during the event being recordedpurposeOfEvent : CodeableConcept [0..*] « The reason the activity took place. (Strength=Extensible)v3.PurposeOfUse+ »AgentSpecification of the participation type the user plays when performing the eventtype : CodeableConcept [0..1] « The Participation type of the agent to the event. (Strength=Extensible)ParticipationRoleType+ »The security role that the user was acting under, that come from local codes defined by the access control security system (e.g. RBAC, ABAC) used in the local contextrole : CodeableConcept [0..*] « What security role enabled the agent to participate in the event. (Strength=Example)SecurityRoleType?? »Reference to who this agent is that was involved in the eventwho : Reference [0..1] « PractitionerRole|Practitioner|Organization| Device|Patient|RelatedPerson »Alternative agent Identifier. For a human, this should be a user identifier text string from authentication system. This identifier would be one known to a common authentication system (e.g. single sign-on), if availablealtId : string [0..1]Human-meaningful name for the agentname : string [0..1]Indicator that the user is or is not the requestor, or initiator, for the event being auditedrequestor : boolean [1..1]Where the event occurredlocation : Reference [0..1] « Location »The policy or plan that authorized the activity being recorded. Typically, a single activity may have multiple applicable policies, such as patient consent, guarantor funding, etc. The policy would also indicate the security token usedpolicy : uri [0..*]Type of media involved. Used when the event is about exporting/importing onto mediamedia : Coding [0..1] « Used when the event is about exporting/importing onto media. (Strength=Extensible)MediaTypeCode+ »The reason (purpose of use), specific to this agent, that was used during the event being recordedpurposeOfUse : CodeableConcept [0..*] « The reason the activity took place. (Strength=Extensible)v3.PurposeOfUse+ »NetworkAn identifier for the network access point of the user device for the audit eventaddress : string [0..1]An identifier for the type of network access point that originated the audit eventtype : code [0..1] « The type of network access point of this agent in the audit event. (Strength=Required)AuditEventAgentNetworkType! »SourceLogical source location within the healthcare enterprise network. For example, a hospital or other provider location within a multi-entity provider groupsite : string [0..1]Identifier of the source where the event was detectedobserver : Reference [1..1] « PractitionerRole|Practitioner| Organization|Device|Patient|RelatedPerson »Code specifying the type of source where event originatedtype : Coding [0..*] « Code specifying the type of system that detected and recorded the event. (Strength=Extensible)AuditEventSourceType+ »EntityIdentifies a specific instance of the entity. The reference should be version specificwhat : Reference [0..1] « Any »The type of the object that was involved in this audit eventtype : Coding [0..1] « Code for the entity type involved in the audit event. (Strength=Extensible)AuditEventEntityType+ »Code representing the role the entity played in the event being auditedrole : Coding [0..1] « Code representing the role the entity played in the audit event. (Strength=Extensible)AuditEventEntityRole+ »Identifier for the data life-cycle stage for the entitylifecycle : Coding [0..1] « Identifier for the data life-cycle stage for the entity. (Strength=Extensible)ObjectLifecycleEvents+ »Security labels for the identified entitysecurityLabel : Coding [0..*] « Security Labels from the Healthcare Privacy and Security Classification System. (Strength=Extensible)All Security Labels+ »A name of the entity in the audit eventname : string [0..1]Text that describes the entity in more detaildescription : string [0..1]The query parameters for a query-type entitiesquery : base64Binary [0..1]DetailThe type of extra detail provided in the valuetype : string [1..1]The value of the extra detailvalue[x] : Type [1..1] « string|base64Binary »Logical network location for application activity, if the activity has a network locationnetwork[0..1]An actor taking an active role in the event or activity that is loggedagent[1..*]The system that is reporting the eventsource[1..1]Tagged value pairs for conveying additional information about the entitydetail[0..*]Specific instances of data or objects that have been accessedentity[0..*]
**XML Template**
```

<[**AuditEvent**](auditevent-definitions.html#AuditEvent "A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.") xmlns="http://hl7.org/fhir"> [![doco](help.png)](xml.html "Documentation for this format")
 <!-- from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language) -->
 <!-- from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension) -->
 <[**type**](auditevent-definitions.html#AuditEvent.type "Identifier for a family of the event.  For example, a menu item, program, rule, policy, function code, application name or URL. It identifies the performed function.")><!-- **1..1** Coding[](datatypes.html#Coding) Type/identifier of event[](valueset-audit-event-type.html) --></type>
 <[**subtype**](auditevent-definitions.html#AuditEvent.subtype "Identifier for the category of event.")><!-- **0..*** Coding[](datatypes.html#Coding) More specific type/id for the event[](valueset-audit-event-sub-type.html) --></subtype>
 <[**action**](auditevent-definitions.html#AuditEvent.action "Indicator for type of action performed during the event that generated the audit.") value="[code[](datatypes.html#code)]"/><!-- **0..1** Type of action performed during the event[](valueset-audit-event-action.html) -->
 <[**period**](auditevent-definitions.html#AuditEvent.period "The period during which the activity occurred.")><!-- **0..1** Period[](datatypes.html#Period) When the activity occurred[](terminologies.html#unbound) --></period>
 <[**recorded**](auditevent-definitions.html#AuditEvent.recorded "The time when the event was recorded.") value="[instant[](datatypes.html#instant)]"/><!-- **1..1** Time when the event was recorded[](terminologies.html#unbound) -->
 <[**outcome**](auditevent-definitions.html#AuditEvent.outcome "Indicates whether the event succeeded or failed.") value="[code[](datatypes.html#code)]"/><!-- **0..1** Whether the event succeeded or failed[](valueset-audit-event-outcome.html) -->
 <[**outcomeDesc**](auditevent-definitions.html#AuditEvent.outcomeDesc "A free text description of the outcome of the event.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Description of the event outcome[](terminologies.html#unbound) -->
 <[**purposeOfEvent**](auditevent-definitions.html#AuditEvent.purposeOfEvent "The purposeOfUse \(reason\) that was used during the event being recorded.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) The purposeOfUse of the event[](v3/PurposeOfUse/vs.html) --></purposeOfEvent>
 <[**agent**](auditevent-definitions.html#AuditEvent.agent "An actor taking an active role in the event or activity that is logged.")>  <!-- **1..*** Actor involved in the event -->
  <[**type**](auditevent-definitions.html#AuditEvent.agent.type "Specification of the participation type the user plays when performing the event.")><!-- **0..1** CodeableConcept[](datatypes.html#CodeableConcept) How agent participated[](valueset-participation-role-type.html) --></type>
  <[**role**](auditevent-definitions.html#AuditEvent.agent.role "The security role that the user was acting under, that come from local codes defined by the access control security system \(e.g. RBAC, ABAC\) used in the local context.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) Agent role in the event[](valueset-security-role-type.html) --></role>
  <[**who**](auditevent-definitions.html#AuditEvent.agent.who "Reference to who this agent is that was involved in the event.")><!-- **0..1** Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|
    Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) Identifier of who[](terminologies.html#unbound) --></who>
  <[**altId**](auditevent-definitions.html#AuditEvent.agent.altId "Alternative agent Identifier. For a human, this should be a user identifier text string from authentication system. This identifier would be one known to a common authentication system \(e.g. single sign-on\), if available.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Alternative User identity[](terminologies.html#unbound) -->
  <[**name**](auditevent-definitions.html#AuditEvent.agent.name "Human-meaningful name for the agent.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Human friendly name for the agent[](terminologies.html#unbound) -->
  <[**requestor**](auditevent-definitions.html#AuditEvent.agent.requestor "Indicator that the user is or is not the requestor, or initiator, for the event being audited.") value="[boolean[](datatypes.html#boolean)]"/><!-- **1..1** Whether user is initiator[](terminologies.html#unbound) -->
  <[**location**](auditevent-definitions.html#AuditEvent.agent.location "Where the event occurred.")><!-- **0..1** Reference[](references.html#Reference)(Location[](location.html#Location)) Where[](terminologies.html#unbound) --></location>
  <[**policy**](auditevent-definitions.html#AuditEvent.agent.policy "The policy or plan that authorized the activity being recorded. Typically, a single activity may have multiple applicable policies, such as patient consent, guarantor funding, etc. The policy would also indicate the security token used.") value="[uri[](datatypes.html#uri)]"/><!-- **0..*** Policy that authorized event[](terminologies.html#unbound) -->
  <[**media**](auditevent-definitions.html#AuditEvent.agent.media "Type of media involved. Used when the event is about exporting/importing onto media.")><!-- **0..1** Coding[](datatypes.html#Coding) Type of media[](valueset-dicm-405-mediatype.html) --></media>
  <[**network**](auditevent-definitions.html#AuditEvent.agent.network "Logical network location for application activity, if the activity has a network location.")>  <!-- **0..1** Logical network location for application activity -->
   <[**address**](auditevent-definitions.html#AuditEvent.agent.network.address "An identifier for the network access point of the user device for the audit event.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Identifier for the network access point of the user device[](terminologies.html#unbound) -->
   <[**type**](auditevent-definitions.html#AuditEvent.agent.network.type "An identifier for the type of network access point that originated the audit event.") value="[code[](datatypes.html#code)]"/><!-- **0..1** The type of network access point[](valueset-network-type.html) -->
  </network>
  <[**purposeOfUse**](auditevent-definitions.html#AuditEvent.agent.purposeOfUse "The reason \(purpose of use\), specific to this agent, that was used during the event being recorded.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) Reason given for this user[](v3/PurposeOfUse/vs.html) --></purposeOfUse>
 </agent>
 <[**source**](auditevent-definitions.html#AuditEvent.source "The system that is reporting the event.")>  <!-- **1..1** Audit Event Reporter -->
  <[**site**](auditevent-definitions.html#AuditEvent.source.site "Logical source location within the healthcare enterprise network.  For example, a hospital or other provider location within a multi-entity provider group.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Logical source location within the enterprise[](terminologies.html#unbound) -->
  <[**observer**](auditevent-definitions.html#AuditEvent.source.observer "Identifier of the source where the event was detected.")><!-- **1..1** Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|
    Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) The identity of source detecting the event[](terminologies.html#unbound) --></observer>
  <[**type**](auditevent-definitions.html#AuditEvent.source.type "Code specifying the type of source where event originated.")><!-- **0..*** Coding[](datatypes.html#Coding) The type of source where event originated[](valueset-audit-source-type.html) --></type>
 </source>
 <[**entity**](auditevent-definitions.html#AuditEvent.entity "Specific instances of data or objects that have been accessed.")>  <!-- **0..*** Data or objects used -->
  <[**what**](auditevent-definitions.html#AuditEvent.entity.what "Identifies a specific instance of the entity. The reference should be version specific.")><!-- **0..1** Reference[](references.html#Reference)(Any[](resourcelist.html)) Specific instance of resource[](terminologies.html#unbound) --></what>
  <[**type**](auditevent-definitions.html#AuditEvent.entity.type "The type of the object that was involved in this audit event.")><!-- **0..1** Coding[](datatypes.html#Coding) Type of entity involved[](valueset-audit-entity-type.html) --></type>
  <[**role**](auditevent-definitions.html#AuditEvent.entity.role "Code representing the role the entity played in the event being audited.")><!-- **0..1** Coding[](datatypes.html#Coding) What role the entity played[](valueset-object-role.html) --></role>
  <[**lifecycle**](auditevent-definitions.html#AuditEvent.entity.lifecycle "Identifier for the data life-cycle stage for the entity.")><!-- **0..1** Coding[](datatypes.html#Coding) Life-cycle stage for the entity[](valueset-object-lifecycle-events.html) --></lifecycle>
  <[**securityLabel**](auditevent-definitions.html#AuditEvent.entity.securityLabel "Security labels for the identified entity.")><!-- **0..*** Coding[](datatypes.html#Coding) Security labels on the entity[](valueset-security-labels.html) --></securityLabel>
  <[**name**](auditevent-definitions.html#AuditEvent.entity.name "A name of the entity in the audit event.") value="[string[](datatypes.html#string)]"/><!-- **![??](lock.png) 0..1** Descriptor for entity[](terminologies.html#unbound) -->
  <[**description**](auditevent-definitions.html#AuditEvent.entity.description "Text that describes the entity in more detail.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Descriptive text[](terminologies.html#unbound) -->
  <[**query**](auditevent-definitions.html#AuditEvent.entity.query "The query parameters for a query-type entities.") value="[base64Binary[](datatypes.html#base64Binary)]"/><!-- **![??](lock.png) 0..1** Query parameters[](terminologies.html#unbound) -->
  <[**detail**](auditevent-definitions.html#AuditEvent.entity.detail "Tagged value pairs for conveying additional information about the entity.")>  <!-- **0..*** Additional Information about the entity -->
   <[**type**](auditevent-definitions.html#AuditEvent.entity.detail.type "The type of extra detail provided in the value.") value="[string[](datatypes.html#string)]"/><!-- **1..1** Name of the property[](terminologies.html#unbound) -->
   <[**value[x]**](auditevent-definitions.html#AuditEvent.entity.detail.value\[x\] "The  value of the extra detail.")><!-- **1..1** string[](datatypes.html#string)|base64Binary[](datatypes.html#base64Binary) Property value[](terminologies.html#unbound) --></value[x]>
  </detail>
 </entity>
</AuditEvent>

```

**JSON Template**
```

{[![doco](help.png)](json.html "Documentation for this format")
  "resourceType" : "[**AuditEvent**](auditevent-definitions.html#AuditEvent "A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.")",
  // from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language)
  // from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension)
  "type[](auditevent-definitions.html#AuditEvent.type "Identifier for a family of the event.  For example, a menu item, program, rule, policy, function code, application name or URL. It identifies the performed function.")" : { Coding[](datatypes.html#Coding) }, // **R!**  Type/identifier of event[](valueset-audit-event-type.html)
  "subtype[](auditevent-definitions.html#AuditEvent.subtype "Identifier for the category of event.")" : [{ Coding[](datatypes.html#Coding) }], // More specific type/id for the event[](valueset-audit-event-sub-type.html)
  "action[](auditevent-definitions.html#AuditEvent.action "Indicator for type of action performed during the event that generated the audit.")" : "<code[](datatypes.html#code)>", // Type of action performed during the event[](valueset-audit-event-action.html)
  "period[](auditevent-definitions.html#AuditEvent.period "The period during which the activity occurred.")" : { Period[](datatypes.html#Period) }, // When the activity occurred[](terminologies.html#unbound)
  "recorded[](auditevent-definitions.html#AuditEvent.recorded "The time when the event was recorded.")" : "<instant[](datatypes.html#instant)>", // **R!**  Time when the event was recorded[](terminologies.html#unbound)
  "outcome[](auditevent-definitions.html#AuditEvent.outcome "Indicates whether the event succeeded or failed.")" : "<code[](datatypes.html#code)>", // Whether the event succeeded or failed[](valueset-audit-event-outcome.html)
  "outcomeDesc[](auditevent-definitions.html#AuditEvent.outcomeDesc "A free text description of the outcome of the event.")" : "<string[](datatypes.html#string)>", // Description of the event outcome[](terminologies.html#unbound)
  "purposeOfEvent[](auditevent-definitions.html#AuditEvent.purposeOfEvent "The purposeOfUse \(reason\) that was used during the event being recorded.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // The purposeOfUse of the event[](v3/PurposeOfUse/vs.html)
  "agent[](auditevent-definitions.html#AuditEvent.agent "An actor taking an active role in the event or activity that is logged.")" : [{ // **R!**  Actor involved in the event[](terminologies.html#unbound)
    "type[](auditevent-definitions.html#AuditEvent.agent.type "Specification of the participation type the user plays when performing the event.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // How agent participated[](valueset-participation-role-type.html)
    "role[](auditevent-definitions.html#AuditEvent.agent.role "The security role that the user was acting under, that come from local codes defined by the access control security system \(e.g. RBAC, ABAC\) used in the local context.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // Agent role in the event[](valueset-security-role-type.html)
    "who[](auditevent-definitions.html#AuditEvent.agent.who "Reference to who this agent is that was involved in the event.")" : { Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|
    Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) }, // Identifier of who[](terminologies.html#unbound)
    "altId[](auditevent-definitions.html#AuditEvent.agent.altId "Alternative agent Identifier. For a human, this should be a user identifier text string from authentication system. This identifier would be one known to a common authentication system \(e.g. single sign-on\), if available.")" : "<string[](datatypes.html#string)>", // Alternative User identity[](terminologies.html#unbound)
    "name[](auditevent-definitions.html#AuditEvent.agent.name "Human-meaningful name for the agent.")" : "<string[](datatypes.html#string)>", // Human friendly name for the agent[](terminologies.html#unbound)
    "requestor[](auditevent-definitions.html#AuditEvent.agent.requestor "Indicator that the user is or is not the requestor, or initiator, for the event being audited.")" : <boolean[](datatypes.html#boolean)>, // **R!**  Whether user is initiator[](terminologies.html#unbound)
    "location[](auditevent-definitions.html#AuditEvent.agent.location "Where the event occurred.")" : { Reference[](references.html#Reference)(Location[](location.html#Location)) }, // Where[](terminologies.html#unbound)
    "policy[](auditevent-definitions.html#AuditEvent.agent.policy "The policy or plan that authorized the activity being recorded. Typically, a single activity may have multiple applicable policies, such as patient consent, guarantor funding, etc. The policy would also indicate the security token used.")" : ["<uri[](datatypes.html#uri)>"], // Policy that authorized event[](terminologies.html#unbound)
    "media[](auditevent-definitions.html#AuditEvent.agent.media "Type of media involved. Used when the event is about exporting/importing onto media.")" : { Coding[](datatypes.html#Coding) }, // Type of media[](valueset-dicm-405-mediatype.html)
    "network[](auditevent-definitions.html#AuditEvent.agent.network "Logical network location for application activity, if the activity has a network location.")" : { // Logical network location for application activity[](terminologies.html#unbound)
      "address[](auditevent-definitions.html#AuditEvent.agent.network.address "An identifier for the network access point of the user device for the audit event.")" : "<string[](datatypes.html#string)>", // Identifier for the network access point of the user device[](terminologies.html#unbound)
      "type[](auditevent-definitions.html#AuditEvent.agent.network.type "An identifier for the type of network access point that originated the audit event.")" : "<code[](datatypes.html#code)>" // The type of network access point[](valueset-network-type.html)
    },
    "purposeOfUse[](auditevent-definitions.html#AuditEvent.agent.purposeOfUse "The reason \(purpose of use\), specific to this agent, that was used during the event being recorded.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }] // Reason given for this user[](v3/PurposeOfUse/vs.html)
  }],
  "source[](auditevent-definitions.html#AuditEvent.source "The system that is reporting the event.")" : { // **R!**  Audit Event Reporter[](terminologies.html#unbound)
    "site[](auditevent-definitions.html#AuditEvent.source.site "Logical source location within the healthcare enterprise network.  For example, a hospital or other provider location within a multi-entity provider group.")" : "<string[](datatypes.html#string)>", // Logical source location within the enterprise[](terminologies.html#unbound)
    "observer[](auditevent-definitions.html#AuditEvent.source.observer "Identifier of the source where the event was detected.")" : { Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|
    Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) }, // **R!**  The identity of source detecting the event[](terminologies.html#unbound)
    "type[](auditevent-definitions.html#AuditEvent.source.type "Code specifying the type of source where event originated.")" : [{ Coding[](datatypes.html#Coding) }] // The type of source where event originated[](valueset-audit-source-type.html)
  },
  "entity[](auditevent-definitions.html#AuditEvent.entity "Specific instances of data or objects that have been accessed.")" : [{ // Data or objects used[](terminologies.html#unbound)
    "what[](auditevent-definitions.html#AuditEvent.entity.what "Identifies a specific instance of the entity. The reference should be version specific.")" : { Reference[](references.html#Reference)(Any[](resourcelist.html)) }, // Specific instance of resource[](terminologies.html#unbound)
    "type[](auditevent-definitions.html#AuditEvent.entity.type "The type of the object that was involved in this audit event.")" : { Coding[](datatypes.html#Coding) }, // Type of entity involved[](valueset-audit-entity-type.html)
    "role[](auditevent-definitions.html#AuditEvent.entity.role "Code representing the role the entity played in the event being audited.")" : { Coding[](datatypes.html#Coding) }, // What role the entity played[](valueset-object-role.html)
    "lifecycle[](auditevent-definitions.html#AuditEvent.entity.lifecycle "Identifier for the data life-cycle stage for the entity.")" : { Coding[](datatypes.html#Coding) }, // Life-cycle stage for the entity[](valueset-object-lifecycle-events.html)
    "securityLabel[](auditevent-definitions.html#AuditEvent.entity.securityLabel "Security labels for the identified entity.")" : [{ Coding[](datatypes.html#Coding) }], // Security labels on the entity[](valueset-security-labels.html)
    "name[](auditevent-definitions.html#AuditEvent.entity.name "A name of the entity in the audit event.")" : "<string[](datatypes.html#string)>", // **C?** Descriptor for entity[](terminologies.html#unbound)
    "description[](auditevent-definitions.html#AuditEvent.entity.description "Text that describes the entity in more detail.")" : "<string[](datatypes.html#string)>", // Descriptive text[](terminologies.html#unbound)
    "query[](auditevent-definitions.html#AuditEvent.entity.query "The query parameters for a query-type entities.")" : "<base64Binary[](datatypes.html#base64Binary)>", // **C?** Query parameters[](terminologies.html#unbound)
    "detail[](auditevent-definitions.html#AuditEvent.entity.detail "Tagged value pairs for conveying additional information about the entity.")" : [{ // Additional Information about the entity[](terminologies.html#unbound)
      "type[](auditevent-definitions.html#AuditEvent.entity.detail.type "The type of extra detail provided in the value.")" : "<string[](datatypes.html#string)>", // **R!**  Name of the property[](terminologies.html#unbound)
      // value[x]: Property value. One of these 2:
      "valueString[](auditevent-definitions.html#AuditEvent.entity.detail.valueString "The  value of the extra detail.")" : "<string[](datatypes.html#string)>"
      "valueBase64Binary[](auditevent-definitions.html#AuditEvent.entity.detail.valueBase64Binary "The  value of the extra detail.")" : "<base64Binary[](datatypes.html#base64Binary)>"
    }]
  }]
}

```

**Turtle Template**
```

@prefix fhir: <http://hl7.org/fhir/> .[![doco](help.png)](rdf.html "Documentation for this format")


[ a fhir:[**AuditEvent**](auditevent-definitions.html#AuditEvent "A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.");
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource[](resource.html): .id[](resource.html#id), .meta[](resource.html#meta), .implicitRules[](resource.html#implicitRules), and .language[](resource.html#language)
  # from DomainResource[](domainresource.html): .text[](narrative.html#Narrative), .contained[](references.html#contained), .extension[](extensibility.html), and .modifierExtension[](extensibility.html#modifierExtension)
  fhir:AuditEvent.type[](auditevent-definitions.html#AuditEvent.type "Identifier for a family of the event.  For example, a menu item, program, rule, policy, function code, application name or URL. It identifies the performed function.") [ Coding[](datatypes.html#Coding) ]; # 1..1 Type/identifier of event
  fhir:AuditEvent.subtype[](auditevent-definitions.html#AuditEvent.subtype "Identifier for the category of event.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* More specific type/id for the event
  fhir:AuditEvent.action[](auditevent-definitions.html#AuditEvent.action "Indicator for type of action performed during the event that generated the audit.") [ code[](datatypes.html#code) ]; # 0..1 Type of action performed during the event
  fhir:AuditEvent.period[](auditevent-definitions.html#AuditEvent.period "The period during which the activity occurred.") [ Period[](datatypes.html#Period) ]; # 0..1 When the activity occurred
  fhir:AuditEvent.recorded[](auditevent-definitions.html#AuditEvent.recorded "The time when the event was recorded.") [ instant[](datatypes.html#instant) ]; # 1..1 Time when the event was recorded
  fhir:AuditEvent.outcome[](auditevent-definitions.html#AuditEvent.outcome "Indicates whether the event succeeded or failed.") [ code[](datatypes.html#code) ]; # 0..1 Whether the event succeeded or failed
  fhir:AuditEvent.outcomeDesc[](auditevent-definitions.html#AuditEvent.outcomeDesc "A free text description of the outcome of the event.") [ string[](datatypes.html#string) ]; # 0..1 Description of the event outcome
  fhir:AuditEvent.purposeOfEvent[](auditevent-definitions.html#AuditEvent.purposeOfEvent "The purposeOfUse \(reason\) that was used during the event being recorded.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* The purposeOfUse of the event
  fhir:AuditEvent.agent[](auditevent-definitions.html#AuditEvent.agent "An actor taking an active role in the event or activity that is logged.") [ # 1..* Actor involved in the event
    fhir:AuditEvent.agent.type[](auditevent-definitions.html#AuditEvent.agent.type "Specification of the participation type the user plays when performing the event.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 0..1 How agent participated
    fhir:AuditEvent.agent.role[](auditevent-definitions.html#AuditEvent.agent.role "The security role that the user was acting under, that come from local codes defined by the access control security system \(e.g. RBAC, ABAC\) used in the local context.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* Agent role in the event
    fhir:AuditEvent.agent.who[](auditevent-definitions.html#AuditEvent.agent.who "Reference to who this agent is that was involved in the event.") [ Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) ]; # 0..1 Identifier of who
    fhir:AuditEvent.agent.altId[](auditevent-definitions.html#AuditEvent.agent.altId "Alternative agent Identifier. For a human, this should be a user identifier text string from authentication system. This identifier would be one known to a common authentication system \(e.g. single sign-on\), if available.") [ string[](datatypes.html#string) ]; # 0..1 Alternative User identity
    fhir:AuditEvent.agent.name[](auditevent-definitions.html#AuditEvent.agent.name "Human-meaningful name for the agent.") [ string[](datatypes.html#string) ]; # 0..1 Human friendly name for the agent
    fhir:AuditEvent.agent.requestor[](auditevent-definitions.html#AuditEvent.agent.requestor "Indicator that the user is or is not the requestor, or initiator, for the event being audited.") [ boolean[](datatypes.html#boolean) ]; # 1..1 Whether user is initiator
    fhir:AuditEvent.agent.location[](auditevent-definitions.html#AuditEvent.agent.location "Where the event occurred.") [ Reference[](references.html#Reference)(Location[](location.html#Location)) ]; # 0..1 Where
    fhir:AuditEvent.agent.policy[](auditevent-definitions.html#AuditEvent.agent.policy "The policy or plan that authorized the activity being recorded. Typically, a single activity may have multiple applicable policies, such as patient consent, guarantor funding, etc. The policy would also indicate the security token used.") [ uri[](datatypes.html#uri) ], ... ; # 0..* Policy that authorized event
    fhir:AuditEvent.agent.media[](auditevent-definitions.html#AuditEvent.agent.media "Type of media involved. Used when the event is about exporting/importing onto media.") [ Coding[](datatypes.html#Coding) ]; # 0..1 Type of media
    fhir:AuditEvent.agent.network[](auditevent-definitions.html#AuditEvent.agent.network "Logical network location for application activity, if the activity has a network location.") [ # 0..1 Logical network location for application activity
      fhir:AuditEvent.agent.network.address[](auditevent-definitions.html#AuditEvent.agent.network.address "An identifier for the network access point of the user device for the audit event.") [ string[](datatypes.html#string) ]; # 0..1 Identifier for the network access point of the user device
      fhir:AuditEvent.agent.network.type[](auditevent-definitions.html#AuditEvent.agent.network.type "An identifier for the type of network access point that originated the audit event.") [ code[](datatypes.html#code) ]; # 0..1 The type of network access point
    ];
    fhir:AuditEvent.agent.purposeOfUse[](auditevent-definitions.html#AuditEvent.agent.purposeOfUse "The reason \(purpose of use\), specific to this agent, that was used during the event being recorded.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* Reason given for this user
  ], ...;
  fhir:AuditEvent.source[](auditevent-definitions.html#AuditEvent.source "The system that is reporting the event.") [ # 1..1 Audit Event Reporter
    fhir:AuditEvent.source.site[](auditevent-definitions.html#AuditEvent.source.site "Logical source location within the healthcare enterprise network.  For example, a hospital or other provider location within a multi-entity provider group.") [ string[](datatypes.html#string) ]; # 0..1 Logical source location within the enterprise
    fhir:AuditEvent.source.observer[](auditevent-definitions.html#AuditEvent.source.observer "Identifier of the source where the event was detected.") [ Reference[](references.html#Reference)(PractitionerRole[](practitionerrole.html#PractitionerRole)|Practitioner[](practitioner.html#Practitioner)|Organization[](organization.html#Organization)|Device[](device.html#Device)|Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) ]; # 1..1 The identity of source detecting the event
    fhir:AuditEvent.source.type[](auditevent-definitions.html#AuditEvent.source.type "Code specifying the type of source where event originated.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* The type of source where event originated
  ];
  fhir:AuditEvent.entity[](auditevent-definitions.html#AuditEvent.entity "Specific instances of data or objects that have been accessed.") [ # 0..* Data or objects used
    fhir:AuditEvent.entity.what[](auditevent-definitions.html#AuditEvent.entity.what "Identifies a specific instance of the entity. The reference should be version specific.") [ Reference[](references.html#Reference)(Any[](resourcelist.html)) ]; # 0..1 Specific instance of resource
    fhir:AuditEvent.entity.type[](auditevent-definitions.html#AuditEvent.entity.type "The type of the object that was involved in this audit event.") [ Coding[](datatypes.html#Coding) ]; # 0..1 Type of entity involved
    fhir:AuditEvent.entity.role[](auditevent-definitions.html#AuditEvent.entity.role "Code representing the role the entity played in the event being audited.") [ Coding[](datatypes.html#Coding) ]; # 0..1 What role the entity played
    fhir:AuditEvent.entity.lifecycle[](auditevent-definitions.html#AuditEvent.entity.lifecycle "Identifier for the data life-cycle stage for the entity.") [ Coding[](datatypes.html#Coding) ]; # 0..1 Life-cycle stage for the entity
    fhir:AuditEvent.entity.securityLabel[](auditevent-definitions.html#AuditEvent.entity.securityLabel "Security labels for the identified entity.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* Security labels on the entity
    fhir:AuditEvent.entity.name[](auditevent-definitions.html#AuditEvent.entity.name "A name of the entity in the audit event.") [ string[](datatypes.html#string) ]; # 0..1 Descriptor for entity
    fhir:AuditEvent.entity.description[](auditevent-definitions.html#AuditEvent.entity.description "Text that describes the entity in more detail.") [ string[](datatypes.html#string) ]; # 0..1 Descriptive text
    fhir:AuditEvent.entity.query[](auditevent-definitions.html#AuditEvent.entity.query "The query parameters for a query-type entities.") [ base64Binary[](datatypes.html#base64Binary) ]; # 0..1 Query parameters
    fhir:AuditEvent.entity.detail[](auditevent-definitions.html#AuditEvent.entity.detail "Tagged value pairs for conveying additional information about the entity.") [ # 0..* Additional Information about the entity
      fhir:AuditEvent.entity.detail.type[](auditevent-definitions.html#AuditEvent.entity.detail.type "The type of extra detail provided in the value.") [ string[](datatypes.html#string) ]; # 1..1 Name of the property
      # AuditEvent.entity.detail.value[x][](auditevent-definitions.html#AuditEvent.entity.detail.value\[x\] "The  value of the extra detail.") : 1..1 Property value. One of these 2
        fhir:AuditEvent.entity.detail.valueString[](auditevent-definitions.html#AuditEvent.entity.detail.valueString "The  value of the extra detail.") [ string[](datatypes.html#string) ]
        fhir:AuditEvent.entity.detail.valueBase64Binary[](auditevent-definitions.html#AuditEvent.entity.detail.valueBase64Binary "The  value of the extra detail.") [ base64Binary[](datatypes.html#base64Binary) ]
    ], ...;
  ], ...;
]

```

**Changes since Release 3**
[AuditEvent](auditevent.html#AuditEvent) |   
---|---  
AuditEvent.action | 
  * Change value set from http://hl7.org/fhir/ValueSet/audit-event-action to http://hl7.org/fhir/ValueSet/audit-event-action|4.0.1

  
AuditEvent.period | 
  * Added Element

  
AuditEvent.outcome | 
  * Change value set from http://hl7.org/fhir/ValueSet/audit-event-outcome to http://hl7.org/fhir/ValueSet/audit-event-outcome|4.0.1

  
AuditEvent.agent.type | 
  * Added Element

  
AuditEvent.agent.role | 
  * Remove Binding `http://hl7.org/fhir/ValueSet/security-role-type` (extensible) 

  
AuditEvent.agent.who | 
  * Added Element

  
AuditEvent.agent.network.type | 
  * Change value set from http://hl7.org/fhir/ValueSet/network-type to http://hl7.org/fhir/ValueSet/network-type|4.0.1

  
AuditEvent.source.observer | 
  * **Added Mandatory Element**

  
AuditEvent.source.type | 
  * Change code system for extensibly bound codes from "http://hl7.org/fhir/security-source-type" to "http://terminology.hl7.org/CodeSystem/security-source-type"

  
AuditEvent.entity.what | 
  * Added Element

  
AuditEvent.entity.role | 
  * Change code system for extensibly bound codes from "http://hl7.org/fhir/object-role" to "http://terminology.hl7.org/CodeSystem/object-role"

  
AuditEvent.entity.detail.value[x] | 
  * Renamed from value to value[x]
  * Add Type string

  
AuditEvent.agent.reference | 
  * deleted

  
AuditEvent.agent.userId | 
  * deleted

  
AuditEvent.source.identifier | 
  * deleted

  
AuditEvent.entity.identifier | 
  * deleted

  
AuditEvent.entity.reference | 
  * deleted

  
See the [Full Difference](diff.html) for further information
This analysis is available as [XML](auditevent.diff.xml) or [JSON](auditevent.diff.json). 
See [R3 <--> R4 Conversion Maps](auditevent-version-maps.html) (status = 8 tests that all execute ok. All tests pass round-trip testing and all r3 resources are valid.)
See the [Profiles & Extensions](auditevent-profiles.html) and the alternate definitions: Master Definition [XML](auditevent.profile.xml.html) + [JSON](auditevent.profile.json.html), [XML](xml.html) [Schema](auditevent.xsd)/[Schematron](auditevent.sch) + [JSON](json.html) [Schema](auditevent.schema.json.html), [ShEx](auditevent.shex.html) (for [Turtle](rdf.html)) + [see the extensions](auditevent-profiles.html) & the [dependency analysis](auditevent-dependencies.html)
###  6.4.3.1 Terminology Bindings [](auditevent.html#tx "link to here")
Path | Definition | Type | Reference  
---|---|---|---  
AuditEvent.type  | Type of event. | [Extensible](terminologies.html#extensible) |  [AuditEventID](valueset-audit-event-type.html)  
AuditEvent.subtype  | Sub-type of event. | [Extensible](terminologies.html#extensible) |  [AuditEventSub-Type](valueset-audit-event-sub-type.html)  
AuditEvent.action  | Indicator for type of action performed during the event that generated the event. | [Required](terminologies.html#required) |  [AuditEventAction](valueset-audit-event-action.html)  
AuditEvent.outcome  | Indicates whether the event succeeded or failed. | [Required](terminologies.html#required) |  [AuditEventOutcome](valueset-audit-event-outcome.html)  
AuditEvent.purposeOfEvent  
AuditEvent.agent.purposeOfUse  | The reason the activity took place. | [Extensible](terminologies.html#extensible) |  [v3.PurposeOfUse](v3/PurposeOfUse/vs.html)  
AuditEvent.agent.type  | The Participation type of the agent to the event. | [Extensible](terminologies.html#extensible) |  [ParticipationRoleType](valueset-participation-role-type.html)  
AuditEvent.agent.role  | What security role enabled the agent to participate in the event. | [Example](terminologies.html#example) |  [SecurityRoleType](valueset-security-role-type.html)  
AuditEvent.agent.media  | Used when the event is about exporting/importing onto media. | [Extensible](terminologies.html#extensible) |  [MediaTypeCode](valueset-dicm-405-mediatype.html)  
AuditEvent.agent.network.type  | The type of network access point of this agent in the audit event. | [Required](terminologies.html#required) |  [AuditEventAgentNetworkType](valueset-network-type.html)  
AuditEvent.source.type  | Code specifying the type of system that detected and recorded the event. | [Extensible](terminologies.html#extensible) |  [AuditEventSourceType](valueset-audit-source-type.html)  
AuditEvent.entity.type  | Code for the entity type involved in the audit event. | [Extensible](terminologies.html#extensible) |  [AuditEventEntityType](valueset-audit-entity-type.html)  
AuditEvent.entity.role  | Code representing the role the entity played in the audit event. | [Extensible](terminologies.html#extensible) |  [AuditEventEntityRole](valueset-object-role.html)  
AuditEvent.entity.lifecycle  | Identifier for the data life-cycle stage for the entity. | [Extensible](terminologies.html#extensible) |  [ObjectLifecycleEvents](valueset-object-lifecycle-events.html)  
AuditEvent.entity.securityLabel  | Security Labels from the Healthcare Privacy and Security Classification System. | [Extensible](terminologies.html#extensible) |  [All Security Labels](valueset-security-labels.html)  
###  6.4.3.2 Constraints [](auditevent.html#invs "link to here")
**id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)**  
---|---|---|---|---  
**sev-1** |  [Rule](conformance-rules.html#rule) | AuditEvent.entity | Either a name or a query (NOT both) | name.empty() or query.empty()  
###  6.4.3.3 Using Coded Values [](auditevent.html#6.4.3.3 "link to here")
The AuditEvent resource and the ATNA Audit record are used in many contexts throughout healthcare. The coded values defined in the "extensible" bindings above are those widely used and/or defined by DICOM, IHE or ISO, who defined these codes to meet very specific use cases. These codes should be used when they are suitable. When needed, other codes can be defined. 
Note: When using codes from a vocabulary, the `display` element for the code can be left off to keep the AuditEvent size small and minimize impact of a large audit log of similar entries. 
The set of codes defined for this resource is expected to grow over time, and additional codes may be proposed / requested using the "Propose a change" link above below. 
###  6.4.3.4 Event codes for Common Scenarios [](auditevent.html#6.4.3.4 "link to here")
This table summarizes common event scenarios, and the codes that should be used for each case. 
**Scenario** |  **type** |  **subtype** |  **action** |   
---|---|---|---|---  
User Login ([example](auditevent-examples.html)) |  [110114](codesystem-dicom-dcim.html#110114) User Authentication |  [110122](codesystem-dicom-dcim.html#110122) User Authentication |  [E](valueset-audit-event-action.html) Execute | One agent which contains the details of the logged-in user.  
User Logout ([example](auditevent-examples.html)) |  [110114](codesystem-dicom-dcim.html#110114) User Authentication |  [110123](codesystem-dicom-dcim.html#110123) User Logout |  [E](valueset-audit-event-action.html) Execute | One agent which contains the details of the logged-out user.  
REST operation logged on server ([example](audit-event-example-vread.html)) |  [rest](valueset-audit-event-type.html) RESTful Operation |  [[code]](valueset-type-restful-interaction.html) defined for operation |  [*](valueset-audit-event-action.html) (see below) | Agent for logged in user, if available.  
Search operation logged on server ([example](audit-event-example-search.html)) |  [rest](valueset-audit-event-type.html) RESTful Operation |  [[code]](valueset-type-restful-interaction.html) defined for operation |  [E](valueset-audit-event-action.html) Execute | Agent for logged in user, if available, and one object with a query element.  
Audit Event Actions for RESTful operations: 
**Operation** |  **Action**  
---|---  
create | C  
read, vread, history-instance, history-type, history-system | R  
update | U  
delete | D  
transaction, operation, conformance, validate, search, search-type, search-system | E  
###  6.4.3.5 Encoding a FHIR operation outcome [](auditevent.html#operationoutcome "link to here")
FHIR interactions can result in a rich description of the outcome using the [OperationOutcome](operationoutcome.html). The [OperationOutcome](operationoutcome.html) Resource is a collection of error, warning or information messages that result from a system action. This describes in detail the outcome of some operation, such as when a [RESTful operation](http.html#operations) fails.
When recording into an AuditEvent that some FHIR interaction has happened, the AuditEvent should include the [OperationOutcome](operationoutcome.html) from that FHIR interaction. This is done by placing the OperationOutcome into an AuditEvent.entity. Likely as a [contained](references.html#contained) resource, given that OperationOutcome resources often are not persisted.
`entity.who` is the OperationOutcome -- Likely [contained](references.html#contained)
`entity.type` is code ` 			OperationOutcome[](codesystem-resource-types.html#resource-types-OperationOutcome) 		`
`entity.description` explains why this OperationOutcome was included.
See [transaction failure example](auditevent-example-error.html): When a client attempts to post (create) an `Observation` Resource, using a server `Patient` endpoint; this would result in an error with an OperationOutcome.
###  6.4.3.6 PurposeOfEvent and PurposeOfUse [](auditevent.html#6.4.3.6 "link to here")
The AuditEvent provides the element `purposeOfEvent` to convey the purpose of the event and `purposeOfUse` to convey the reason that a particular actor (machine, person, software) was involved in the event. 
`purposeOfEvent` is an element at the level of AuditEvent and can convey the purpose of the activity that resulted in the event. This will occur when the system that is reporting the event is aware of the purpose of the event. A specific example would be a radiology reporting system where a radiologist has created and is sending a finished report. This system likely knows the purpose, e.g., "treatment". It is multi-valued because the one event may be related to multiple purposes. 
It is also commonplace that the reporting system does not have information about the purpose of the event. In these cases, the event report would not have a purposeOfEvent. 
It is also likely that the same event will be reported from different perspectives, e.g., by both the sender and recipient of a communication. These two different perspectives can have different knowledge regarding the `purposeOfEvent`. 
`purposeOfUse` is an element at the level of `agent` within AuditEvent. This describes the reason that this person, machine, or software is participating in the activity that resulted in the event. For example, an individual person participating in the event may assert a purpose of use from their perspective. It is also possible that they are participating for multiple reasons and report multiple purposeOfUse. 
The reporting system might not have knowledge regarding why a particular machine or person was involved and would omit this element in those cases. 
When the same event is reported from multiple perspectives, the reports can have different knowledge regarding the purpose. 
##  6.4.4 Search Parameters [](auditevent.html#search "link to here")
Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.
**Name** | **Type** | **Description** | **Expression** | **In Common**  
---|---|---|---|---  
action | [token](search.html#token) | Type of action performed during the event | AuditEvent.action |   
address | [string](search.html#string) | Identifier for the network access point of the user device | AuditEvent.agent.network.address |   
agent | [reference](search.html#reference) | Identifier of who | AuditEvent.agent.who  
([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) |   
agent-name | [string](search.html#string) | Human friendly name for the agent | AuditEvent.agent.name |   
agent-role | [token](search.html#token) | Agent role in the event | AuditEvent.agent.role |   
altid | [token](search.html#token) | Alternative User identity | AuditEvent.agent.altId |   
date | [date](search.html#date) | Time when the event was recorded | AuditEvent.recorded |   
entity | [reference](search.html#reference) | Specific instance of resource | AuditEvent.entity.what  
(Any) |   
entity-name | [string](search.html#string) | Descriptor for entity | AuditEvent.entity.name |   
entity-role | [token](search.html#token) | What role the entity played | AuditEvent.entity.role |   
entity-type | [token](search.html#token) | Type of entity involved | AuditEvent.entity.type |   
outcome | [token](search.html#token) | Whether the event succeeded or failed | AuditEvent.outcome |   
patient | [reference](search.html#reference) | Identifier of who | AuditEvent.agent.who.where(resolve() is Patient) | AuditEvent.entity.what.where(resolve() is Patient)  
([Patient](patient.html)) |   
policy | [uri](search.html#uri) | Policy that authorized event | AuditEvent.agent.policy |   
site | [token](search.html#token) | Logical source location within the enterprise | AuditEvent.source.site |   
source | [reference](search.html#reference) | The identity of source detecting the event | AuditEvent.source.observer  
([Practitioner](practitioner.html), [Organization](organization.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) |   
subtype | [token](search.html#token) | More specific type/id for the event | AuditEvent.subtype |   
type | [token](search.html#token) | Type/identifier of event | AuditEvent.type |   
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:34+1100. [QA Page](qa.html)   
Links: [Search ![](external.png)](http://hl7.org/fhir/search.cfm) | [Version History](history.html) | [Table of Contents](toc.html) | [Credits](credits.html) | [Compare to R3 ![](external.png)](http://services.w3.org/htmldiff?doc1=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fauditevent.html&doc2=http%3A%2F%2Fbuild.fhir.org%2Fauditevent.html) | [![CC0](cc0.png)](license.html) | [Propose a change ![](external.png)](http://hl7.org/fhir-issues)
