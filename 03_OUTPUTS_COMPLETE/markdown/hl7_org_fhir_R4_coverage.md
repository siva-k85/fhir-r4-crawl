---
url: https://hl7.org/fhir/R4/coverage.html
title: Coverage
source: official_download
extracted: local_file_conversion
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


  * [![](financial.png) Financial](financial-module.html)
  * **Coverage**


**This page is part of a downloaded copy of this specification.** This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html)
  * [Content](#)
  * [Examples](coverage-examples.html)
  * [Detailed Descriptions](coverage-definitions.html)
  * [Mappings](coverage-mappings.html)
  * [Profiles & Extensions](coverage-profiles.html)
  * [R3 Conversions](coverage-version-maps.html)


#  13.1 Resource Coverage - Content [](coverage.html#13.1 "link to here")
[Financial Management ![](external.png)](http://www.hl7.org/Special/committees/fm/index.cfm) Work Group |  [Maturity Level](versions.html#maturity): 2 |  [Trial Use](versions.html#std-process "Standard Status") |  [Security Category](security.html#SecPrivConsiderations): Patient |  [Compartments](compartmentdefinition.html): [Patient](compartmentdefinition-patient.html), [RelatedPerson](compartmentdefinition-relatedperson.html)  
---|---|---|---|---  
Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.
##  13.1.1 Scope and Usage [](coverage.html#scope "link to here")
The Coverage resource is intended to provide the high-level identifiers and descriptors of an insurance plan, typically the information which would appear on an insurance card, which may be used to pay, in part or in whole, for the provision of health care products and services. 
This resource may also be used to register 'SelfPay' where an individual or organization other than an insurer is taking responsibility for payment for a portion of the health care costs. Selfpay should not be confused with being a guarantor of the patient's account. 
The Coverage resource is a "event" resource from a FHIR workflow perspective - see [Workflow Request.](workflow.html#event)
##  13.1.2 Boundaries and Relationships [](coverage.html#bnr "link to here")
**The eClaim domain includes a number of related insurance resources**
Coverage | The Coverage resource is intended to provide the high-level identifiers and descriptors of a specific insurance plan for a specific individual - essentially the insurance card information. This may alternately provide the individual or organization, selfpay, which will pay for products and services rendered.  
---|---  
[Contract](contract.html) | A Contract resource holds the references to parties who have entered into an agreement of some type, the parties who may sign or witness such an agreement, descriptors of the type of agreement and even the actual text or executable copy of the agreement. The agreement may be of a variety of types including service contracts, insurance contracts, directives, etc. The contract may be either definitional or actual instances.   
[InsurancePlan](insuranceplan.html) | The InsurancePlan resource holds the definition of an insurance plan which an insurer may offer to potential clients through insurance brokers or an online insurance marketplace. This is only the plan definition and does not contain or reference a list of individuals who have purchased the plan.   
This resource is referenced by [Account](account.html#Account), [Claim](claim.html#Claim), [ClaimResponse](claimresponse.html#ClaimResponse), [CoverageEligibilityRequest](coverageeligibilityrequest.html#CoverageEligibilityRequest), [CoverageEligibilityResponse](coverageeligibilityresponse.html#CoverageEligibilityResponse), [DeviceRequest](devicerequest.html#DeviceRequest), [EnrollmentRequest](enrollmentrequest.html#EnrollmentRequest), [ExplanationOfBenefit](explanationofbenefit.html#ExplanationOfBenefit), [MedicationRequest](medicationrequest.html#MedicationRequest), [ServiceRequest](servicerequest.html#ServiceRequest) and [Task](task.html#Task)
##  13.1.3 Resource Content [](coverage.html#resource "link to here")
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
![.](tbl_spacer.png)![.](icon_resource.png) [Coverage](coverage-definitions.html#Coverage "Coverage : Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Insurance or medical plan or a payment agreement  
Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.

Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource \(including cannot change the meaning of modifierExtension itself\).")  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [identifier](coverage-definitions.html#Coverage.identifier "Coverage.identifier : A unique identifier assigned to this coverage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Identifier](datatypes.html#Identifier) | Business Identifier for the coverage  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [status](coverage-definitions.html#Coverage.status "Coverage.status : The status of the resource instance.") |  [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | active | cancelled | draft | entered-in-error  
[Financial Resource Status Codes](valueset-fm-status.html "A code specifying the state of the resource instance.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](coverage-definitions.html#Coverage.type "Coverage.type : The type of coverage: social program, medical plan, accident coverage \(workers compensation, auto\), group health or payment by an individual or organization.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Coverage category such as medical or accident  
[Coverage Type and Self-Pay Codes](valueset-coverage-type.html "The type of insurance: public health, worker compensation; private accident, auto, private health, etc.\) or a direct payment by an individual or organization.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [policyHolder](coverage-definitions.html#Coverage.policyHolder "Coverage.policyHolder : The party who 'owns' the insurance policy.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | Owner of the policy  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [subscriber](coverage-definitions.html#Coverage.subscriber "Coverage.subscriber : The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is due.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Subscriber to the policy  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [subscriberId](coverage-definitions.html#Coverage.subscriberId "Coverage.subscriberId : The insurer assigned ID for the Subscriber.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | ID assigned to the subscriber  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [beneficiary](coverage-definitions.html#Coverage.beneficiary "Coverage.beneficiary : The party who benefits from the insurance coverage; the patient when products and/or services are provided.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [Reference](references.html#Reference)([Patient](patient.html)) | Plan beneficiary  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [dependent](coverage-definitions.html#Coverage.dependent "Coverage.dependent : A unique identifier for a dependent under the coverage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Dependent number  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [relationship](coverage-definitions.html#Coverage.relationship "Coverage.relationship : The relationship of beneficiary \(patient\) to the subscriber.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Beneficiary relationship to the subscriber  
[SubscriberPolicyholder Relationship Codes](valueset-subscriber-relationship.html "The relationship between the Subscriber and the Beneficiary \(insured/covered party/patient\).") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [period](coverage-definitions.html#Coverage.period "Coverage.period : Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in force.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Coverage start and end dates  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [payor](coverage-definitions.html#Coverage.payor "Coverage.payor : The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreements.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..* |  [Reference](references.html#Reference)([Organization](organization.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Issuer of the policy  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [class](coverage-definitions.html#Coverage.class "Coverage.class : A suite of underwriter specific classifiers.") |  | 0..* | [BackboneElement](backboneelement.html) | Additional coverage classifications  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](coverage-definitions.html#Coverage.class.type "Coverage.class.type : The type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, Plan.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of class such as 'group' or 'plan'  
[Coverage Class Codes](valueset-coverage-class.html "The policy classifications, eg. Group, Plan, Class, etc.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [value](coverage-definitions.html#Coverage.class.value "Coverage.class.value : The alphanumeric string value associated with the insurer issued label.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Value associated with the type  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [name](coverage-definitions.html#Coverage.class.name "Coverage.class.name : A short description for the class.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Human readable description of the type and value  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [order](coverage-definitions.html#Coverage.order "Coverage.order : The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of care.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Relative order of the coverage  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [network](coverage-definitions.html#Coverage.network "Coverage.network : The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions apply.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Insurer network  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [costToBeneficiary](coverage-definitions.html#Coverage.costToBeneficiary "Coverage.costToBeneficiary : A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.") |  | 0..* | [BackboneElement](backboneelement.html) | Patient payments for services/products  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](coverage-definitions.html#Coverage.costToBeneficiary.type "Coverage.costToBeneficiary.type : The category of patient centric costs associated with treatment.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Cost category  
[Coverage Copay Type Codes](valueset-coverage-copay-type.html "The types of services to which patient copayments are specified.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_choice.gif) [value[x]](coverage-definitions.html#Coverage.costToBeneficiary.value_x_ "Coverage.costToBeneficiary.value\[x\] : The amount due from the patient for the cost category.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  | The amount or percentage due from the beneficiary  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) valueQuantity |  |  | [SimpleQuantity](datatypes.html#SimpleQuantity) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_datatype.gif) valueMoney |  |  | [Money](datatypes.html#Money) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [exception](coverage-definitions.html#Coverage.costToBeneficiary.exception "Coverage.costToBeneficiary.exception : A suite of codes indicating exceptions or reductions to patient costs and their effective periods.") |  | 0..* | [BackboneElement](backboneelement.html) | Exceptions for patient payments  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](coverage-definitions.html#Coverage.costToBeneficiary.exception.type "Coverage.costToBeneficiary.exception.type : The code for the specific exception.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Exception category  
[Example Coverage Financial Exception Codes](valueset-coverage-financial-exception.html "The types of exceptions from the part or full value of financial obligations such as copays.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_datatype.gif) [period](coverage-definitions.html#Coverage.costToBeneficiary.exception.period "Coverage.costToBeneficiary.exception.period : The timeframe during when the exception is in force.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | The effective period of the exception  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [subrogation](coverage-definitions.html#Coverage.subrogation "Coverage.subrogation : When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costs.") |  | 0..1 | [boolean](datatypes.html#boolean) | Reimbursement to insurer  
![.](tbl_spacer.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) [contract](coverage-definitions.html#Coverage.contract "Coverage.contract : The policy\(s\) which constitute this insurance coverage.") |  | 0..* |  [Reference](references.html#Reference)([Contract](contract.html)) | Contract details  
  
  
[![doco](help16.png) Documentation for this format](formats.html#table "Legend for this format")  
**UML Diagram** ([Legend](formats.html#uml))
Coverage (DomainResource)A unique identifier assigned to this coverageidentifier : Identifier [0..*]The status of the resource instance (this element modifies the meaning of other elements)status : code [1..1] « A code specifying the state of the resource instance. (Strength=Required)FinancialResourceStatusCodes! »The type of coverage: social program, medical plan, accident coverage (workers compensation, auto), group health or payment by an individual or organizationtype : CodeableConcept [0..1] « The type of insurance: public health, worker compensation; private accident, auto, private health, etc.) or a direct payment by an individual or organization. (Strength=Preferred)CoverageTypeAndSelf-PayCodes? »The party who 'owns' the insurance policypolicyHolder : Reference [0..1] « Patient|RelatedPerson|Organization »The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is duesubscriber : Reference [0..1] « Patient|RelatedPerson »The insurer assigned ID for the SubscribersubscriberId : string [0..1]The party who benefits from the insurance coverage; the patient when products and/or services are providedbeneficiary : Reference [1..1] « Patient »A unique identifier for a dependent under the coveragedependent : string [0..1]The relationship of beneficiary (patient) to the subscriberrelationship : CodeableConcept [0..1] « The relationship between the Subscriber and the Beneficiary (insured/covered party/patient). (Strength=Extensible)SubscriberRelationshipCodes+ »Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in forceperiod : Period [0..1]The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreementspayor : Reference [1..*] « Organization|Patient|RelatedPerson »The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of careorder : positiveInt [0..1]The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions applynetwork : string [0..1]When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costssubrogation : boolean [0..1]The policy(s) which constitute this insurance coveragecontract : Reference [0..*] « Contract »ClassThe type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, Plantype : CodeableConcept [1..1] « The policy classifications, eg. Group, Plan, Class, etc. (Strength=Extensible)CoverageClassCodes+ »The alphanumeric string value associated with the insurer issued labelvalue : string [1..1]A short description for the classname : string [0..1]CostToBeneficiaryThe category of patient centric costs associated with treatmenttype : CodeableConcept [0..1] « The types of services to which patient copayments are specified. (Strength=Extensible)CoverageCopayTypeCodes+ »The amount due from the patient for the cost categoryvalue[x] : Type [1..1] « Quantity(SimpleQuantity)|Money »ExemptionThe code for the specific exceptiontype : CodeableConcept [1..1] « The types of exceptions from the part or full value of financial obligations such as copays. (Strength=Example)ExampleCoverageFinancialExcep...?? »The timeframe during when the exception is in forceperiod : Period [0..1]A suite of underwriter specific classifiersclass[0..*]A suite of codes indicating exceptions or reductions to patient costs and their effective periodsexception[0..*]A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been included on the health cardcostToBeneficiary[0..*]
**XML Template**
```

<[**Coverage**](coverage-definitions.html#Coverage "Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.") xmlns="http://hl7.org/fhir"> [![doco](help.png)](xml.html "Documentation for this format")
 <!-- from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language) -->
 <!-- from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension) -->
 <[**identifier**](coverage-definitions.html#Coverage.identifier "A unique identifier assigned to this coverage.")><!-- **0..*** Identifier[](datatypes.html#Identifier) Business Identifier for the coverage[](terminologies.html#unbound) --></identifier>
 <[**status**](coverage-definitions.html#Coverage.status "The status of the resource instance \(this element modifies the meaning of other elements\)") value="[code[](datatypes.html#code)]"/><!-- **1..1** active | cancelled | draft | entered-in-error[](valueset-fm-status.html) -->
 <[**type**](coverage-definitions.html#Coverage.type "The type of coverage: social program, medical plan, accident coverage \(workers compensation, auto\), group health or payment by an individual or organization.")><!-- **0..1** CodeableConcept[](datatypes.html#CodeableConcept) Coverage category such as medical or accident[](valueset-coverage-type.html) --></type>
 <[**policyHolder**](coverage-definitions.html#Coverage.policyHolder "The party who 'owns' the insurance policy.")><!-- **0..1** Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)|Organization[](organization.html#Organization)) Owner of the policy[](terminologies.html#unbound) --></policyHolder>
 <[**subscriber**](coverage-definitions.html#Coverage.subscriber "The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is due.")><!-- **0..1** Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) Subscriber to the policy[](terminologies.html#unbound) --></subscriber>
 <[**subscriberId**](coverage-definitions.html#Coverage.subscriberId "The insurer assigned ID for the Subscriber.") value="[string[](datatypes.html#string)]"/><!-- **0..1** ID assigned to the subscriber[](terminologies.html#unbound) -->
 <[**beneficiary**](coverage-definitions.html#Coverage.beneficiary "The party who benefits from the insurance coverage; the patient when products and/or services are provided.")><!-- **1..1** Reference[](references.html#Reference)(Patient[](patient.html#Patient)) Plan beneficiary[](terminologies.html#unbound) --></beneficiary>
 <[**dependent**](coverage-definitions.html#Coverage.dependent "A unique identifier for a dependent under the coverage.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Dependent number[](terminologies.html#unbound) -->
 <[**relationship**](coverage-definitions.html#Coverage.relationship "The relationship of beneficiary \(patient\) to the subscriber.")><!-- **0..1** CodeableConcept[](datatypes.html#CodeableConcept) Beneficiary relationship to the subscriber[](valueset-subscriber-relationship.html) --></relationship>
 <[**period**](coverage-definitions.html#Coverage.period "Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in force.")><!-- **0..1** Period[](datatypes.html#Period) Coverage start and end dates[](terminologies.html#unbound) --></period>
 <[**payor**](coverage-definitions.html#Coverage.payor "The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreements.")><!-- **1..*** Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) Issuer of the policy[](terminologies.html#unbound) --></payor>
 <[**class**](coverage-definitions.html#Coverage.class "A suite of underwriter specific classifiers.")>  <!-- **0..*** Additional coverage classifications -->
  <[**type**](coverage-definitions.html#Coverage.class.type "The type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, Plan.")><!-- **1..1** CodeableConcept[](datatypes.html#CodeableConcept) Type of class such as 'group' or 'plan'[](valueset-coverage-class.html) --></type>
  <[**value**](coverage-definitions.html#Coverage.class.value "The alphanumeric string value associated with the insurer issued label.") value="[string[](datatypes.html#string)]"/><!-- **1..1** Value associated with the type[](terminologies.html#unbound) -->
  <[**name**](coverage-definitions.html#Coverage.class.name "A short description for the class.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Human readable description of the type and value[](terminologies.html#unbound) -->
 </class>
 <[**order**](coverage-definitions.html#Coverage.order "The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of care.") value="[positiveInt[](datatypes.html#positiveInt)]"/><!-- **0..1** Relative order of the coverage[](terminologies.html#unbound) -->
 <[**network**](coverage-definitions.html#Coverage.network "The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions apply.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Insurer network[](terminologies.html#unbound) -->
 <[**costToBeneficiary**](coverage-definitions.html#Coverage.costToBeneficiary "A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.")>  <!-- **0..*** Patient payments for services/products -->
  <[**type**](coverage-definitions.html#Coverage.costToBeneficiary.type "The category of patient centric costs associated with treatment.")><!-- **0..1** CodeableConcept[](datatypes.html#CodeableConcept) Cost category[](valueset-coverage-copay-type.html) --></type>
  <[**value[x]**](coverage-definitions.html#Coverage.costToBeneficiary.value%5Bx%5D "The amount due from the patient for the cost category.")><!-- **1..1** Quantity[](datatypes.html#Quantity)(SimpleQuantity[](datatypes.html#SimpleQuantity))|Money[](datatypes.html#Money) The amount or percentage due from the beneficiary[](terminologies.html#unbound) --></value[x]>
  <[**exception**](coverage-definitions.html#Coverage.costToBeneficiary.exception "A suite of codes indicating exceptions or reductions to patient costs and their effective periods.")>  <!-- **0..*** Exceptions for patient payments -->
   <[**type**](coverage-definitions.html#Coverage.costToBeneficiary.exception.type "The code for the specific exception.")><!-- **1..1** CodeableConcept[](datatypes.html#CodeableConcept) Exception category[](valueset-coverage-financial-exception.html) --></type>
   <[**period**](coverage-definitions.html#Coverage.costToBeneficiary.exception.period "The timeframe during when the exception is in force.")><!-- **0..1** Period[](datatypes.html#Period) The effective period of the exception[](terminologies.html#unbound) --></period>
  </exception>
 </costToBeneficiary>
 <[**subrogation**](coverage-definitions.html#Coverage.subrogation "When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costs.") value="[boolean[](datatypes.html#boolean)]"/><!-- **0..1** Reimbursement to insurer[](terminologies.html#unbound) -->
 <[**contract**](coverage-definitions.html#Coverage.contract "The policy\(s\) which constitute this insurance coverage.")><!-- **0..*** Reference[](references.html#Reference)(Contract[](contract.html#Contract)) Contract details[](terminologies.html#unbound) --></contract>
</Coverage>

```

**JSON Template**
```

{[![doco](help.png)](json.html "Documentation for this format")
  "resourceType" : "[**Coverage**](coverage-definitions.html#Coverage "Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.")",
  // from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language)
  // from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension)
  "identifier[](coverage-definitions.html#Coverage.identifier "A unique identifier assigned to this coverage.")" : [{ Identifier[](datatypes.html#Identifier) }], // Business Identifier for the coverage[](terminologies.html#unbound)
  "[status](coverage-definitions.html#Coverage.status "The status of the resource instance \(this element modifies the meaning of other elements\)")" : "<code[](datatypes.html#code)>", // **R!**  active | cancelled | draft | entered-in-error[](valueset-fm-status.html)
  "type[](coverage-definitions.html#Coverage.type "The type of coverage: social program, medical plan, accident coverage \(workers compensation, auto\), group health or payment by an individual or organization.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // Coverage category such as medical or accident[](valueset-coverage-type.html)
  "policyHolder[](coverage-definitions.html#Coverage.policyHolder "The party who 'owns' the insurance policy.")" : { Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)|Organization[](organization.html#Organization)) }, // Owner of the policy[](terminologies.html#unbound)
  "subscriber[](coverage-definitions.html#Coverage.subscriber "The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is due.")" : { Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) }, // Subscriber to the policy[](terminologies.html#unbound)
  "subscriberId[](coverage-definitions.html#Coverage.subscriberId "The insurer assigned ID for the Subscriber.")" : "<string[](datatypes.html#string)>", // ID assigned to the subscriber[](terminologies.html#unbound)
  "beneficiary[](coverage-definitions.html#Coverage.beneficiary "The party who benefits from the insurance coverage; the patient when products and/or services are provided.")" : { Reference[](references.html#Reference)(Patient[](patient.html#Patient)) }, // **R!**  Plan beneficiary[](terminologies.html#unbound)
  "dependent[](coverage-definitions.html#Coverage.dependent "A unique identifier for a dependent under the coverage.")" : "<string[](datatypes.html#string)>", // Dependent number[](terminologies.html#unbound)
  "relationship[](coverage-definitions.html#Coverage.relationship "The relationship of beneficiary \(patient\) to the subscriber.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // Beneficiary relationship to the subscriber[](valueset-subscriber-relationship.html)
  "period[](coverage-definitions.html#Coverage.period "Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in force.")" : { Period[](datatypes.html#Period) }, // Coverage start and end dates[](terminologies.html#unbound)
  "payor[](coverage-definitions.html#Coverage.payor "The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreements.")" : [{ Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) }], // **R!**  Issuer of the policy[](terminologies.html#unbound)
  "class[](coverage-definitions.html#Coverage.class "A suite of underwriter specific classifiers.")" : [{ // Additional coverage classifications[](terminologies.html#unbound)
    "type[](coverage-definitions.html#Coverage.class.type "The type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, Plan.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // **R!**  Type of class such as 'group' or 'plan'[](valueset-coverage-class.html)
    "value[](coverage-definitions.html#Coverage.class.value "The alphanumeric string value associated with the insurer issued label.")" : "<string[](datatypes.html#string)>", // **R!**  Value associated with the type[](terminologies.html#unbound)
    "name[](coverage-definitions.html#Coverage.class.name "A short description for the class.")" : "<string[](datatypes.html#string)>" // Human readable description of the type and value[](terminologies.html#unbound)
  }],
  "order[](coverage-definitions.html#Coverage.order "The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of care.")" : "<positiveInt[](datatypes.html#positiveInt)>", // Relative order of the coverage[](terminologies.html#unbound)
  "network[](coverage-definitions.html#Coverage.network "The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions apply.")" : "<string[](datatypes.html#string)>", // Insurer network[](terminologies.html#unbound)
  "costToBeneficiary[](coverage-definitions.html#Coverage.costToBeneficiary "A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.")" : [{ // Patient payments for services/products[](terminologies.html#unbound)
    "type[](coverage-definitions.html#Coverage.costToBeneficiary.type "The category of patient centric costs associated with treatment.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // Cost category[](valueset-coverage-copay-type.html)
    // value[x]: The amount or percentage due from the beneficiary. One of these 2:
    "valueQuantity[](coverage-definitions.html#Coverage.costToBeneficiary.valueQuantity "The amount due from the patient for the cost category.")" : { Quantity[](datatypes.html#Quantity)(SimpleQuantity[](datatypes.html#SimpleQuantity)) },
    "valueMoney[](coverage-definitions.html#Coverage.costToBeneficiary.valueMoney "The amount due from the patient for the cost category.")" : { Money[](datatypes.html#Money) },
    "exception[](coverage-definitions.html#Coverage.costToBeneficiary.exception "A suite of codes indicating exceptions or reductions to patient costs and their effective periods.")" : [{ // Exceptions for patient payments[](terminologies.html#unbound)
      "type[](coverage-definitions.html#Coverage.costToBeneficiary.exception.type "The code for the specific exception.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // **R!**  Exception category[](valueset-coverage-financial-exception.html)
      "period[](coverage-definitions.html#Coverage.costToBeneficiary.exception.period "The timeframe during when the exception is in force.")" : { Period[](datatypes.html#Period) } // The effective period of the exception[](terminologies.html#unbound)
    }]
  }],
  "subrogation[](coverage-definitions.html#Coverage.subrogation "When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costs.")" : <boolean[](datatypes.html#boolean)>, // Reimbursement to insurer[](terminologies.html#unbound)
  "contract[](coverage-definitions.html#Coverage.contract "The policy\(s\) which constitute this insurance coverage.")" : [{ Reference[](references.html#Reference)(Contract[](contract.html#Contract)) }] // Contract details[](terminologies.html#unbound)
}

```

**Turtle Template**
```

@prefix fhir: <http://hl7.org/fhir/> .[![doco](help.png)](rdf.html "Documentation for this format")


[ a fhir:[**Coverage**](coverage-definitions.html#Coverage "Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.");
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource[](resource.html): .id[](resource.html#id), .meta[](resource.html#meta), .implicitRules[](resource.html#implicitRules), and .language[](resource.html#language)
  # from DomainResource[](domainresource.html): .text[](narrative.html#Narrative), .contained[](references.html#contained), .extension[](extensibility.html), and .modifierExtension[](extensibility.html#modifierExtension)
  fhir:Coverage.identifier[](coverage-definitions.html#Coverage.identifier "A unique identifier assigned to this coverage.") [ Identifier[](datatypes.html#Identifier) ], ... ; # 0..* Business Identifier for the coverage
  fhir:[Coverage.status](coverage-definitions.html#Coverage.status "The status of the resource instance \(this element modifies the meaning of other elements\)") [ code[](datatypes.html#code) ]; # 1..1 active | cancelled | draft | entered-in-error
  fhir:Coverage.type[](coverage-definitions.html#Coverage.type "The type of coverage: social program, medical plan, accident coverage \(workers compensation, auto\), group health or payment by an individual or organization.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 0..1 Coverage category such as medical or accident
  fhir:Coverage.policyHolder[](coverage-definitions.html#Coverage.policyHolder "The party who 'owns' the insurance policy.") [ Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)|Organization[](organization.html#Organization)) ]; # 0..1 Owner of the policy
  fhir:Coverage.subscriber[](coverage-definitions.html#Coverage.subscriber "The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is due.") [ Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) ]; # 0..1 Subscriber to the policy
  fhir:Coverage.subscriberId[](coverage-definitions.html#Coverage.subscriberId "The insurer assigned ID for the Subscriber.") [ string[](datatypes.html#string) ]; # 0..1 ID assigned to the subscriber
  fhir:Coverage.beneficiary[](coverage-definitions.html#Coverage.beneficiary "The party who benefits from the insurance coverage; the patient when products and/or services are provided.") [ Reference[](references.html#Reference)(Patient[](patient.html#Patient)) ]; # 1..1 Plan beneficiary
  fhir:Coverage.dependent[](coverage-definitions.html#Coverage.dependent "A unique identifier for a dependent under the coverage.") [ string[](datatypes.html#string) ]; # 0..1 Dependent number
  fhir:Coverage.relationship[](coverage-definitions.html#Coverage.relationship "The relationship of beneficiary \(patient\) to the subscriber.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 0..1 Beneficiary relationship to the subscriber
  fhir:Coverage.period[](coverage-definitions.html#Coverage.period "Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in force.") [ Period[](datatypes.html#Period) ]; # 0..1 Coverage start and end dates
  fhir:Coverage.payor[](coverage-definitions.html#Coverage.payor "The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreements.") [ Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) ], ... ; # 1..* Issuer of the policy
  fhir:Coverage.class[](coverage-definitions.html#Coverage.class "A suite of underwriter specific classifiers.") [ # 0..* Additional coverage classifications
    fhir:Coverage.class.type[](coverage-definitions.html#Coverage.class.type "The type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, Plan.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 1..1 Type of class such as 'group' or 'plan'
    fhir:Coverage.class.value[](coverage-definitions.html#Coverage.class.value "The alphanumeric string value associated with the insurer issued label.") [ string[](datatypes.html#string) ]; # 1..1 Value associated with the type
    fhir:Coverage.class.name[](coverage-definitions.html#Coverage.class.name "A short description for the class.") [ string[](datatypes.html#string) ]; # 0..1 Human readable description of the type and value
  ], ...;
  fhir:Coverage.order[](coverage-definitions.html#Coverage.order "The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of care.") [ positiveInt[](datatypes.html#positiveInt) ]; # 0..1 Relative order of the coverage
  fhir:Coverage.network[](coverage-definitions.html#Coverage.network "The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions apply.") [ string[](datatypes.html#string) ]; # 0..1 Insurer network
  fhir:Coverage.costToBeneficiary[](coverage-definitions.html#Coverage.costToBeneficiary "A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.") [ # 0..* Patient payments for services/products
    fhir:Coverage.costToBeneficiary.type[](coverage-definitions.html#Coverage.costToBeneficiary.type "The category of patient centric costs associated with treatment.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 0..1 Cost category
    # Coverage.costToBeneficiary.value[x][](coverage-definitions.html#Coverage.costToBeneficiary.value%5Bx%5D "The amount due from the patient for the cost category.") : 1..1 The amount or percentage due from the beneficiary. One of these 2
      fhir:Coverage.costToBeneficiary.valueSimpleQuantity[](coverage-definitions.html#Coverage.costToBeneficiary.valueSimpleQuantity "The amount due from the patient for the cost category.") [ Quantity[](datatypes.html#Quantity)(SimpleQuantity[](datatypes.html#SimpleQuantity)) ]
      fhir:Coverage.costToBeneficiary.valueMoney[](coverage-definitions.html#Coverage.costToBeneficiary.valueMoney "The amount due from the patient for the cost category.") [ Money[](datatypes.html#Money) ]
    fhir:Coverage.costToBeneficiary.exception[](coverage-definitions.html#Coverage.costToBeneficiary.exception "A suite of codes indicating exceptions or reductions to patient costs and their effective periods.") [ # 0..* Exceptions for patient payments
      fhir:Coverage.costToBeneficiary.exception.type[](coverage-definitions.html#Coverage.costToBeneficiary.exception.type "The code for the specific exception.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 1..1 Exception category
      fhir:Coverage.costToBeneficiary.exception.period[](coverage-definitions.html#Coverage.costToBeneficiary.exception.period "The timeframe during when the exception is in force.") [ Period[](datatypes.html#Period) ]; # 0..1 The effective period of the exception
    ], ...;
  ], ...;
  fhir:Coverage.subrogation[](coverage-definitions.html#Coverage.subrogation "When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costs.") [ boolean[](datatypes.html#boolean) ]; # 0..1 Reimbursement to insurer
  fhir:Coverage.contract[](coverage-definitions.html#Coverage.contract "The policy\(s\) which constitute this insurance coverage.") [ Reference[](references.html#Reference)(Contract[](contract.html#Contract)) ], ... ; # 0..* Contract details
]

```

**Changes since R3**
[Coverage](coverage.html#Coverage) |   
---|---  
Coverage.status | 
  * Min Cardinality changed from 0 to 1
  * Change value set from http://hl7.org/fhir/ValueSet/fm-status to http://hl7.org/fhir/ValueSet/fm-status|4.0.1

  
Coverage.beneficiary | 
  * Min Cardinality changed from 0 to 1

  
Coverage.relationship | 
  * Add Binding `http://hl7.org/fhir/ValueSet/subscriber-relationship` (extensible) 

  
Coverage.payor | 
  * Min Cardinality changed from 0 to 1

  
Coverage.class | 
  * Renamed from grouping to class
  * Max Cardinality changed from 1 to *

  
Coverage.class.type | 
  * **Added Mandatory Element**

  
Coverage.class.value | 
  * **Added Mandatory Element**

  
Coverage.class.name | 
  * Added Element

  
Coverage.costToBeneficiary | 
  * Added Element

  
Coverage.costToBeneficiary.type | 
  * Added Element

  
Coverage.costToBeneficiary.value[x] | 
  * **Added Mandatory Element**

  
Coverage.costToBeneficiary.exception | 
  * Added Element

  
Coverage.costToBeneficiary.exception.type | 
  * **Added Mandatory Element**

  
Coverage.costToBeneficiary.exception.period | 
  * Added Element

  
Coverage.subrogation | 
  * Added Element

  
Coverage.grouping.group | 
  * deleted

  
Coverage.grouping.groupDisplay | 
  * deleted

  
Coverage.grouping.subGroup | 
  * deleted

  
Coverage.grouping.subGroupDisplay | 
  * deleted

  
Coverage.grouping.plan | 
  * deleted

  
Coverage.grouping.planDisplay | 
  * deleted

  
Coverage.grouping.subPlan | 
  * deleted

  
Coverage.grouping.subPlanDisplay | 
  * deleted

  
Coverage.grouping.class | 
  * deleted

  
Coverage.grouping.classDisplay | 
  * deleted

  
Coverage.grouping.subClass | 
  * deleted

  
Coverage.grouping.subClassDisplay | 
  * deleted

  
Coverage.sequence | 
  * deleted

  
See the [Full Difference](diff.html) for further information
This analysis is available as [XML](coverage.diff.xml) or [JSON](coverage.diff.json). 
See [R3 <--> R4 Conversion Maps](coverage-version-maps.html) (status = 4 tests that all execute ok. 1 fail round-trip testing and all r3 resources are valid.)
**Structure**
[Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") |  [Description & Constraints](formats.html#table "Additional information about the element")[![doco](help16.png)](formats.html#table "Legend for this format")  
---|---|---|---|---  
![.](tbl_spacer.png)![.](icon_resource.png) [Coverage](coverage-definitions.html#Coverage "Coverage : Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.") | [TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | Insurance or medical plan or a payment agreement  
Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.

Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource \(including cannot change the meaning of modifierExtension itself\).")  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [identifier](coverage-definitions.html#Coverage.identifier "Coverage.identifier : A unique identifier assigned to this coverage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [Identifier](datatypes.html#Identifier) | Business Identifier for the coverage  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [status](coverage-definitions.html#Coverage.status "Coverage.status : The status of the resource instance.") |  [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | active | cancelled | draft | entered-in-error  
[Financial Resource Status Codes](valueset-fm-status.html "A code specifying the state of the resource instance.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](coverage-definitions.html#Coverage.type "Coverage.type : The type of coverage: social program, medical plan, accident coverage \(workers compensation, auto\), group health or payment by an individual or organization.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Coverage category such as medical or accident  
[Coverage Type and Self-Pay Codes](valueset-coverage-type.html "The type of insurance: public health, worker compensation; private accident, auto, private health, etc.\) or a direct payment by an individual or organization.") ([Preferred](terminologies.html#preferred "Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to do so to be considered conformant."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [policyHolder](coverage-definitions.html#Coverage.policyHolder "Coverage.policyHolder : The party who 'owns' the insurance policy.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html) | [Organization](organization.html)) | Owner of the policy  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [subscriber](coverage-definitions.html#Coverage.subscriber "Coverage.subscriber : The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is due.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 |  [Reference](references.html#Reference)([Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Subscriber to the policy  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [subscriberId](coverage-definitions.html#Coverage.subscriberId "Coverage.subscriberId : The insurer assigned ID for the Subscriber.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | ID assigned to the subscriber  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [beneficiary](coverage-definitions.html#Coverage.beneficiary "Coverage.beneficiary : The party who benefits from the insurance coverage; the patient when products and/or services are provided.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [Reference](references.html#Reference)([Patient](patient.html)) | Plan beneficiary  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [dependent](coverage-definitions.html#Coverage.dependent "Coverage.dependent : A unique identifier for a dependent under the coverage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Dependent number  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [relationship](coverage-definitions.html#Coverage.relationship "Coverage.relationship : The relationship of beneficiary \(patient\) to the subscriber.") |  | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Beneficiary relationship to the subscriber  
[SubscriberPolicyholder Relationship Codes](valueset-subscriber-relationship.html "The relationship between the Subscriber and the Beneficiary \(insured/covered party/patient\).") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [period](coverage-definitions.html#Coverage.period "Coverage.period : Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in force.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | Coverage start and end dates  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_reference.png) [payor](coverage-definitions.html#Coverage.payor "Coverage.payor : The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreements.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..* |  [Reference](references.html#Reference)([Organization](organization.html) | [Patient](patient.html) | [RelatedPerson](relatedperson.html)) | Issuer of the policy  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [class](coverage-definitions.html#Coverage.class "Coverage.class : A suite of underwriter specific classifiers.") |  | 0..* | [BackboneElement](backboneelement.html) | Additional coverage classifications  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](coverage-definitions.html#Coverage.class.type "Coverage.class.type : The type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, Plan.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Type of class such as 'group' or 'plan'  
[Coverage Class Codes](valueset-coverage-class.html "The policy classifications, eg. Group, Plan, Class, etc.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [value](coverage-definitions.html#Coverage.class.value "Coverage.class.value : The alphanumeric string value associated with the insurer issued label.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [string](datatypes.html#string) | Value associated with the type  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [name](coverage-definitions.html#Coverage.class.name "Coverage.class.name : A short description for the class.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Human readable description of the type and value  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [order](coverage-definitions.html#Coverage.order "Coverage.order : The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of care.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [positiveInt](datatypes.html#positiveInt) | Relative order of the coverage  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [network](coverage-definitions.html#Coverage.network "Coverage.network : The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions apply.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Insurer network  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [costToBeneficiary](coverage-definitions.html#Coverage.costToBeneficiary "Coverage.costToBeneficiary : A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.") |  | 0..* | [BackboneElement](backboneelement.html) | Patient payments for services/products  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](coverage-definitions.html#Coverage.costToBeneficiary.type "Coverage.costToBeneficiary.type : The category of patient centric costs associated with treatment.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Cost category  
[Coverage Copay Type Codes](valueset-coverage-copay-type.html "The types of services to which patient copayments are specified.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_choice.gif) [value[x]](coverage-definitions.html#Coverage.costToBeneficiary.value_x_ "Coverage.costToBeneficiary.value\[x\] : The amount due from the patient for the cost category.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  | The amount or percentage due from the beneficiary  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) valueQuantity |  |  | [SimpleQuantity](datatypes.html#SimpleQuantity) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_datatype.gif) valueMoney |  |  | [Money](datatypes.html#Money) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [exception](coverage-definitions.html#Coverage.costToBeneficiary.exception "Coverage.costToBeneficiary.exception : A suite of codes indicating exceptions or reductions to patient costs and their effective periods.") |  | 0..* | [BackboneElement](backboneelement.html) | Exceptions for patient payments  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [type](coverage-definitions.html#Coverage.costToBeneficiary.exception.type "Coverage.costToBeneficiary.exception.type : The code for the specific exception.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [CodeableConcept](datatypes.html#CodeableConcept) | Exception category  
[Example Coverage Financial Exception Codes](valueset-coverage-financial-exception.html "The types of exceptions from the part or full value of financial obligations such as copays.") ([Example](terminologies.html#example "Instances are not expected or even encouraged to draw from the specified value set.  The value set merely provides examples of the types of concepts intended to be included."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_datatype.gif) [period](coverage-definitions.html#Coverage.costToBeneficiary.exception.period "Coverage.costToBeneficiary.exception.period : The timeframe during when the exception is in force.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [Period](datatypes.html#Period) | The effective period of the exception  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [subrogation](coverage-definitions.html#Coverage.subrogation "Coverage.subrogation : When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costs.") |  | 0..1 | [boolean](datatypes.html#boolean) | Reimbursement to insurer  
![.](tbl_spacer.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) [contract](coverage-definitions.html#Coverage.contract "Coverage.contract : The policy\(s\) which constitute this insurance coverage.") |  | 0..* |  [Reference](references.html#Reference)([Contract](contract.html)) | Contract details  
  
  
[![doco](help16.png) Documentation for this format](formats.html#table "Legend for this format")  
**UML Diagram** ([Legend](formats.html#uml))
Coverage (DomainResource)A unique identifier assigned to this coverageidentifier : Identifier [0..*]The status of the resource instance (this element modifies the meaning of other elements)status : code [1..1] « A code specifying the state of the resource instance. (Strength=Required)FinancialResourceStatusCodes! »The type of coverage: social program, medical plan, accident coverage (workers compensation, auto), group health or payment by an individual or organizationtype : CodeableConcept [0..1] « The type of insurance: public health, worker compensation; private accident, auto, private health, etc.) or a direct payment by an individual or organization. (Strength=Preferred)CoverageTypeAndSelf-PayCodes? »The party who 'owns' the insurance policypolicyHolder : Reference [0..1] « Patient|RelatedPerson|Organization »The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is duesubscriber : Reference [0..1] « Patient|RelatedPerson »The insurer assigned ID for the SubscribersubscriberId : string [0..1]The party who benefits from the insurance coverage; the patient when products and/or services are providedbeneficiary : Reference [1..1] « Patient »A unique identifier for a dependent under the coveragedependent : string [0..1]The relationship of beneficiary (patient) to the subscriberrelationship : CodeableConcept [0..1] « The relationship between the Subscriber and the Beneficiary (insured/covered party/patient). (Strength=Extensible)SubscriberRelationshipCodes+ »Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in forceperiod : Period [0..1]The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreementspayor : Reference [1..*] « Organization|Patient|RelatedPerson »The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of careorder : positiveInt [0..1]The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions applynetwork : string [0..1]When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costssubrogation : boolean [0..1]The policy(s) which constitute this insurance coveragecontract : Reference [0..*] « Contract »ClassThe type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, Plantype : CodeableConcept [1..1] « The policy classifications, eg. Group, Plan, Class, etc. (Strength=Extensible)CoverageClassCodes+ »The alphanumeric string value associated with the insurer issued labelvalue : string [1..1]A short description for the classname : string [0..1]CostToBeneficiaryThe category of patient centric costs associated with treatmenttype : CodeableConcept [0..1] « The types of services to which patient copayments are specified. (Strength=Extensible)CoverageCopayTypeCodes+ »The amount due from the patient for the cost categoryvalue[x] : Type [1..1] « Quantity(SimpleQuantity)|Money »ExemptionThe code for the specific exceptiontype : CodeableConcept [1..1] « The types of exceptions from the part or full value of financial obligations such as copays. (Strength=Example)ExampleCoverageFinancialExcep...?? »The timeframe during when the exception is in forceperiod : Period [0..1]A suite of underwriter specific classifiersclass[0..*]A suite of codes indicating exceptions or reductions to patient costs and their effective periodsexception[0..*]A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been included on the health cardcostToBeneficiary[0..*]
**XML Template**
```

<[**Coverage**](coverage-definitions.html#Coverage "Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.") xmlns="http://hl7.org/fhir"> [![doco](help.png)](xml.html "Documentation for this format")
 <!-- from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language) -->
 <!-- from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension) -->
 <[**identifier**](coverage-definitions.html#Coverage.identifier "A unique identifier assigned to this coverage.")><!-- **0..*** Identifier[](datatypes.html#Identifier) Business Identifier for the coverage[](terminologies.html#unbound) --></identifier>
 <[**status**](coverage-definitions.html#Coverage.status "The status of the resource instance \(this element modifies the meaning of other elements\)") value="[code[](datatypes.html#code)]"/><!-- **1..1** active | cancelled | draft | entered-in-error[](valueset-fm-status.html) -->
 <[**type**](coverage-definitions.html#Coverage.type "The type of coverage: social program, medical plan, accident coverage \(workers compensation, auto\), group health or payment by an individual or organization.")><!-- **0..1** CodeableConcept[](datatypes.html#CodeableConcept) Coverage category such as medical or accident[](valueset-coverage-type.html) --></type>
 <[**policyHolder**](coverage-definitions.html#Coverage.policyHolder "The party who 'owns' the insurance policy.")><!-- **0..1** Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)|Organization[](organization.html#Organization)) Owner of the policy[](terminologies.html#unbound) --></policyHolder>
 <[**subscriber**](coverage-definitions.html#Coverage.subscriber "The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is due.")><!-- **0..1** Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) Subscriber to the policy[](terminologies.html#unbound) --></subscriber>
 <[**subscriberId**](coverage-definitions.html#Coverage.subscriberId "The insurer assigned ID for the Subscriber.") value="[string[](datatypes.html#string)]"/><!-- **0..1** ID assigned to the subscriber[](terminologies.html#unbound) -->
 <[**beneficiary**](coverage-definitions.html#Coverage.beneficiary "The party who benefits from the insurance coverage; the patient when products and/or services are provided.")><!-- **1..1** Reference[](references.html#Reference)(Patient[](patient.html#Patient)) Plan beneficiary[](terminologies.html#unbound) --></beneficiary>
 <[**dependent**](coverage-definitions.html#Coverage.dependent "A unique identifier for a dependent under the coverage.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Dependent number[](terminologies.html#unbound) -->
 <[**relationship**](coverage-definitions.html#Coverage.relationship "The relationship of beneficiary \(patient\) to the subscriber.")><!-- **0..1** CodeableConcept[](datatypes.html#CodeableConcept) Beneficiary relationship to the subscriber[](valueset-subscriber-relationship.html) --></relationship>
 <[**period**](coverage-definitions.html#Coverage.period "Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in force.")><!-- **0..1** Period[](datatypes.html#Period) Coverage start and end dates[](terminologies.html#unbound) --></period>
 <[**payor**](coverage-definitions.html#Coverage.payor "The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreements.")><!-- **1..*** Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) Issuer of the policy[](terminologies.html#unbound) --></payor>
 <[**class**](coverage-definitions.html#Coverage.class "A suite of underwriter specific classifiers.")>  <!-- **0..*** Additional coverage classifications -->
  <[**type**](coverage-definitions.html#Coverage.class.type "The type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, Plan.")><!-- **1..1** CodeableConcept[](datatypes.html#CodeableConcept) Type of class such as 'group' or 'plan'[](valueset-coverage-class.html) --></type>
  <[**value**](coverage-definitions.html#Coverage.class.value "The alphanumeric string value associated with the insurer issued label.") value="[string[](datatypes.html#string)]"/><!-- **1..1** Value associated with the type[](terminologies.html#unbound) -->
  <[**name**](coverage-definitions.html#Coverage.class.name "A short description for the class.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Human readable description of the type and value[](terminologies.html#unbound) -->
 </class>
 <[**order**](coverage-definitions.html#Coverage.order "The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of care.") value="[positiveInt[](datatypes.html#positiveInt)]"/><!-- **0..1** Relative order of the coverage[](terminologies.html#unbound) -->
 <[**network**](coverage-definitions.html#Coverage.network "The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions apply.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Insurer network[](terminologies.html#unbound) -->
 <[**costToBeneficiary**](coverage-definitions.html#Coverage.costToBeneficiary "A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.")>  <!-- **0..*** Patient payments for services/products -->
  <[**type**](coverage-definitions.html#Coverage.costToBeneficiary.type "The category of patient centric costs associated with treatment.")><!-- **0..1** CodeableConcept[](datatypes.html#CodeableConcept) Cost category[](valueset-coverage-copay-type.html) --></type>
  <[**value[x]**](coverage-definitions.html#Coverage.costToBeneficiary.value%5Bx%5D "The amount due from the patient for the cost category.")><!-- **1..1** Quantity[](datatypes.html#Quantity)(SimpleQuantity[](datatypes.html#SimpleQuantity))|Money[](datatypes.html#Money) The amount or percentage due from the beneficiary[](terminologies.html#unbound) --></value[x]>
  <[**exception**](coverage-definitions.html#Coverage.costToBeneficiary.exception "A suite of codes indicating exceptions or reductions to patient costs and their effective periods.")>  <!-- **0..*** Exceptions for patient payments -->
   <[**type**](coverage-definitions.html#Coverage.costToBeneficiary.exception.type "The code for the specific exception.")><!-- **1..1** CodeableConcept[](datatypes.html#CodeableConcept) Exception category[](valueset-coverage-financial-exception.html) --></type>
   <[**period**](coverage-definitions.html#Coverage.costToBeneficiary.exception.period "The timeframe during when the exception is in force.")><!-- **0..1** Period[](datatypes.html#Period) The effective period of the exception[](terminologies.html#unbound) --></period>
  </exception>
 </costToBeneficiary>
 <[**subrogation**](coverage-definitions.html#Coverage.subrogation "When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costs.") value="[boolean[](datatypes.html#boolean)]"/><!-- **0..1** Reimbursement to insurer[](terminologies.html#unbound) -->
 <[**contract**](coverage-definitions.html#Coverage.contract "The policy\(s\) which constitute this insurance coverage.")><!-- **0..*** Reference[](references.html#Reference)(Contract[](contract.html#Contract)) Contract details[](terminologies.html#unbound) --></contract>
</Coverage>

```

**JSON Template**
```

{[![doco](help.png)](json.html "Documentation for this format")
  "resourceType" : "[**Coverage**](coverage-definitions.html#Coverage "Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.")",
  // from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language)
  // from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension)
  "identifier[](coverage-definitions.html#Coverage.identifier "A unique identifier assigned to this coverage.")" : [{ Identifier[](datatypes.html#Identifier) }], // Business Identifier for the coverage[](terminologies.html#unbound)
  "[status](coverage-definitions.html#Coverage.status "The status of the resource instance \(this element modifies the meaning of other elements\)")" : "<code[](datatypes.html#code)>", // **R!**  active | cancelled | draft | entered-in-error[](valueset-fm-status.html)
  "type[](coverage-definitions.html#Coverage.type "The type of coverage: social program, medical plan, accident coverage \(workers compensation, auto\), group health or payment by an individual or organization.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // Coverage category such as medical or accident[](valueset-coverage-type.html)
  "policyHolder[](coverage-definitions.html#Coverage.policyHolder "The party who 'owns' the insurance policy.")" : { Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)|Organization[](organization.html#Organization)) }, // Owner of the policy[](terminologies.html#unbound)
  "subscriber[](coverage-definitions.html#Coverage.subscriber "The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is due.")" : { Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) }, // Subscriber to the policy[](terminologies.html#unbound)
  "subscriberId[](coverage-definitions.html#Coverage.subscriberId "The insurer assigned ID for the Subscriber.")" : "<string[](datatypes.html#string)>", // ID assigned to the subscriber[](terminologies.html#unbound)
  "beneficiary[](coverage-definitions.html#Coverage.beneficiary "The party who benefits from the insurance coverage; the patient when products and/or services are provided.")" : { Reference[](references.html#Reference)(Patient[](patient.html#Patient)) }, // **R!**  Plan beneficiary[](terminologies.html#unbound)
  "dependent[](coverage-definitions.html#Coverage.dependent "A unique identifier for a dependent under the coverage.")" : "<string[](datatypes.html#string)>", // Dependent number[](terminologies.html#unbound)
  "relationship[](coverage-definitions.html#Coverage.relationship "The relationship of beneficiary \(patient\) to the subscriber.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // Beneficiary relationship to the subscriber[](valueset-subscriber-relationship.html)
  "period[](coverage-definitions.html#Coverage.period "Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in force.")" : { Period[](datatypes.html#Period) }, // Coverage start and end dates[](terminologies.html#unbound)
  "payor[](coverage-definitions.html#Coverage.payor "The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreements.")" : [{ Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) }], // **R!**  Issuer of the policy[](terminologies.html#unbound)
  "class[](coverage-definitions.html#Coverage.class "A suite of underwriter specific classifiers.")" : [{ // Additional coverage classifications[](terminologies.html#unbound)
    "type[](coverage-definitions.html#Coverage.class.type "The type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, Plan.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // **R!**  Type of class such as 'group' or 'plan'[](valueset-coverage-class.html)
    "value[](coverage-definitions.html#Coverage.class.value "The alphanumeric string value associated with the insurer issued label.")" : "<string[](datatypes.html#string)>", // **R!**  Value associated with the type[](terminologies.html#unbound)
    "name[](coverage-definitions.html#Coverage.class.name "A short description for the class.")" : "<string[](datatypes.html#string)>" // Human readable description of the type and value[](terminologies.html#unbound)
  }],
  "order[](coverage-definitions.html#Coverage.order "The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of care.")" : "<positiveInt[](datatypes.html#positiveInt)>", // Relative order of the coverage[](terminologies.html#unbound)
  "network[](coverage-definitions.html#Coverage.network "The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions apply.")" : "<string[](datatypes.html#string)>", // Insurer network[](terminologies.html#unbound)
  "costToBeneficiary[](coverage-definitions.html#Coverage.costToBeneficiary "A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.")" : [{ // Patient payments for services/products[](terminologies.html#unbound)
    "type[](coverage-definitions.html#Coverage.costToBeneficiary.type "The category of patient centric costs associated with treatment.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // Cost category[](valueset-coverage-copay-type.html)
    // value[x]: The amount or percentage due from the beneficiary. One of these 2:
    "valueQuantity[](coverage-definitions.html#Coverage.costToBeneficiary.valueQuantity "The amount due from the patient for the cost category.")" : { Quantity[](datatypes.html#Quantity)(SimpleQuantity[](datatypes.html#SimpleQuantity)) },
    "valueMoney[](coverage-definitions.html#Coverage.costToBeneficiary.valueMoney "The amount due from the patient for the cost category.")" : { Money[](datatypes.html#Money) },
    "exception[](coverage-definitions.html#Coverage.costToBeneficiary.exception "A suite of codes indicating exceptions or reductions to patient costs and their effective periods.")" : [{ // Exceptions for patient payments[](terminologies.html#unbound)
      "type[](coverage-definitions.html#Coverage.costToBeneficiary.exception.type "The code for the specific exception.")" : { CodeableConcept[](datatypes.html#CodeableConcept) }, // **R!**  Exception category[](valueset-coverage-financial-exception.html)
      "period[](coverage-definitions.html#Coverage.costToBeneficiary.exception.period "The timeframe during when the exception is in force.")" : { Period[](datatypes.html#Period) } // The effective period of the exception[](terminologies.html#unbound)
    }]
  }],
  "subrogation[](coverage-definitions.html#Coverage.subrogation "When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costs.")" : <boolean[](datatypes.html#boolean)>, // Reimbursement to insurer[](terminologies.html#unbound)
  "contract[](coverage-definitions.html#Coverage.contract "The policy\(s\) which constitute this insurance coverage.")" : [{ Reference[](references.html#Reference)(Contract[](contract.html#Contract)) }] // Contract details[](terminologies.html#unbound)
}

```

**Turtle Template**
```

@prefix fhir: <http://hl7.org/fhir/> .[![doco](help.png)](rdf.html "Documentation for this format")


[ a fhir:[**Coverage**](coverage-definitions.html#Coverage "Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.");
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource[](resource.html): .id[](resource.html#id), .meta[](resource.html#meta), .implicitRules[](resource.html#implicitRules), and .language[](resource.html#language)
  # from DomainResource[](domainresource.html): .text[](narrative.html#Narrative), .contained[](references.html#contained), .extension[](extensibility.html), and .modifierExtension[](extensibility.html#modifierExtension)
  fhir:Coverage.identifier[](coverage-definitions.html#Coverage.identifier "A unique identifier assigned to this coverage.") [ Identifier[](datatypes.html#Identifier) ], ... ; # 0..* Business Identifier for the coverage
  fhir:[Coverage.status](coverage-definitions.html#Coverage.status "The status of the resource instance \(this element modifies the meaning of other elements\)") [ code[](datatypes.html#code) ]; # 1..1 active | cancelled | draft | entered-in-error
  fhir:Coverage.type[](coverage-definitions.html#Coverage.type "The type of coverage: social program, medical plan, accident coverage \(workers compensation, auto\), group health or payment by an individual or organization.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 0..1 Coverage category such as medical or accident
  fhir:Coverage.policyHolder[](coverage-definitions.html#Coverage.policyHolder "The party who 'owns' the insurance policy.") [ Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)|Organization[](organization.html#Organization)) ]; # 0..1 Owner of the policy
  fhir:Coverage.subscriber[](coverage-definitions.html#Coverage.subscriber "The party who has signed-up for or 'owns' the contractual relationship to the policy or to whom the benefit of the policy for services rendered to them or their family is due.") [ Reference[](references.html#Reference)(Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) ]; # 0..1 Subscriber to the policy
  fhir:Coverage.subscriberId[](coverage-definitions.html#Coverage.subscriberId "The insurer assigned ID for the Subscriber.") [ string[](datatypes.html#string) ]; # 0..1 ID assigned to the subscriber
  fhir:Coverage.beneficiary[](coverage-definitions.html#Coverage.beneficiary "The party who benefits from the insurance coverage; the patient when products and/or services are provided.") [ Reference[](references.html#Reference)(Patient[](patient.html#Patient)) ]; # 1..1 Plan beneficiary
  fhir:Coverage.dependent[](coverage-definitions.html#Coverage.dependent "A unique identifier for a dependent under the coverage.") [ string[](datatypes.html#string) ]; # 0..1 Dependent number
  fhir:Coverage.relationship[](coverage-definitions.html#Coverage.relationship "The relationship of beneficiary \(patient\) to the subscriber.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 0..1 Beneficiary relationship to the subscriber
  fhir:Coverage.period[](coverage-definitions.html#Coverage.period "Time period during which the coverage is in force. A missing start date indicates the start date isn't known, a missing end date means the coverage is continuing to be in force.") [ Period[](datatypes.html#Period) ]; # 0..1 Coverage start and end dates
  fhir:Coverage.payor[](coverage-definitions.html#Coverage.payor "The program or plan underwriter or payor including both insurance and non-insurance agreements, such as patient-pay agreements.") [ Reference[](references.html#Reference)(Organization[](organization.html#Organization)|Patient[](patient.html#Patient)|RelatedPerson[](relatedperson.html#RelatedPerson)) ], ... ; # 1..* Issuer of the policy
  fhir:Coverage.class[](coverage-definitions.html#Coverage.class "A suite of underwriter specific classifiers.") [ # 0..* Additional coverage classifications
    fhir:Coverage.class.type[](coverage-definitions.html#Coverage.class.type "The type of classification for which an insurer-specific class label or number and optional name is provided, for example may be used to identify a class of coverage or employer group, Policy, Plan.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 1..1 Type of class such as 'group' or 'plan'
    fhir:Coverage.class.value[](coverage-definitions.html#Coverage.class.value "The alphanumeric string value associated with the insurer issued label.") [ string[](datatypes.html#string) ]; # 1..1 Value associated with the type
    fhir:Coverage.class.name[](coverage-definitions.html#Coverage.class.name "A short description for the class.") [ string[](datatypes.html#string) ]; # 0..1 Human readable description of the type and value
  ], ...;
  fhir:Coverage.order[](coverage-definitions.html#Coverage.order "The order of applicability of this coverage relative to other coverages which are currently in force. Note, there may be gaps in the numbering and this does not imply primary, secondary etc. as the specific positioning of coverages depends upon the episode of care.") [ positiveInt[](datatypes.html#positiveInt) ]; # 0..1 Relative order of the coverage
  fhir:Coverage.network[](coverage-definitions.html#Coverage.network "The insurer-specific identifier for the insurer-defined network of providers to which the beneficiary may seek treatment which will be covered at the 'in-network' rate, otherwise 'out of network' terms and conditions apply.") [ string[](datatypes.html#string) ]; # 0..1 Insurer network
  fhir:Coverage.costToBeneficiary[](coverage-definitions.html#Coverage.costToBeneficiary "A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.") [ # 0..* Patient payments for services/products
    fhir:Coverage.costToBeneficiary.type[](coverage-definitions.html#Coverage.costToBeneficiary.type "The category of patient centric costs associated with treatment.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 0..1 Cost category
    # Coverage.costToBeneficiary.value[x][](coverage-definitions.html#Coverage.costToBeneficiary.value%5Bx%5D "The amount due from the patient for the cost category.") : 1..1 The amount or percentage due from the beneficiary. One of these 2
      fhir:Coverage.costToBeneficiary.valueSimpleQuantity[](coverage-definitions.html#Coverage.costToBeneficiary.valueSimpleQuantity "The amount due from the patient for the cost category.") [ Quantity[](datatypes.html#Quantity)(SimpleQuantity[](datatypes.html#SimpleQuantity)) ]
      fhir:Coverage.costToBeneficiary.valueMoney[](coverage-definitions.html#Coverage.costToBeneficiary.valueMoney "The amount due from the patient for the cost category.") [ Money[](datatypes.html#Money) ]
    fhir:Coverage.costToBeneficiary.exception[](coverage-definitions.html#Coverage.costToBeneficiary.exception "A suite of codes indicating exceptions or reductions to patient costs and their effective periods.") [ # 0..* Exceptions for patient payments
      fhir:Coverage.costToBeneficiary.exception.type[](coverage-definitions.html#Coverage.costToBeneficiary.exception.type "The code for the specific exception.") [ CodeableConcept[](datatypes.html#CodeableConcept) ]; # 1..1 Exception category
      fhir:Coverage.costToBeneficiary.exception.period[](coverage-definitions.html#Coverage.costToBeneficiary.exception.period "The timeframe during when the exception is in force.") [ Period[](datatypes.html#Period) ]; # 0..1 The effective period of the exception
    ], ...;
  ], ...;
  fhir:Coverage.subrogation[](coverage-definitions.html#Coverage.subrogation "When 'subrogation=true' this insurance instance has been included not for adjudication but to provide insurers with the details to recover costs.") [ boolean[](datatypes.html#boolean) ]; # 0..1 Reimbursement to insurer
  fhir:Coverage.contract[](coverage-definitions.html#Coverage.contract "The policy\(s\) which constitute this insurance coverage.") [ Reference[](references.html#Reference)(Contract[](contract.html#Contract)) ], ... ; # 0..* Contract details
]

```

**Changes since Release 3**
[Coverage](coverage.html#Coverage) |   
---|---  
Coverage.status | 
  * Min Cardinality changed from 0 to 1
  * Change value set from http://hl7.org/fhir/ValueSet/fm-status to http://hl7.org/fhir/ValueSet/fm-status|4.0.1

  
Coverage.beneficiary | 
  * Min Cardinality changed from 0 to 1

  
Coverage.relationship | 
  * Add Binding `http://hl7.org/fhir/ValueSet/subscriber-relationship` (extensible) 

  
Coverage.payor | 
  * Min Cardinality changed from 0 to 1

  
Coverage.class | 
  * Renamed from grouping to class
  * Max Cardinality changed from 1 to *

  
Coverage.class.type | 
  * **Added Mandatory Element**

  
Coverage.class.value | 
  * **Added Mandatory Element**

  
Coverage.class.name | 
  * Added Element

  
Coverage.costToBeneficiary | 
  * Added Element

  
Coverage.costToBeneficiary.type | 
  * Added Element

  
Coverage.costToBeneficiary.value[x] | 
  * **Added Mandatory Element**

  
Coverage.costToBeneficiary.exception | 
  * Added Element

  
Coverage.costToBeneficiary.exception.type | 
  * **Added Mandatory Element**

  
Coverage.costToBeneficiary.exception.period | 
  * Added Element

  
Coverage.subrogation | 
  * Added Element

  
Coverage.grouping.group | 
  * deleted

  
Coverage.grouping.groupDisplay | 
  * deleted

  
Coverage.grouping.subGroup | 
  * deleted

  
Coverage.grouping.subGroupDisplay | 
  * deleted

  
Coverage.grouping.plan | 
  * deleted

  
Coverage.grouping.planDisplay | 
  * deleted

  
Coverage.grouping.subPlan | 
  * deleted

  
Coverage.grouping.subPlanDisplay | 
  * deleted

  
Coverage.grouping.class | 
  * deleted

  
Coverage.grouping.classDisplay | 
  * deleted

  
Coverage.grouping.subClass | 
  * deleted

  
Coverage.grouping.subClassDisplay | 
  * deleted

  
Coverage.sequence | 
  * deleted

  
See the [Full Difference](diff.html) for further information
This analysis is available as [XML](coverage.diff.xml) or [JSON](coverage.diff.json). 
See [R3 <--> R4 Conversion Maps](coverage-version-maps.html) (status = 4 tests that all execute ok. 1 fail round-trip testing and all r3 resources are valid.)
See the [Profiles & Extensions](coverage-profiles.html) and the alternate definitions: Master Definition [XML](coverage.profile.xml.html) + [JSON](coverage.profile.json.html), [XML](xml.html) [Schema](coverage.xsd)/[Schematron](coverage.sch) + [JSON](json.html) [Schema](coverage.schema.json.html), [ShEx](coverage.shex.html) (for [Turtle](rdf.html)) + [see the extensions](coverage-profiles.html) & the [dependency analysis](coverage-dependencies.html)
###  13.1.3.1 Terminology Bindings [](coverage.html#tx "link to here")
Path | Definition | Type | Reference  
---|---|---|---  
Coverage.status  | A code specifying the state of the resource instance. | [Required](terminologies.html#required) |  [FinancialResourceStatusCodes](valueset-fm-status.html)  
Coverage.type  | The type of insurance: public health, worker compensation; private accident, auto, private health, etc.) or a direct payment by an individual or organization. | [Preferred](terminologies.html#preferred) |  [CoverageTypeAndSelf-PayCodes](valueset-coverage-type.html)  
Coverage.relationship  | The relationship between the Subscriber and the Beneficiary (insured/covered party/patient). | [Extensible](terminologies.html#extensible) |  [SubscriberRelationshipCodes](valueset-subscriber-relationship.html)  
Coverage.class.type  | The policy classifications, eg. Group, Plan, Class, etc. | [Extensible](terminologies.html#extensible) |  [CoverageClassCodes](valueset-coverage-class.html)  
Coverage.costToBeneficiary.type  | The types of services to which patient copayments are specified. | [Extensible](terminologies.html#extensible) |  [CoverageCopayTypeCodes](valueset-coverage-copay-type.html)  
Coverage.costToBeneficiary.exception.type  | The types of exceptions from the part or full value of financial obligations such as copays. | [Example](terminologies.html#example) |  [ExampleCoverageFinancialExceptionCodes](valueset-coverage-financial-exception.html)  
##  13.1.4 Search Parameters [](coverage.html#search "link to here")
Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.
**Name** | **Type** | **Description** | **Expression** | **In Common**  
---|---|---|---|---  
beneficiary | [reference](search.html#reference) | Covered party | Coverage.beneficiary  
([Patient](patient.html)) |   
class-type | [token](search.html#token) | Coverage class (eg. plan, group) | Coverage.class.type |   
class-value | [string](search.html#string) | Value of the class (eg. Plan number, group number) | Coverage.class.value |   
dependent | [string](search.html#string) | Dependent number | Coverage.dependent |   
identifier | [token](search.html#token) | The primary identifier of the insured and the coverage | Coverage.identifier |   
patient | [reference](search.html#reference) | Retrieve coverages for a patient | Coverage.beneficiary  
([Patient](patient.html)) |   
payor | [reference](search.html#reference) | The identity of the insurer or party paying for services | Coverage.payor  
([Organization](organization.html), [Patient](patient.html), [RelatedPerson](relatedperson.html)) |   
policy-holder | [reference](search.html#reference) | Reference to the policyholder | Coverage.policyHolder  
([Organization](organization.html), [Patient](patient.html), [RelatedPerson](relatedperson.html)) |   
status | [token](search.html#token) | The status of the Coverage | Coverage.status |   
subscriber | [reference](search.html#reference) | Reference to the subscriber | Coverage.subscriber  
([Patient](patient.html), [RelatedPerson](relatedperson.html)) |   
type | [token](search.html#token) | The kind of coverage (health plan, auto, Workers Compensation) | Coverage.type |   
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:34+1100. [QA Page](qa.html)   
Links: [Search ![](external.png)](http://hl7.org/fhir/search.cfm) | [Version History](history.html) | [Table of Contents](toc.html) | [Credits](credits.html) | [Compare to R3 ![](external.png)](http://services.w3.org/htmldiff?doc1=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fcoverage.html&doc2=http%3A%2F%2Fbuild.fhir.org%2Fcoverage.html) | [![CC0](cc0.png)](license.html) | [Propose a change ![](external.png)](http://hl7.org/fhir-issues)
