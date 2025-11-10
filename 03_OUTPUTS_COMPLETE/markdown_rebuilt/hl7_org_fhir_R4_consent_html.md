---
url: https://hl7.org/fhir/R4/consent.html
title: consent.html
source: official_download
extracted: local_file_conversion
mirror_path: consent.html
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
  * **Consent**


**This page is part of a downloaded copy of this specification.** This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html)
  * [Content](#)
  * [Examples](consent-examples.html)
  * [Detailed Descriptions](consent-definitions.html)
  * [Mappings](consent-mappings.html)
  * [Profiles & Extensions](consent-profiles.html)
  * [R3 Conversions](consent-version-maps.html)


#  6.2 Resource Consent - Content [](consent.html#6.2 "link to here")
[Community Based Collaborative Care ![](external.png)](http://www.hl7.org/Special/committees/homehealth/index.cfm) Work Group |  [Maturity Level](versions.html#maturity): 2 |  [Trial Use](versions.html#std-process "Standard Status") |  [Security Category](security.html#SecPrivConsiderations): Patient |  [Compartments](compartmentdefinition.html): [Patient](compartmentdefinition-patient.html)  
---|---|---|---|---  
A record of a healthcare consumer’s choices, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
##  6.2.1 Scope and Usage [](consent.html#scope "link to here")
The purpose of this Resource is to be used to express a Consent regarding Healthcare. There are four anticipated uses for the Consent Resource, all of which are written or verbal agreements by a healthcare consumer [grantor] or a personal representative, made to an authorized entity [grantee] concerning authorized or restricted actions with any limitations on purpose of use, and handling instructions to which the authorized entity must comply: 
  * Privacy Consent Directive: Agreement to collect, access, use or disclose (share) information.
  * Medical Treatment Consent Directive: Consent to undergo a specific treatment (or record of refusal to consent).
  * Research Consent Directive: Consent to participate in research protocol and information sharing required.
  * Advance Care Directives: Consent to instructions for potentially needed medical treatment (e.g. DNR).


This resource is scoped to cover all four uses, but at this time, only the privacy use case is modeled. The scope of the resource may change when the other possible scopes are investigated, tested, or profiled. 
A FHIR Consent Directive instance is considered the encoded legally binding Consent Directive if it meets requirements of a policy domain requirements for an enforceable contract. In some domains, electronic signatures of one or both of the parties to the content of an encoded representation of a Consent Form is deemed to constitute a legally binding Consent Directive. Some domains accept a notary’s electronic signature over the wet or electronic signature of a party to the Consent Directive as the additional identity proofing required to make an encoded Consent Directive legally binding. Other domains may only accept a wet signature or might not require the parties’ signatures at all. 
Whatever the criteria are for making an encoded FHIR Consent Directive legally binding, anything less than a legally binding representation of a Consent Directive must be identified as such, i.e., as a derivative of the legally binding Consent Directive, which has specific usage in Consent Directive workflow management. 
**Definitions:**
Consent | The record of a healthcare consumer’s policy choices, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time  
---|---  
Consent Directive | The legal record of a healthcare consumer's agreement with a party responsible for enforcing the consumer’s choices, which permits or denies identified actors or roles to perform actions affecting the consumer within a given context for specific purposes and periods of time  
Consent Form | Human readable consent content describing one or more actions impacting the grantor for which the grantee would be authorized or prohibited from performing. It includes the terms, rules, and conditions pertaining to the authorization or restrictions, such as effective time, applicability or scope, purposes of use, obligations and prohibitions to which the grantee must comply. Once a Consent Form is “executed” by means required by policy, such as verbal agreement, wet signature, or electronic/digital signature, it becomes a legally binding Consent Directive.  
Consent Directive Derivative | Consent Content that conveys the minimal set of information needed to manage Consent Directive workflow, including providing Consent Directive content sufficient to: 
  * Represent a Consent Directive
  * Register or index a Consent Directive
  * Query and respond about a Consent Directive
  * Retrieve a Consent Directive
  * Notify authorized entities about Consent Directive status changes
  * Determine entities authorized to collect, access, use or disclose information about the Consent Directive or about the information governed by the Consent Directive.

Derived Consent content includes the Security Labels encoding the applicable privacy and security policies. Consent Security Labels inform recipients about specific access control measures required for compliance.  
Consent Statement | A Consent Directive derivative has less than full fidelity to the legally binding Consent Directive from which it was "transcribed". It provides recipients with the full content representation they may require for compliance purposes, and typically include a reference to or an attached unstructured representation for recipients needing an exact copy of the legal agreement.  
Consent Registration | The legal record of a healthcare consumer's agreement with a party responsible for enforcing the consumer’s choices, which permits or denies identified actors or roles to perform actions affecting the consumer within a given context for specific purposes and periods of timeA Consent Directive derivative that conveys the minimal set of information needed to register an active and revoked Consent Directive, or to update Consent status as it changes during its lifecycle.  
Consent Query/Response Types | The FHIR Consent Resource specifies multiple Consent Search parameters, which support many types of queries for Consent Resource content. There are several Query/Response patterns that are typically used for obtaining information about consent directive content for the following use cases: 
  * Find Active Consent Directive: A query that includes sufficient consent directive content to determine whether a specific party is authorized to share information governed by a consent directive with another specific party. The Response is either: 
    * “Yes” meaning that both parties are authorized to share the information with one another.
    * “No” meaning that the authorized querier is not permitted to share with another specific party
    * “No information found” meaning that there is no active Consent Directive in which the querier is authorized to share the governed information.
  * Find Consent Directive Authorized Entities: A query that includes sufficient consent directive content to return a list of entities with which the querier is authorized to share governed information. The response to an authorized querier is the list of any authorized entities with which the querier is permitted to share governed information. The response to an unauthorized querier is that “no information is found”.
  * Find Consent Directive(s): A query that includes sufficient consent directive content to return a list of Consent Directive metadata for an authorized querier to determine what Consent Directives are available, and to locate and retrieve one or more of those Consent Directives as needed.

  
Policy context | Any organizational or jurisdictional policies, which may limit the consumer’s policy choices, and which includes the named range of actions allowed  
Healthcare Consumer | The individual establishing his/her personal consent (i.e. Consenter). In FHIR, this is referred to as the 'Patient' though this word is not used across all contexts of care  
###  6.2.1.1 Privacy Consent Directive (PCD) [](consent.html#PCD "link to here")
Privacy policies define how Individually Identifiable Health Information (IIHI) is to be collected, accessed, used and disclosed. A Privacy Consent Directive as a legal record of a patient's (e.g. a healthcare consumer) agreement with a party responsible for enforcing the patient's choices, which permits or denies identified actors or roles to perform actions affecting the patient within a given context for specific purposes and periods of time. All consent directives have a policy context, which is any set of organizational or jurisdictional policies which may limit the consumer’s policy choices, and which include a named range of actions allowed. In addition, Privacy Consent Directives provide the ability for a healthcare consumer to delegate authority to a Substitute Decision Maker who may act on behalf of that individual. Alternatively, a consumer may author/publish their privacy preferences as a self-declared Privacy Consent Directive. 
The Consent resource on FHIR provides support for alternative representations for expressing interoperable health information privacy consent directives in a standard form for the exchange and enforcement by sending, intermediating, or receiving systems of privacy policies that can be enforced by consuming systems (e.g., scanned documents, of computable structured entries elements, FHIR structures with optional attached, or referenced unstructured representations.) It may be used to represent the Privacy Consent Directive itself, a Consent Statement, which electronically represents a Consent Directive, or Consent Metadata, which is the minimum necessary consent content derived from a Consent Directive for use in workflow management. 
##  6.2.2 Boundaries and Relationships [](consent.html#bnr "link to here")
Consent management - particularly privacy consent - is complicated by the fact that consent to share is often itself necessary to protect. The need to protect the privacy of the privacy statement itself competes with the execution of the consent statement. For this reason, it is common to deal with 'consent statements' that are only partial representations of the full consent statement that the patient provided. 
For this reason, the consent resource contains two elements that refer back to the source: a master identifier, and a direct reference to content from which this Consent Statement was derived. That reference can be one of several things: 
  * A reference to another consent resource from which this limited statement was derived
  * A reference to a document format for the original source (e.g. PDF or CDA - see the [HL7 CDAR2 ConsentDirective Implementation Guide ![](external.png)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=280), which incorporated the [IHE Basic Patient Privacy Consents (BPPC) ![](external.png)](http://wiki.ihe.net/index.php?title=Basic_Patient_Privacy_Consents) ), either directly, or in a reference
  * The source can be included in the consent as an attachment


The consent statements represent a chain that refers back to the original source consent directive. Applications may be able to follow the chain back to the source but should not generally assume that they are authorized to do this. 
Consent Directives are executed by verbal acknowledge or by being signed - either on paper, or digitally. Consent Signatures will be found in the [Provenance](provenance.html) resource (example [consent](consent-example-signature.html) and [signature](provenance-consent-signature.html)). Implementation Guides will generally make rules about what signatures are required, and how they are to be shared and used. 
##  6.2.3 Background and Context [](consent.html#bnc "link to here")
Change to "The Consent resource is structured with a base policy (represented as Consent.policy/Consent.policyRule) which is either opt-in or opt-out, followed by a listing of exceptions to that policy (represented as Consent.provision(s)). The exceptions can be additional positive or negative exceptions upon the base policy. The set of exceptions include a list of data objects, list of authors, list of recipients, list of Organizations, list of purposeOfUse, and Date Range. 
The enforcement of the Privacy Consent Directive is not included but is expected that enforcement can be done using a mix of the various Access Control enforcement methodologies (e.g. OAuth, UMA, XACML). This enforcement includes the details of the enforcement meaning of the elements of the Privacy Consent Directive, such as the rules in place when there is an opt-in consent would be specific about which organizational roles have access to what kinds of resources (e.g. RBAC, ABAC). The specification of these details is not in scope for the Consent resource. 
This resource is referenced by itself and [ResearchSubject](researchsubject.html#ResearchSubject)
##  6.2.4 Resource Content [](consent.html#resource "link to here")
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
![.](tbl_spacer.png)![.](icon_resource.png) [Consent](consent-definitions.html#Consent "Consent : A record of a healthcare consumer’s  choices, which permits or denies identified recipient\(s\) or recipient role\(s\) to perform one or more actions within a given policy context, for specific purposes and periods of time.") |  [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A healthcare consumer's choices to permit or deny recipients or roles to perform actions for specific purposes and periods of time  
+ Rule: Either a Policy or PolicyRule  
+ Rule: IF Scope=privacy, there must be a patient  
+ Rule: IF Scope=research, there must be a patient  
+ Rule: IF Scope=adr, there must be a patient  
+ Rule: IF Scope=treatment, there must be a patient  
Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.

Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource \(including cannot change the meaning of modifierExtension itself\).")  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [identifier](consent-definitions.html#Consent.identifier "Consent.identifier : Unique identifier for this copy of the Consent Statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Identifier](datatypes.html#Identifier) | Identifier for this record (external references)  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [status](consent-definitions.html#Consent.status "Consent.status : Indicates the current state of this consent.") |  [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | proposed | active | rejected | inactive | entered-in-error  
[ConsentState](valueset-consent-state-codes.html "Indicates the state of the consent.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [scope](consent-definitions.html#Consent.scope "Consent.scope : A selector of the type of consent being presented: ADR, Privacy, Treatment, Research.  This list is now extensible.") |  [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Which of the four areas this resource covers (extensible)  
[Consent Scope Codes](valueset-consent-scope.html "The four anticipated uses for the Consent Resource.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [category](consent-definitions.html#Consent.category "Consent.category : A classification of the type of consents found in the statement. This element supports indexing and retrieval of consent statements.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..* | [CodeableConcept](datatypes.html#CodeableConcept) | Classification of the consent statement - for indexing/retrieval  
[Consent Category Codes](valueset-consent-category.html "A classification of the type of consents found in a consent statement.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [patient](consent-definitions.html#Consent.patient "Consent.patient : The patient/healthcare consumer to whom this consent applies.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  [Reference](references.html#Reference)([Patient](patient.html)) | Who the consent applies to  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [dateTime](consent-definitions.html#Consent.dateTime "Consent.dateTime : When this  Consent was issued / created / indexed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | When this Consent was created or indexed  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [performer](consent-definitions.html#Consent.performer "Consent.performer : Either the Grantor, which is the entity responsible for granting the rights listed in a Consent Directive or the Grantee, which is the entity responsible for complying with the Consent Directive, including any obligations or limitations on authorizations and enforcement of prohibitions.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* |  [Reference](references.html#Reference)([Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [RelatedPerson](relatedperson.html) | [PractitionerRole](practitionerrole.html)) | Who is agreeing to the policy and rules  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [organization](consent-definitions.html#Consent.organization "Consent.organization : The organization that manages the consent, and the framework within which it is executed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* |  [Reference](references.html#Reference)([Organization](organization.html)) | Custodian of the consent  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_choice.gif) [source[x]](consent-definitions.html#Consent.source_x_ "Consent.source\[x\] : The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Source from which this consent is taken  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) sourceAttachment |  |  | [Attachment](datatypes.html#Attachment) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) sourceReference |  |  |  [Reference](references.html#Reference)([Consent](consent.html) | [DocumentReference](documentreference.html) | [Contract](contract.html) | [QuestionnaireResponse](questionnaireresponse.html)) |   
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [policy](consent-definitions.html#Consent.policy "Consent.policy : The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.") |  | 0..* | [BackboneElement](backboneelement.html) | Policies covered by this consent  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [authority](consent-definitions.html#Consent.policy.authority "Consent.policy.authority : Entity or Organization having regulatory jurisdiction or accountability for  enforcing policies pertaining to Consent Directives.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | Enforcement source for policy  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [uri](consent-definitions.html#Consent.policy.uri "Consent.policy.uri : The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | Specific policy covered by this consent  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [policyRule](consent-definitions.html#Consent.policyRule "Consent.policyRule : A reference to the specific base computable regulation or policy.") |  [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Regulation that this consents to  
[Consent PolicyRule Codes](valueset-consent-policy.html "Regulatory policy examples.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [verification](consent-definitions.html#Consent.verification "Consent.verification : Whether a treatment instruction \(e.g. artificial respiration yes or no\) was verified with the patient, his/her family or another authorized person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [BackboneElement](backboneelement.html) | Consent Verified by patient or family  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [verified](consent-definitions.html#Consent.verification.verified "Consent.verification.verified : Has the instruction been verified.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [boolean](datatypes.html#boolean) | Has been verified  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [verifiedWith](consent-definitions.html#Consent.verification.verifiedWith "Consent.verification.verifiedWith : Who verified the instruction \(Patient, Relative or other Authorized Person\).") |  | 0..1 |  [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Person who verified  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [verificationDate](consent-definitions.html#Consent.verification.verificationDate "Consent.verification.verificationDate : Date verification was collected.") |  | 0..1 | [dateTime](datatypes.html#dateTime) | When consent verified  
![.](tbl_spacer.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [provision](consent-definitions.html#Consent.provision "Consent.provision : An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [BackboneElement](backboneelement.html) | Constraints to the base Consent.policyRule  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [type](consent-definitions.html#Consent.provision.type "Consent.provision.type : Action  to take - permit or deny - when the rule conditions are met.  Not permitted in root rule, required in all nested rules.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | deny | permit  
[ConsentProvisionType](valueset-consent-provision-type.html "How a rule statement is applied, such as adding additional consent or removing consent.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [period](consent-definitions.html#Consent.provision.period "Consent.provision.period : The timeframe in this rule is valid.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Timeframe for this rule  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_element.gif) [actor](consent-definitions.html#Consent.provision.actor "Consent.provision.actor : Who or what is controlled by this rule. Use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).") |  | 0..* | [BackboneElement](backboneelement.html) | Who|what controlled by this rule (or group, by role)  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [role](consent-definitions.html#Consent.provision.actor.role "Consent.provision.actor.role : How the individual is involved in the resources content that is described in the exception.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | How the actor is involved  
[SecurityRoleType](valueset-security-role-type.html "How an actor is involved in the consent considerations.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) [reference](consent-definitions.html#Consent.provision.actor.reference "Consent.provision.actor.reference : The resource that identifies the actor. To identify actors by type, use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).") |  | 1..1 |  [Reference](references.html#Reference)([Device](device.html) | [Group](group.html) | [CareTeam](careteam.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [RelatedPerson](relatedperson.html) | [PractitionerRole](practitionerrole.html)) | Resource for the actor (or group, by role)  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [action](consent-definitions.html#Consent.provision.action "Consent.provision.action : Actions controlled by this Rule.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Actions controlled by this rule  
[Consent Action Codes](valueset-consent-action.html "Detailed codes for the consent action.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [securityLabel](consent-definitions.html#Consent.provision.securityLabel "Consent.provision.securityLabel : A security label, comprised of 0..* security label fields \(Privacy tags\), which define which resources are controlled by this exception.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Coding](datatypes.html#Coding) | Security Labels that define affected resources  
[SecurityLabels](valueset-security-labels.html "Security Labels from the Healthcare Privacy and Security Classification System.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [purpose](consent-definitions.html#Consent.provision.purpose "Consent.provision.purpose : The context of the activities a user is taking - why the user is accessing the data - that are controlled by this rule.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Coding](datatypes.html#Coding) | Context of activities covered by this rule  
[V3 Value SetPurposeOfUse](v3/PurposeOfUse/vs.html "What purposes of use are controlled by this exception. If more than one label is specified, operations must have all the specified labels.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [class](consent-definitions.html#Consent.provision.class "Consent.provision.class : The class of information covered by this rule. The type can be a FHIR resource type, a profile on a type, or a CDA document, or some other type that indicates what sort of information the consent relates to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Coding](datatypes.html#Coding) | e.g. Resource Type, Profile, CDA, etc.  
[Consent Content Class](valueset-consent-content-class.html "The class \(type\) of information a consent rule covers.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [code](consent-definitions.html#Consent.provision.code "Consent.provision.code : If this code is found in an instance, then the rule applies.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | e.g. LOINC or SNOMED CT code, etc. in the content  
[Consent Content Codes](valueset-consent-content-code.html "If this code is found in an instance, then the exception applies.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [dataPeriod](consent-definitions.html#Consent.provision.dataPeriod "Consent.provision.dataPeriod : Clinical or Operational Relevant period of time that bounds the data controlled by this rule.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Timeframe for data controlled by this rule  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_element.gif) [data](consent-definitions.html#Consent.provision.data "Consent.provision.data : The resources controlled by this rule if specific resources are referenced.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [BackboneElement](backboneelement.html) | Data controlled by this rule  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [meaning](consent-definitions.html#Consent.provision.data.meaning "Consent.provision.data.meaning : How the resource reference is interpreted when testing consent restrictions.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | instance | related | dependents | authoredby  
[ConsentDataMeaning](valueset-consent-data-meaning.html "How a resource reference is interpreted when testing consent restrictions.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) [reference](consent-definitions.html#Consent.provision.data.reference "Consent.provision.data.reference : A reference to a specific resource that defines which resources are covered by this consent.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [Reference](references.html#Reference)([Any](resourcelist.html)) | The actual data reference  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_reuse.png) [provision](consent-definitions.html#Consent.provision.provision "Consent.provision.provision : Rules which provide exceptions to the base rule or subrules.") |  | 0..* | see [provision](#Consent.provision "Consent.provision") | Nested Exception Rules  
  
  
[![doco](help16.png) Documentation for this format](formats.html#table "Legend for this format")  
**UML Diagram** ([Legend](formats.html#uml))
Consent (DomainResource)Unique identifier for this copy of the Consent Statementidentifier : Identifier [0..*]Indicates the current state of this consent (this element modifies the meaning of other elements)status : code [1..1] « Indicates the state of the consent. (Strength=Required)ConsentState! »A selector of the type of consent being presented: ADR, Privacy, Treatment, Research. This list is now extensible (this element modifies the meaning of other elements)scope : CodeableConcept [1..1] « The four anticipated uses for the Consent Resource. (Strength=Extensible)ConsentScopeCodes+ »A classification of the type of consents found in the statement. This element supports indexing and retrieval of consent statementscategory : CodeableConcept [1..*] « A classification of the type of consents found in a consent statement. (Strength=Extensible)ConsentCategoryCodes+ »The patient/healthcare consumer to whom this consent appliespatient : Reference [0..1] « Patient »When this Consent was issued / created / indexeddateTime : dateTime [0..1]Either the Grantor, which is the entity responsible for granting the rights listed in a Consent Directive or the Grantee, which is the entity responsible for complying with the Consent Directive, including any obligations or limitations on authorizations and enforcement of prohibitionsperformer : Reference [0..*] « Organization|Patient|Practitioner| RelatedPerson|PractitionerRole »The organization that manages the consent, and the framework within which it is executedorganization : Reference [0..*] « Organization »The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository (e.g. XDS) that stores the original consent documentsource[x] : Type [0..1] « Attachment|Reference(Consent| DocumentReference|Contract|QuestionnaireResponse) »A reference to the specific base computable regulation or policypolicyRule : CodeableConcept [0..1] « Regulatory policy examples. (Strength=Extensible)ConsentPolicyRuleCodes+ »PolicyEntity or Organization having regulatory jurisdiction or accountability for enforcing policies pertaining to Consent Directivesauthority : uri [0..1]The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in lawuri : uri [0..1]VerificationHas the instruction been verifiedverified : boolean [1..1]Who verified the instruction (Patient, Relative or other Authorized Person)verifiedWith : Reference [0..1] « Patient|RelatedPerson »Date verification was collectedverificationDate : dateTime [0..1]provisionAction to take - permit or deny - when the rule conditions are met. Not permitted in root rule, required in all nested rulestype : code [0..1] « How a rule statement is applied, such as adding additional consent or removing consent. (Strength=Required)ConsentProvisionType! »The timeframe in this rule is validperiod : Period [0..1]Actions controlled by this Ruleaction : CodeableConcept [0..*] « Detailed codes for the consent action. (Strength=Example)ConsentActionCodes?? »A security label, comprised of 0..* security label fields (Privacy tags), which define which resources are controlled by this exceptionsecurityLabel : Coding [0..*] « Security Labels from the Healthcare Privacy and Security Classification System. (Strength=Extensible)All Security Labels+ »The context of the activities a user is taking - why the user is accessing the data - that are controlled by this rulepurpose : Coding [0..*] « What purposes of use are controlled by this exception. If more than one label is specified, operations must have all the specified labels. (Strength=Extensible)v3.PurposeOfUse+ »The class of information covered by this rule. The type can be a FHIR resource type, a profile on a type, or a CDA document, or some other type that indicates what sort of information the consent relates toclass : Coding [0..*] « The class (type) of information a consent rule covers. (Strength=Extensible)ConsentContentClass+ »If this code is found in an instance, then the rule appliescode : CodeableConcept [0..*] « If this code is found in an instance, then the exception applies. (Strength=Example)ConsentContentCodes?? »Clinical or Operational Relevant period of time that bounds the data controlled by this ruledataPeriod : Period [0..1]provisionActorHow the individual is involved in the resources content that is described in the exceptionrole : CodeableConcept [1..1] « How an actor is involved in the consent considerations. (Strength=Extensible)SecurityRoleType+ »The resource that identifies the actor. To identify actors by type, use group to identify a set of actors by some property they share (e.g. 'admitting officers')reference : Reference [1..1] « Device|Group|CareTeam|Organization| Patient|Practitioner|RelatedPerson|PractitionerRole »provisionDataHow the resource reference is interpreted when testing consent restrictionsmeaning : code [1..1] « How a resource reference is interpreted when testing consent restrictions. (Strength=Required)ConsentDataMeaning! »A reference to a specific resource that defines which resources are covered by this consentreference : Reference [1..1] « Any »The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in lawpolicy[0..*]Whether a treatment instruction (e.g. artificial respiration yes or no) was verified with the patient, his/her family or another authorized personverification[0..*]Who or what is controlled by this rule. Use group to identify a set of actors by some property they share (e.g. 'admitting officers')actor[0..*]The resources controlled by this rule if specific resources are referenceddata[0..*]Rules which provide exceptions to the base rule or subrulesprovision[0..*]An exception to the base policy of this consent. An exception can be an addition or removal of access permissionsprovision[0..1]
**XML Template**
```

<[**Consent**](consent-definitions.html#Consent "A record of a healthcare consumerâ€™s  choices, which permits or denies identified recipient\(s\) or recipient role\(s\) to perform one or more actions within a given policy context, for specific purposes and periods of time.") xmlns="http://hl7.org/fhir"> [![doco](help.png)](xml.html "Documentation for this format")
 <!-- from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language) -->
 <!-- from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension) -->
 <[**identifier**](consent-definitions.html#Consent.identifier "Unique identifier for this copy of the Consent Statement.")><!-- **0..*** Identifier[](datatypes.html#Identifier) Identifier for this record (external references)[](terminologies.html#unbound) --></identifier>
 <[**status**](consent-definitions.html#Consent.status "Indicates the current state of this consent \(this element modifies the meaning of other elements\)") value="[code[](datatypes.html#code)]"/><!-- **1..1** draft | proposed | active | rejected | inactive | entered-in-error[](valueset-consent-state-codes.html) -->
 <[**scope**](consent-definitions.html#Consent.scope "A selector of the type of consent being presented: ADR, Privacy, Treatment, Research.  This list is now extensible \(this element modifies the meaning of other elements\)")><!-- **1..1** CodeableConcept[](datatypes.html#CodeableConcept) Which of the four areas this resource covers (extensible)[](valueset-consent-scope.html) --></scope>
 <[**category**](consent-definitions.html#Consent.category "A classification of the type of consents found in the statement. This element supports indexing and retrieval of consent statements.")><!-- **1..*** CodeableConcept[](datatypes.html#CodeableConcept) Classification of the consent statement - for indexing/retrieval[](valueset-consent-category.html) --></category>
 <[**patient**](consent-definitions.html#Consent.patient "The patient/healthcare consumer to whom this consent applies.")><!-- **0..1** Reference[](references.html#Reference)(Patient[](patient.html#Patient)) Who the consent applies to[](terminologies.html#unbound) --></patient>
 <[**dateTime**](consent-definitions.html#Consent.dateTime "When this  Consent was issued / created / indexed.") value="[dateTime[](datatypes.html#dateTime)]"/><!-- **0..1** When this Consent was created or indexed[](terminologies.html#unbound) -->
 <[**performer**](consent-definitions.html#Consent.performer "Either the Grantor, which is the entity responsible for granting the rights listed in a Consent Directive or the Grantee, which is the entity responsible for complying with the Consent Directive, including any obligations or limitations on authorizations and enforcement of prohibitions.")><!-- **0..*** Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|
   PractitionerRole[](practitionerrole.html#PractitionerRole)) Who is agreeing to the policy and rules[](terminologies.html#unbound) --></performer>
 <[**organization**](consent-definitions.html#Consent.organization "The organization that manages the consent, and the framework within which it is executed.")><!-- **0..*** Reference[](references.html#Reference)(Organization[](organization.html#Organization)) Custodian of the consent[](terminologies.html#unbound) --></organization>
 <[**source[x]**](consent-definitions.html#Consent.source\[x\] "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.")><!-- **0..1** Attachment[](datatypes.html#Attachment)|Reference[](references.html#Reference)(Consent[](consent.html#Consent)|DocumentReference[](documentreference.html#DocumentReference)|Contract[](contract.html#Contract)|
   QuestionnaireResponse[](questionnaireresponse.html#QuestionnaireResponse)) Source from which this consent is taken[](terminologies.html#unbound) --></source[x]>
 <[**policy**](consent-definitions.html#Consent.policy "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.")>  <!-- **0..*** Policies covered by this consent -->
  <[**authority**](consent-definitions.html#Consent.policy.authority "Entity or Organization having regulatory jurisdiction or accountability for  enforcing policies pertaining to Consent Directives.") value="[uri[](datatypes.html#uri)]"/><!-- **![??](lock.png) 0..1** Enforcement source for policy[](terminologies.html#unbound) -->
  <[**uri**](consent-definitions.html#Consent.policy.uri "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.") value="[uri[](datatypes.html#uri)]"/><!-- **![??](lock.png) 0..1** Specific policy covered by this consent[](terminologies.html#unbound) -->
 </policy>
 <[**policyRule**](consent-definitions.html#Consent.policyRule "A reference to the specific base computable regulation or policy.")><!-- **![??](lock.png) 0..1** CodeableConcept[](datatypes.html#CodeableConcept) Regulation that this consents to[](valueset-consent-policy.html) --></policyRule>
 <[**verification**](consent-definitions.html#Consent.verification "Whether a treatment instruction \(e.g. artificial respiration yes or no\) was verified with the patient, his/her family or another authorized person.")>  <!-- **0..*** Consent Verified by patient or family -->
  <[**verified**](consent-definitions.html#Consent.verification.verified "Has the instruction been verified.") value="[boolean[](datatypes.html#boolean)]"/><!-- **1..1** Has been verified[](terminologies.html#unbound) -->
  <[**verifiedWith**](consent-definitions.html#Consent.verification.verifiedWith "Who verified the instruction \(Patient, Relative or other Authorized Person\).")><!-- **0..1** Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) Person who verified[](terminologies.html#unbound) --></verifiedWith>
  <[**verificationDate**](consent-definitions.html#Consent.verification.verificationDate "Date verification was collected.") value="[dateTime[](datatypes.html#dateTime)]"/><!-- **0..1** When consent verified[](terminologies.html#unbound) -->
 </verification>
 <[**provision**](consent-definitions.html#Consent.provision "An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.")>  <!-- **0..1** Constraints to the base Consent.policyRule -->
  <[**type**](consent-definitions.html#Consent.provision.type "Action  to take - permit or deny - when the rule conditions are met.  Not permitted in root rule, required in all nested rules.") value="[code[](datatypes.html#code)]"/><!-- **0..1** deny | permit[](valueset-consent-provision-type.html) -->
  <[**period**](consent-definitions.html#Consent.provision.period "The timeframe in this rule is valid.")><!-- **0..1** Period[](datatypes.html#Period) Timeframe for this rule[](terminologies.html#unbound) --></period>
  <[**actor**](consent-definitions.html#Consent.provision.actor "Who or what is controlled by this rule. Use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).")>  <!-- **0..*** Who|what controlled by this rule (or group, by role) -->
   <[**role**](consent-definitions.html#Consent.provision.actor.role "How the individual is involved in the resources content that is described in the exception.")><!-- **1..1** CodeableConcept[](datatypes.html#CodeableConcept) How the actor is involved[](valueset-security-role-type.html) --></role>
   <[**reference**](consent-definitions.html#Consent.provision.actor.reference "The resource that identifies the actor. To identify actors by type, use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).")><!-- **1..1** Reference[](references.html#Reference)(Device[](device.html#Device)|Group[](group.html#Group)|CareTeam[](careteam.html#CareTeam)|Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|
     Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|PractitionerRole[](practitionerrole.html#PractitionerRole)) Resource for the actor (or group, by role)[](terminologies.html#unbound) --></reference>
  </actor>
  <[**action**](consent-definitions.html#Consent.provision.action "Actions controlled by this Rule.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) Actions controlled by this rule[](valueset-consent-action.html) --></action>
  <[**securityLabel**](consent-definitions.html#Consent.provision.securityLabel "A security label, comprised of 0..* security label fields \(Privacy tags\), which define which resources are controlled by this exception.")><!-- **0..*** Coding[](datatypes.html#Coding) Security Labels that define affected resources[](valueset-security-labels.html) --></securityLabel>
  <[**purpose**](consent-definitions.html#Consent.provision.purpose "The context of the activities a user is taking - why the user is accessing the data - that are controlled by this rule.")><!-- **0..*** Coding[](datatypes.html#Coding) Context of activities covered by this rule[](v3/PurposeOfUse/vs.html) --></purpose>
  <[**class**](consent-definitions.html#Consent.provision.class "The class of information covered by this rule. The type can be a FHIR resource type, a profile on a type, or a CDA document, or some other type that indicates what sort of information the consent relates to.")><!-- **0..*** Coding[](datatypes.html#Coding) e.g. Resource Type, Profile, CDA, etc.[](valueset-consent-content-class.html) --></class>
  <[**code**](consent-definitions.html#Consent.provision.code "If this code is found in an instance, then the rule applies.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) e.g. LOINC or SNOMED CT code, etc. in the content[](valueset-consent-content-code.html) --></code>
  <[**dataPeriod**](consent-definitions.html#Consent.provision.dataPeriod "Clinical or Operational Relevant period of time that bounds the data controlled by this rule.")><!-- **0..1** Period[](datatypes.html#Period) Timeframe for data controlled by this rule[](terminologies.html#unbound) --></dataPeriod>
  <[**data**](consent-definitions.html#Consent.provision.data "The resources controlled by this rule if specific resources are referenced.")>  <!-- **0..*** Data controlled by this rule -->
   <[**meaning**](consent-definitions.html#Consent.provision.data.meaning "How the resource reference is interpreted when testing consent restrictions.") value="[code[](datatypes.html#code)]"/><!-- **1..1** instance | related | dependents | authoredby[](valueset-consent-data-meaning.html) -->
   <[**reference**](consent-definitions.html#Consent.provision.data.reference "A reference to a specific resource that defines which resources are covered by this consent.")><!-- **1..1** Reference[](references.html#Reference)(Any[](resourcelist.html)) The actual data reference[](terminologies.html#unbound) --></reference>
  </data>
  <[**provision**](consent-definitions.html#Consent.provision.provision "Rules which provide exceptions to the base rule or subrules.")><!-- **0..*** Content as for Consent.provision Nested Exception Rules[](terminologies.html#unbound) --></provision>
 </provision>
</Consent>

```

**JSON Template**
```

{[![doco](help.png)](json.html "Documentation for this format")
  "resourceType" : "[**Consent**](consent-definitions.html#Consent "A record of a healthcare consumerâ€™s  choices, which permits or denies identified recipient\(s\) or recipient role\(s\) to perform one or more actions within a given policy context, for specific purposes and periods of time.")",
  // from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language)
  // from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension)
  "identifier[](consent-definitions.html#Consent.identifier "Unique identifier for this copy of the Consent Statement.")" : [{ Identifier[](datatypes.html#Identifier) }], // Identifier for this record (external references)[](terminologies.html#unbound)
  "[status](consent-definitions.html#Consent.status "Indicates the current state of this consent \(this element modifies the meaning of other elements\)")" : "<code[](datatypes.html#code)>", // **R!**  draft | proposed | active | rejected | inactive | entered-in-error[](valueset-consent-state-codes.html)
  "[scope](consent-definitions.html#Consent.scope "A selector of the type of consent being presented: ADR, Privacy, Treatment, Research.  This list is now extensible \(this element modifies the meaning of other elements\)")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // **R!**  Which of the four areas this resource covers (extensible)[](valueset-consent-scope.html)
  "category[](consent-definitions.html#Consent.category "A classification of the type of consents found in the statement. This element supports indexing and retrieval of consent statements.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // **R!**  Classification of the consent statement - for indexing/retrieval[](valueset-consent-category.html)
  "patient[](consent-definitions.html#Consent.patient "The patient/healthcare consumer to whom this consent applies.")" : { Reference[](references.html#Reference)(Patient[](patient.html#Patient)) }, // Who the consent applies to[](terminologies.html#unbound)
  "dateTime[](consent-definitions.html#Consent.dateTime "When this  Consent was issued / created / indexed.")" : "<dateTime[](datatypes.html#dateTime)>", // When this Consent was created or indexed[](terminologies.html#unbound)
  "performer[](consent-definitions.html#Consent.performer "Either the Grantor, which is the entity responsible for granting the rights listed in a Consent Directive or the Grantee, which is the entity responsible for complying with the Consent Directive, including any obligations or limitations on authorizations and enforcement of prohibitions.")" : [{ Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|
   PractitionerRole[](practitionerrole.html#PractitionerRole)) }], // Who is agreeing to the policy and rules[](terminologies.html#unbound)
  "organization[](consent-definitions.html#Consent.organization "The organization that manages the consent, and the framework within which it is executed.")" : [{ Reference[](references.html#Reference)(Organization[](organization.html#Organization)) }], // Custodian of the consent[](terminologies.html#unbound)
  // source[x]: Source from which this consent is taken. One of these 2:
  "sourceAttachment[](consent-definitions.html#Consent.sourceAttachment "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.")" : { Attachment[](datatypes.html#Attachment) },
  "sourceReference[](consent-definitions.html#Consent.sourceReference "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.")" : { Reference[](references.html#Reference)(Consent[](consent.html#Consent)|DocumentReference[](documentreference.html#DocumentReference)|Contract[](contract.html#Contract)|
   QuestionnaireResponse[](questionnaireresponse.html#QuestionnaireResponse)) },
  "policy[](consent-definitions.html#Consent.policy "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.")" : [{ // Policies covered by this consent[](terminologies.html#unbound)
    "authority[](consent-definitions.html#Consent.policy.authority "Entity or Organization having regulatory jurisdiction or accountability for  enforcing policies pertaining to Consent Directives.")" : "<uri[](datatypes.html#uri)>", // **C?** Enforcement source for policy[](terminologies.html#unbound)
    "uri[](consent-definitions.html#Consent.policy.uri "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.")" : "<uri[](datatypes.html#uri)>" // **C?** Specific policy covered by this consent[](terminologies.html#unbound)
  }],
  "policyRule[](consent-definitions.html#Consent.policyRule "A reference to the specific base computable regulation or policy.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // **C?** Regulation that this consents to[](valueset-consent-policy.html)
  "verification[](consent-definitions.html#Consent.verification "Whether a treatment instruction \(e.g. artificial respiration yes or no\) was verified with the patient, his/her family or another authorized person.")" : [{ // Consent Verified by patient or family[](terminologies.html#unbound)
    "verified[](consent-definitions.html#Consent.verification.verified "Has the instruction been verified.")" : <boolean[](datatypes.html#boolean)>, // **R!**  Has been verified[](terminologies.html#unbound)
    "verifiedWith[](consent-definitions.html#Consent.verification.verifiedWith "Who verified the instruction \(Patient, Relative or other Authorized Person\).")" : { Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) }, // Person who verified[](terminologies.html#unbound)
    "verificationDate[](consent-definitions.html#Consent.verification.verificationDate "Date verification was collected.")" : "<dateTime[](datatypes.html#dateTime)>" // When consent verified[](terminologies.html#unbound)
  }],
  "provision[](consent-definitions.html#Consent.provision "An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.")" : { // Constraints to the base Consent.policyRule[](terminologies.html#unbound)
    "type[](consent-definitions.html#Consent.provision.type "Action  to take - permit or deny - when the rule conditions are met.  Not permitted in root rule, required in all nested rules.")" : "<code[](datatypes.html#code)>", // deny | permit[](valueset-consent-provision-type.html)
    "period[](consent-definitions.html#Consent.provision.period "The timeframe in this rule is valid.")" : { Period[](datatypes.html#Period) }, // Timeframe for this rule[](terminologies.html#unbound)
    "actor[](consent-definitions.html#Consent.provision.actor "Who or what is controlled by this rule. Use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).")" : [{ // Who|what controlled by this rule (or group, by role)[](terminologies.html#unbound)
      "role[](consent-definitions.html#Consent.provision.actor.role "How the individual is involved in the resources content that is described in the exception.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // **R!**  How the actor is involved[](valueset-security-role-type.html)
      "reference[](consent-definitions.html#Consent.provision.actor.reference "The resource that identifies the actor. To identify actors by type, use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).")" : { Reference[](references.html#Reference)(Device[](device.html#Device)|Group[](group.html#Group)|CareTeam[](careteam.html#CareTeam)|Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|
     Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|PractitionerRole[](practitionerrole.html#PractitionerRole)) } // **R!**  Resource for the actor (or group, by role)[](terminologies.html#unbound)
    }],
    "action[](consent-definitions.html#Consent.provision.action "Actions controlled by this Rule.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // Actions controlled by this rule[](valueset-consent-action.html)
    "securityLabel[](consent-definitions.html#Consent.provision.securityLabel "A security label, comprised of 0..* security label fields \(Privacy tags\), which define which resources are controlled by this exception.")" : [{ Coding[](datatypes.html#Coding) }], // Security Labels that define affected resources[](valueset-security-labels.html)
    "purpose[](consent-definitions.html#Consent.provision.purpose "The context of the activities a user is taking - why the user is accessing the data - that are controlled by this rule.")" : [{ Coding[](datatypes.html#Coding) }], // Context of activities covered by this rule[](v3/PurposeOfUse/vs.html)
    "class[](consent-definitions.html#Consent.provision.class "The class of information covered by this rule. The type can be a FHIR resource type, a profile on a type, or a CDA document, or some other type that indicates what sort of information the consent relates to.")" : [{ Coding[](datatypes.html#Coding) }], // e.g. Resource Type, Profile, CDA, etc.[](valueset-consent-content-class.html)
    "code[](consent-definitions.html#Consent.provision.code "If this code is found in an instance, then the rule applies.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // e.g. LOINC or SNOMED CT code, etc. in the content[](valueset-consent-content-code.html)
    "dataPeriod[](consent-definitions.html#Consent.provision.dataPeriod "Clinical or Operational Relevant period of time that bounds the data controlled by this rule.")" : { Period[](datatypes.html#Period) }, // Timeframe for data controlled by this rule[](terminologies.html#unbound)
    "data[](consent-definitions.html#Consent.provision.data "The resources controlled by this rule if specific resources are referenced.")" : [{ // Data controlled by this rule[](terminologies.html#unbound)
      "meaning[](consent-definitions.html#Consent.provision.data.meaning "How the resource reference is interpreted when testing consent restrictions.")" : "<code[](datatypes.html#code)>", // **R!**  instance | related | dependents | authoredby[](valueset-consent-data-meaning.html)
      "reference[](consent-definitions.html#Consent.provision.data.reference "A reference to a specific resource that defines which resources are covered by this consent.")" : { Reference[](references.html#Reference)(Any[](resourcelist.html)) } // **R!**  The actual data reference[](terminologies.html#unbound)
    }],
    "provision[](consent-definitions.html#Consent.provision.provision "Rules which provide exceptions to the base rule or subrules.")" : [{ Content as for Consent.provision }] // Nested Exception Rules[](terminologies.html#unbound)
  }
}

```

**Turtle Template**
```

@prefix fhir: <http://hl7.org/fhir/> .[![doco](help.png)](rdf.html "Documentation for this format")


[ a fhir:[**Consent**](consent-definitions.html#Consent "A record of a healthcare consumerâ€™s  choices, which permits or denies identified recipient\(s\) or recipient role\(s\) to perform one or more actions within a given policy context, for specific purposes and periods of time.");
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource[](resource.html): .id[](resource.html#id), .meta[](resource.html#meta), .implicitRules[](resource.html#implicitRules), and .language[](resource.html#language)
  # from DomainResource[](domainresource.html): .text[](narrative.html#Narrative), .contained[](references.html#contained), .extension[](extensibility.html), and .modifierExtension[](extensibility.html#modifierExtension)
  fhir:Consent.identifier[](consent-definitions.html#Consent.identifier "Unique identifier for this copy of the Consent Statement.") [ Identifier[](datatypes.html#Identifier) ], ... ; # 0..* Identifier for this record (external references)
  fhir:[Consent.status](consent-definitions.html#Consent.status "Indicates the current state of this consent \(this element modifies the meaning of other elements\)") [ code[](datatypes.html#code) ]; # 1..1 draft | proposed | active | rejected | inactive | entered-in-error
  fhir:[Consent.scope](consent-definitions.html#Consent.scope "A selector of the type of consent being presented: ADR, Privacy, Treatment, Research.  This list is now extensible \(this element modifies the meaning of other elements\)") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 1..1 Which of the four areas this resource covers (extensible)
  fhir:Consent.category[](consent-definitions.html#Consent.category "A classification of the type of consents found in the statement. This element supports indexing and retrieval of consent statements.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 1..* Classification of the consent statement - for indexing/retrieval
  fhir:Consent.patient[](consent-definitions.html#Consent.patient "The patient/healthcare consumer to whom this consent applies.") [ Reference[](references.html#Reference)(Patient[](patient.html#Patient)) ]; # 0..1 Who the consent applies to
  fhir:Consent.dateTime[](consent-definitions.html#Consent.dateTime "When this  Consent was issued / created / indexed.") [ dateTime[](datatypes.html#dateTime) ]; # 0..1 When this Consent was created or indexed
  fhir:Consent.performer[](consent-definitions.html#Consent.performer "Either the Grantor, which is the entity responsible for granting the rights listed in a Consent Directive or the Grantee, which is the entity responsible for complying with the Consent Directive, including any obligations or limitations on authorizations and enforcement of prohibitions.") [ Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|PractitionerRole[](practitionerrole.html#PractitionerRole)) ], ... ; # 0..* Who is agreeing to the policy and rules
  fhir:Consent.organization[](consent-definitions.html#Consent.organization "The organization that manages the consent, and the framework within which it is executed.") [ Reference[](references.html#Reference)(Organization[](organization.html#Organization)) ], ... ; # 0..* Custodian of the consent
  # Consent.source[x][](consent-definitions.html#Consent.source\[x\] "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.") : 0..1 Source from which this consent is taken. One of these 2
    fhir:Consent.sourceAttachment[](consent-definitions.html#Consent.sourceAttachment "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.") [ Attachment[](datatypes.html#Attachment) ]
    fhir:Consent.sourceReference[](consent-definitions.html#Consent.sourceReference "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.") [ Reference[](references.html#Reference)(Consent[](consent.html#Consent)|DocumentReference[](documentreference.html#DocumentReference)|Contract[](contract.html#Contract)|QuestionnaireResponse[](questionnaireresponse.html#QuestionnaireResponse)) ]
  fhir:Consent.policy[](consent-definitions.html#Consent.policy "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.") [ # 0..* Policies covered by this consent
    fhir:Consent.policy.authority[](consent-definitions.html#Consent.policy.authority "Entity or Organization having regulatory jurisdiction or accountability for  enforcing policies pertaining to Consent Directives.") [ uri[](datatypes.html#uri) ]; # 0..1 Enforcement source for policy
    fhir:Consent.policy.uri[](consent-definitions.html#Consent.policy.uri "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.") [ uri[](datatypes.html#uri) ]; # 0..1 Specific policy covered by this consent
  ], ...;
  fhir:Consent.policyRule[](consent-definitions.html#Consent.policyRule "A reference to the specific base computable regulation or policy.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 0..1 Regulation that this consents to
  fhir:Consent.verification[](consent-definitions.html#Consent.verification "Whether a treatment instruction \(e.g. artificial respiration yes or no\) was verified with the patient, his/her family or another authorized person.") [ # 0..* Consent Verified by patient or family
    fhir:Consent.verification.verified[](consent-definitions.html#Consent.verification.verified "Has the instruction been verified.") [ boolean[](datatypes.html#boolean) ]; # 1..1 Has been verified
    fhir:Consent.verification.verifiedWith[](consent-definitions.html#Consent.verification.verifiedWith "Who verified the instruction \(Patient, Relative or other Authorized Person\).") [ Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) ]; # 0..1 Person who verified
    fhir:Consent.verification.verificationDate[](consent-definitions.html#Consent.verification.verificationDate "Date verification was collected.") [ dateTime[](datatypes.html#dateTime) ]; # 0..1 When consent verified
  ], ...;
  fhir:Consent.provision[](consent-definitions.html#Consent.provision "An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.") [ # 0..1 Constraints to the base Consent.policyRule
    fhir:Consent.provision.type[](consent-definitions.html#Consent.provision.type "Action  to take - permit or deny - when the rule conditions are met.  Not permitted in root rule, required in all nested rules.") [ code[](datatypes.html#code) ]; # 0..1 deny | permit
    fhir:Consent.provision.period[](consent-definitions.html#Consent.provision.period "The timeframe in this rule is valid.") [ Period[](datatypes.html#Period) ]; # 0..1 Timeframe for this rule
    fhir:Consent.provision.actor[](consent-definitions.html#Consent.provision.actor "Who or what is controlled by this rule. Use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).") [ # 0..* Who|what controlled by this rule (or group, by role)
      fhir:Consent.provision.actor.role[](consent-definitions.html#Consent.provision.actor.role "How the individual is involved in the resources content that is described in the exception.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 1..1 How the actor is involved
      fhir:Consent.provision.actor.reference[](consent-definitions.html#Consent.provision.actor.reference "The resource that identifies the actor. To identify actors by type, use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).") [ Reference[](references.html#Reference)(Device[](device.html#Device)|Group[](group.html#Group)|CareTeam[](careteam.html#CareTeam)|Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|
  PractitionerRole[](practitionerrole.html#PractitionerRole)) ]; # 1..1 Resource for the actor (or group, by role)
    ], ...;
    fhir:Consent.provision.action[](consent-definitions.html#Consent.provision.action "Actions controlled by this Rule.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* Actions controlled by this rule
    fhir:Consent.provision.securityLabel[](consent-definitions.html#Consent.provision.securityLabel "A security label, comprised of 0..* security label fields \(Privacy tags\), which define which resources are controlled by this exception.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* Security Labels that define affected resources
    fhir:Consent.provision.purpose[](consent-definitions.html#Consent.provision.purpose "The context of the activities a user is taking - why the user is accessing the data - that are controlled by this rule.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* Context of activities covered by this rule
    fhir:Consent.provision.class[](consent-definitions.html#Consent.provision.class "The class of information covered by this rule. The type can be a FHIR resource type, a profile on a type, or a CDA document, or some other type that indicates what sort of information the consent relates to.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* e.g. Resource Type, Profile, CDA, etc.
    fhir:Consent.provision.code[](consent-definitions.html#Consent.provision.code "If this code is found in an instance, then the rule applies.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* e.g. LOINC or SNOMED CT code, etc. in the content
    fhir:Consent.provision.dataPeriod[](consent-definitions.html#Consent.provision.dataPeriod "Clinical or Operational Relevant period of time that bounds the data controlled by this rule.") [ Period[](datatypes.html#Period) ]; # 0..1 Timeframe for data controlled by this rule
    fhir:Consent.provision.data[](consent-definitions.html#Consent.provision.data "The resources controlled by this rule if specific resources are referenced.") [ # 0..* Data controlled by this rule
      fhir:Consent.provision.data.meaning[](consent-definitions.html#Consent.provision.data.meaning "How the resource reference is interpreted when testing consent restrictions.") [ code[](datatypes.html#code) ]; # 1..1 instance | related | dependents | authoredby
      fhir:Consent.provision.data.reference[](consent-definitions.html#Consent.provision.data.reference "A reference to a specific resource that defines which resources are covered by this consent.") [ Reference[](references.html#Reference)(Any[](resourcelist.html)) ]; # 1..1 The actual data reference
    ], ...;
    fhir:Consent.provision.provision[](consent-definitions.html#Consent.provision.provision "Rules which provide exceptions to the base rule or subrules.") [ [See Consent.provision](#ttl-Consent.provision) ], ... ; # 0..* Nested Exception Rules
  ];
]

```

**Changes since R3**
[Consent](consent.html#Consent) |   
---|---  
Consent.identifier | 
  * Max Cardinality changed from 1 to *

  
Consent.status | 
  * Change value set from http://hl7.org/fhir/ValueSet/consent-state-codes to http://hl7.org/fhir/ValueSet/consent-state-codes|4.0.1

  
Consent.scope | 
  * **Added Mandatory Element**

  
Consent.category | 
  * Min Cardinality changed from 0 to 1
  * Add Binding `http://hl7.org/fhir/ValueSet/consent-category` (extensible) 

  
Consent.patient | 
  * Min Cardinality changed from 1 to 0

  
Consent.performer | 
  * Added Element

  
Consent.source[x] | 
  * Remove Type Identifier

  
Consent.policyRule | 
  * Type changed from uri to CodeableConcept
  * Add Binding `http://hl7.org/fhir/ValueSet/consent-policy` (extensible) 

  
Consent.verification | 
  * Added Element

  
Consent.verification.verified | 
  * **Added Mandatory Element**

  
Consent.verification.verifiedWith | 
  * Added Element

  
Consent.verification.verificationDate | 
  * Added Element

  
Consent.provision | 
  * Added Element

  
Consent.provision.type | 
  * Added Element

  
Consent.provision.period | 
  * Added Element

  
Consent.provision.actor | 
  * Added Element

  
Consent.provision.actor.role | 
  * **Added Mandatory Element**

  
Consent.provision.actor.reference | 
  * **Added Mandatory Element**

  
Consent.provision.action | 
  * Added Element

  
Consent.provision.securityLabel | 
  * Added Element

  
Consent.provision.purpose | 
  * Added Element

  
Consent.provision.class | 
  * Added Element

  
Consent.provision.code | 
  * Added Element

  
Consent.provision.dataPeriod | 
  * Added Element

  
Consent.provision.data | 
  * Added Element

  
Consent.provision.data.meaning | 
  * **Added Mandatory Element**

  
Consent.provision.data.reference | 
  * **Added Mandatory Element**

  
Consent.provision.provision | 
  * Added Element

  
Consent.period | 
  * deleted

  
Consent.consentingParty | 
  * deleted

  
Consent.actor | 
  * deleted

  
Consent.action | 
  * deleted

  
Consent.securityLabel | 
  * deleted

  
Consent.purpose | 
  * deleted

  
Consent.dataPeriod | 
  * deleted

  
Consent.data | 
  * deleted

  
Consent.except | 
  * deleted

  
See the [Full Difference](diff.html) for further information
This analysis is available as [XML](consent.diff.xml) or [JSON](consent.diff.json). 
See [R3 <--> R4 Conversion Maps](consent-version-maps.html) (status = 12 tests that all execute ok. All tests pass round-trip testing and 12 r3 resources are invalid (0 errors).)
**Structure**
[Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") |  [Description & Constraints](formats.html#table "Additional information about the element")[![doco](help16.png)](formats.html#table "Legend for this format")  
---|---|---|---|---  
![.](tbl_spacer.png)![.](icon_resource.png) [Consent](consent-definitions.html#Consent "Consent : A record of a healthcare consumer’s  choices, which permits or denies identified recipient\(s\) or recipient role\(s\) to perform one or more actions within a given policy context, for specific purposes and periods of time.") |  [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A healthcare consumer's choices to permit or deny recipients or roles to perform actions for specific purposes and periods of time  
+ Rule: Either a Policy or PolicyRule  
+ Rule: IF Scope=privacy, there must be a patient  
+ Rule: IF Scope=research, there must be a patient  
+ Rule: IF Scope=adr, there must be a patient  
+ Rule: IF Scope=treatment, there must be a patient  
Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.

Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource \(including cannot change the meaning of modifierExtension itself\).")  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [identifier](consent-definitions.html#Consent.identifier "Consent.identifier : Unique identifier for this copy of the Consent Statement.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Identifier](datatypes.html#Identifier) | Identifier for this record (external references)  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [status](consent-definitions.html#Consent.status "Consent.status : Indicates the current state of this consent.") |  [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | proposed | active | rejected | inactive | entered-in-error  
[ConsentState](valueset-consent-state-codes.html "Indicates the state of the consent.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [scope](consent-definitions.html#Consent.scope "Consent.scope : A selector of the type of consent being presented: ADR, Privacy, Treatment, Research.  This list is now extensible.") |  [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Which of the four areas this resource covers (extensible)  
[Consent Scope Codes](valueset-consent-scope.html "The four anticipated uses for the Consent Resource.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [category](consent-definitions.html#Consent.category "Consent.category : A classification of the type of consents found in the statement. This element supports indexing and retrieval of consent statements.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..* | [CodeableConcept](datatypes.html#CodeableConcept) | Classification of the consent statement - for indexing/retrieval  
[Consent Category Codes](valueset-consent-category.html "A classification of the type of consents found in a consent statement.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [patient](consent-definitions.html#Consent.patient "Consent.patient : The patient/healthcare consumer to whom this consent applies.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  [Reference](references.html#Reference)([Patient](patient.html)) | Who the consent applies to  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [dateTime](consent-definitions.html#Consent.dateTime "Consent.dateTime : When this  Consent was issued / created / indexed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | When this Consent was created or indexed  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [performer](consent-definitions.html#Consent.performer "Consent.performer : Either the Grantor, which is the entity responsible for granting the rights listed in a Consent Directive or the Grantee, which is the entity responsible for complying with the Consent Directive, including any obligations or limitations on authorizations and enforcement of prohibitions.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* |  [Reference](references.html#Reference)([Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [RelatedPerson](relatedperson.html) | [PractitionerRole](practitionerrole.html)) | Who is agreeing to the policy and rules  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [organization](consent-definitions.html#Consent.organization "Consent.organization : The organization that manages the consent, and the framework within which it is executed.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* |  [Reference](references.html#Reference)([Organization](organization.html)) | Custodian of the consent  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_choice.gif) [source[x]](consent-definitions.html#Consent.source_x_ "Consent.source\[x\] : The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  | Source from which this consent is taken  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) sourceAttachment |  |  | [Attachment](datatypes.html#Attachment) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) sourceReference |  |  |  [Reference](references.html#Reference)([Consent](consent.html) | [DocumentReference](documentreference.html) | [Contract](contract.html) | [QuestionnaireResponse](questionnaireresponse.html)) |   
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [policy](consent-definitions.html#Consent.policy "Consent.policy : The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.") |  | 0..* | [BackboneElement](backboneelement.html) | Policies covered by this consent  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [authority](consent-definitions.html#Consent.policy.authority "Consent.policy.authority : Entity or Organization having regulatory jurisdiction or accountability for  enforcing policies pertaining to Consent Directives.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | Enforcement source for policy  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [uri](consent-definitions.html#Consent.policy.uri "Consent.policy.uri : The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [uri](datatypes.html#uri) | Specific policy covered by this consent  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [policyRule](consent-definitions.html#Consent.policyRule "Consent.policyRule : A reference to the specific base computable regulation or policy.") |  [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Regulation that this consents to  
[Consent PolicyRule Codes](valueset-consent-policy.html "Regulatory policy examples.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [verification](consent-definitions.html#Consent.verification "Consent.verification : Whether a treatment instruction \(e.g. artificial respiration yes or no\) was verified with the patient, his/her family or another authorized person.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [BackboneElement](backboneelement.html) | Consent Verified by patient or family  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [verified](consent-definitions.html#Consent.verification.verified "Consent.verification.verified : Has the instruction been verified.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [boolean](datatypes.html#boolean) | Has been verified  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [verifiedWith](consent-definitions.html#Consent.verification.verifiedWith "Consent.verification.verifiedWith : Who verified the instruction \(Patient, Relative or other Authorized Person\).") |  | 0..1 |  [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Person who verified  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [verificationDate](consent-definitions.html#Consent.verification.verificationDate "Consent.verification.verificationDate : Date verification was collected.") |  | 0..1 | [dateTime](datatypes.html#dateTime) | When consent verified  
![.](tbl_spacer.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [provision](consent-definitions.html#Consent.provision "Consent.provision : An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [BackboneElement](backboneelement.html) | Constraints to the base Consent.policyRule  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [type](consent-definitions.html#Consent.provision.type "Consent.provision.type : Action  to take - permit or deny - when the rule conditions are met.  Not permitted in root rule, required in all nested rules.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | deny | permit  
[ConsentProvisionType](valueset-consent-provision-type.html "How a rule statement is applied, such as adding additional consent or removing consent.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [period](consent-definitions.html#Consent.provision.period "Consent.provision.period : The timeframe in this rule is valid.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Timeframe for this rule  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_element.gif) [actor](consent-definitions.html#Consent.provision.actor "Consent.provision.actor : Who or what is controlled by this rule. Use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).") |  | 0..* | [BackboneElement](backboneelement.html) | Who|what controlled by this rule (or group, by role)  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [role](consent-definitions.html#Consent.provision.actor.role "Consent.provision.actor.role : How the individual is involved in the resources content that is described in the exception.") |  | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | How the actor is involved  
[SecurityRoleType](valueset-security-role-type.html "How an actor is involved in the consent considerations.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) [reference](consent-definitions.html#Consent.provision.actor.reference "Consent.provision.actor.reference : The resource that identifies the actor. To identify actors by type, use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).") |  | 1..1 |  [Reference](references.html#Reference)([Device](device.html) | [Group](group.html) | [CareTeam](careteam.html) | [Organization](organization.html) | [Patient](patient.html) | [Practitioner](practitioner.html) | [RelatedPerson](relatedperson.html) | [PractitionerRole](practitionerrole.html)) | Resource for the actor (or group, by role)  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [action](consent-definitions.html#Consent.provision.action "Consent.provision.action : Actions controlled by this Rule.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Actions controlled by this rule  
[Consent Action Codes](valueset-consent-action.html "Detailed codes for the consent action.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [securityLabel](consent-definitions.html#Consent.provision.securityLabel "Consent.provision.securityLabel : A security label, comprised of 0..* security label fields \(Privacy tags\), which define which resources are controlled by this exception.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Coding](datatypes.html#Coding) | Security Labels that define affected resources  
[SecurityLabels](valueset-security-labels.html "Security Labels from the Healthcare Privacy and Security Classification System.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [purpose](consent-definitions.html#Consent.provision.purpose "Consent.provision.purpose : The context of the activities a user is taking - why the user is accessing the data - that are controlled by this rule.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Coding](datatypes.html#Coding) | Context of activities covered by this rule  
[V3 Value SetPurposeOfUse](v3/PurposeOfUse/vs.html "What purposes of use are controlled by this exception. If more than one label is specified, operations must have all the specified labels.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [class](consent-definitions.html#Consent.provision.class "Consent.provision.class : The class of information covered by this rule. The type can be a FHIR resource type, a profile on a type, or a CDA document, or some other type that indicates what sort of information the consent relates to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Coding](datatypes.html#Coding) | e.g. Resource Type, Profile, CDA, etc.  
[Consent Content Class](valueset-consent-content-class.html "The class \(type\) of information a consent rule covers.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [code](consent-definitions.html#Consent.provision.code "Consent.provision.code : If this code is found in an instance, then the rule applies.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | e.g. LOINC or SNOMED CT code, etc. in the content  
[Consent Content Codes](valueset-consent-content-code.html "If this code is found in an instance, then the exception applies.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included."))  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [dataPeriod](consent-definitions.html#Consent.provision.dataPeriod "Consent.provision.dataPeriod : Clinical or Operational Relevant period of time that bounds the data controlled by this rule.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Timeframe for data controlled by this rule  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_element.gif) [data](consent-definitions.html#Consent.provision.data "Consent.provision.data : The resources controlled by this rule if specific resources are referenced.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [BackboneElement](backboneelement.html) | Data controlled by this rule  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [meaning](consent-definitions.html#Consent.provision.data.meaning "Consent.provision.data.meaning : How the resource reference is interpreted when testing consent restrictions.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | instance | related | dependents | authoredby  
[ConsentDataMeaning](valueset-consent-data-meaning.html "How a resource reference is interpreted when testing consent restrictions.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) [reference](consent-definitions.html#Consent.provision.data.reference "Consent.provision.data.reference : A reference to a specific resource that defines which resources are covered by this consent.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [Reference](references.html#Reference)([Any](resourcelist.html)) | The actual data reference  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_reuse.png) [provision](consent-definitions.html#Consent.provision.provision "Consent.provision.provision : Rules which provide exceptions to the base rule or subrules.") |  | 0..* | see [provision](#Consent.provision "Consent.provision") | Nested Exception Rules  
  
  
[![doco](help16.png) Documentation for this format](formats.html#table "Legend for this format")  
**UML Diagram** ([Legend](formats.html#uml))
Consent (DomainResource)Unique identifier for this copy of the Consent Statementidentifier : Identifier [0..*]Indicates the current state of this consent (this element modifies the meaning of other elements)status : code [1..1] « Indicates the state of the consent. (Strength=Required)ConsentState! »A selector of the type of consent being presented: ADR, Privacy, Treatment, Research. This list is now extensible (this element modifies the meaning of other elements)scope : CodeableConcept [1..1] « The four anticipated uses for the Consent Resource. (Strength=Extensible)ConsentScopeCodes+ »A classification of the type of consents found in the statement. This element supports indexing and retrieval of consent statementscategory : CodeableConcept [1..*] « A classification of the type of consents found in a consent statement. (Strength=Extensible)ConsentCategoryCodes+ »The patient/healthcare consumer to whom this consent appliespatient : Reference [0..1] « Patient »When this Consent was issued / created / indexeddateTime : dateTime [0..1]Either the Grantor, which is the entity responsible for granting the rights listed in a Consent Directive or the Grantee, which is the entity responsible for complying with the Consent Directive, including any obligations or limitations on authorizations and enforcement of prohibitionsperformer : Reference [0..*] « Organization|Patient|Practitioner| RelatedPerson|PractitionerRole »The organization that manages the consent, and the framework within which it is executedorganization : Reference [0..*] « Organization »The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository (e.g. XDS) that stores the original consent documentsource[x] : Type [0..1] « Attachment|Reference(Consent| DocumentReference|Contract|QuestionnaireResponse) »A reference to the specific base computable regulation or policypolicyRule : CodeableConcept [0..1] « Regulatory policy examples. (Strength=Extensible)ConsentPolicyRuleCodes+ »PolicyEntity or Organization having regulatory jurisdiction or accountability for enforcing policies pertaining to Consent Directivesauthority : uri [0..1]The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in lawuri : uri [0..1]VerificationHas the instruction been verifiedverified : boolean [1..1]Who verified the instruction (Patient, Relative or other Authorized Person)verifiedWith : Reference [0..1] « Patient|RelatedPerson »Date verification was collectedverificationDate : dateTime [0..1]provisionAction to take - permit or deny - when the rule conditions are met. Not permitted in root rule, required in all nested rulestype : code [0..1] « How a rule statement is applied, such as adding additional consent or removing consent. (Strength=Required)ConsentProvisionType! »The timeframe in this rule is validperiod : Period [0..1]Actions controlled by this Ruleaction : CodeableConcept [0..*] « Detailed codes for the consent action. (Strength=Example)ConsentActionCodes?? »A security label, comprised of 0..* security label fields (Privacy tags), which define which resources are controlled by this exceptionsecurityLabel : Coding [0..*] « Security Labels from the Healthcare Privacy and Security Classification System. (Strength=Extensible)All Security Labels+ »The context of the activities a user is taking - why the user is accessing the data - that are controlled by this rulepurpose : Coding [0..*] « What purposes of use are controlled by this exception. If more than one label is specified, operations must have all the specified labels. (Strength=Extensible)v3.PurposeOfUse+ »The class of information covered by this rule. The type can be a FHIR resource type, a profile on a type, or a CDA document, or some other type that indicates what sort of information the consent relates toclass : Coding [0..*] « The class (type) of information a consent rule covers. (Strength=Extensible)ConsentContentClass+ »If this code is found in an instance, then the rule appliescode : CodeableConcept [0..*] « If this code is found in an instance, then the exception applies. (Strength=Example)ConsentContentCodes?? »Clinical or Operational Relevant period of time that bounds the data controlled by this ruledataPeriod : Period [0..1]provisionActorHow the individual is involved in the resources content that is described in the exceptionrole : CodeableConcept [1..1] « How an actor is involved in the consent considerations. (Strength=Extensible)SecurityRoleType+ »The resource that identifies the actor. To identify actors by type, use group to identify a set of actors by some property they share (e.g. 'admitting officers')reference : Reference [1..1] « Device|Group|CareTeam|Organization| Patient|Practitioner|RelatedPerson|PractitionerRole »provisionDataHow the resource reference is interpreted when testing consent restrictionsmeaning : code [1..1] « How a resource reference is interpreted when testing consent restrictions. (Strength=Required)ConsentDataMeaning! »A reference to a specific resource that defines which resources are covered by this consentreference : Reference [1..1] « Any »The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in lawpolicy[0..*]Whether a treatment instruction (e.g. artificial respiration yes or no) was verified with the patient, his/her family or another authorized personverification[0..*]Who or what is controlled by this rule. Use group to identify a set of actors by some property they share (e.g. 'admitting officers')actor[0..*]The resources controlled by this rule if specific resources are referenceddata[0..*]Rules which provide exceptions to the base rule or subrulesprovision[0..*]An exception to the base policy of this consent. An exception can be an addition or removal of access permissionsprovision[0..1]
**XML Template**
```

<[**Consent**](consent-definitions.html#Consent "A record of a healthcare consumerâ€™s  choices, which permits or denies identified recipient\(s\) or recipient role\(s\) to perform one or more actions within a given policy context, for specific purposes and periods of time.") xmlns="http://hl7.org/fhir"> [![doco](help.png)](xml.html "Documentation for this format")
 <!-- from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language) -->
 <!-- from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension) -->
 <[**identifier**](consent-definitions.html#Consent.identifier "Unique identifier for this copy of the Consent Statement.")><!-- **0..*** Identifier[](datatypes.html#Identifier) Identifier for this record (external references)[](terminologies.html#unbound) --></identifier>
 <[**status**](consent-definitions.html#Consent.status "Indicates the current state of this consent \(this element modifies the meaning of other elements\)") value="[code[](datatypes.html#code)]"/><!-- **1..1** draft | proposed | active | rejected | inactive | entered-in-error[](valueset-consent-state-codes.html) -->
 <[**scope**](consent-definitions.html#Consent.scope "A selector of the type of consent being presented: ADR, Privacy, Treatment, Research.  This list is now extensible \(this element modifies the meaning of other elements\)")><!-- **1..1** CodeableConcept[](datatypes.html#CodeableConcept) Which of the four areas this resource covers (extensible)[](valueset-consent-scope.html) --></scope>
 <[**category**](consent-definitions.html#Consent.category "A classification of the type of consents found in the statement. This element supports indexing and retrieval of consent statements.")><!-- **1..*** CodeableConcept[](datatypes.html#CodeableConcept) Classification of the consent statement - for indexing/retrieval[](valueset-consent-category.html) --></category>
 <[**patient**](consent-definitions.html#Consent.patient "The patient/healthcare consumer to whom this consent applies.")><!-- **0..1** Reference[](references.html#Reference)(Patient[](patient.html#Patient)) Who the consent applies to[](terminologies.html#unbound) --></patient>
 <[**dateTime**](consent-definitions.html#Consent.dateTime "When this  Consent was issued / created / indexed.") value="[dateTime[](datatypes.html#dateTime)]"/><!-- **0..1** When this Consent was created or indexed[](terminologies.html#unbound) -->
 <[**performer**](consent-definitions.html#Consent.performer "Either the Grantor, which is the entity responsible for granting the rights listed in a Consent Directive or the Grantee, which is the entity responsible for complying with the Consent Directive, including any obligations or limitations on authorizations and enforcement of prohibitions.")><!-- **0..*** Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|
   PractitionerRole[](practitionerrole.html#PractitionerRole)) Who is agreeing to the policy and rules[](terminologies.html#unbound) --></performer>
 <[**organization**](consent-definitions.html#Consent.organization "The organization that manages the consent, and the framework within which it is executed.")><!-- **0..*** Reference[](references.html#Reference)(Organization[](organization.html#Organization)) Custodian of the consent[](terminologies.html#unbound) --></organization>
 <[**source[x]**](consent-definitions.html#Consent.source\[x\] "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.")><!-- **0..1** Attachment[](datatypes.html#Attachment)|Reference[](references.html#Reference)(Consent[](consent.html#Consent)|DocumentReference[](documentreference.html#DocumentReference)|Contract[](contract.html#Contract)|
   QuestionnaireResponse[](questionnaireresponse.html#QuestionnaireResponse)) Source from which this consent is taken[](terminologies.html#unbound) --></source[x]>
 <[**policy**](consent-definitions.html#Consent.policy "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.")>  <!-- **0..*** Policies covered by this consent -->
  <[**authority**](consent-definitions.html#Consent.policy.authority "Entity or Organization having regulatory jurisdiction or accountability for  enforcing policies pertaining to Consent Directives.") value="[uri[](datatypes.html#uri)]"/><!-- **![??](lock.png) 0..1** Enforcement source for policy[](terminologies.html#unbound) -->
  <[**uri**](consent-definitions.html#Consent.policy.uri "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.") value="[uri[](datatypes.html#uri)]"/><!-- **![??](lock.png) 0..1** Specific policy covered by this consent[](terminologies.html#unbound) -->
 </policy>
 <[**policyRule**](consent-definitions.html#Consent.policyRule "A reference to the specific base computable regulation or policy.")><!-- **![??](lock.png) 0..1** CodeableConcept[](datatypes.html#CodeableConcept) Regulation that this consents to[](valueset-consent-policy.html) --></policyRule>
 <[**verification**](consent-definitions.html#Consent.verification "Whether a treatment instruction \(e.g. artificial respiration yes or no\) was verified with the patient, his/her family or another authorized person.")>  <!-- **0..*** Consent Verified by patient or family -->
  <[**verified**](consent-definitions.html#Consent.verification.verified "Has the instruction been verified.") value="[boolean[](datatypes.html#boolean)]"/><!-- **1..1** Has been verified[](terminologies.html#unbound) -->
  <[**verifiedWith**](consent-definitions.html#Consent.verification.verifiedWith "Who verified the instruction \(Patient, Relative or other Authorized Person\).")><!-- **0..1** Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) Person who verified[](terminologies.html#unbound) --></verifiedWith>
  <[**verificationDate**](consent-definitions.html#Consent.verification.verificationDate "Date verification was collected.") value="[dateTime[](datatypes.html#dateTime)]"/><!-- **0..1** When consent verified[](terminologies.html#unbound) -->
 </verification>
 <[**provision**](consent-definitions.html#Consent.provision "An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.")>  <!-- **0..1** Constraints to the base Consent.policyRule -->
  <[**type**](consent-definitions.html#Consent.provision.type "Action  to take - permit or deny - when the rule conditions are met.  Not permitted in root rule, required in all nested rules.") value="[code[](datatypes.html#code)]"/><!-- **0..1** deny | permit[](valueset-consent-provision-type.html) -->
  <[**period**](consent-definitions.html#Consent.provision.period "The timeframe in this rule is valid.")><!-- **0..1** Period[](datatypes.html#Period) Timeframe for this rule[](terminologies.html#unbound) --></period>
  <[**actor**](consent-definitions.html#Consent.provision.actor "Who or what is controlled by this rule. Use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).")>  <!-- **0..*** Who|what controlled by this rule (or group, by role) -->
   <[**role**](consent-definitions.html#Consent.provision.actor.role "How the individual is involved in the resources content that is described in the exception.")><!-- **1..1** CodeableConcept[](datatypes.html#CodeableConcept) How the actor is involved[](valueset-security-role-type.html) --></role>
   <[**reference**](consent-definitions.html#Consent.provision.actor.reference "The resource that identifies the actor. To identify actors by type, use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).")><!-- **1..1** Reference[](references.html#Reference)(Device[](device.html#Device)|Group[](group.html#Group)|CareTeam[](careteam.html#CareTeam)|Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|
     Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|PractitionerRole[](practitionerrole.html#PractitionerRole)) Resource for the actor (or group, by role)[](terminologies.html#unbound) --></reference>
  </actor>
  <[**action**](consent-definitions.html#Consent.provision.action "Actions controlled by this Rule.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) Actions controlled by this rule[](valueset-consent-action.html) --></action>
  <[**securityLabel**](consent-definitions.html#Consent.provision.securityLabel "A security label, comprised of 0..* security label fields \(Privacy tags\), which define which resources are controlled by this exception.")><!-- **0..*** Coding[](datatypes.html#Coding) Security Labels that define affected resources[](valueset-security-labels.html) --></securityLabel>
  <[**purpose**](consent-definitions.html#Consent.provision.purpose "The context of the activities a user is taking - why the user is accessing the data - that are controlled by this rule.")><!-- **0..*** Coding[](datatypes.html#Coding) Context of activities covered by this rule[](v3/PurposeOfUse/vs.html) --></purpose>
  <[**class**](consent-definitions.html#Consent.provision.class "The class of information covered by this rule. The type can be a FHIR resource type, a profile on a type, or a CDA document, or some other type that indicates what sort of information the consent relates to.")><!-- **0..*** Coding[](datatypes.html#Coding) e.g. Resource Type, Profile, CDA, etc.[](valueset-consent-content-class.html) --></class>
  <[**code**](consent-definitions.html#Consent.provision.code "If this code is found in an instance, then the rule applies.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) e.g. LOINC or SNOMED CT code, etc. in the content[](valueset-consent-content-code.html) --></code>
  <[**dataPeriod**](consent-definitions.html#Consent.provision.dataPeriod "Clinical or Operational Relevant period of time that bounds the data controlled by this rule.")><!-- **0..1** Period[](datatypes.html#Period) Timeframe for data controlled by this rule[](terminologies.html#unbound) --></dataPeriod>
  <[**data**](consent-definitions.html#Consent.provision.data "The resources controlled by this rule if specific resources are referenced.")>  <!-- **0..*** Data controlled by this rule -->
   <[**meaning**](consent-definitions.html#Consent.provision.data.meaning "How the resource reference is interpreted when testing consent restrictions.") value="[code[](datatypes.html#code)]"/><!-- **1..1** instance | related | dependents | authoredby[](valueset-consent-data-meaning.html) -->
   <[**reference**](consent-definitions.html#Consent.provision.data.reference "A reference to a specific resource that defines which resources are covered by this consent.")><!-- **1..1** Reference[](references.html#Reference)(Any[](resourcelist.html)) The actual data reference[](terminologies.html#unbound) --></reference>
  </data>
  <[**provision**](consent-definitions.html#Consent.provision.provision "Rules which provide exceptions to the base rule or subrules.")><!-- **0..*** Content as for Consent.provision Nested Exception Rules[](terminologies.html#unbound) --></provision>
 </provision>
</Consent>

```

**JSON Template**
```

{[![doco](help.png)](json.html "Documentation for this format")
  "resourceType" : "[**Consent**](consent-definitions.html#Consent "A record of a healthcare consumerâ€™s  choices, which permits or denies identified recipient\(s\) or recipient role\(s\) to perform one or more actions within a given policy context, for specific purposes and periods of time.")",
  // from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language)
  // from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension)
  "identifier[](consent-definitions.html#Consent.identifier "Unique identifier for this copy of the Consent Statement.")" : [{ Identifier[](datatypes.html#Identifier) }], // Identifier for this record (external references)[](terminologies.html#unbound)
  "[status](consent-definitions.html#Consent.status "Indicates the current state of this consent \(this element modifies the meaning of other elements\)")" : "<code[](datatypes.html#code)>", // **R!**  draft | proposed | active | rejected | inactive | entered-in-error[](valueset-consent-state-codes.html)
  "[scope](consent-definitions.html#Consent.scope "A selector of the type of consent being presented: ADR, Privacy, Treatment, Research.  This list is now extensible \(this element modifies the meaning of other elements\)")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // **R!**  Which of the four areas this resource covers (extensible)[](valueset-consent-scope.html)
  "category[](consent-definitions.html#Consent.category "A classification of the type of consents found in the statement. This element supports indexing and retrieval of consent statements.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // **R!**  Classification of the consent statement - for indexing/retrieval[](valueset-consent-category.html)
  "patient[](consent-definitions.html#Consent.patient "The patient/healthcare consumer to whom this consent applies.")" : { Reference[](references.html#Reference)(Patient[](patient.html#Patient)) }, // Who the consent applies to[](terminologies.html#unbound)
  "dateTime[](consent-definitions.html#Consent.dateTime "When this  Consent was issued / created / indexed.")" : "<dateTime[](datatypes.html#dateTime)>", // When this Consent was created or indexed[](terminologies.html#unbound)
  "performer[](consent-definitions.html#Consent.performer "Either the Grantor, which is the entity responsible for granting the rights listed in a Consent Directive or the Grantee, which is the entity responsible for complying with the Consent Directive, including any obligations or limitations on authorizations and enforcement of prohibitions.")" : [{ Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|
   PractitionerRole[](practitionerrole.html#PractitionerRole)) }], // Who is agreeing to the policy and rules[](terminologies.html#unbound)
  "organization[](consent-definitions.html#Consent.organization "The organization that manages the consent, and the framework within which it is executed.")" : [{ Reference[](references.html#Reference)(Organization[](organization.html#Organization)) }], // Custodian of the consent[](terminologies.html#unbound)
  // source[x]: Source from which this consent is taken. One of these 2:
  "sourceAttachment[](consent-definitions.html#Consent.sourceAttachment "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.")" : { Attachment[](datatypes.html#Attachment) },
  "sourceReference[](consent-definitions.html#Consent.sourceReference "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.")" : { Reference[](references.html#Reference)(Consent[](consent.html#Consent)|DocumentReference[](documentreference.html#DocumentReference)|Contract[](contract.html#Contract)|
   QuestionnaireResponse[](questionnaireresponse.html#QuestionnaireResponse)) },
  "policy[](consent-definitions.html#Consent.policy "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.")" : [{ // Policies covered by this consent[](terminologies.html#unbound)
    "authority[](consent-definitions.html#Consent.policy.authority "Entity or Organization having regulatory jurisdiction or accountability for  enforcing policies pertaining to Consent Directives.")" : "<uri[](datatypes.html#uri)>", // **C?** Enforcement source for policy[](terminologies.html#unbound)
    "uri[](consent-definitions.html#Consent.policy.uri "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.")" : "<uri[](datatypes.html#uri)>" // **C?** Specific policy covered by this consent[](terminologies.html#unbound)
  }],
  "policyRule[](consent-definitions.html#Consent.policyRule "A reference to the specific base computable regulation or policy.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // **C?** Regulation that this consents to[](valueset-consent-policy.html)
  "verification[](consent-definitions.html#Consent.verification "Whether a treatment instruction \(e.g. artificial respiration yes or no\) was verified with the patient, his/her family or another authorized person.")" : [{ // Consent Verified by patient or family[](terminologies.html#unbound)
    "verified[](consent-definitions.html#Consent.verification.verified "Has the instruction been verified.")" : <boolean[](datatypes.html#boolean)>, // **R!**  Has been verified[](terminologies.html#unbound)
    "verifiedWith[](consent-definitions.html#Consent.verification.verifiedWith "Who verified the instruction \(Patient, Relative or other Authorized Person\).")" : { Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) }, // Person who verified[](terminologies.html#unbound)
    "verificationDate[](consent-definitions.html#Consent.verification.verificationDate "Date verification was collected.")" : "<dateTime[](datatypes.html#dateTime)>" // When consent verified[](terminologies.html#unbound)
  }],
  "provision[](consent-definitions.html#Consent.provision "An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.")" : { // Constraints to the base Consent.policyRule[](terminologies.html#unbound)
    "type[](consent-definitions.html#Consent.provision.type "Action  to take - permit or deny - when the rule conditions are met.  Not permitted in root rule, required in all nested rules.")" : "<code[](datatypes.html#code)>", // deny | permit[](valueset-consent-provision-type.html)
    "period[](consent-definitions.html#Consent.provision.period "The timeframe in this rule is valid.")" : { Period[](datatypes.html#Period) }, // Timeframe for this rule[](terminologies.html#unbound)
    "actor[](consent-definitions.html#Consent.provision.actor "Who or what is controlled by this rule. Use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).")" : [{ // Who|what controlled by this rule (or group, by role)[](terminologies.html#unbound)
      "role[](consent-definitions.html#Consent.provision.actor.role "How the individual is involved in the resources content that is described in the exception.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // **R!**  How the actor is involved[](valueset-security-role-type.html)
      "reference[](consent-definitions.html#Consent.provision.actor.reference "The resource that identifies the actor. To identify actors by type, use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).")" : { Reference[](references.html#Reference)(Device[](device.html#Device)|Group[](group.html#Group)|CareTeam[](careteam.html#CareTeam)|Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|
     Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|PractitionerRole[](practitionerrole.html#PractitionerRole)) } // **R!**  Resource for the actor (or group, by role)[](terminologies.html#unbound)
    }],
    "action[](consent-definitions.html#Consent.provision.action "Actions controlled by this Rule.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // Actions controlled by this rule[](valueset-consent-action.html)
    "securityLabel[](consent-definitions.html#Consent.provision.securityLabel "A security label, comprised of 0..* security label fields \(Privacy tags\), which define which resources are controlled by this exception.")" : [{ Coding[](datatypes.html#Coding) }], // Security Labels that define affected resources[](valueset-security-labels.html)
    "purpose[](consent-definitions.html#Consent.provision.purpose "The context of the activities a user is taking - why the user is accessing the data - that are controlled by this rule.")" : [{ Coding[](datatypes.html#Coding) }], // Context of activities covered by this rule[](v3/PurposeOfUse/vs.html)
    "class[](consent-definitions.html#Consent.provision.class "The class of information covered by this rule. The type can be a FHIR resource type, a profile on a type, or a CDA document, or some other type that indicates what sort of information the consent relates to.")" : [{ Coding[](datatypes.html#Coding) }], // e.g. Resource Type, Profile, CDA, etc.[](valueset-consent-content-class.html)
    "code[](consent-definitions.html#Consent.provision.code "If this code is found in an instance, then the rule applies.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // e.g. LOINC or SNOMED CT code, etc. in the content[](valueset-consent-content-code.html)
    "dataPeriod[](consent-definitions.html#Consent.provision.dataPeriod "Clinical or Operational Relevant period of time that bounds the data controlled by this rule.")" : { Period[](datatypes.html#Period) }, // Timeframe for data controlled by this rule[](terminologies.html#unbound)
    "data[](consent-definitions.html#Consent.provision.data "The resources controlled by this rule if specific resources are referenced.")" : [{ // Data controlled by this rule[](terminologies.html#unbound)
      "meaning[](consent-definitions.html#Consent.provision.data.meaning "How the resource reference is interpreted when testing consent restrictions.")" : "<code[](datatypes.html#code)>", // **R!**  instance | related | dependents | authoredby[](valueset-consent-data-meaning.html)
      "reference[](consent-definitions.html#Consent.provision.data.reference "A reference to a specific resource that defines which resources are covered by this consent.")" : { Reference[](references.html#Reference)(Any[](resourcelist.html)) } // **R!**  The actual data reference[](terminologies.html#unbound)
    }],
    "provision[](consent-definitions.html#Consent.provision.provision "Rules which provide exceptions to the base rule or subrules.")" : [{ Content as for Consent.provision }] // Nested Exception Rules[](terminologies.html#unbound)
  }
}

```

**Turtle Template**
```

@prefix fhir: <http://hl7.org/fhir/> .[![doco](help.png)](rdf.html "Documentation for this format")


[ a fhir:[**Consent**](consent-definitions.html#Consent "A record of a healthcare consumerâ€™s  choices, which permits or denies identified recipient\(s\) or recipient role\(s\) to perform one or more actions within a given policy context, for specific purposes and periods of time.");
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource[](resource.html): .id[](resource.html#id), .meta[](resource.html#meta), .implicitRules[](resource.html#implicitRules), and .language[](resource.html#language)
  # from DomainResource[](domainresource.html): .text[](narrative.html#Narrative), .contained[](references.html#contained), .extension[](extensibility.html), and .modifierExtension[](extensibility.html#modifierExtension)
  fhir:Consent.identifier[](consent-definitions.html#Consent.identifier "Unique identifier for this copy of the Consent Statement.") [ Identifier[](datatypes.html#Identifier) ], ... ; # 0..* Identifier for this record (external references)
  fhir:[Consent.status](consent-definitions.html#Consent.status "Indicates the current state of this consent \(this element modifies the meaning of other elements\)") [ code[](datatypes.html#code) ]; # 1..1 draft | proposed | active | rejected | inactive | entered-in-error
  fhir:[Consent.scope](consent-definitions.html#Consent.scope "A selector of the type of consent being presented: ADR, Privacy, Treatment, Research.  This list is now extensible \(this element modifies the meaning of other elements\)") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 1..1 Which of the four areas this resource covers (extensible)
  fhir:Consent.category[](consent-definitions.html#Consent.category "A classification of the type of consents found in the statement. This element supports indexing and retrieval of consent statements.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 1..* Classification of the consent statement - for indexing/retrieval
  fhir:Consent.patient[](consent-definitions.html#Consent.patient "The patient/healthcare consumer to whom this consent applies.") [ Reference[](references.html#Reference)(Patient[](patient.html#Patient)) ]; # 0..1 Who the consent applies to
  fhir:Consent.dateTime[](consent-definitions.html#Consent.dateTime "When this  Consent was issued / created / indexed.") [ dateTime[](datatypes.html#dateTime) ]; # 0..1 When this Consent was created or indexed
  fhir:Consent.performer[](consent-definitions.html#Consent.performer "Either the Grantor, which is the entity responsible for granting the rights listed in a Consent Directive or the Grantee, which is the entity responsible for complying with the Consent Directive, including any obligations or limitations on authorizations and enforcement of prohibitions.") [ Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|PractitionerRole[](practitionerrole.html#PractitionerRole)) ], ... ; # 0..* Who is agreeing to the policy and rules
  fhir:Consent.organization[](consent-definitions.html#Consent.organization "The organization that manages the consent, and the framework within which it is executed.") [ Reference[](references.html#Reference)(Organization[](organization.html#Organization)) ], ... ; # 0..* Custodian of the consent
  # Consent.source[x][](consent-definitions.html#Consent.source\[x\] "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.") : 0..1 Source from which this consent is taken. One of these 2
    fhir:Consent.sourceAttachment[](consent-definitions.html#Consent.sourceAttachment "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.") [ Attachment[](datatypes.html#Attachment) ]
    fhir:Consent.sourceReference[](consent-definitions.html#Consent.sourceReference "The source on which this consent statement is based. The source might be a scanned original paper form, or a reference to a consent that links back to such a source, a reference to a document repository \(e.g. XDS\) that stores the original consent document.") [ Reference[](references.html#Reference)(Consent[](consent.html#Consent)|DocumentReference[](documentreference.html#DocumentReference)|Contract[](contract.html#Contract)|QuestionnaireResponse[](questionnaireresponse.html#QuestionnaireResponse)) ]
  fhir:Consent.policy[](consent-definitions.html#Consent.policy "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.") [ # 0..* Policies covered by this consent
    fhir:Consent.policy.authority[](consent-definitions.html#Consent.policy.authority "Entity or Organization having regulatory jurisdiction or accountability for  enforcing policies pertaining to Consent Directives.") [ uri[](datatypes.html#uri) ]; # 0..1 Enforcement source for policy
    fhir:Consent.policy.uri[](consent-definitions.html#Consent.policy.uri "The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.") [ uri[](datatypes.html#uri) ]; # 0..1 Specific policy covered by this consent
  ], ...;
  fhir:Consent.policyRule[](consent-definitions.html#Consent.policyRule "A reference to the specific base computable regulation or policy.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 0..1 Regulation that this consents to
  fhir:Consent.verification[](consent-definitions.html#Consent.verification "Whether a treatment instruction \(e.g. artificial respiration yes or no\) was verified with the patient, his/her family or another authorized person.") [ # 0..* Consent Verified by patient or family
    fhir:Consent.verification.verified[](consent-definitions.html#Consent.verification.verified "Has the instruction been verified.") [ boolean[](datatypes.html#boolean) ]; # 1..1 Has been verified
    fhir:Consent.verification.verifiedWith[](consent-definitions.html#Consent.verification.verifiedWith "Who verified the instruction \(Patient, Relative or other Authorized Person\).") [ Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) ]; # 0..1 Person who verified
    fhir:Consent.verification.verificationDate[](consent-definitions.html#Consent.verification.verificationDate "Date verification was collected.") [ dateTime[](datatypes.html#dateTime) ]; # 0..1 When consent verified
  ], ...;
  fhir:Consent.provision[](consent-definitions.html#Consent.provision "An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.") [ # 0..1 Constraints to the base Consent.policyRule
    fhir:Consent.provision.type[](consent-definitions.html#Consent.provision.type "Action  to take - permit or deny - when the rule conditions are met.  Not permitted in root rule, required in all nested rules.") [ code[](datatypes.html#code) ]; # 0..1 deny | permit
    fhir:Consent.provision.period[](consent-definitions.html#Consent.provision.period "The timeframe in this rule is valid.") [ Period[](datatypes.html#Period) ]; # 0..1 Timeframe for this rule
    fhir:Consent.provision.actor[](consent-definitions.html#Consent.provision.actor "Who or what is controlled by this rule. Use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).") [ # 0..* Who|what controlled by this rule (or group, by role)
      fhir:Consent.provision.actor.role[](consent-definitions.html#Consent.provision.actor.role "How the individual is involved in the resources content that is described in the exception.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 1..1 How the actor is involved
      fhir:Consent.provision.actor.reference[](consent-definitions.html#Consent.provision.actor.reference "The resource that identifies the actor. To identify actors by type, use group to identify a set of actors by some property they share \(e.g. 'admitting officers'\).") [ Reference[](references.html#Reference)(Device[](device.html#Device)|Group[](group.html#Group)|CareTeam[](careteam.html#CareTeam)|Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|Practitioner[](practitioner.html#Practitioner)|RelatedPerson[](relatedperson.html#RelatedPerson)|
  PractitionerRole[](practitionerrole.html#PractitionerRole)) ]; # 1..1 Resource for the actor (or group, by role)
    ], ...;
    fhir:Consent.provision.action[](consent-definitions.html#Consent.provision.action "Actions controlled by this Rule.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* Actions controlled by this rule
    fhir:Consent.provision.securityLabel[](consent-definitions.html#Consent.provision.securityLabel "A security label, comprised of 0..* security label fields \(Privacy tags\), which define which resources are controlled by this exception.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* Security Labels that define affected resources
    fhir:Consent.provision.purpose[](consent-definitions.html#Consent.provision.purpose "The context of the activities a user is taking - why the user is accessing the data - that are controlled by this rule.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* Context of activities covered by this rule
    fhir:Consent.provision.class[](consent-definitions.html#Consent.provision.class "The class of information covered by this rule. The type can be a FHIR resource type, a profile on a type, or a CDA document, or some other type that indicates what sort of information the consent relates to.") [ Coding[](datatypes.html#Coding) ], ... ; # 0..* e.g. Resource Type, Profile, CDA, etc.
    fhir:Consent.provision.code[](consent-definitions.html#Consent.provision.code "If this code is found in an instance, then the rule applies.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* e.g. LOINC or SNOMED CT code, etc. in the content
    fhir:Consent.provision.dataPeriod[](consent-definitions.html#Consent.provision.dataPeriod "Clinical or Operational Relevant period of time that bounds the data controlled by this rule.") [ Period[](datatypes.html#Period) ]; # 0..1 Timeframe for data controlled by this rule
    fhir:Consent.provision.data[](consent-definitions.html#Consent.provision.data "The resources controlled by this rule if specific resources are referenced.") [ # 0..* Data controlled by this rule
      fhir:Consent.provision.data.meaning[](consent-definitions.html#Consent.provision.data.meaning "How the resource reference is interpreted when testing consent restrictions.") [ code[](datatypes.html#code) ]; # 1..1 instance | related | dependents | authoredby
      fhir:Consent.provision.data.reference[](consent-definitions.html#Consent.provision.data.reference "A reference to a specific resource that defines which resources are covered by this consent.") [ Reference[](references.html#Reference)(Any[](resourcelist.html)) ]; # 1..1 The actual data reference
    ], ...;
    fhir:Consent.provision.provision[](consent-definitions.html#Consent.provision.provision "Rules which provide exceptions to the base rule or subrules.") [ [See Consent.provision](#ttl-Consent.provision) ], ... ; # 0..* Nested Exception Rules
  ];
]

```

**Changes since Release 3**
[Consent](consent.html#Consent) |   
---|---  
Consent.identifier | 
  * Max Cardinality changed from 1 to *

  
Consent.status | 
  * Change value set from http://hl7.org/fhir/ValueSet/consent-state-codes to http://hl7.org/fhir/ValueSet/consent-state-codes|4.0.1

  
Consent.scope | 
  * **Added Mandatory Element**

  
Consent.category | 
  * Min Cardinality changed from 0 to 1
  * Add Binding `http://hl7.org/fhir/ValueSet/consent-category` (extensible) 

  
Consent.patient | 
  * Min Cardinality changed from 1 to 0

  
Consent.performer | 
  * Added Element

  
Consent.source[x] | 
  * Remove Type Identifier

  
Consent.policyRule | 
  * Type changed from uri to CodeableConcept
  * Add Binding `http://hl7.org/fhir/ValueSet/consent-policy` (extensible) 

  
Consent.verification | 
  * Added Element

  
Consent.verification.verified | 
  * **Added Mandatory Element**

  
Consent.verification.verifiedWith | 
  * Added Element

  
Consent.verification.verificationDate | 
  * Added Element

  
Consent.provision | 
  * Added Element

  
Consent.provision.type | 
  * Added Element

  
Consent.provision.period | 
  * Added Element

  
Consent.provision.actor | 
  * Added Element

  
Consent.provision.actor.role | 
  * **Added Mandatory Element**

  
Consent.provision.actor.reference | 
  * **Added Mandatory Element**

  
Consent.provision.action | 
  * Added Element

  
Consent.provision.securityLabel | 
  * Added Element

  
Consent.provision.purpose | 
  * Added Element

  
Consent.provision.class | 
  * Added Element

  
Consent.provision.code | 
  * Added Element

  
Consent.provision.dataPeriod | 
  * Added Element

  
Consent.provision.data | 
  * Added Element

  
Consent.provision.data.meaning | 
  * **Added Mandatory Element**

  
Consent.provision.data.reference | 
  * **Added Mandatory Element**

  
Consent.provision.provision | 
  * Added Element

  
Consent.period | 
  * deleted

  
Consent.consentingParty | 
  * deleted

  
Consent.actor | 
  * deleted

  
Consent.action | 
  * deleted

  
Consent.securityLabel | 
  * deleted

  
Consent.purpose | 
  * deleted

  
Consent.dataPeriod | 
  * deleted

  
Consent.data | 
  * deleted

  
Consent.except | 
  * deleted

  
See the [Full Difference](diff.html) for further information
This analysis is available as [XML](consent.diff.xml) or [JSON](consent.diff.json). 
See [R3 <--> R4 Conversion Maps](consent-version-maps.html) (status = 12 tests that all execute ok. All tests pass round-trip testing and 12 r3 resources are invalid (0 errors).)
See the [Profiles & Extensions](consent-profiles.html) and the alternate definitions: Master Definition [XML](consent.profile.xml.html) + [JSON](consent.profile.json.html), [XML](xml.html) [Schema](consent.xsd)/[Schematron](consent.sch) + [JSON](json.html) [Schema](consent.schema.json.html), [ShEx](consent.shex.html) (for [Turtle](rdf.html)) + [see the extensions](consent-profiles.html) & the [dependency analysis](consent-dependencies.html)
###  6.2.4.1 Terminology Bindings [](consent.html#tx "link to here")
Path | Definition | Type | Reference  
---|---|---|---  
Consent.status  | Indicates the state of the consent. | [Required](terminologies.html#required) |  [ConsentState](valueset-consent-state-codes.html)  
Consent.scope  | The four anticipated uses for the Consent Resource. | [Extensible](terminologies.html#extensible) |  [ConsentScopeCodes](valueset-consent-scope.html)  
Consent.category  | A classification of the type of consents found in a consent statement. | [Extensible](terminologies.html#extensible) |  [ConsentCategoryCodes](valueset-consent-category.html)  
Consent.policyRule  | Regulatory policy examples. | [Extensible](terminologies.html#extensible) |  [ConsentPolicyRuleCodes](valueset-consent-policy.html)  
Consent.provision.type  | How a rule statement is applied, such as adding additional consent or removing consent. | [Required](terminologies.html#required) |  [ConsentProvisionType](valueset-consent-provision-type.html)  
Consent.provision.actor.role  | How an actor is involved in the consent considerations. | [Extensible](terminologies.html#extensible) |  [SecurityRoleType](valueset-security-role-type.html)  
Consent.provision.action  | Detailed codes for the consent action. | [Example](terminologies.html#example) |  [ConsentActionCodes](valueset-consent-action.html)  
Consent.provision.securityLabel  | Security Labels from the Healthcare Privacy and Security Classification System. | [Extensible](terminologies.html#extensible) |  [All Security Labels](valueset-security-labels.html)  
Consent.provision.purpose  | What purposes of use are controlled by this exception. If more than one label is specified, operations must have all the specified labels. | [Extensible](terminologies.html#extensible) |  [v3.PurposeOfUse](v3/PurposeOfUse/vs.html)  
Consent.provision.class  | The class (type) of information a consent rule covers. | [Extensible](terminologies.html#extensible) |  [ConsentContentClass](valueset-consent-content-class.html)  
Consent.provision.code  | If this code is found in an instance, then the exception applies. | [Example](terminologies.html#example) |  [ConsentContentCodes](valueset-consent-content-code.html)  
Consent.provision.data.meaning  | How a resource reference is interpreted when testing consent restrictions. | [Required](terminologies.html#required) |  [ConsentDataMeaning](valueset-consent-data-meaning.html)  
###  6.2.4.2 Constraints [](consent.html#invs "link to here")
**id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)**  
---|---|---|---|---  
**ppc-1** |  [Rule](conformance-rules.html#rule) | (base) | Either a Policy or PolicyRule | policy.exists() or policyRule.exists()  
**ppc-2** |  [Rule](conformance-rules.html#rule) | (base) | IF Scope=privacy, there must be a patient | patient.exists() or scope.coding.where(system='something' and code='patient-privacy').exists().not()  
**ppc-3** |  [Rule](conformance-rules.html#rule) | (base) | IF Scope=research, there must be a patient | patient.exists() or scope.coding.where(system='something' and code='research').exists().not()  
**ppc-4** |  [Rule](conformance-rules.html#rule) | (base) | IF Scope=adr, there must be a patient | patient.exists() or scope.coding.where(system='something' and code='adr').exists().not()  
**ppc-5** |  [Rule](conformance-rules.html#rule) | (base) | IF Scope=treatment, there must be a patient | patient.exists() or scope.coding.where(system='something' and code='treatment').exists().not()  
##  6.2.5 Policies [](consent.html#6.2.5 "link to here")
The Consent resource has a reference to a single `policyRule`. Many organizations will work in a context where multiple different consent regulations and policies apply. In these cases, the single policy rule reference refers to a policy document that resolves and reconciles the various policies and presents a single policy for patient consent. If it is still necessary to track which of the underlying policies an exception is make in regard to, the `policy` may be used. 
##  6.2.6 General Model [](consent.html#6.2.6 "link to here")
The following is the general model of Privacy Consent Directives. 
There are context setting parameters: 
  1. Who - The **patient**
  2. What - The **data** - specific resources are listed, empty list means all data covered by the consent.
  3. Where - The **domain** and **authority** - what is the location boundary and authority boundary of this consent
  4. When - The **issued** or captured
  5. When - The timeframe for which the Consent **applies**
  6. How - The **actions** covered. (such as purposes of use that are covered)
  7. Whom - The **recipient** are grantees by the consent. 


A Privacy Consent may transition through many states including: that no consent has been sought, consent has been proposed, consent has been rejected, and consent approved. 
There are set of patterns.
  1. No consent: All settings need a policy for when no consent has been captured. Often this allows treatment only.;
  2. Opt-out: [No sharing allowed for the specified domain, location, actions, and purposes](consent-example-Out.html);
  3. Opt-out with exceptions: No sharing allowed, with some exceptions where it is allowed. Example: [Withhold Authorization for Treatment except for Emergency Treatment](consent-example-Emergency.html);
  4. Opt-in: Sharing for some purpose of use is authorized [Sharing allowed for Treatment, Payment, and normal Operations](consent-example.html); and
  5. Opt-in with restrictions: Sharing allowed, but the patient may make exceptions (See the Canadian examples).


For each of these patterns (positive or negative pattern), there can be exceptions. These exceptions are explicitly recorded in the **except** element. 
##  6.2.7 Realm specifics [](consent.html#6.2.7 "link to here")
###  6.2.7.1 US Realm Sample Use-Cases [](consent.html#6.2.7.1 "link to here")
Five categories of Privacy Consent Directives are described in the Office of the National Coordinator for Health Information (ONC) Consent Directives Document released March 31, 2010, and include the following US-specific "Core consent options" for electronic exchange: 
  1. No consent: Health information of patients is automatically included—patients cannot opt out;
  2. Opt-out: Default is for health information of patients to be included automatically, but the patient can [opt out completely](consent-example-Out.html);
  3. Opt-out with exceptions: Default is for health information of patients to be included, but the patient can opt out completely or allow only select data to be included;
  4. Opt-in: Default is that no patient health information is included; patients must actively [express consent](consent-example.html) to be included, but if they do so then their information must be all in or all out; and
  5. Opt-in with restrictions: Default is that no patient health information is made available, but the patient may allow a subset of select data to be included.


A common exception is to explicitly exclude or explicitly include [a period of time](consent-example-notTime.html). 
###  6.2.7.2 Canada Realm Sample Use-Cases [](consent.html#6.2.7.2 "link to here")
The following scenarios are based on existing jurisdictional policy and are realized in existing systems in Canada. The default policy is one of implied consent for the provision of care, so these scenarios all deal with withdrawal or withholding consent for that purpose. In other jurisdictions, where an express consent model is used (Opt-In), these examples would contain the phrase "consent to" rather than "withhold" or "withdraw" consent for. 
  1. Withhold or withdraw consent for disclosure of records related to specific domain (e.g. DI, LAB, etc.)
  2. Withhold or withdraw [consent for disclosure of a specific record](consent-example-notThis.html) (e.g. Lab Order/Result) 
  3. Withhold or withdraw [consent for disclosure to a specific provider organization](consent-example-notOrg.html)
  4. Withhold or withdraw [consent for disclosure to a specific provider agent](consent-example-notThem.html) (an individual within an organization) 
  5. Withhold or withdraw [consent for disclosure of records that were authored by a specific organization](consent-example-notAuthor.html) (or service delivery location). 
  6. Combinations of the above 


###  6.2.7.3 Non-Treatment Use-Cases [](consent.html#6.2.7.3 "link to here")
Also shown is an example where a [Patient has authorized disclosure to a specific individual for purposes directed by the patient](consent-example-grantor.html) (possibly not a treatment case). 
##  6.2.8 Search Parameters [](consent.html#search "link to here")
Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.
**Name** | **Type** | **Description** | **Expression** | **In Common**  
---|---|---|---|---  
action | [token](search.html#token) | Actions controlled by this rule | Consent.provision.action |   
actor | [reference](search.html#reference) | Resource for the actor (or group, by role) | Consent.provision.actor.reference  
([Practitioner](practitioner.html), [Group](group.html), [Organization](organization.html), [CareTeam](careteam.html), [Device](device.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) |   
category | [token](search.html#token) | Classification of the consent statement - for indexing/retrieval | Consent.category |   
consentor | [reference](search.html#reference) | Who is agreeing to the policy and rules | Consent.performer  
([Practitioner](practitioner.html), [Organization](organization.html), [Patient](patient.html), [PractitionerRole](practitionerrole.html), [RelatedPerson](relatedperson.html)) |   
data | [reference](search.html#reference) | The actual data reference | Consent.provision.data.reference  
(Any) |   
date | [date](search.html#date) | When this Consent was created or indexed | Consent.dateTime | [17 Resources](searchparameter-registry.html#clinical-date)  
identifier | [token](search.html#token) | Identifier for this record (external references) | Consent.identifier | [30 Resources](searchparameter-registry.html#clinical-identifier)  
organization | [reference](search.html#reference) | Custodian of the consent | Consent.organization  
([Organization](organization.html)) |   
patient | [reference](search.html#reference) | Who the consent applies to | Consent.patient  
([Patient](patient.html)) | [33 Resources](searchparameter-registry.html#clinical-patient)  
period | [date](search.html#date) | Timeframe for this rule | Consent.provision.period |   
purpose | [token](search.html#token) | Context of activities covered by this rule | Consent.provision.purpose |   
scope | [token](search.html#token) | Which of the four areas this resource covers (extensible) | Consent.scope |   
security-label | [token](search.html#token) | Security Labels that define affected resources | Consent.provision.securityLabel |   
source-reference | [reference](search.html#reference) | Search by reference to a Consent, DocumentReference, Contract or QuestionnaireResponse | Consent.source  
([Consent](consent.html), [Contract](contract.html), [QuestionnaireResponse](questionnaireresponse.html), [DocumentReference](documentreference.html)) |   
status | [token](search.html#token) | draft | proposed | active | rejected | inactive | entered-in-error | Consent.status |   
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:34+1100. [QA Page](qa.html)   
Links: [Search ![](external.png)](http://hl7.org/fhir/search.cfm) | [Version History](history.html) | [Table of Contents](toc.html) | [Credits](credits.html) | [Compare to R3 ![](external.png)](http://services.w3.org/htmldiff?doc1=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fconsent.html&doc2=http%3A%2F%2Fbuild.fhir.org%2Fconsent.html) | [![CC0](cc0.png)](license.html) | [Propose a change ![](external.png)](http://hl7.org/fhir-issues)
