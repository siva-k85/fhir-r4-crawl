---
url: https://hl7.org/fhir/R4/implementationguide.html
title: implementationguide.html
source: official_download
extracted: local_file_conversion
mirror_path: implementationguide.html
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


  * [![](conformance.jpg) Conformance](conformance-module.html)
  * **ImplementationGuide**


**This page is part of a downloaded copy of this specification.** This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html)
  * [Content](#)
  * [Examples](implementationguide-examples.html)
  * [Detailed Descriptions](implementationguide-definitions.html)
  * [Mappings](implementationguide-mappings.html)
  * [Profiles & Extensions](implementationguide-profiles.html)
  * [R3 Conversions](implementationguide-version-maps.html)


#  5.8 Resource ImplementationGuide - Content [](implementationguide.html#5.8 "link to here")
[FHIR Infrastructure ![](external.png)](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group |  [Maturity Level](versions.html#maturity): 1 |  [Trial Use](versions.html#std-process "Standard Status") |  [Security Category](security.html#SecPrivConsiderations): Anonymous |  [Compartments](compartmentdefinition.html): Not linked to any defined compartments  
---|---|---|---|---  
A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.
##  5.8.1 Scope and Usage [](implementationguide.html#scope "link to here")
An implementation guide (IG) is a set of rules about how FHIR resources are used (or should be used) to solve a particular problem, with associated documentation to support and clarify the usage. Classically, FHIR implementation guides are published on the web after they are generated using the [FHIR Implementation Guide Publisher ![](external.png)](https://confluence.hl7.org/display/FHIR/IG+Publisher+Documentation). 
The `ImplementationGuide` resource is a single resource that defines the logical content of the IG, along with the important entry pages into the publication, so that the logical package that the IG represents, so that the contents are computable. 
In particular, validators are able to use the ImplementationGuide resource to validate content against the implementation guide as a whole. The significant conformance expectation introduced by the ImplementationGuide resource is the idea of [Default Profiles](#default). Implementations may conform to multiple implementation guides at once, but this requires that the implementation guides are compatible (see [below](#compatibility)). 
##  5.8.2 Boundaries and Relationships [](implementationguide.html#bnr "link to here")
Implementation Guides contain two different types of resource references: 
  * Contents: A set of logical statements which implementations must conform to. These are almost always [conformance resources](conformance-module.html)
  * Examples: Examples that illustrate the intent of the profiles defined in the implementation guide. These can be any kind of resource


An application's [Capability Statement](capabilitystatement.html) may identify one or more implementation guides that an application conforms to. 
This resource is referenced by [ElementDefinition](elementdefinition.html#ElementDefinition), [CapabilityStatement](capabilitystatement.html#CapabilityStatement) and itself
##  5.8.3 Resource Content [](implementationguide.html#resource "link to here")
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
![.](tbl_spacer.png)![.](icon_resource.png) [ImplementationGuide](implementationguide-definitions.html#ImplementationGuide "ImplementationGuide : A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.") |  [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A set of rules about how FHIR is used  
+ Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation  
+ Rule: If a resource has a fhirVersion, it must be oe of the versions defined for the Implementation Guide  
Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.

Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource \(including cannot change the meaning of modifierExtension itself\).")  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [url](implementationguide-definitions.html#ImplementationGuide.url "ImplementationGuide.url : An absolute URI that is used to identify this implementation guide when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this implementation guide is \(or will be\) published. This URL can be the target of a canonical reference. It SHALL remain the same when the implementation guide is stored on different servers.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [uri](datatypes.html#uri) | Canonical identifier for this implementation guide, represented as a URI (globally unique)  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [version](implementationguide-definitions.html#ImplementationGuide.version "ImplementationGuide.version : The identifier that is used to identify this version of the implementation guide when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the implementation guide author and is not expected to be globally unique. For example, it might be a timestamp \(e.g. yyyymmdd\) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Business version of the implementation guide  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](implementationguide-definitions.html#ImplementationGuide.name "ImplementationGuide.name : A natural language name identifying the implementation guide. This name should be usable as an identifier for the module by machine processing applications such as code generation.") |  [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..1 | [string](datatypes.html#string) | Name for this implementation guide (computer friendly)  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [title](implementationguide-definitions.html#ImplementationGuide.title "ImplementationGuide.title : A short, descriptive, user-friendly title for the implementation guide.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this implementation guide (human friendly)  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [status](implementationguide-definitions.html#ImplementationGuide.status "ImplementationGuide.status : The status of this implementation guide. Enables tracking the life-cycle of the content.") |  [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown  
[PublicationStatus](valueset-publication-status.html "The lifecycle status of an artifact.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [experimental](implementationguide-definitions.html#ImplementationGuide.experimental "ImplementationGuide.experimental : A Boolean value to indicate that this implementation guide is authored for testing purposes \(or education/evaluation/marketing\) and is not intended to be used for genuine usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [date](implementationguide-definitions.html#ImplementationGuide.date "ImplementationGuide.date : The date  \(and optionally time\) when the implementation guide was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the implementation guide changes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date last changed  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [publisher](implementationguide-definitions.html#ImplementationGuide.publisher "ImplementationGuide.publisher : The name of the organization or individual that published the implementation guide.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual)  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [contact](implementationguide-definitions.html#ImplementationGuide.contact "ImplementationGuide.contact : Contact details to assist a user in finding and communicating with the publisher.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [description](implementationguide-definitions.html#ImplementationGuide.description "ImplementationGuide.description : A free text natural language description of the implementation guide from a consumer's perspective.") |  | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the implementation guide  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [useContext](implementationguide-definitions.html#ImplementationGuide.useContext "ImplementationGuide.useContext : The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories \(gender, age, ...\) or may be references to specific programs \(insurance plans, studies, ...\) and may be used to assist with indexing and searching for appropriate implementation guide instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [jurisdiction](implementationguide-definitions.html#ImplementationGuide.jurisdiction "ImplementationGuide.jurisdiction : A legal or geographic region in which the implementation guide is intended to be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Intended jurisdiction for implementation guide (if applicable)  
[Jurisdiction](valueset-jurisdiction.html "Countries and regions within which this artifact is targeted for use.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [copyright](implementationguide-definitions.html#ImplementationGuide.copyright "ImplementationGuide.copyright : A copyright statement relating to the implementation guide and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the implementation guide.") |  | 0..1 | [markdown](datatypes.html#markdown) | Use and/or publishing restrictions  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [packageId](implementationguide-definitions.html#ImplementationGuide.packageId "ImplementationGuide.packageId : The NPM package name for this Implementation Guide, used in the NPM package distribution, which is the primary mechanism by which FHIR based tooling manages IG dependencies. This value must be globally unique, and should be assigned with care.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [id](datatypes.html#id) | NPM Package name for IG  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [license](implementationguide-definitions.html#ImplementationGuide.license "ImplementationGuide.license : The license that applies to this Implementation Guide, using an SPDX license code, or 'not-open-source'.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | SPDX license code for this IG (or not-open-source)  
[SPDXLicense](valueset-spdx-license.html "The license that applies to an Implementation Guide \(using an SPDX license Identifiers, or 'not-open-source'\). The binding is required but new SPDX license Identifiers are allowed to be used \(https://spdx.org/licenses/\).") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [fhirVersion](implementationguide-definitions.html#ImplementationGuide.fhirVersion "ImplementationGuide.fhirVersion : The version\(s\) of the FHIR specification that this ImplementationGuide targets - e.g. describes how to use. The value of this element is the formal version of the specification, without the revision number, e.g. \[publication\].\[major\].\[minor\], which is 4.0.1. for this version.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..* | [code](datatypes.html#code) | FHIR Version(s) this Implementation Guide targets  
[FHIRVersion](valueset-FHIR-version.html "All published FHIR Versions.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [dependsOn](implementationguide-definitions.html#ImplementationGuide.dependsOn "ImplementationGuide.dependsOn : Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guides.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [BackboneElement](backboneelement.html) | Another Implementation guide this depends on  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [uri](implementationguide-definitions.html#ImplementationGuide.dependsOn.uri "ImplementationGuide.dependsOn.uri : A canonical reference to the Implementation guide for the dependency.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [canonical](datatypes.html#canonical)([ImplementationGuide](implementationguide.html)) | Identity of the IG that this depends on  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [packageId](implementationguide-definitions.html#ImplementationGuide.dependsOn.packageId "ImplementationGuide.dependsOn.packageId : The NPM package name for the Implementation Guide that this IG depends on.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [id](datatypes.html#id) | NPM Package name for IG this depends on  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [version](implementationguide-definitions.html#ImplementationGuide.dependsOn.version "ImplementationGuide.dependsOn.version : The version of the IG that is depended on, when the correct version is required to understand the IG correctly.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Version of the IG  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [global](implementationguide-definitions.html#ImplementationGuide.global "ImplementationGuide.global : A set of profiles that all resources covered by this implementation guide must conform to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [BackboneElement](backboneelement.html) | Profiles that apply globally  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [type](implementationguide-definitions.html#ImplementationGuide.global.type "ImplementationGuide.global.type : The type of resource that all instances must conform to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | Type this profile applies to  
[ResourceType](valueset-resource-types.html "One of the resource types defined as part of this version of FHIR.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) [profile](implementationguide-definitions.html#ImplementationGuide.global.profile "ImplementationGuide.global.profile : A reference to the profile that all instances must conform to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Profile that all resources must conform to  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [definition](implementationguide-definitions.html#ImplementationGuide.definition "ImplementationGuide.definition : The information needed by an IG publisher tool to publish the whole implementation guide.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [BackboneElement](backboneelement.html) | Information needed to build the IG  
+ Rule: If a resource has a groupingId, it must refer to a grouping defined in the Implementation Guide  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_element.gif) [grouping](implementationguide-definitions.html#ImplementationGuide.definition.grouping "ImplementationGuide.definition.grouping : A logical group of resources. Logical groups can be used when building pages.") |  | 0..* | [BackboneElement](backboneelement.html) | Grouping used to present related resources in the IG  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](implementationguide-definitions.html#ImplementationGuide.definition.grouping.name "ImplementationGuide.definition.grouping.name : The human-readable title to display for the package of resources when rendering the implementation guide.") |  | 1..1 | [string](datatypes.html#string) | Descriptive name for the package  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [description](implementationguide-definitions.html#ImplementationGuide.definition.grouping.description "ImplementationGuide.definition.grouping.description : Human readable text describing the package.") |  | 0..1 | [string](datatypes.html#string) | Human readable text describing the package  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_element.gif) [resource](implementationguide-definitions.html#ImplementationGuide.definition.resource "ImplementationGuide.definition.resource : A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.") |  | 1..* | [BackboneElement](backboneelement.html) | Resource in the implementation guide  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [reference](implementationguide-definitions.html#ImplementationGuide.definition.resource.reference "ImplementationGuide.definition.resource.reference : Where this resource is found.") |  | 1..1 |  [Reference](references.html#Reference)([Any](resourcelist.html)) | Location of the resource  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [fhirVersion](implementationguide-definitions.html#ImplementationGuide.definition.resource.fhirVersion "ImplementationGuide.definition.resource.fhirVersion : Indicates the FHIR Version\(s\) this artifact is intended to apply to. If no versions are specified, the resource is assumed to apply to all the versions stated in ImplementationGuide.fhirVersion.") |  | 0..* | [code](datatypes.html#code) | Versions this applies to (if different to IG)  
[FHIRVersion](valueset-FHIR-version.html "All published FHIR Versions.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](implementationguide-definitions.html#ImplementationGuide.definition.resource.name "ImplementationGuide.definition.resource.name : A human assigned name for the resource. All resources SHOULD have a name, but the name may be extracted from the resource \(e.g. ValueSet.name\).") |  | 0..1 | [string](datatypes.html#string) | Human Name for the resource  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [description](implementationguide-definitions.html#ImplementationGuide.definition.resource.description "ImplementationGuide.definition.resource.description : A description of the reason that a resource has been included in the implementation guide.") |  | 0..1 | [string](datatypes.html#string) | Reason why included in guide  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_choice.gif) [example[x]](implementationguide-definitions.html#ImplementationGuide.definition.resource.example_x_ "ImplementationGuide.definition.resource.example\[x\] : If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") |  | 0..1 |  | Is an example/What is this an example of?  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) exampleBoolean |  |  | [boolean](datatypes.html#boolean) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) exampleCanonical |  |  |  [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [groupingId](implementationguide-definitions.html#ImplementationGuide.definition.resource.groupingId "ImplementationGuide.definition.resource.groupingId : Reference to the id of the grouping this resource appears in.") |  | 0..1 | [id](datatypes.html#id) | Grouping this is part of  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_element.gif) [page](implementationguide-definitions.html#ImplementationGuide.definition.page "ImplementationGuide.definition.page : A page / section in the implementation guide. The root page is the implementation guide home page.") |  | 0..1 | [BackboneElement](backboneelement.html) | Page/Section in the Guide  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_choice.gif) [name[x]](implementationguide-definitions.html#ImplementationGuide.definition.page.name_x_ "ImplementationGuide.definition.page.name\[x\] : The source address for the page.") |  | 1..1 |  | Where to find that page  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) nameUrl |  |  | [url](datatypes.html#url) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) nameReference |  |  |  [Reference](references.html#Reference)([Binary](http.html)) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [title](implementationguide-definitions.html#ImplementationGuide.definition.page.title "ImplementationGuide.definition.page.title : A short title used to represent this page in navigational structures such as table of contents, bread crumbs, etc.") |  | 1..1 | [string](datatypes.html#string) | Short title shown for navigational assistance  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [generation](implementationguide-definitions.html#ImplementationGuide.definition.page.generation "ImplementationGuide.definition.page.generation : A code that indicates how the page is generated.") |  | 1..1 | [code](datatypes.html#code) | html | markdown | xml | generated  
[GuidePageGeneration](valueset-guide-page-generation.html "A code that indicates how the page is generated.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reuse.png) [page](implementationguide-definitions.html#ImplementationGuide.definition.page.page "ImplementationGuide.definition.page.page : Nested Pages/Sections under this page.") |  | 0..* | see [page](#ImplementationGuide.definition.page "ImplementationGuide.definition.page") | Nested Pages / Sections  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_element.gif) [parameter](implementationguide-definitions.html#ImplementationGuide.definition.parameter "ImplementationGuide.definition.parameter : Defines how IG is built by tools.") |  | 0..* | [BackboneElement](backboneelement.html) | Defines how IG is built by tools  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [code](implementationguide-definitions.html#ImplementationGuide.definition.parameter.code "ImplementationGuide.definition.parameter.code : apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template.") |  | 1..1 | [code](datatypes.html#code) | apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template  
[GuideParameterCode](valueset-guide-parameter-code.html "Code of parameter that is input to the guide.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [value](implementationguide-definitions.html#ImplementationGuide.definition.parameter.value "ImplementationGuide.definition.parameter.value : Value for named type.") |  | 1..1 | [string](datatypes.html#string) | Value for named type  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [template](implementationguide-definitions.html#ImplementationGuide.definition.template "ImplementationGuide.definition.template : A template for building resources.") |  | 0..* | [BackboneElement](backboneelement.html) | A template for building resources  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [code](implementationguide-definitions.html#ImplementationGuide.definition.template.code "ImplementationGuide.definition.template.code : Type of template specified.") |  | 1..1 | [code](datatypes.html#code) | Type of template specified  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [source](implementationguide-definitions.html#ImplementationGuide.definition.template.source "ImplementationGuide.definition.template.source : The source location for the template.") |  | 1..1 | [string](datatypes.html#string) | The source location for the template  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [scope](implementationguide-definitions.html#ImplementationGuide.definition.template.scope "ImplementationGuide.definition.template.scope : The scope in which the template applies.") |  | 0..1 | [string](datatypes.html#string) | The scope in which the template applies  
![.](tbl_spacer.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [manifest](implementationguide-definitions.html#ImplementationGuide.manifest "ImplementationGuide.manifest : Information about an assembled implementation guide, created by the publication tooling.") |  | 0..1 | [BackboneElement](backboneelement.html) | Information about an assembled IG  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [rendering](implementationguide-definitions.html#ImplementationGuide.manifest.rendering "ImplementationGuide.manifest.rendering : A pointer to official web page, PDF or other rendering of the implementation guide.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [url](datatypes.html#url) | Location of rendered implementation guide  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_element.gif) [resource](implementationguide-definitions.html#ImplementationGuide.manifest.resource "ImplementationGuide.manifest.resource : A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..* | [BackboneElement](backboneelement.html) | Resource in the implementation guide  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [reference](implementationguide-definitions.html#ImplementationGuide.manifest.resource.reference "ImplementationGuide.manifest.resource.reference : Where this resource is found.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [Reference](references.html#Reference)([Any](resourcelist.html)) | Location of the resource  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_choice.gif) [example[x]](implementationguide-definitions.html#ImplementationGuide.manifest.resource.example_x_ "ImplementationGuide.manifest.resource.example\[x\] : If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") |  | 0..1 |  | Is an example/What is this an example of?  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) exampleBoolean |  |  | [boolean](datatypes.html#boolean) |   
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) exampleCanonical |  |  |  [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) |   
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [relativePath](implementationguide-definitions.html#ImplementationGuide.manifest.resource.relativePath "ImplementationGuide.manifest.resource.relativePath : The relative path for primary page for this resource within the IG.") |  | 0..1 | [url](datatypes.html#url) | Relative path for page in IG  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_element.gif) [page](implementationguide-definitions.html#ImplementationGuide.manifest.page "ImplementationGuide.manifest.page : Information about a page within the IG.") |  | 0..* | [BackboneElement](backboneelement.html) | HTML page within the parent IG  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](implementationguide-definitions.html#ImplementationGuide.manifest.page.name "ImplementationGuide.manifest.page.name : Relative path to the page.") |  | 1..1 | [string](datatypes.html#string) | HTML page name  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [title](implementationguide-definitions.html#ImplementationGuide.manifest.page.title "ImplementationGuide.manifest.page.title : Label for the page intended for human display.") |  | 0..1 | [string](datatypes.html#string) | Title of the page, for references  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [anchor](implementationguide-definitions.html#ImplementationGuide.manifest.page.anchor "ImplementationGuide.manifest.page.anchor : The name of an anchor available on the page.") |  | 0..* | [string](datatypes.html#string) | Anchor available on the page  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [image](implementationguide-definitions.html#ImplementationGuide.manifest.image "ImplementationGuide.manifest.image : Indicates a relative path to an image that exists within the IG.") |  | 0..* | [string](datatypes.html#string) | Image within the IG  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [other](implementationguide-definitions.html#ImplementationGuide.manifest.other "ImplementationGuide.manifest.other : Indicates the relative path of an additional non-page, non-image file that is part of the IG - e.g. zip, jar and similar files that could be the target of a hyperlink in a derived IG.") |  | 0..* | [string](datatypes.html#string) | Additional linkable file in IG  
  
  
[![doco](help16.png) Documentation for this format](formats.html#table "Legend for this format")  
**UML Diagram** ([Legend](formats.html#uml))
ImplementationGuide (DomainResource)An absolute URI that is used to identify this implementation guide when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this implementation guide is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the implementation guide is stored on different serversurl : uri [1..1]The identifier that is used to identify this version of the implementation guide when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the implementation guide author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequenceversion : string [0..1]A natural language name identifying the implementation guide. This name should be usable as an identifier for the module by machine processing applications such as code generationname : string [1..1]A short, descriptive, user-friendly title for the implementation guidetitle : string [0..1]The status of this implementation guide. Enables tracking the life-cycle of the content (this element modifies the meaning of other elements)status : code [1..1] « The lifecycle status of an artifact. (Strength=Required)PublicationStatus! »A Boolean value to indicate that this implementation guide is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usageexperimental : boolean [0..1]The date (and optionally time) when the implementation guide was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the implementation guide changesdate : dateTime [0..1]The name of the organization or individual that published the implementation guidepublisher : string [0..1]Contact details to assist a user in finding and communicating with the publishercontact : ContactDetail [0..*]A free text natural language description of the implementation guide from a consumer's perspectivedescription : markdown [0..1]The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate implementation guide instancesuseContext : UsageContext [0..*]A legal or geographic region in which the implementation guide is intended to be usedjurisdiction : CodeableConcept [0..*] « Countries and regions within which this artifact is targeted for use. (Strength=Extensible)Jurisdiction ValueSet+ »A copyright statement relating to the implementation guide and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the implementation guidecopyright : markdown [0..1]The NPM package name for this Implementation Guide, used in the NPM package distribution, which is the primary mechanism by which FHIR based tooling manages IG dependencies. This value must be globally unique, and should be assigned with carepackageId : id [1..1]The license that applies to this Implementation Guide, using an SPDX license code, or 'not-open-source'license : code [0..1] « The license that applies to an Implementation Guide (using an SPDX license Identifiers, or 'not-open-source'). The binding is required but new SPDX license Identifiers are allowed to be used (https://spdx.org/licenses/). (Strength=Required)SPDXLicense! »The version(s) of the FHIR specification that this ImplementationGuide targets - e.g. describes how to use. The value of this element is the formal version of the specification, without the revision number, e.g. [publication].[major].[minor], which is 4.0.1. for this versionfhirVersion : code [1..*] « All published FHIR Versions. (Strength=Required)FHIRVersion! »DependsOnA canonical reference to the Implementation guide for the dependencyuri : canonical [1..1] « ImplementationGuide »The NPM package name for the Implementation Guide that this IG depends onpackageId : id [0..1]The version of the IG that is depended on, when the correct version is required to understand the IG correctlyversion : string [0..1]GlobalThe type of resource that all instances must conform totype : code [1..1] « One of the resource types defined as part of this version of FHIR. (Strength=Required)ResourceType! »A reference to the profile that all instances must conform toprofile : canonical [1..1] « StructureDefinition »DefinitionGroupingThe human-readable title to display for the package of resources when rendering the implementation guidename : string [1..1]Human readable text describing the packagedescription : string [0..1]ResourceWhere this resource is foundreference : Reference [1..1] « Any »Indicates the FHIR Version(s) this artifact is intended to apply to. If no versions are specified, the resource is assumed to apply to all the versions stated in ImplementationGuide.fhirVersionfhirVersion : code [0..*] « All published FHIR Versions. (Strength=Required)FHIRVersion! »A human assigned name for the resource. All resources SHOULD have a name, but the name may be extracted from the resource (e.g. ValueSet.name)name : string [0..1]A description of the reason that a resource has been included in the implementation guidedescription : string [0..1]If true or a reference, indicates the resource is an example instance. If a reference is present, indicates that the example is an example of the specified profileexample[x] : Type [0..1] « boolean|canonical(StructureDefinition) »Reference to the id of the grouping this resource appears ingroupingId : id [0..1]PageThe source address for the pagename[x] : Type [1..1] « url|Reference(Binary) »A short title used to represent this page in navigational structures such as table of contents, bread crumbs, etctitle : string [1..1]A code that indicates how the page is generatedgeneration : code [1..1] « A code that indicates how the page is generated. (Strength=Required)GuidePageGeneration! »Parameterapply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-templatecode : code [1..1] « Code of parameter that is input to the guide. (Strength=Required)GuideParameterCode! »Value for named typevalue : string [1..1]TemplateType of template specifiedcode : code [1..1]The source location for the templatesource : string [1..1]The scope in which the template appliesscope : string [0..1]ManifestA pointer to official web page, PDF or other rendering of the implementation guiderendering : url [0..1]Indicates a relative path to an image that exists within the IGimage : string [0..*]Indicates the relative path of an additional non-page, non-image file that is part of the IG - e.g. zip, jar and similar files that could be the target of a hyperlink in a derived IGother : string [0..*]ManifestResourceWhere this resource is foundreference : Reference [1..1] « Any »If true or a reference, indicates the resource is an example instance. If a reference is present, indicates that the example is an example of the specified profileexample[x] : Type [0..1] « boolean|canonical(StructureDefinition) »The relative path for primary page for this resource within the IGrelativePath : url [0..1]ManifestPageRelative path to the pagename : string [1..1]Label for the page intended for human displaytitle : string [0..1]The name of an anchor available on the pageanchor : string [0..*]Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guidesdependsOn[0..*]A set of profiles that all resources covered by this implementation guide must conform toglobal[0..*]A logical group of resources. Logical groups can be used when building pagesgrouping[0..*]A resource that is part of the implementation guide. Conformance resources (value set, structure definition, capability statements etc.) are obvious candidates for inclusion, but any kind of resource can be included as an example resourceresource[1..*]Nested Pages/Sections under this pagepage[0..*]A page / section in the implementation guide. The root page is the implementation guide home pagepage[0..1]Defines how IG is built by toolsparameter[0..*]A template for building resourcestemplate[0..*]The information needed by an IG publisher tool to publish the whole implementation guidedefinition[0..1]A resource that is part of the implementation guide. Conformance resources (value set, structure definition, capability statements etc.) are obvious candidates for inclusion, but any kind of resource can be included as an example resourceresource[1..*]Information about a page within the IGpage[0..*]Information about an assembled implementation guide, created by the publication toolingmanifest[0..1]
**XML Template**
```

<[**ImplementationGuide**](implementationguide-definitions.html#ImplementationGuide "A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.") xmlns="http://hl7.org/fhir"> [![doco](help.png)](xml.html "Documentation for this format")
 <!-- from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language) -->
 <!-- from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension) -->
 <[**url**](implementationguide-definitions.html#ImplementationGuide.url "An absolute URI that is used to identify this implementation guide when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this implementation guide is \(or will be\) published. This URL can be the target of a canonical reference. It SHALL remain the same when the implementation guide is stored on different servers.") value="[uri[](datatypes.html#uri)]"/><!-- **1..1** Canonical identifier for this implementation guide, represented as a URI (globally unique)[](terminologies.html#unbound) -->
 <[**version**](implementationguide-definitions.html#ImplementationGuide.version "The identifier that is used to identify this version of the implementation guide when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the implementation guide author and is not expected to be globally unique. For example, it might be a timestamp \(e.g. yyyymmdd\) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Business version of the implementation guide[](terminologies.html#unbound) -->
 <[**name**](implementationguide-definitions.html#ImplementationGuide.name "A natural language name identifying the implementation guide. This name should be usable as an identifier for the module by machine processing applications such as code generation.") value="[string[](datatypes.html#string)]"/><!-- **![??](lock.png) 1..1** Name for this implementation guide (computer friendly)[](terminologies.html#unbound) -->
 <[**title**](implementationguide-definitions.html#ImplementationGuide.title "A short, descriptive, user-friendly title for the implementation guide.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Name for this implementation guide (human friendly)[](terminologies.html#unbound) -->
 <[**status**](implementationguide-definitions.html#ImplementationGuide.status "The status of this implementation guide. Enables tracking the life-cycle of the content \(this element modifies the meaning of other elements\)") value="[code[](datatypes.html#code)]"/><!-- **1..1** draft | active | retired | unknown[](valueset-publication-status.html) -->
 <[**experimental**](implementationguide-definitions.html#ImplementationGuide.experimental "A Boolean value to indicate that this implementation guide is authored for testing purposes \(or education/evaluation/marketing\) and is not intended to be used for genuine usage.") value="[boolean[](datatypes.html#boolean)]"/><!-- **0..1** For testing purposes, not real usage[](terminologies.html#unbound) -->
 <[**date**](implementationguide-definitions.html#ImplementationGuide.date "The date  \(and optionally time\) when the implementation guide was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the implementation guide changes.") value="[dateTime[](datatypes.html#dateTime)]"/><!-- **0..1** Date last changed[](terminologies.html#unbound) -->
 <[**publisher**](implementationguide-definitions.html#ImplementationGuide.publisher "The name of the organization or individual that published the implementation guide.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Name of the publisher (organization or individual)[](terminologies.html#unbound) -->
 <[**contact**](implementationguide-definitions.html#ImplementationGuide.contact "Contact details to assist a user in finding and communicating with the publisher.")><!-- **0..*** ContactDetail[](metadatatypes.html#ContactDetail) Contact details for the publisher[](terminologies.html#unbound) --></contact>
 <[**description**](implementationguide-definitions.html#ImplementationGuide.description "A free text natural language description of the implementation guide from a consumer's perspective.") value="[markdown[](datatypes.html#markdown)]"/><!-- **0..1** Natural language description of the implementation guide[](terminologies.html#unbound) -->
 <[**useContext**](implementationguide-definitions.html#ImplementationGuide.useContext "The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories \(gender, age, ...\) or may be references to specific programs \(insurance plans, studies, ...\) and may be used to assist with indexing and searching for appropriate implementation guide instances.")><!-- **0..*** UsageContext[](metadatatypes.html#UsageContext) The context that the content is intended to support[](terminologies.html#unbound) --></useContext>
 <[**jurisdiction**](implementationguide-definitions.html#ImplementationGuide.jurisdiction "A legal or geographic region in which the implementation guide is intended to be used.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) Intended jurisdiction for implementation guide (if applicable)[](valueset-jurisdiction.html) --></jurisdiction>
 <[**copyright**](implementationguide-definitions.html#ImplementationGuide.copyright "A copyright statement relating to the implementation guide and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the implementation guide.") value="[markdown[](datatypes.html#markdown)]"/><!-- **0..1** Use and/or publishing restrictions[](terminologies.html#unbound) -->
 <[**packageId**](implementationguide-definitions.html#ImplementationGuide.packageId "The NPM package name for this Implementation Guide, used in the NPM package distribution, which is the primary mechanism by which FHIR based tooling manages IG dependencies. This value must be globally unique, and should be assigned with care.") value="[id[](datatypes.html#id)]"/><!-- **1..1** NPM Package name for IG[](terminologies.html#unbound) -->
 <[**license**](implementationguide-definitions.html#ImplementationGuide.license "The license that applies to this Implementation Guide, using an SPDX license code, or 'not-open-source'.") value="[code[](datatypes.html#code)]"/><!-- **0..1** SPDX license code for this IG (or not-open-source)[](valueset-spdx-license.html) -->
 <[**fhirVersion**](implementationguide-definitions.html#ImplementationGuide.fhirVersion "The version\(s\) of the FHIR specification that this ImplementationGuide targets - e.g. describes how to use. The value of this element is the formal version of the specification, without the revision number, e.g. \[publication\].\[major\].\[minor\], which is 4.0.1. for this version.") value="[code[](datatypes.html#code)]"/><!-- **1..*** FHIR Version(s) this Implementation Guide targets[](valueset-FHIR-version.html) -->
 <[**dependsOn**](implementationguide-definitions.html#ImplementationGuide.dependsOn "Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guides.")>  <!-- **0..*** Another Implementation guide this depends on -->
  <[**uri**](implementationguide-definitions.html#ImplementationGuide.dependsOn.uri "A canonical reference to the Implementation guide for the dependency.")><!-- **1..1** canonical[](datatypes.html#canonical)(ImplementationGuide[](implementationguide.html#ImplementationGuide)) Identity of the IG that this depends on[](terminologies.html#unbound) --></uri>
  <[**packageId**](implementationguide-definitions.html#ImplementationGuide.dependsOn.packageId "The NPM package name for the Implementation Guide that this IG depends on.") value="[id[](datatypes.html#id)]"/><!-- **0..1** NPM Package name for IG this depends on[](terminologies.html#unbound) -->
  <[**version**](implementationguide-definitions.html#ImplementationGuide.dependsOn.version "The version of the IG that is depended on, when the correct version is required to understand the IG correctly.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Version of the IG[](terminologies.html#unbound) -->
 </dependsOn>
 <[**global**](implementationguide-definitions.html#ImplementationGuide.global "A set of profiles that all resources covered by this implementation guide must conform to.")>  <!-- **0..*** Profiles that apply globally -->
  <[**type**](implementationguide-definitions.html#ImplementationGuide.global.type "The type of resource that all instances must conform to.") value="[code[](datatypes.html#code)]"/><!-- **1..1** Type this profile applies to[](valueset-resource-types.html) -->
  <[**profile**](implementationguide-definitions.html#ImplementationGuide.global.profile "A reference to the profile that all instances must conform to.")><!-- **1..1** canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) Profile that all resources must conform to[](terminologies.html#unbound) --></profile>
 </global>
 <[**definition**](implementationguide-definitions.html#ImplementationGuide.definition "The information needed by an IG publisher tool to publish the whole implementation guide.")>  <!-- **0..1** Information needed to build the IG -->
  <[**grouping**](implementationguide-definitions.html#ImplementationGuide.definition.grouping "A logical group of resources. Logical groups can be used when building pages.")>  <!-- **0..*** Grouping used to present related resources in the IG -->
   <[**name**](implementationguide-definitions.html#ImplementationGuide.definition.grouping.name "The human-readable title to display for the package of resources when rendering the implementation guide.") value="[string[](datatypes.html#string)]"/><!-- **1..1** Descriptive name for the package[](terminologies.html#unbound) -->
   <[**description**](implementationguide-definitions.html#ImplementationGuide.definition.grouping.description "Human readable text describing the package.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Human readable text describing the package[](terminologies.html#unbound) -->
  </grouping>
  <[**resource**](implementationguide-definitions.html#ImplementationGuide.definition.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.")>  <!-- **1..*** Resource in the implementation guide -->
   <[**reference**](implementationguide-definitions.html#ImplementationGuide.definition.resource.reference "Where this resource is found.")><!-- **1..1** Reference[](references.html#Reference)(Any[](resourcelist.html)) Location of the resource[](terminologies.html#unbound) --></reference>
   <[**fhirVersion**](implementationguide-definitions.html#ImplementationGuide.definition.resource.fhirVersion "Indicates the FHIR Version\(s\) this artifact is intended to apply to. If no versions are specified, the resource is assumed to apply to all the versions stated in ImplementationGuide.fhirVersion.") value="[code[](datatypes.html#code)]"/><!-- **0..*** Versions this applies to (if different to IG)[](valueset-FHIR-version.html) -->
   <[**name**](implementationguide-definitions.html#ImplementationGuide.definition.resource.name "A human assigned name for the resource. All resources SHOULD have a name, but the name may be extracted from the resource \(e.g. ValueSet.name\).") value="[string[](datatypes.html#string)]"/><!-- **0..1** Human Name for the resource[](terminologies.html#unbound) -->
   <[**description**](implementationguide-definitions.html#ImplementationGuide.definition.resource.description "A description of the reason that a resource has been included in the implementation guide.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Reason why included in guide[](terminologies.html#unbound) -->
   <[**example[x]**](implementationguide-definitions.html#ImplementationGuide.definition.resource.example\[x\] "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")><!-- **0..1** boolean[](datatypes.html#boolean)|canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) Is an example/What is this an example of?[](terminologies.html#unbound) --></example[x]>
   <[**groupingId**](implementationguide-definitions.html#ImplementationGuide.definition.resource.groupingId "Reference to the id of the grouping this resource appears in.") value="[id[](datatypes.html#id)]"/><!-- **0..1** Grouping this is part of[](terminologies.html#unbound) -->
  </resource>
  <[**page**](implementationguide-definitions.html#ImplementationGuide.definition.page "A page / section in the implementation guide. The root page is the implementation guide home page.")>  <!-- **0..1** Page/Section in the Guide -->
   <[**name[x]**](implementationguide-definitions.html#ImplementationGuide.definition.page.name\[x\] "The source address for the page.")><!-- **1..1** url[](datatypes.html#url)|Reference[](references.html#Reference)(Binary[](binary.html#Binary)) Where to find that page[](terminologies.html#unbound) --></name[x]>
   <[**title**](implementationguide-definitions.html#ImplementationGuide.definition.page.title "A short title used to represent this page in navigational structures such as table of contents, bread crumbs, etc.") value="[string[](datatypes.html#string)]"/><!-- **1..1** Short title shown for navigational assistance[](terminologies.html#unbound) -->
   <[**generation**](implementationguide-definitions.html#ImplementationGuide.definition.page.generation "A code that indicates how the page is generated.") value="[code[](datatypes.html#code)]"/><!-- **1..1** html | markdown | xml | generated[](valueset-guide-page-generation.html) -->
   <[**page**](implementationguide-definitions.html#ImplementationGuide.definition.page.page "Nested Pages/Sections under this page.")><!-- **0..*** Content as for ImplementationGuide.definition.page Nested Pages / Sections[](terminologies.html#unbound) --></page>
  </page>
  <[**parameter**](implementationguide-definitions.html#ImplementationGuide.definition.parameter "Defines how IG is built by tools.")>  <!-- **0..*** Defines how IG is built by tools -->
   <[**code**](implementationguide-definitions.html#ImplementationGuide.definition.parameter.code "apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template.") value="[code[](datatypes.html#code)]"/><!-- **1..1** apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template[](valueset-guide-parameter-code.html) -->
   <[**value**](implementationguide-definitions.html#ImplementationGuide.definition.parameter.value "Value for named type.") value="[string[](datatypes.html#string)]"/><!-- **1..1** Value for named type[](terminologies.html#unbound) -->
  </parameter>
  <[**template**](implementationguide-definitions.html#ImplementationGuide.definition.template "A template for building resources.")>  <!-- **0..*** A template for building resources -->
   <[**code**](implementationguide-definitions.html#ImplementationGuide.definition.template.code "Type of template specified.") value="[code[](datatypes.html#code)]"/><!-- **1..1** Type of template specified[](terminologies.html#unbound) -->
   <[**source**](implementationguide-definitions.html#ImplementationGuide.definition.template.source "The source location for the template.") value="[string[](datatypes.html#string)]"/><!-- **1..1** The source location for the template[](terminologies.html#unbound) -->
   <[**scope**](implementationguide-definitions.html#ImplementationGuide.definition.template.scope "The scope in which the template applies.") value="[string[](datatypes.html#string)]"/><!-- **0..1** The scope in which the template applies[](terminologies.html#unbound) -->
  </template>
 </definition>
 <[**manifest**](implementationguide-definitions.html#ImplementationGuide.manifest "Information about an assembled implementation guide, created by the publication tooling.")>  <!-- **0..1** Information about an assembled IG -->
  <[**rendering**](implementationguide-definitions.html#ImplementationGuide.manifest.rendering "A pointer to official web page, PDF or other rendering of the implementation guide.") value="[url[](datatypes.html#url)]"/><!-- **0..1** Location of rendered implementation guide[](terminologies.html#unbound) -->
  <[**resource**](implementationguide-definitions.html#ImplementationGuide.manifest.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.")>  <!-- **1..*** Resource in the implementation guide -->
   <[**reference**](implementationguide-definitions.html#ImplementationGuide.manifest.resource.reference "Where this resource is found.")><!-- **1..1** Reference[](references.html#Reference)(Any[](resourcelist.html)) Location of the resource[](terminologies.html#unbound) --></reference>
   <[**example[x]**](implementationguide-definitions.html#ImplementationGuide.manifest.resource.example\[x\] "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")><!-- **0..1** boolean[](datatypes.html#boolean)|canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) Is an example/What is this an example of?[](terminologies.html#unbound) --></example[x]>
   <[**relativePath**](implementationguide-definitions.html#ImplementationGuide.manifest.resource.relativePath "The relative path for primary page for this resource within the IG.") value="[url[](datatypes.html#url)]"/><!-- **0..1** Relative path for page in IG[](terminologies.html#unbound) -->
  </resource>
  <[**page**](implementationguide-definitions.html#ImplementationGuide.manifest.page "Information about a page within the IG.")>  <!-- **0..*** HTML page within the parent IG -->
   <[**name**](implementationguide-definitions.html#ImplementationGuide.manifest.page.name "Relative path to the page.") value="[string[](datatypes.html#string)]"/><!-- **1..1** HTML page name[](terminologies.html#unbound) -->
   <[**title**](implementationguide-definitions.html#ImplementationGuide.manifest.page.title "Label for the page intended for human display.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Title of the page, for references[](terminologies.html#unbound) -->
   <[**anchor**](implementationguide-definitions.html#ImplementationGuide.manifest.page.anchor "The name of an anchor available on the page.") value="[string[](datatypes.html#string)]"/><!-- **0..*** Anchor available on the page[](terminologies.html#unbound) -->
  </page>
  <[**image**](implementationguide-definitions.html#ImplementationGuide.manifest.image "Indicates a relative path to an image that exists within the IG.") value="[string[](datatypes.html#string)]"/><!-- **0..*** Image within the IG[](terminologies.html#unbound) -->
  <[**other**](implementationguide-definitions.html#ImplementationGuide.manifest.other "Indicates the relative path of an additional non-page, non-image file that is part of the IG - e.g. zip, jar and similar files that could be the target of a hyperlink in a derived IG.") value="[string[](datatypes.html#string)]"/><!-- **0..*** Additional linkable file in IG[](terminologies.html#unbound) -->
 </manifest>
</ImplementationGuide>

```

**JSON Template**
```

{[![doco](help.png)](json.html "Documentation for this format")
  "resourceType" : "[**ImplementationGuide**](implementationguide-definitions.html#ImplementationGuide "A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.")",
  // from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language)
  // from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension)
  "url[](implementationguide-definitions.html#ImplementationGuide.url "An absolute URI that is used to identify this implementation guide when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this implementation guide is \(or will be\) published. This URL can be the target of a canonical reference. It SHALL remain the same when the implementation guide is stored on different servers.")" : "<uri[](datatypes.html#uri)>", // **R!**  Canonical identifier for this implementation guide, represented as a URI (globally unique)[](terminologies.html#unbound)
  "version[](implementationguide-definitions.html#ImplementationGuide.version "The identifier that is used to identify this version of the implementation guide when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the implementation guide author and is not expected to be globally unique. For example, it might be a timestamp \(e.g. yyyymmdd\) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.")" : "<string[](datatypes.html#string)>", // Business version of the implementation guide[](terminologies.html#unbound)
  "name[](implementationguide-definitions.html#ImplementationGuide.name "A natural language name identifying the implementation guide. This name should be usable as an identifier for the module by machine processing applications such as code generation.")" : "<string[](datatypes.html#string)>", // **C?** **R!**  Name for this implementation guide (computer friendly)[](terminologies.html#unbound)
  "title[](implementationguide-definitions.html#ImplementationGuide.title "A short, descriptive, user-friendly title for the implementation guide.")" : "<string[](datatypes.html#string)>", // Name for this implementation guide (human friendly)[](terminologies.html#unbound)
  "[status](implementationguide-definitions.html#ImplementationGuide.status "The status of this implementation guide. Enables tracking the life-cycle of the content \(this element modifies the meaning of other elements\)")" : "<code[](datatypes.html#code)>", // **R!**  draft | active | retired | unknown[](valueset-publication-status.html)
  "experimental[](implementationguide-definitions.html#ImplementationGuide.experimental "A Boolean value to indicate that this implementation guide is authored for testing purposes \(or education/evaluation/marketing\) and is not intended to be used for genuine usage.")" : <boolean[](datatypes.html#boolean)>, // For testing purposes, not real usage[](terminologies.html#unbound)
  "date[](implementationguide-definitions.html#ImplementationGuide.date "The date  \(and optionally time\) when the implementation guide was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the implementation guide changes.")" : "<dateTime[](datatypes.html#dateTime)>", // Date last changed[](terminologies.html#unbound)
  "publisher[](implementationguide-definitions.html#ImplementationGuide.publisher "The name of the organization or individual that published the implementation guide.")" : "<string[](datatypes.html#string)>", // Name of the publisher (organization or individual)[](terminologies.html#unbound)
  "contact[](implementationguide-definitions.html#ImplementationGuide.contact "Contact details to assist a user in finding and communicating with the publisher.")" : [{ ContactDetail[](metadatatypes.html#ContactDetail) }], // Contact details for the publisher[](terminologies.html#unbound)
  "description[](implementationguide-definitions.html#ImplementationGuide.description "A free text natural language description of the implementation guide from a consumer's perspective.")" : "<markdown[](datatypes.html#markdown)>", // Natural language description of the implementation guide[](terminologies.html#unbound)
  "useContext[](implementationguide-definitions.html#ImplementationGuide.useContext "The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories \(gender, age, ...\) or may be references to specific programs \(insurance plans, studies, ...\) and may be used to assist with indexing and searching for appropriate implementation guide instances.")" : [{ UsageContext[](metadatatypes.html#UsageContext) }], // The context that the content is intended to support[](terminologies.html#unbound)
  "jurisdiction[](implementationguide-definitions.html#ImplementationGuide.jurisdiction "A legal or geographic region in which the implementation guide is intended to be used.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // Intended jurisdiction for implementation guide (if applicable)[](valueset-jurisdiction.html)
  "copyright[](implementationguide-definitions.html#ImplementationGuide.copyright "A copyright statement relating to the implementation guide and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the implementation guide.")" : "<markdown[](datatypes.html#markdown)>", // Use and/or publishing restrictions[](terminologies.html#unbound)
  "packageId[](implementationguide-definitions.html#ImplementationGuide.packageId "The NPM package name for this Implementation Guide, used in the NPM package distribution, which is the primary mechanism by which FHIR based tooling manages IG dependencies. This value must be globally unique, and should be assigned with care.")" : "<id[](datatypes.html#id)>", // **R!**  NPM Package name for IG[](terminologies.html#unbound)
  "license[](implementationguide-definitions.html#ImplementationGuide.license "The license that applies to this Implementation Guide, using an SPDX license code, or 'not-open-source'.")" : "<code[](datatypes.html#code)>", // SPDX license code for this IG (or not-open-source)[](valueset-spdx-license.html)
  "fhirVersion[](implementationguide-definitions.html#ImplementationGuide.fhirVersion "The version\(s\) of the FHIR specification that this ImplementationGuide targets - e.g. describes how to use. The value of this element is the formal version of the specification, without the revision number, e.g. \[publication\].\[major\].\[minor\], which is 4.0.1. for this version.")" : ["<code[](datatypes.html#code)>"], // **R!**  FHIR Version(s) this Implementation Guide targets[](valueset-FHIR-version.html)
  "dependsOn[](implementationguide-definitions.html#ImplementationGuide.dependsOn "Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guides.")" : [{ // Another Implementation guide this depends on[](terminologies.html#unbound)
    "uri[](implementationguide-definitions.html#ImplementationGuide.dependsOn.uri "A canonical reference to the Implementation guide for the dependency.")" : { canonical[](datatypes.html#canonical)(ImplementationGuide[](implementationguide.html#ImplementationGuide)) }, // **R!**  Identity of the IG that this depends on[](terminologies.html#unbound)
    "packageId[](implementationguide-definitions.html#ImplementationGuide.dependsOn.packageId "The NPM package name for the Implementation Guide that this IG depends on.")" : "<id[](datatypes.html#id)>", // NPM Package name for IG this depends on[](terminologies.html#unbound)
    "version[](implementationguide-definitions.html#ImplementationGuide.dependsOn.version "The version of the IG that is depended on, when the correct version is required to understand the IG correctly.")" : "<string[](datatypes.html#string)>" // Version of the IG[](terminologies.html#unbound)
  }],
  "global[](implementationguide-definitions.html#ImplementationGuide.global "A set of profiles that all resources covered by this implementation guide must conform to.")" : [{ // Profiles that apply globally[](terminologies.html#unbound)
    "type[](implementationguide-definitions.html#ImplementationGuide.global.type "The type of resource that all instances must conform to.")" : "<code[](datatypes.html#code)>", // **R!**  Type this profile applies to[](valueset-resource-types.html)
    "profile[](implementationguide-definitions.html#ImplementationGuide.global.profile "A reference to the profile that all instances must conform to.")" : { canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) } // **R!**  Profile that all resources must conform to[](terminologies.html#unbound)
  }],
  "definition[](implementationguide-definitions.html#ImplementationGuide.definition "The information needed by an IG publisher tool to publish the whole implementation guide.")" : { // Information needed to build the IG[](terminologies.html#unbound)
    "grouping[](implementationguide-definitions.html#ImplementationGuide.definition.grouping "A logical group of resources. Logical groups can be used when building pages.")" : [{ // Grouping used to present related resources in the IG[](terminologies.html#unbound)
      "name[](implementationguide-definitions.html#ImplementationGuide.definition.grouping.name "The human-readable title to display for the package of resources when rendering the implementation guide.")" : "<string[](datatypes.html#string)>", // **R!**  Descriptive name for the package[](terminologies.html#unbound)
      "description[](implementationguide-definitions.html#ImplementationGuide.definition.grouping.description "Human readable text describing the package.")" : "<string[](datatypes.html#string)>" // Human readable text describing the package[](terminologies.html#unbound)
    }],
    "resource[](implementationguide-definitions.html#ImplementationGuide.definition.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.")" : [{ // **R!**  Resource in the implementation guide[](terminologies.html#unbound)
      "reference[](implementationguide-definitions.html#ImplementationGuide.definition.resource.reference "Where this resource is found.")" : { Reference[](references.html#Reference)(Any[](resourcelist.html)) }, // **R!**  Location of the resource[](terminologies.html#unbound)
      "fhirVersion[](implementationguide-definitions.html#ImplementationGuide.definition.resource.fhirVersion "Indicates the FHIR Version\(s\) this artifact is intended to apply to. If no versions are specified, the resource is assumed to apply to all the versions stated in ImplementationGuide.fhirVersion.")" : ["<code[](datatypes.html#code)>"], // Versions this applies to (if different to IG)[](valueset-FHIR-version.html)
      "name[](implementationguide-definitions.html#ImplementationGuide.definition.resource.name "A human assigned name for the resource. All resources SHOULD have a name, but the name may be extracted from the resource \(e.g. ValueSet.name\).")" : "<string[](datatypes.html#string)>", // Human Name for the resource[](terminologies.html#unbound)
      "description[](implementationguide-definitions.html#ImplementationGuide.definition.resource.description "A description of the reason that a resource has been included in the implementation guide.")" : "<string[](datatypes.html#string)>", // Reason why included in guide[](terminologies.html#unbound)
      // example[x]: Is an example/What is this an example of?. One of these 2:
      "exampleBoolean[](implementationguide-definitions.html#ImplementationGuide.definition.resource.exampleBoolean "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")" : <boolean[](datatypes.html#boolean)>,
      "exampleCanonical[](implementationguide-definitions.html#ImplementationGuide.definition.resource.exampleCanonical "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")" : { canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) },
      "groupingId[](implementationguide-definitions.html#ImplementationGuide.definition.resource.groupingId "Reference to the id of the grouping this resource appears in.")" : "<id[](datatypes.html#id)>" // Grouping this is part of[](terminologies.html#unbound)
    }],
    "page[](implementationguide-definitions.html#ImplementationGuide.definition.page "A page / section in the implementation guide. The root page is the implementation guide home page.")" : { // Page/Section in the Guide[](terminologies.html#unbound)
      // name[x]: Where to find that page. One of these 2:
      "nameUrl[](implementationguide-definitions.html#ImplementationGuide.definition.page.nameUrl "The source address for the page.")" : "<url[](datatypes.html#url)>",
      "nameReference[](implementationguide-definitions.html#ImplementationGuide.definition.page.nameReference "The source address for the page.")" : { Reference[](references.html#Reference)(Binary[](binary.html#Binary)) },
      "title[](implementationguide-definitions.html#ImplementationGuide.definition.page.title "A short title used to represent this page in navigational structures such as table of contents, bread crumbs, etc.")" : "<string[](datatypes.html#string)>", // **R!**  Short title shown for navigational assistance[](terminologies.html#unbound)
      "generation[](implementationguide-definitions.html#ImplementationGuide.definition.page.generation "A code that indicates how the page is generated.")" : "<code[](datatypes.html#code)>", // **R!**  html | markdown | xml | generated[](valueset-guide-page-generation.html)
      "page[](implementationguide-definitions.html#ImplementationGuide.definition.page.page "Nested Pages/Sections under this page.")" : [{ Content as for ImplementationGuide.definition.page }] // Nested Pages / Sections[](terminologies.html#unbound)
    },
    "parameter[](implementationguide-definitions.html#ImplementationGuide.definition.parameter "Defines how IG is built by tools.")" : [{ // Defines how IG is built by tools[](terminologies.html#unbound)
      "code[](implementationguide-definitions.html#ImplementationGuide.definition.parameter.code "apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template.")" : "<code[](datatypes.html#code)>", // **R!**  apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template[](valueset-guide-parameter-code.html)
      "value[](implementationguide-definitions.html#ImplementationGuide.definition.parameter.value "Value for named type.")" : "<string[](datatypes.html#string)>" // **R!**  Value for named type[](terminologies.html#unbound)
    }],
    "template[](implementationguide-definitions.html#ImplementationGuide.definition.template "A template for building resources.")" : [{ // A template for building resources[](terminologies.html#unbound)
      "code[](implementationguide-definitions.html#ImplementationGuide.definition.template.code "Type of template specified.")" : "<code[](datatypes.html#code)>", // **R!**  Type of template specified[](terminologies.html#unbound)
      "source[](implementationguide-definitions.html#ImplementationGuide.definition.template.source "The source location for the template.")" : "<string[](datatypes.html#string)>", // **R!**  The source location for the template[](terminologies.html#unbound)
      "scope[](implementationguide-definitions.html#ImplementationGuide.definition.template.scope "The scope in which the template applies.")" : "<string[](datatypes.html#string)>" // The scope in which the template applies[](terminologies.html#unbound)
    }]
  },
  "manifest[](implementationguide-definitions.html#ImplementationGuide.manifest "Information about an assembled implementation guide, created by the publication tooling.")" : { // Information about an assembled IG[](terminologies.html#unbound)
    "rendering[](implementationguide-definitions.html#ImplementationGuide.manifest.rendering "A pointer to official web page, PDF or other rendering of the implementation guide.")" : "<url[](datatypes.html#url)>", // Location of rendered implementation guide[](terminologies.html#unbound)
    "resource[](implementationguide-definitions.html#ImplementationGuide.manifest.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.")" : [{ // **R!**  Resource in the implementation guide[](terminologies.html#unbound)
      "reference[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.reference "Where this resource is found.")" : { Reference[](references.html#Reference)(Any[](resourcelist.html)) }, // **R!**  Location of the resource[](terminologies.html#unbound)
      // example[x]: Is an example/What is this an example of?. One of these 2:
      "exampleBoolean[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.exampleBoolean "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")" : <boolean[](datatypes.html#boolean)>,
      "exampleCanonical[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.exampleCanonical "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")" : { canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) },
      "relativePath[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.relativePath "The relative path for primary page for this resource within the IG.")" : "<url[](datatypes.html#url)>" // Relative path for page in IG[](terminologies.html#unbound)
    }],
    "page[](implementationguide-definitions.html#ImplementationGuide.manifest.page "Information about a page within the IG.")" : [{ // HTML page within the parent IG[](terminologies.html#unbound)
      "name[](implementationguide-definitions.html#ImplementationGuide.manifest.page.name "Relative path to the page.")" : "<string[](datatypes.html#string)>", // **R!**  HTML page name[](terminologies.html#unbound)
      "title[](implementationguide-definitions.html#ImplementationGuide.manifest.page.title "Label for the page intended for human display.")" : "<string[](datatypes.html#string)>", // Title of the page, for references[](terminologies.html#unbound)
      "anchor[](implementationguide-definitions.html#ImplementationGuide.manifest.page.anchor "The name of an anchor available on the page.")" : ["<string[](datatypes.html#string)>"] // Anchor available on the page[](terminologies.html#unbound)
    }],
    "image[](implementationguide-definitions.html#ImplementationGuide.manifest.image "Indicates a relative path to an image that exists within the IG.")" : ["<string[](datatypes.html#string)>"], // Image within the IG[](terminologies.html#unbound)
    "other[](implementationguide-definitions.html#ImplementationGuide.manifest.other "Indicates the relative path of an additional non-page, non-image file that is part of the IG - e.g. zip, jar and similar files that could be the target of a hyperlink in a derived IG.")" : ["<string[](datatypes.html#string)>"] // Additional linkable file in IG[](terminologies.html#unbound)
  }
}

```

**Turtle Template**
```

@prefix fhir: <http://hl7.org/fhir/> .[![doco](help.png)](rdf.html "Documentation for this format")


[ a fhir:[**ImplementationGuide**](implementationguide-definitions.html#ImplementationGuide "A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.");
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource[](resource.html): .id[](resource.html#id), .meta[](resource.html#meta), .implicitRules[](resource.html#implicitRules), and .language[](resource.html#language)
  # from DomainResource[](domainresource.html): .text[](narrative.html#Narrative), .contained[](references.html#contained), .extension[](extensibility.html), and .modifierExtension[](extensibility.html#modifierExtension)
  fhir:ImplementationGuide.url[](implementationguide-definitions.html#ImplementationGuide.url "An absolute URI that is used to identify this implementation guide when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this implementation guide is \(or will be\) published. This URL can be the target of a canonical reference. It SHALL remain the same when the implementation guide is stored on different servers.") [ uri[](datatypes.html#uri) ]; # 1..1 Canonical identifier for this implementation guide, represented as a URI (globally unique)
  fhir:ImplementationGuide.version[](implementationguide-definitions.html#ImplementationGuide.version "The identifier that is used to identify this version of the implementation guide when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the implementation guide author and is not expected to be globally unique. For example, it might be a timestamp \(e.g. yyyymmdd\) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") [ string[](datatypes.html#string) ]; # 0..1 Business version of the implementation guide
  fhir:ImplementationGuide.name[](implementationguide-definitions.html#ImplementationGuide.name "A natural language name identifying the implementation guide. This name should be usable as an identifier for the module by machine processing applications such as code generation.") [ string[](datatypes.html#string) ]; # 1..1 Name for this implementation guide (computer friendly)
  fhir:ImplementationGuide.title[](implementationguide-definitions.html#ImplementationGuide.title "A short, descriptive, user-friendly title for the implementation guide.") [ string[](datatypes.html#string) ]; # 0..1 Name for this implementation guide (human friendly)
  fhir:[ImplementationGuide.status](implementationguide-definitions.html#ImplementationGuide.status "The status of this implementation guide. Enables tracking the life-cycle of the content \(this element modifies the meaning of other elements\)") [ code[](datatypes.html#code) ]; # 1..1 draft | active | retired | unknown
  fhir:ImplementationGuide.experimental[](implementationguide-definitions.html#ImplementationGuide.experimental "A Boolean value to indicate that this implementation guide is authored for testing purposes \(or education/evaluation/marketing\) and is not intended to be used for genuine usage.") [ boolean[](datatypes.html#boolean) ]; # 0..1 For testing purposes, not real usage
  fhir:ImplementationGuide.date[](implementationguide-definitions.html#ImplementationGuide.date "The date  \(and optionally time\) when the implementation guide was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the implementation guide changes.") [ dateTime[](datatypes.html#dateTime) ]; # 0..1 Date last changed
  fhir:ImplementationGuide.publisher[](implementationguide-definitions.html#ImplementationGuide.publisher "The name of the organization or individual that published the implementation guide.") [ string[](datatypes.html#string) ]; # 0..1 Name of the publisher (organization or individual)
  fhir:ImplementationGuide.contact[](implementationguide-definitions.html#ImplementationGuide.contact "Contact details to assist a user in finding and communicating with the publisher.") [ ContactDetail[](metadatatypes.html#ContactDetail) ], ... ; # 0..* Contact details for the publisher
  fhir:ImplementationGuide.description[](implementationguide-definitions.html#ImplementationGuide.description "A free text natural language description of the implementation guide from a consumer's perspective.") [ markdown[](datatypes.html#markdown) ]; # 0..1 Natural language description of the implementation guide
  fhir:ImplementationGuide.useContext[](implementationguide-definitions.html#ImplementationGuide.useContext "The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories \(gender, age, ...\) or may be references to specific programs \(insurance plans, studies, ...\) and may be used to assist with indexing and searching for appropriate implementation guide instances.") [ UsageContext[](metadatatypes.html#UsageContext) ], ... ; # 0..* The context that the content is intended to support
  fhir:ImplementationGuide.jurisdiction[](implementationguide-definitions.html#ImplementationGuide.jurisdiction "A legal or geographic region in which the implementation guide is intended to be used.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* Intended jurisdiction for implementation guide (if applicable)
  fhir:ImplementationGuide.copyright[](implementationguide-definitions.html#ImplementationGuide.copyright "A copyright statement relating to the implementation guide and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the implementation guide.") [ markdown[](datatypes.html#markdown) ]; # 0..1 Use and/or publishing restrictions
  fhir:ImplementationGuide.packageId[](implementationguide-definitions.html#ImplementationGuide.packageId "The NPM package name for this Implementation Guide, used in the NPM package distribution, which is the primary mechanism by which FHIR based tooling manages IG dependencies. This value must be globally unique, and should be assigned with care.") [ id[](datatypes.html#id) ]; # 1..1 NPM Package name for IG
  fhir:ImplementationGuide.license[](implementationguide-definitions.html#ImplementationGuide.license "The license that applies to this Implementation Guide, using an SPDX license code, or 'not-open-source'.") [ code[](datatypes.html#code) ]; # 0..1 SPDX license code for this IG (or not-open-source)
  fhir:ImplementationGuide.fhirVersion[](implementationguide-definitions.html#ImplementationGuide.fhirVersion "The version\(s\) of the FHIR specification that this ImplementationGuide targets - e.g. describes how to use. The value of this element is the formal version of the specification, without the revision number, e.g. \[publication\].\[major\].\[minor\], which is 4.0.1. for this version.") [ code[](datatypes.html#code) ], ... ; # 1..* FHIR Version(s) this Implementation Guide targets
  fhir:ImplementationGuide.dependsOn[](implementationguide-definitions.html#ImplementationGuide.dependsOn "Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guides.") [ # 0..* Another Implementation guide this depends on
    fhir:ImplementationGuide.dependsOn.uri[](implementationguide-definitions.html#ImplementationGuide.dependsOn.uri "A canonical reference to the Implementation guide for the dependency.") [ canonical[](datatypes.html#canonical)(ImplementationGuide[](implementationguide.html#ImplementationGuide)) ]; # 1..1 Identity of the IG that this depends on
    fhir:ImplementationGuide.dependsOn.packageId[](implementationguide-definitions.html#ImplementationGuide.dependsOn.packageId "The NPM package name for the Implementation Guide that this IG depends on.") [ id[](datatypes.html#id) ]; # 0..1 NPM Package name for IG this depends on
    fhir:ImplementationGuide.dependsOn.version[](implementationguide-definitions.html#ImplementationGuide.dependsOn.version "The version of the IG that is depended on, when the correct version is required to understand the IG correctly.") [ string[](datatypes.html#string) ]; # 0..1 Version of the IG
  ], ...;
  fhir:ImplementationGuide.global[](implementationguide-definitions.html#ImplementationGuide.global "A set of profiles that all resources covered by this implementation guide must conform to.") [ # 0..* Profiles that apply globally
    fhir:ImplementationGuide.global.type[](implementationguide-definitions.html#ImplementationGuide.global.type "The type of resource that all instances must conform to.") [ code[](datatypes.html#code) ]; # 1..1 Type this profile applies to
    fhir:ImplementationGuide.global.profile[](implementationguide-definitions.html#ImplementationGuide.global.profile "A reference to the profile that all instances must conform to.") [ canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) ]; # 1..1 Profile that all resources must conform to
  ], ...;
  fhir:ImplementationGuide.definition[](implementationguide-definitions.html#ImplementationGuide.definition "The information needed by an IG publisher tool to publish the whole implementation guide.") [ # 0..1 Information needed to build the IG
    fhir:ImplementationGuide.definition.grouping[](implementationguide-definitions.html#ImplementationGuide.definition.grouping "A logical group of resources. Logical groups can be used when building pages.") [ # 0..* Grouping used to present related resources in the IG
      fhir:ImplementationGuide.definition.grouping.name[](implementationguide-definitions.html#ImplementationGuide.definition.grouping.name "The human-readable title to display for the package of resources when rendering the implementation guide.") [ string[](datatypes.html#string) ]; # 1..1 Descriptive name for the package
      fhir:ImplementationGuide.definition.grouping.description[](implementationguide-definitions.html#ImplementationGuide.definition.grouping.description "Human readable text describing the package.") [ string[](datatypes.html#string) ]; # 0..1 Human readable text describing the package
    ], ...;
    fhir:ImplementationGuide.definition.resource[](implementationguide-definitions.html#ImplementationGuide.definition.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.") [ # 1..* Resource in the implementation guide
      fhir:ImplementationGuide.definition.resource.reference[](implementationguide-definitions.html#ImplementationGuide.definition.resource.reference "Where this resource is found.") [ Reference[](references.html#Reference)(Any[](resourcelist.html)) ]; # 1..1 Location of the resource
      fhir:ImplementationGuide.definition.resource.fhirVersion[](implementationguide-definitions.html#ImplementationGuide.definition.resource.fhirVersion "Indicates the FHIR Version\(s\) this artifact is intended to apply to. If no versions are specified, the resource is assumed to apply to all the versions stated in ImplementationGuide.fhirVersion.") [ code[](datatypes.html#code) ], ... ; # 0..* Versions this applies to (if different to IG)
      fhir:ImplementationGuide.definition.resource.name[](implementationguide-definitions.html#ImplementationGuide.definition.resource.name "A human assigned name for the resource. All resources SHOULD have a name, but the name may be extracted from the resource \(e.g. ValueSet.name\).") [ string[](datatypes.html#string) ]; # 0..1 Human Name for the resource
      fhir:ImplementationGuide.definition.resource.description[](implementationguide-definitions.html#ImplementationGuide.definition.resource.description "A description of the reason that a resource has been included in the implementation guide.") [ string[](datatypes.html#string) ]; # 0..1 Reason why included in guide
      # ImplementationGuide.definition.resource.example[x][](implementationguide-definitions.html#ImplementationGuide.definition.resource.example\[x\] "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") : 0..1 Is an example/What is this an example of?. One of these 2
        fhir:ImplementationGuide.definition.resource.exampleBoolean[](implementationguide-definitions.html#ImplementationGuide.definition.resource.exampleBoolean "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") [ boolean[](datatypes.html#boolean) ]
        fhir:ImplementationGuide.definition.resource.exampleCanonical[](implementationguide-definitions.html#ImplementationGuide.definition.resource.exampleCanonical "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") [ canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) ]
      fhir:ImplementationGuide.definition.resource.groupingId[](implementationguide-definitions.html#ImplementationGuide.definition.resource.groupingId "Reference to the id of the grouping this resource appears in.") [ id[](datatypes.html#id) ]; # 0..1 Grouping this is part of
    ], ...;
    fhir:ImplementationGuide.definition.page[](implementationguide-definitions.html#ImplementationGuide.definition.page "A page / section in the implementation guide. The root page is the implementation guide home page.") [ # 0..1 Page/Section in the Guide
      # ImplementationGuide.definition.page.name[x][](implementationguide-definitions.html#ImplementationGuide.definition.page.name\[x\] "The source address for the page.") : 1..1 Where to find that page. One of these 2
        fhir:ImplementationGuide.definition.page.nameUrl[](implementationguide-definitions.html#ImplementationGuide.definition.page.nameUrl "The source address for the page.") [ url[](datatypes.html#url) ]
        fhir:ImplementationGuide.definition.page.nameReference[](implementationguide-definitions.html#ImplementationGuide.definition.page.nameReference "The source address for the page.") [ Reference[](references.html#Reference)(Binary[](binary.html#Binary)) ]
      fhir:ImplementationGuide.definition.page.title[](implementationguide-definitions.html#ImplementationGuide.definition.page.title "A short title used to represent this page in navigational structures such as table of contents, bread crumbs, etc.") [ string[](datatypes.html#string) ]; # 1..1 Short title shown for navigational assistance
      fhir:ImplementationGuide.definition.page.generation[](implementationguide-definitions.html#ImplementationGuide.definition.page.generation "A code that indicates how the page is generated.") [ code[](datatypes.html#code) ]; # 1..1 html | markdown | xml | generated
      fhir:ImplementationGuide.definition.page.page[](implementationguide-definitions.html#ImplementationGuide.definition.page.page "Nested Pages/Sections under this page.") [ [See ImplementationGuide.definition.page](#ttl-ImplementationGuide.definition.page) ], ... ; # 0..* Nested Pages / Sections
    ];
    fhir:ImplementationGuide.definition.parameter[](implementationguide-definitions.html#ImplementationGuide.definition.parameter "Defines how IG is built by tools.") [ # 0..* Defines how IG is built by tools
      fhir:ImplementationGuide.definition.parameter.code[](implementationguide-definitions.html#ImplementationGuide.definition.parameter.code "apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template.") [ code[](datatypes.html#code) ]; # 1..1 apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template
      fhir:ImplementationGuide.definition.parameter.value[](implementationguide-definitions.html#ImplementationGuide.definition.parameter.value "Value for named type.") [ string[](datatypes.html#string) ]; # 1..1 Value for named type
    ], ...;
    fhir:ImplementationGuide.definition.template[](implementationguide-definitions.html#ImplementationGuide.definition.template "A template for building resources.") [ # 0..* A template for building resources
      fhir:ImplementationGuide.definition.template.code[](implementationguide-definitions.html#ImplementationGuide.definition.template.code "Type of template specified.") [ code[](datatypes.html#code) ]; # 1..1 Type of template specified
      fhir:ImplementationGuide.definition.template.source[](implementationguide-definitions.html#ImplementationGuide.definition.template.source "The source location for the template.") [ string[](datatypes.html#string) ]; # 1..1 The source location for the template
      fhir:ImplementationGuide.definition.template.scope[](implementationguide-definitions.html#ImplementationGuide.definition.template.scope "The scope in which the template applies.") [ string[](datatypes.html#string) ]; # 0..1 The scope in which the template applies
    ], ...;
  ];
  fhir:ImplementationGuide.manifest[](implementationguide-definitions.html#ImplementationGuide.manifest "Information about an assembled implementation guide, created by the publication tooling.") [ # 0..1 Information about an assembled IG
    fhir:ImplementationGuide.manifest.rendering[](implementationguide-definitions.html#ImplementationGuide.manifest.rendering "A pointer to official web page, PDF or other rendering of the implementation guide.") [ url[](datatypes.html#url) ]; # 0..1 Location of rendered implementation guide
    fhir:ImplementationGuide.manifest.resource[](implementationguide-definitions.html#ImplementationGuide.manifest.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.") [ # 1..* Resource in the implementation guide
      fhir:ImplementationGuide.manifest.resource.reference[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.reference "Where this resource is found.") [ Reference[](references.html#Reference)(Any[](resourcelist.html)) ]; # 1..1 Location of the resource
      # ImplementationGuide.manifest.resource.example[x][](implementationguide-definitions.html#ImplementationGuide.manifest.resource.example\[x\] "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") : 0..1 Is an example/What is this an example of?. One of these 2
        fhir:ImplementationGuide.manifest.resource.exampleBoolean[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.exampleBoolean "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") [ boolean[](datatypes.html#boolean) ]
        fhir:ImplementationGuide.manifest.resource.exampleCanonical[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.exampleCanonical "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") [ canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) ]
      fhir:ImplementationGuide.manifest.resource.relativePath[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.relativePath "The relative path for primary page for this resource within the IG.") [ url[](datatypes.html#url) ]; # 0..1 Relative path for page in IG
    ], ...;
    fhir:ImplementationGuide.manifest.page[](implementationguide-definitions.html#ImplementationGuide.manifest.page "Information about a page within the IG.") [ # 0..* HTML page within the parent IG
      fhir:ImplementationGuide.manifest.page.name[](implementationguide-definitions.html#ImplementationGuide.manifest.page.name "Relative path to the page.") [ string[](datatypes.html#string) ]; # 1..1 HTML page name
      fhir:ImplementationGuide.manifest.page.title[](implementationguide-definitions.html#ImplementationGuide.manifest.page.title "Label for the page intended for human display.") [ string[](datatypes.html#string) ]; # 0..1 Title of the page, for references
      fhir:ImplementationGuide.manifest.page.anchor[](implementationguide-definitions.html#ImplementationGuide.manifest.page.anchor "The name of an anchor available on the page.") [ string[](datatypes.html#string) ], ... ; # 0..* Anchor available on the page
    ], ...;
    fhir:ImplementationGuide.manifest.image[](implementationguide-definitions.html#ImplementationGuide.manifest.image "Indicates a relative path to an image that exists within the IG.") [ string[](datatypes.html#string) ], ... ; # 0..* Image within the IG
    fhir:ImplementationGuide.manifest.other[](implementationguide-definitions.html#ImplementationGuide.manifest.other "Indicates the relative path of an additional non-page, non-image file that is part of the IG - e.g. zip, jar and similar files that could be the target of a hyperlink in a derived IG.") [ string[](datatypes.html#string) ], ... ; # 0..* Additional linkable file in IG
  ];
]

```

**Changes since R3**
[ImplementationGuide](implementationguide.html#ImplementationGuide) |   
---|---  
ImplementationGuide | 
  * Min Cardinality changed from 1 to 0
  * Max Cardinality changed from 1 to *

  
ImplementationGuide.title | 
  * Added Element

  
ImplementationGuide.status | 
  * Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1

  
ImplementationGuide.experimental | 
  * No longer marked as Modifier

  
ImplementationGuide.packageId | 
  * **Added Mandatory Element**

  
ImplementationGuide.license | 
  * Added Element

  
ImplementationGuide.fhirVersion | 
  * Min Cardinality changed from 0 to 1
  * Max Cardinality changed from 1 to *
  * Type changed from id to code
  * Add Binding `http://hl7.org/fhir/ValueSet/FHIR-version|4.0.1` (required) 

  
ImplementationGuide.dependsOn | 
  * Renamed from dependency to dependsOn

  
ImplementationGuide.dependsOn.uri | 
  * Moved from ImplementationGuide.dependency to ImplementationGuide.dependsOn
  * Type changed from uri to canonical(ImplementationGuide)

  
ImplementationGuide.dependsOn.packageId | 
  * Added Element

  
ImplementationGuide.dependsOn.version | 
  * Added Element

  
ImplementationGuide.global.type | 
  * Change value set from http://hl7.org/fhir/ValueSet/resource-types to http://hl7.org/fhir/ValueSet/resource-types|4.0.1

  
ImplementationGuide.global.profile | 
  * Type changed from Reference(StructureDefinition) to canonical(StructureDefinition)

  
ImplementationGuide.definition | 
  * Added Element

  
ImplementationGuide.definition.grouping | 
  * Added Element

  
ImplementationGuide.definition.grouping.name | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.grouping.description | 
  * Added Element

  
ImplementationGuide.definition.resource | 
  * Moved from ImplementationGuide.package to ImplementationGuide.definition

  
ImplementationGuide.definition.resource.reference | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.resource.fhirVersion | 
  * Added Element

  
ImplementationGuide.definition.resource.example[x] | 
  * Moved from ImplementationGuide.package.resource.example to example[x]
  * Min Cardinality changed from 1 to 0
  * Add Type canonical(StructureDefinition)

  
ImplementationGuide.definition.resource.groupingId | 
  * Added Element

  
ImplementationGuide.definition.page | 
  * Moved from ImplementationGuide to ImplementationGuide.definition

  
ImplementationGuide.definition.page.name[x] | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.page.generation | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.parameter | 
  * Added Element

  
ImplementationGuide.definition.parameter.code | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.parameter.value | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.template | 
  * Added Element

  
ImplementationGuide.definition.template.code | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.template.source | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.template.scope | 
  * Added Element

  
ImplementationGuide.manifest | 
  * Added Element

  
ImplementationGuide.manifest.rendering | 
  * Added Element

  
ImplementationGuide.manifest.resource | 
  * **Added Mandatory Element**

  
ImplementationGuide.manifest.resource.reference | 
  * **Added Mandatory Element**

  
ImplementationGuide.manifest.resource.example[x] | 
  * Added Element

  
ImplementationGuide.manifest.resource.relativePath | 
  * Added Element

  
ImplementationGuide.manifest.page | 
  * Added Element

  
ImplementationGuide.manifest.page.name | 
  * **Added Mandatory Element**

  
ImplementationGuide.manifest.page.title | 
  * Added Element

  
ImplementationGuide.manifest.page.anchor | 
  * Added Element

  
ImplementationGuide.manifest.image | 
  * Added Element

  
ImplementationGuide.manifest.other | 
  * Added Element

  
ImplementationGuide.dependency.type | 
  * deleted

  
ImplementationGuide.package | 
  * deleted

  
ImplementationGuide.binary | 
  * deleted

  
ImplementationGuide.page.source | 
  * deleted

  
ImplementationGuide.page.kind | 
  * deleted

  
ImplementationGuide.page.type | 
  * deleted

  
ImplementationGuide.page.package | 
  * deleted

  
ImplementationGuide.page.format | 
  * deleted

  
See the [Full Difference](diff.html) for further information
This analysis is available as [XML](implementationguide.diff.xml) or [JSON](implementationguide.diff.json). 
See [R3 <--> R4 Conversion Maps](implementationguide-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)
**Structure**
[Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") |  [Description & Constraints](formats.html#table "Additional information about the element")[![doco](help16.png)](formats.html#table "Legend for this format")  
---|---|---|---|---  
![.](tbl_spacer.png)![.](icon_resource.png) [ImplementationGuide](implementationguide-definitions.html#ImplementationGuide "ImplementationGuide : A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.") |  [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[TU](versions.html#std-process "Standards Status = Trial Use") |  | [DomainResource](domainresource.html) | A set of rules about how FHIR is used  
+ Warning: Name should be usable as an identifier for the module by machine processing applications such as code generation  
+ Rule: If a resource has a fhirVersion, it must be oe of the versions defined for the Implementation Guide  
Elements defined in Ancestors: [id](resource.html#Resource "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes."), [meta](resource.html#Resource "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource."), [implicitRules](resource.html#Resource "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc."), [language](resource.html#Resource "The base language in which the resource is written."), [text](domainresource.html#DomainResource "A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety."), [contained](domainresource.html#DomainResource "These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope."), [extension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension."), [modifierExtension](domainresource.html#DomainResource "May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.

Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource \(including cannot change the meaning of modifierExtension itself\).")  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [url](implementationguide-definitions.html#ImplementationGuide.url "ImplementationGuide.url : An absolute URI that is used to identify this implementation guide when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this implementation guide is \(or will be\) published. This URL can be the target of a canonical reference. It SHALL remain the same when the implementation guide is stored on different servers.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [uri](datatypes.html#uri) | Canonical identifier for this implementation guide, represented as a URI (globally unique)  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [version](implementationguide-definitions.html#ImplementationGuide.version "ImplementationGuide.version : The identifier that is used to identify this version of the implementation guide when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the implementation guide author and is not expected to be globally unique. For example, it might be a timestamp \(e.g. yyyymmdd\) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Business version of the implementation guide  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](implementationguide-definitions.html#ImplementationGuide.name "ImplementationGuide.name : A natural language name identifying the implementation guide. This name should be usable as an identifier for the module by machine processing applications such as code generation.") |  [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries")[I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 1..1 | [string](datatypes.html#string) | Name for this implementation guide (computer friendly)  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [title](implementationguide-definitions.html#ImplementationGuide.title "ImplementationGuide.title : A short, descriptive, user-friendly title for the implementation guide.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name for this implementation guide (human friendly)  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [status](implementationguide-definitions.html#ImplementationGuide.status "ImplementationGuide.status : The status of this implementation guide. Enables tracking the life-cycle of the content.") |  [?!](conformance-rules.html#isModifier "This element is a modifier element")[Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | draft | active | retired | unknown  
[PublicationStatus](valueset-publication-status.html "The lifecycle status of an artifact.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [experimental](implementationguide-definitions.html#ImplementationGuide.experimental "ImplementationGuide.experimental : A Boolean value to indicate that this implementation guide is authored for testing purposes \(or education/evaluation/marketing\) and is not intended to be used for genuine usage.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [boolean](datatypes.html#boolean) | For testing purposes, not real usage  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [date](implementationguide-definitions.html#ImplementationGuide.date "ImplementationGuide.date : The date  \(and optionally time\) when the implementation guide was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the implementation guide changes.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [dateTime](datatypes.html#dateTime) | Date last changed  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [publisher](implementationguide-definitions.html#ImplementationGuide.publisher "ImplementationGuide.publisher : The name of the organization or individual that published the implementation guide.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Name of the publisher (organization or individual)  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [contact](implementationguide-definitions.html#ImplementationGuide.contact "ImplementationGuide.contact : Contact details to assist a user in finding and communicating with the publisher.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [ContactDetail](metadatatypes.html#ContactDetail) | Contact details for the publisher  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [description](implementationguide-definitions.html#ImplementationGuide.description "ImplementationGuide.description : A free text natural language description of the implementation guide from a consumer's perspective.") |  | 0..1 | [markdown](datatypes.html#markdown) | Natural language description of the implementation guide  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [useContext](implementationguide-definitions.html#ImplementationGuide.useContext "ImplementationGuide.useContext : The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories \(gender, age, ...\) or may be references to specific programs \(insurance plans, studies, ...\) and may be used to assist with indexing and searching for appropriate implementation guide instances.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [UsageContext](metadatatypes.html#UsageContext) | The context that the content is intended to support  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_datatype.gif) [jurisdiction](implementationguide-definitions.html#ImplementationGuide.jurisdiction "ImplementationGuide.jurisdiction : A legal or geographic region in which the implementation guide is intended to be used.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [CodeableConcept](datatypes.html#CodeableConcept) | Intended jurisdiction for implementation guide (if applicable)  
[Jurisdiction](valueset-jurisdiction.html "Countries and regions within which this artifact is targeted for use.") ([Extensible](terminologies.html#extensible "To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within the value set can apply to the concept being communicated.  If the value set does not cover the concept \(based on human review\), alternate codings \(or, data type allowing, text\) may be included instead."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [copyright](implementationguide-definitions.html#ImplementationGuide.copyright "ImplementationGuide.copyright : A copyright statement relating to the implementation guide and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the implementation guide.") |  | 0..1 | [markdown](datatypes.html#markdown) | Use and/or publishing restrictions  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [packageId](implementationguide-definitions.html#ImplementationGuide.packageId "ImplementationGuide.packageId : The NPM package name for this Implementation Guide, used in the NPM package distribution, which is the primary mechanism by which FHIR based tooling manages IG dependencies. This value must be globally unique, and should be assigned with care.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [id](datatypes.html#id) | NPM Package name for IG  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [license](implementationguide-definitions.html#ImplementationGuide.license "ImplementationGuide.license : The license that applies to this Implementation Guide, using an SPDX license code, or 'not-open-source'.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [code](datatypes.html#code) | SPDX license code for this IG (or not-open-source)  
[SPDXLicense](valueset-spdx-license.html "The license that applies to an Implementation Guide \(using an SPDX license Identifiers, or 'not-open-source'\). The binding is required but new SPDX license Identifiers are allowed to be used \(https://spdx.org/licenses/\).") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [fhirVersion](implementationguide-definitions.html#ImplementationGuide.fhirVersion "ImplementationGuide.fhirVersion : The version\(s\) of the FHIR specification that this ImplementationGuide targets - e.g. describes how to use. The value of this element is the formal version of the specification, without the revision number, e.g. \[publication\].\[major\].\[minor\], which is 4.0.1. for this version.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..* | [code](datatypes.html#code) | FHIR Version(s) this Implementation Guide targets  
[FHIRVersion](valueset-FHIR-version.html "All published FHIR Versions.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [dependsOn](implementationguide-definitions.html#ImplementationGuide.dependsOn "ImplementationGuide.dependsOn : Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guides.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [BackboneElement](backboneelement.html) | Another Implementation guide this depends on  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [uri](implementationguide-definitions.html#ImplementationGuide.dependsOn.uri "ImplementationGuide.dependsOn.uri : A canonical reference to the Implementation guide for the dependency.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [canonical](datatypes.html#canonical)([ImplementationGuide](implementationguide.html)) | Identity of the IG that this depends on  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [packageId](implementationguide-definitions.html#ImplementationGuide.dependsOn.packageId "ImplementationGuide.dependsOn.packageId : The NPM package name for the Implementation Guide that this IG depends on.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [id](datatypes.html#id) | NPM Package name for IG this depends on  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [version](implementationguide-definitions.html#ImplementationGuide.dependsOn.version "ImplementationGuide.dependsOn.version : The version of the IG that is depended on, when the correct version is required to understand the IG correctly.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [string](datatypes.html#string) | Version of the IG  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [global](implementationguide-definitions.html#ImplementationGuide.global "ImplementationGuide.global : A set of profiles that all resources covered by this implementation guide must conform to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..* | [BackboneElement](backboneelement.html) | Profiles that apply globally  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [type](implementationguide-definitions.html#ImplementationGuide.global.type "ImplementationGuide.global.type : The type of resource that all instances must conform to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 | [code](datatypes.html#code) | Type this profile applies to  
[ResourceType](valueset-resource-types.html "One of the resource types defined as part of this version of FHIR.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) [profile](implementationguide-definitions.html#ImplementationGuide.global.profile "ImplementationGuide.global.profile : A reference to the profile that all instances must conform to.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) | Profile that all resources must conform to  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_element.gif) [definition](implementationguide-definitions.html#ImplementationGuide.definition "ImplementationGuide.definition : The information needed by an IG publisher tool to publish the whole implementation guide.") | [I](conformance-rules.html#constraints "This element has or is affected by some invariants") | 0..1 | [BackboneElement](backboneelement.html) | Information needed to build the IG  
+ Rule: If a resource has a groupingId, it must refer to a grouping defined in the Implementation Guide  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_element.gif) [grouping](implementationguide-definitions.html#ImplementationGuide.definition.grouping "ImplementationGuide.definition.grouping : A logical group of resources. Logical groups can be used when building pages.") |  | 0..* | [BackboneElement](backboneelement.html) | Grouping used to present related resources in the IG  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](implementationguide-definitions.html#ImplementationGuide.definition.grouping.name "ImplementationGuide.definition.grouping.name : The human-readable title to display for the package of resources when rendering the implementation guide.") |  | 1..1 | [string](datatypes.html#string) | Descriptive name for the package  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [description](implementationguide-definitions.html#ImplementationGuide.definition.grouping.description "ImplementationGuide.definition.grouping.description : Human readable text describing the package.") |  | 0..1 | [string](datatypes.html#string) | Human readable text describing the package  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_element.gif) [resource](implementationguide-definitions.html#ImplementationGuide.definition.resource "ImplementationGuide.definition.resource : A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.") |  | 1..* | [BackboneElement](backboneelement.html) | Resource in the implementation guide  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [reference](implementationguide-definitions.html#ImplementationGuide.definition.resource.reference "ImplementationGuide.definition.resource.reference : Where this resource is found.") |  | 1..1 |  [Reference](references.html#Reference)([Any](resourcelist.html)) | Location of the resource  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [fhirVersion](implementationguide-definitions.html#ImplementationGuide.definition.resource.fhirVersion "ImplementationGuide.definition.resource.fhirVersion : Indicates the FHIR Version\(s\) this artifact is intended to apply to. If no versions are specified, the resource is assumed to apply to all the versions stated in ImplementationGuide.fhirVersion.") |  | 0..* | [code](datatypes.html#code) | Versions this applies to (if different to IG)  
[FHIRVersion](valueset-FHIR-version.html "All published FHIR Versions.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](implementationguide-definitions.html#ImplementationGuide.definition.resource.name "ImplementationGuide.definition.resource.name : A human assigned name for the resource. All resources SHOULD have a name, but the name may be extracted from the resource \(e.g. ValueSet.name\).") |  | 0..1 | [string](datatypes.html#string) | Human Name for the resource  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [description](implementationguide-definitions.html#ImplementationGuide.definition.resource.description "ImplementationGuide.definition.resource.description : A description of the reason that a resource has been included in the implementation guide.") |  | 0..1 | [string](datatypes.html#string) | Reason why included in guide  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_choice.gif) [example[x]](implementationguide-definitions.html#ImplementationGuide.definition.resource.example_x_ "ImplementationGuide.definition.resource.example\[x\] : If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") |  | 0..1 |  | Is an example/What is this an example of?  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) exampleBoolean |  |  | [boolean](datatypes.html#boolean) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) exampleCanonical |  |  |  [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [groupingId](implementationguide-definitions.html#ImplementationGuide.definition.resource.groupingId "ImplementationGuide.definition.resource.groupingId : Reference to the id of the grouping this resource appears in.") |  | 0..1 | [id](datatypes.html#id) | Grouping this is part of  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_element.gif) [page](implementationguide-definitions.html#ImplementationGuide.definition.page "ImplementationGuide.definition.page : A page / section in the implementation guide. The root page is the implementation guide home page.") |  | 0..1 | [BackboneElement](backboneelement.html) | Page/Section in the Guide  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_choice.gif) [name[x]](implementationguide-definitions.html#ImplementationGuide.definition.page.name_x_ "ImplementationGuide.definition.page.name\[x\] : The source address for the page.") |  | 1..1 |  | Where to find that page  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) nameUrl |  |  | [url](datatypes.html#url) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) nameReference |  |  |  [Reference](references.html#Reference)([Binary](http.html)) |   
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [title](implementationguide-definitions.html#ImplementationGuide.definition.page.title "ImplementationGuide.definition.page.title : A short title used to represent this page in navigational structures such as table of contents, bread crumbs, etc.") |  | 1..1 | [string](datatypes.html#string) | Short title shown for navigational assistance  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [generation](implementationguide-definitions.html#ImplementationGuide.definition.page.generation "ImplementationGuide.definition.page.generation : A code that indicates how the page is generated.") |  | 1..1 | [code](datatypes.html#code) | html | markdown | xml | generated  
[GuidePageGeneration](valueset-guide-page-generation.html "A code that indicates how the page is generated.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reuse.png) [page](implementationguide-definitions.html#ImplementationGuide.definition.page.page "ImplementationGuide.definition.page.page : Nested Pages/Sections under this page.") |  | 0..* | see [page](#ImplementationGuide.definition.page "ImplementationGuide.definition.page") | Nested Pages / Sections  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_element.gif) [parameter](implementationguide-definitions.html#ImplementationGuide.definition.parameter "ImplementationGuide.definition.parameter : Defines how IG is built by tools.") |  | 0..* | [BackboneElement](backboneelement.html) | Defines how IG is built by tools  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [code](implementationguide-definitions.html#ImplementationGuide.definition.parameter.code "ImplementationGuide.definition.parameter.code : apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template.") |  | 1..1 | [code](datatypes.html#code) | apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template  
[GuideParameterCode](valueset-guide-parameter-code.html "Code of parameter that is input to the guide.") ([Required](terminologies.html#required "To be conformant, the concept in this element SHALL be from the specified value set."))  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [value](implementationguide-definitions.html#ImplementationGuide.definition.parameter.value "ImplementationGuide.definition.parameter.value : Value for named type.") |  | 1..1 | [string](datatypes.html#string) | Value for named type  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [template](implementationguide-definitions.html#ImplementationGuide.definition.template "ImplementationGuide.definition.template : A template for building resources.") |  | 0..* | [BackboneElement](backboneelement.html) | A template for building resources  
  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [code](implementationguide-definitions.html#ImplementationGuide.definition.template.code "ImplementationGuide.definition.template.code : Type of template specified.") |  | 1..1 | [code](datatypes.html#code) | Type of template specified  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [source](implementationguide-definitions.html#ImplementationGuide.definition.template.source "ImplementationGuide.definition.template.source : The source location for the template.") |  | 1..1 | [string](datatypes.html#string) | The source location for the template  
![.](tbl_spacer.png)![.](tbl_vline.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [scope](implementationguide-definitions.html#ImplementationGuide.definition.template.scope "ImplementationGuide.definition.template.scope : The scope in which the template applies.") |  | 0..1 | [string](datatypes.html#string) | The scope in which the template applies  
![.](tbl_spacer.png)![.](tbl_vjoin_end.png)![.](icon_element.gif) [manifest](implementationguide-definitions.html#ImplementationGuide.manifest "ImplementationGuide.manifest : Information about an assembled implementation guide, created by the publication tooling.") |  | 0..1 | [BackboneElement](backboneelement.html) | Information about an assembled IG  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [rendering](implementationguide-definitions.html#ImplementationGuide.manifest.rendering "ImplementationGuide.manifest.rendering : A pointer to official web page, PDF or other rendering of the implementation guide.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 0..1 | [url](datatypes.html#url) | Location of rendered implementation guide  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_element.gif) [resource](implementationguide-definitions.html#ImplementationGuide.manifest.resource "ImplementationGuide.manifest.resource : A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..* | [BackboneElement](backboneelement.html) | Resource in the implementation guide  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_reference.png) [reference](implementationguide-definitions.html#ImplementationGuide.manifest.resource.reference "ImplementationGuide.manifest.resource.reference : Where this resource is found.") | [Σ](elementdefinition-definitions.html#ElementDefinition.isSummary "This element is included in summaries") | 1..1 |  [Reference](references.html#Reference)([Any](resourcelist.html)) | Location of the resource  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_choice.gif) [example[x]](implementationguide-definitions.html#ImplementationGuide.manifest.resource.example_x_ "ImplementationGuide.manifest.resource.example\[x\] : If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") |  | 0..1 |  | Is an example/What is this an example of?  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) exampleBoolean |  |  | [boolean](datatypes.html#boolean) |   
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_reference.png) exampleCanonical |  |  |  [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html)) |   
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [relativePath](implementationguide-definitions.html#ImplementationGuide.manifest.resource.relativePath "ImplementationGuide.manifest.resource.relativePath : The relative path for primary page for this resource within the IG.") |  | 0..1 | [url](datatypes.html#url) | Relative path for page in IG  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_element.gif) [page](implementationguide-definitions.html#ImplementationGuide.manifest.page "ImplementationGuide.manifest.page : Information about a page within the IG.") |  | 0..* | [BackboneElement](backboneelement.html) | HTML page within the parent IG  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [name](implementationguide-definitions.html#ImplementationGuide.manifest.page.name "ImplementationGuide.manifest.page.name : Relative path to the page.") |  | 1..1 | [string](datatypes.html#string) | HTML page name  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [title](implementationguide-definitions.html#ImplementationGuide.manifest.page.title "ImplementationGuide.manifest.page.title : Label for the page intended for human display.") |  | 0..1 | [string](datatypes.html#string) | Title of the page, for references  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vline.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [anchor](implementationguide-definitions.html#ImplementationGuide.manifest.page.anchor "ImplementationGuide.manifest.page.anchor : The name of an anchor available on the page.") |  | 0..* | [string](datatypes.html#string) | Anchor available on the page  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [image](implementationguide-definitions.html#ImplementationGuide.manifest.image "ImplementationGuide.manifest.image : Indicates a relative path to an image that exists within the IG.") |  | 0..* | [string](datatypes.html#string) | Image within the IG  
  
![.](tbl_spacer.png)![.](tbl_blank.png)![.](tbl_vjoin_end.png)![.](icon_primitive.png) [other](implementationguide-definitions.html#ImplementationGuide.manifest.other "ImplementationGuide.manifest.other : Indicates the relative path of an additional non-page, non-image file that is part of the IG - e.g. zip, jar and similar files that could be the target of a hyperlink in a derived IG.") |  | 0..* | [string](datatypes.html#string) | Additional linkable file in IG  
  
  
[![doco](help16.png) Documentation for this format](formats.html#table "Legend for this format")  
**UML Diagram** ([Legend](formats.html#uml))
ImplementationGuide (DomainResource)An absolute URI that is used to identify this implementation guide when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this implementation guide is (or will be) published. This URL can be the target of a canonical reference. It SHALL remain the same when the implementation guide is stored on different serversurl : uri [1..1]The identifier that is used to identify this version of the implementation guide when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the implementation guide author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequenceversion : string [0..1]A natural language name identifying the implementation guide. This name should be usable as an identifier for the module by machine processing applications such as code generationname : string [1..1]A short, descriptive, user-friendly title for the implementation guidetitle : string [0..1]The status of this implementation guide. Enables tracking the life-cycle of the content (this element modifies the meaning of other elements)status : code [1..1] « The lifecycle status of an artifact. (Strength=Required)PublicationStatus! »A Boolean value to indicate that this implementation guide is authored for testing purposes (or education/evaluation/marketing) and is not intended to be used for genuine usageexperimental : boolean [0..1]The date (and optionally time) when the implementation guide was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the implementation guide changesdate : dateTime [0..1]The name of the organization or individual that published the implementation guidepublisher : string [0..1]Contact details to assist a user in finding and communicating with the publishercontact : ContactDetail [0..*]A free text natural language description of the implementation guide from a consumer's perspectivedescription : markdown [0..1]The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories (gender, age, ...) or may be references to specific programs (insurance plans, studies, ...) and may be used to assist with indexing and searching for appropriate implementation guide instancesuseContext : UsageContext [0..*]A legal or geographic region in which the implementation guide is intended to be usedjurisdiction : CodeableConcept [0..*] « Countries and regions within which this artifact is targeted for use. (Strength=Extensible)Jurisdiction ValueSet+ »A copyright statement relating to the implementation guide and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the implementation guidecopyright : markdown [0..1]The NPM package name for this Implementation Guide, used in the NPM package distribution, which is the primary mechanism by which FHIR based tooling manages IG dependencies. This value must be globally unique, and should be assigned with carepackageId : id [1..1]The license that applies to this Implementation Guide, using an SPDX license code, or 'not-open-source'license : code [0..1] « The license that applies to an Implementation Guide (using an SPDX license Identifiers, or 'not-open-source'). The binding is required but new SPDX license Identifiers are allowed to be used (https://spdx.org/licenses/). (Strength=Required)SPDXLicense! »The version(s) of the FHIR specification that this ImplementationGuide targets - e.g. describes how to use. The value of this element is the formal version of the specification, without the revision number, e.g. [publication].[major].[minor], which is 4.0.1. for this versionfhirVersion : code [1..*] « All published FHIR Versions. (Strength=Required)FHIRVersion! »DependsOnA canonical reference to the Implementation guide for the dependencyuri : canonical [1..1] « ImplementationGuide »The NPM package name for the Implementation Guide that this IG depends onpackageId : id [0..1]The version of the IG that is depended on, when the correct version is required to understand the IG correctlyversion : string [0..1]GlobalThe type of resource that all instances must conform totype : code [1..1] « One of the resource types defined as part of this version of FHIR. (Strength=Required)ResourceType! »A reference to the profile that all instances must conform toprofile : canonical [1..1] « StructureDefinition »DefinitionGroupingThe human-readable title to display for the package of resources when rendering the implementation guidename : string [1..1]Human readable text describing the packagedescription : string [0..1]ResourceWhere this resource is foundreference : Reference [1..1] « Any »Indicates the FHIR Version(s) this artifact is intended to apply to. If no versions are specified, the resource is assumed to apply to all the versions stated in ImplementationGuide.fhirVersionfhirVersion : code [0..*] « All published FHIR Versions. (Strength=Required)FHIRVersion! »A human assigned name for the resource. All resources SHOULD have a name, but the name may be extracted from the resource (e.g. ValueSet.name)name : string [0..1]A description of the reason that a resource has been included in the implementation guidedescription : string [0..1]If true or a reference, indicates the resource is an example instance. If a reference is present, indicates that the example is an example of the specified profileexample[x] : Type [0..1] « boolean|canonical(StructureDefinition) »Reference to the id of the grouping this resource appears ingroupingId : id [0..1]PageThe source address for the pagename[x] : Type [1..1] « url|Reference(Binary) »A short title used to represent this page in navigational structures such as table of contents, bread crumbs, etctitle : string [1..1]A code that indicates how the page is generatedgeneration : code [1..1] « A code that indicates how the page is generated. (Strength=Required)GuidePageGeneration! »Parameterapply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-templatecode : code [1..1] « Code of parameter that is input to the guide. (Strength=Required)GuideParameterCode! »Value for named typevalue : string [1..1]TemplateType of template specifiedcode : code [1..1]The source location for the templatesource : string [1..1]The scope in which the template appliesscope : string [0..1]ManifestA pointer to official web page, PDF or other rendering of the implementation guiderendering : url [0..1]Indicates a relative path to an image that exists within the IGimage : string [0..*]Indicates the relative path of an additional non-page, non-image file that is part of the IG - e.g. zip, jar and similar files that could be the target of a hyperlink in a derived IGother : string [0..*]ManifestResourceWhere this resource is foundreference : Reference [1..1] « Any »If true or a reference, indicates the resource is an example instance. If a reference is present, indicates that the example is an example of the specified profileexample[x] : Type [0..1] « boolean|canonical(StructureDefinition) »The relative path for primary page for this resource within the IGrelativePath : url [0..1]ManifestPageRelative path to the pagename : string [1..1]Label for the page intended for human displaytitle : string [0..1]The name of an anchor available on the pageanchor : string [0..*]Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guidesdependsOn[0..*]A set of profiles that all resources covered by this implementation guide must conform toglobal[0..*]A logical group of resources. Logical groups can be used when building pagesgrouping[0..*]A resource that is part of the implementation guide. Conformance resources (value set, structure definition, capability statements etc.) are obvious candidates for inclusion, but any kind of resource can be included as an example resourceresource[1..*]Nested Pages/Sections under this pagepage[0..*]A page / section in the implementation guide. The root page is the implementation guide home pagepage[0..1]Defines how IG is built by toolsparameter[0..*]A template for building resourcestemplate[0..*]The information needed by an IG publisher tool to publish the whole implementation guidedefinition[0..1]A resource that is part of the implementation guide. Conformance resources (value set, structure definition, capability statements etc.) are obvious candidates for inclusion, but any kind of resource can be included as an example resourceresource[1..*]Information about a page within the IGpage[0..*]Information about an assembled implementation guide, created by the publication toolingmanifest[0..1]
**XML Template**
```

<[**ImplementationGuide**](implementationguide-definitions.html#ImplementationGuide "A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.") xmlns="http://hl7.org/fhir"> [![doco](help.png)](xml.html "Documentation for this format")
 <!-- from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language) -->
 <!-- from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension) -->
 <[**url**](implementationguide-definitions.html#ImplementationGuide.url "An absolute URI that is used to identify this implementation guide when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this implementation guide is \(or will be\) published. This URL can be the target of a canonical reference. It SHALL remain the same when the implementation guide is stored on different servers.") value="[uri[](datatypes.html#uri)]"/><!-- **1..1** Canonical identifier for this implementation guide, represented as a URI (globally unique)[](terminologies.html#unbound) -->
 <[**version**](implementationguide-definitions.html#ImplementationGuide.version "The identifier that is used to identify this version of the implementation guide when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the implementation guide author and is not expected to be globally unique. For example, it might be a timestamp \(e.g. yyyymmdd\) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Business version of the implementation guide[](terminologies.html#unbound) -->
 <[**name**](implementationguide-definitions.html#ImplementationGuide.name "A natural language name identifying the implementation guide. This name should be usable as an identifier for the module by machine processing applications such as code generation.") value="[string[](datatypes.html#string)]"/><!-- **![??](lock.png) 1..1** Name for this implementation guide (computer friendly)[](terminologies.html#unbound) -->
 <[**title**](implementationguide-definitions.html#ImplementationGuide.title "A short, descriptive, user-friendly title for the implementation guide.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Name for this implementation guide (human friendly)[](terminologies.html#unbound) -->
 <[**status**](implementationguide-definitions.html#ImplementationGuide.status "The status of this implementation guide. Enables tracking the life-cycle of the content \(this element modifies the meaning of other elements\)") value="[code[](datatypes.html#code)]"/><!-- **1..1** draft | active | retired | unknown[](valueset-publication-status.html) -->
 <[**experimental**](implementationguide-definitions.html#ImplementationGuide.experimental "A Boolean value to indicate that this implementation guide is authored for testing purposes \(or education/evaluation/marketing\) and is not intended to be used for genuine usage.") value="[boolean[](datatypes.html#boolean)]"/><!-- **0..1** For testing purposes, not real usage[](terminologies.html#unbound) -->
 <[**date**](implementationguide-definitions.html#ImplementationGuide.date "The date  \(and optionally time\) when the implementation guide was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the implementation guide changes.") value="[dateTime[](datatypes.html#dateTime)]"/><!-- **0..1** Date last changed[](terminologies.html#unbound) -->
 <[**publisher**](implementationguide-definitions.html#ImplementationGuide.publisher "The name of the organization or individual that published the implementation guide.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Name of the publisher (organization or individual)[](terminologies.html#unbound) -->
 <[**contact**](implementationguide-definitions.html#ImplementationGuide.contact "Contact details to assist a user in finding and communicating with the publisher.")><!-- **0..*** ContactDetail[](metadatatypes.html#ContactDetail) Contact details for the publisher[](terminologies.html#unbound) --></contact>
 <[**description**](implementationguide-definitions.html#ImplementationGuide.description "A free text natural language description of the implementation guide from a consumer's perspective.") value="[markdown[](datatypes.html#markdown)]"/><!-- **0..1** Natural language description of the implementation guide[](terminologies.html#unbound) -->
 <[**useContext**](implementationguide-definitions.html#ImplementationGuide.useContext "The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories \(gender, age, ...\) or may be references to specific programs \(insurance plans, studies, ...\) and may be used to assist with indexing and searching for appropriate implementation guide instances.")><!-- **0..*** UsageContext[](metadatatypes.html#UsageContext) The context that the content is intended to support[](terminologies.html#unbound) --></useContext>
 <[**jurisdiction**](implementationguide-definitions.html#ImplementationGuide.jurisdiction "A legal or geographic region in which the implementation guide is intended to be used.")><!-- **0..*** CodeableConcept[](datatypes.html#CodeableConcept) Intended jurisdiction for implementation guide (if applicable)[](valueset-jurisdiction.html) --></jurisdiction>
 <[**copyright**](implementationguide-definitions.html#ImplementationGuide.copyright "A copyright statement relating to the implementation guide and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the implementation guide.") value="[markdown[](datatypes.html#markdown)]"/><!-- **0..1** Use and/or publishing restrictions[](terminologies.html#unbound) -->
 <[**packageId**](implementationguide-definitions.html#ImplementationGuide.packageId "The NPM package name for this Implementation Guide, used in the NPM package distribution, which is the primary mechanism by which FHIR based tooling manages IG dependencies. This value must be globally unique, and should be assigned with care.") value="[id[](datatypes.html#id)]"/><!-- **1..1** NPM Package name for IG[](terminologies.html#unbound) -->
 <[**license**](implementationguide-definitions.html#ImplementationGuide.license "The license that applies to this Implementation Guide, using an SPDX license code, or 'not-open-source'.") value="[code[](datatypes.html#code)]"/><!-- **0..1** SPDX license code for this IG (or not-open-source)[](valueset-spdx-license.html) -->
 <[**fhirVersion**](implementationguide-definitions.html#ImplementationGuide.fhirVersion "The version\(s\) of the FHIR specification that this ImplementationGuide targets - e.g. describes how to use. The value of this element is the formal version of the specification, without the revision number, e.g. \[publication\].\[major\].\[minor\], which is 4.0.1. for this version.") value="[code[](datatypes.html#code)]"/><!-- **1..*** FHIR Version(s) this Implementation Guide targets[](valueset-FHIR-version.html) -->
 <[**dependsOn**](implementationguide-definitions.html#ImplementationGuide.dependsOn "Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guides.")>  <!-- **0..*** Another Implementation guide this depends on -->
  <[**uri**](implementationguide-definitions.html#ImplementationGuide.dependsOn.uri "A canonical reference to the Implementation guide for the dependency.")><!-- **1..1** canonical[](datatypes.html#canonical)(ImplementationGuide[](implementationguide.html#ImplementationGuide)) Identity of the IG that this depends on[](terminologies.html#unbound) --></uri>
  <[**packageId**](implementationguide-definitions.html#ImplementationGuide.dependsOn.packageId "The NPM package name for the Implementation Guide that this IG depends on.") value="[id[](datatypes.html#id)]"/><!-- **0..1** NPM Package name for IG this depends on[](terminologies.html#unbound) -->
  <[**version**](implementationguide-definitions.html#ImplementationGuide.dependsOn.version "The version of the IG that is depended on, when the correct version is required to understand the IG correctly.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Version of the IG[](terminologies.html#unbound) -->
 </dependsOn>
 <[**global**](implementationguide-definitions.html#ImplementationGuide.global "A set of profiles that all resources covered by this implementation guide must conform to.")>  <!-- **0..*** Profiles that apply globally -->
  <[**type**](implementationguide-definitions.html#ImplementationGuide.global.type "The type of resource that all instances must conform to.") value="[code[](datatypes.html#code)]"/><!-- **1..1** Type this profile applies to[](valueset-resource-types.html) -->
  <[**profile**](implementationguide-definitions.html#ImplementationGuide.global.profile "A reference to the profile that all instances must conform to.")><!-- **1..1** canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) Profile that all resources must conform to[](terminologies.html#unbound) --></profile>
 </global>
 <[**definition**](implementationguide-definitions.html#ImplementationGuide.definition "The information needed by an IG publisher tool to publish the whole implementation guide.")>  <!-- **0..1** Information needed to build the IG -->
  <[**grouping**](implementationguide-definitions.html#ImplementationGuide.definition.grouping "A logical group of resources. Logical groups can be used when building pages.")>  <!-- **0..*** Grouping used to present related resources in the IG -->
   <[**name**](implementationguide-definitions.html#ImplementationGuide.definition.grouping.name "The human-readable title to display for the package of resources when rendering the implementation guide.") value="[string[](datatypes.html#string)]"/><!-- **1..1** Descriptive name for the package[](terminologies.html#unbound) -->
   <[**description**](implementationguide-definitions.html#ImplementationGuide.definition.grouping.description "Human readable text describing the package.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Human readable text describing the package[](terminologies.html#unbound) -->
  </grouping>
  <[**resource**](implementationguide-definitions.html#ImplementationGuide.definition.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.")>  <!-- **1..*** Resource in the implementation guide -->
   <[**reference**](implementationguide-definitions.html#ImplementationGuide.definition.resource.reference "Where this resource is found.")><!-- **1..1** Reference[](references.html#Reference)(Any[](resourcelist.html)) Location of the resource[](terminologies.html#unbound) --></reference>
   <[**fhirVersion**](implementationguide-definitions.html#ImplementationGuide.definition.resource.fhirVersion "Indicates the FHIR Version\(s\) this artifact is intended to apply to. If no versions are specified, the resource is assumed to apply to all the versions stated in ImplementationGuide.fhirVersion.") value="[code[](datatypes.html#code)]"/><!-- **0..*** Versions this applies to (if different to IG)[](valueset-FHIR-version.html) -->
   <[**name**](implementationguide-definitions.html#ImplementationGuide.definition.resource.name "A human assigned name for the resource. All resources SHOULD have a name, but the name may be extracted from the resource \(e.g. ValueSet.name\).") value="[string[](datatypes.html#string)]"/><!-- **0..1** Human Name for the resource[](terminologies.html#unbound) -->
   <[**description**](implementationguide-definitions.html#ImplementationGuide.definition.resource.description "A description of the reason that a resource has been included in the implementation guide.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Reason why included in guide[](terminologies.html#unbound) -->
   <[**example[x]**](implementationguide-definitions.html#ImplementationGuide.definition.resource.example\[x\] "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")><!-- **0..1** boolean[](datatypes.html#boolean)|canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) Is an example/What is this an example of?[](terminologies.html#unbound) --></example[x]>
   <[**groupingId**](implementationguide-definitions.html#ImplementationGuide.definition.resource.groupingId "Reference to the id of the grouping this resource appears in.") value="[id[](datatypes.html#id)]"/><!-- **0..1** Grouping this is part of[](terminologies.html#unbound) -->
  </resource>
  <[**page**](implementationguide-definitions.html#ImplementationGuide.definition.page "A page / section in the implementation guide. The root page is the implementation guide home page.")>  <!-- **0..1** Page/Section in the Guide -->
   <[**name[x]**](implementationguide-definitions.html#ImplementationGuide.definition.page.name\[x\] "The source address for the page.")><!-- **1..1** url[](datatypes.html#url)|Reference[](references.html#Reference)(Binary[](binary.html#Binary)) Where to find that page[](terminologies.html#unbound) --></name[x]>
   <[**title**](implementationguide-definitions.html#ImplementationGuide.definition.page.title "A short title used to represent this page in navigational structures such as table of contents, bread crumbs, etc.") value="[string[](datatypes.html#string)]"/><!-- **1..1** Short title shown for navigational assistance[](terminologies.html#unbound) -->
   <[**generation**](implementationguide-definitions.html#ImplementationGuide.definition.page.generation "A code that indicates how the page is generated.") value="[code[](datatypes.html#code)]"/><!-- **1..1** html | markdown | xml | generated[](valueset-guide-page-generation.html) -->
   <[**page**](implementationguide-definitions.html#ImplementationGuide.definition.page.page "Nested Pages/Sections under this page.")><!-- **0..*** Content as for ImplementationGuide.definition.page Nested Pages / Sections[](terminologies.html#unbound) --></page>
  </page>
  <[**parameter**](implementationguide-definitions.html#ImplementationGuide.definition.parameter "Defines how IG is built by tools.")>  <!-- **0..*** Defines how IG is built by tools -->
   <[**code**](implementationguide-definitions.html#ImplementationGuide.definition.parameter.code "apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template.") value="[code[](datatypes.html#code)]"/><!-- **1..1** apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template[](valueset-guide-parameter-code.html) -->
   <[**value**](implementationguide-definitions.html#ImplementationGuide.definition.parameter.value "Value for named type.") value="[string[](datatypes.html#string)]"/><!-- **1..1** Value for named type[](terminologies.html#unbound) -->
  </parameter>
  <[**template**](implementationguide-definitions.html#ImplementationGuide.definition.template "A template for building resources.")>  <!-- **0..*** A template for building resources -->
   <[**code**](implementationguide-definitions.html#ImplementationGuide.definition.template.code "Type of template specified.") value="[code[](datatypes.html#code)]"/><!-- **1..1** Type of template specified[](terminologies.html#unbound) -->
   <[**source**](implementationguide-definitions.html#ImplementationGuide.definition.template.source "The source location for the template.") value="[string[](datatypes.html#string)]"/><!-- **1..1** The source location for the template[](terminologies.html#unbound) -->
   <[**scope**](implementationguide-definitions.html#ImplementationGuide.definition.template.scope "The scope in which the template applies.") value="[string[](datatypes.html#string)]"/><!-- **0..1** The scope in which the template applies[](terminologies.html#unbound) -->
  </template>
 </definition>
 <[**manifest**](implementationguide-definitions.html#ImplementationGuide.manifest "Information about an assembled implementation guide, created by the publication tooling.")>  <!-- **0..1** Information about an assembled IG -->
  <[**rendering**](implementationguide-definitions.html#ImplementationGuide.manifest.rendering "A pointer to official web page, PDF or other rendering of the implementation guide.") value="[url[](datatypes.html#url)]"/><!-- **0..1** Location of rendered implementation guide[](terminologies.html#unbound) -->
  <[**resource**](implementationguide-definitions.html#ImplementationGuide.manifest.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.")>  <!-- **1..*** Resource in the implementation guide -->
   <[**reference**](implementationguide-definitions.html#ImplementationGuide.manifest.resource.reference "Where this resource is found.")><!-- **1..1** Reference[](references.html#Reference)(Any[](resourcelist.html)) Location of the resource[](terminologies.html#unbound) --></reference>
   <[**example[x]**](implementationguide-definitions.html#ImplementationGuide.manifest.resource.example\[x\] "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")><!-- **0..1** boolean[](datatypes.html#boolean)|canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) Is an example/What is this an example of?[](terminologies.html#unbound) --></example[x]>
   <[**relativePath**](implementationguide-definitions.html#ImplementationGuide.manifest.resource.relativePath "The relative path for primary page for this resource within the IG.") value="[url[](datatypes.html#url)]"/><!-- **0..1** Relative path for page in IG[](terminologies.html#unbound) -->
  </resource>
  <[**page**](implementationguide-definitions.html#ImplementationGuide.manifest.page "Information about a page within the IG.")>  <!-- **0..*** HTML page within the parent IG -->
   <[**name**](implementationguide-definitions.html#ImplementationGuide.manifest.page.name "Relative path to the page.") value="[string[](datatypes.html#string)]"/><!-- **1..1** HTML page name[](terminologies.html#unbound) -->
   <[**title**](implementationguide-definitions.html#ImplementationGuide.manifest.page.title "Label for the page intended for human display.") value="[string[](datatypes.html#string)]"/><!-- **0..1** Title of the page, for references[](terminologies.html#unbound) -->
   <[**anchor**](implementationguide-definitions.html#ImplementationGuide.manifest.page.anchor "The name of an anchor available on the page.") value="[string[](datatypes.html#string)]"/><!-- **0..*** Anchor available on the page[](terminologies.html#unbound) -->
  </page>
  <[**image**](implementationguide-definitions.html#ImplementationGuide.manifest.image "Indicates a relative path to an image that exists within the IG.") value="[string[](datatypes.html#string)]"/><!-- **0..*** Image within the IG[](terminologies.html#unbound) -->
  <[**other**](implementationguide-definitions.html#ImplementationGuide.manifest.other "Indicates the relative path of an additional non-page, non-image file that is part of the IG - e.g. zip, jar and similar files that could be the target of a hyperlink in a derived IG.") value="[string[](datatypes.html#string)]"/><!-- **0..*** Additional linkable file in IG[](terminologies.html#unbound) -->
 </manifest>
</ImplementationGuide>

```

**JSON Template**
```

{[![doco](help.png)](json.html "Documentation for this format")
  "resourceType" : "[**ImplementationGuide**](implementationguide-definitions.html#ImplementationGuide "A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.")",
  // from Resource[](resource.html): id[](resource.html#id), meta[](resource.html#meta), implicitRules[](resource.html#implicitRules), and language[](resource.html#language)
  // from DomainResource[](domainresource.html): text[](narrative.html#Narrative), contained[](references.html#contained), extension[](extensibility.html), and modifierExtension[](extensibility.html#modifierExtension)
  "url[](implementationguide-definitions.html#ImplementationGuide.url "An absolute URI that is used to identify this implementation guide when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this implementation guide is \(or will be\) published. This URL can be the target of a canonical reference. It SHALL remain the same when the implementation guide is stored on different servers.")" : "<uri[](datatypes.html#uri)>", // **R!**  Canonical identifier for this implementation guide, represented as a URI (globally unique)[](terminologies.html#unbound)
  "version[](implementationguide-definitions.html#ImplementationGuide.version "The identifier that is used to identify this version of the implementation guide when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the implementation guide author and is not expected to be globally unique. For example, it might be a timestamp \(e.g. yyyymmdd\) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.")" : "<string[](datatypes.html#string)>", // Business version of the implementation guide[](terminologies.html#unbound)
  "name[](implementationguide-definitions.html#ImplementationGuide.name "A natural language name identifying the implementation guide. This name should be usable as an identifier for the module by machine processing applications such as code generation.")" : "<string[](datatypes.html#string)>", // **C?** **R!**  Name for this implementation guide (computer friendly)[](terminologies.html#unbound)
  "title[](implementationguide-definitions.html#ImplementationGuide.title "A short, descriptive, user-friendly title for the implementation guide.")" : "<string[](datatypes.html#string)>", // Name for this implementation guide (human friendly)[](terminologies.html#unbound)
  "[status](implementationguide-definitions.html#ImplementationGuide.status "The status of this implementation guide. Enables tracking the life-cycle of the content \(this element modifies the meaning of other elements\)")" : "<code[](datatypes.html#code)>", // **R!**  draft | active | retired | unknown[](valueset-publication-status.html)
  "experimental[](implementationguide-definitions.html#ImplementationGuide.experimental "A Boolean value to indicate that this implementation guide is authored for testing purposes \(or education/evaluation/marketing\) and is not intended to be used for genuine usage.")" : <boolean[](datatypes.html#boolean)>, // For testing purposes, not real usage[](terminologies.html#unbound)
  "date[](implementationguide-definitions.html#ImplementationGuide.date "The date  \(and optionally time\) when the implementation guide was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the implementation guide changes.")" : "<dateTime[](datatypes.html#dateTime)>", // Date last changed[](terminologies.html#unbound)
  "publisher[](implementationguide-definitions.html#ImplementationGuide.publisher "The name of the organization or individual that published the implementation guide.")" : "<string[](datatypes.html#string)>", // Name of the publisher (organization or individual)[](terminologies.html#unbound)
  "contact[](implementationguide-definitions.html#ImplementationGuide.contact "Contact details to assist a user in finding and communicating with the publisher.")" : [{ ContactDetail[](metadatatypes.html#ContactDetail) }], // Contact details for the publisher[](terminologies.html#unbound)
  "description[](implementationguide-definitions.html#ImplementationGuide.description "A free text natural language description of the implementation guide from a consumer's perspective.")" : "<markdown[](datatypes.html#markdown)>", // Natural language description of the implementation guide[](terminologies.html#unbound)
  "useContext[](implementationguide-definitions.html#ImplementationGuide.useContext "The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories \(gender, age, ...\) or may be references to specific programs \(insurance plans, studies, ...\) and may be used to assist with indexing and searching for appropriate implementation guide instances.")" : [{ UsageContext[](metadatatypes.html#UsageContext) }], // The context that the content is intended to support[](terminologies.html#unbound)
  "jurisdiction[](implementationguide-definitions.html#ImplementationGuide.jurisdiction "A legal or geographic region in which the implementation guide is intended to be used.")" : [{ CodeableConcept[](datatypes.html#CodeableConcept) }], // Intended jurisdiction for implementation guide (if applicable)[](valueset-jurisdiction.html)
  "copyright[](implementationguide-definitions.html#ImplementationGuide.copyright "A copyright statement relating to the implementation guide and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the implementation guide.")" : "<markdown[](datatypes.html#markdown)>", // Use and/or publishing restrictions[](terminologies.html#unbound)
  "packageId[](implementationguide-definitions.html#ImplementationGuide.packageId "The NPM package name for this Implementation Guide, used in the NPM package distribution, which is the primary mechanism by which FHIR based tooling manages IG dependencies. This value must be globally unique, and should be assigned with care.")" : "<id[](datatypes.html#id)>", // **R!**  NPM Package name for IG[](terminologies.html#unbound)
  "license[](implementationguide-definitions.html#ImplementationGuide.license "The license that applies to this Implementation Guide, using an SPDX license code, or 'not-open-source'.")" : "<code[](datatypes.html#code)>", // SPDX license code for this IG (or not-open-source)[](valueset-spdx-license.html)
  "fhirVersion[](implementationguide-definitions.html#ImplementationGuide.fhirVersion "The version\(s\) of the FHIR specification that this ImplementationGuide targets - e.g. describes how to use. The value of this element is the formal version of the specification, without the revision number, e.g. \[publication\].\[major\].\[minor\], which is 4.0.1. for this version.")" : ["<code[](datatypes.html#code)>"], // **R!**  FHIR Version(s) this Implementation Guide targets[](valueset-FHIR-version.html)
  "dependsOn[](implementationguide-definitions.html#ImplementationGuide.dependsOn "Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guides.")" : [{ // Another Implementation guide this depends on[](terminologies.html#unbound)
    "uri[](implementationguide-definitions.html#ImplementationGuide.dependsOn.uri "A canonical reference to the Implementation guide for the dependency.")" : { canonical[](datatypes.html#canonical)(ImplementationGuide[](implementationguide.html#ImplementationGuide)) }, // **R!**  Identity of the IG that this depends on[](terminologies.html#unbound)
    "packageId[](implementationguide-definitions.html#ImplementationGuide.dependsOn.packageId "The NPM package name for the Implementation Guide that this IG depends on.")" : "<id[](datatypes.html#id)>", // NPM Package name for IG this depends on[](terminologies.html#unbound)
    "version[](implementationguide-definitions.html#ImplementationGuide.dependsOn.version "The version of the IG that is depended on, when the correct version is required to understand the IG correctly.")" : "<string[](datatypes.html#string)>" // Version of the IG[](terminologies.html#unbound)
  }],
  "global[](implementationguide-definitions.html#ImplementationGuide.global "A set of profiles that all resources covered by this implementation guide must conform to.")" : [{ // Profiles that apply globally[](terminologies.html#unbound)
    "type[](implementationguide-definitions.html#ImplementationGuide.global.type "The type of resource that all instances must conform to.")" : "<code[](datatypes.html#code)>", // **R!**  Type this profile applies to[](valueset-resource-types.html)
    "profile[](implementationguide-definitions.html#ImplementationGuide.global.profile "A reference to the profile that all instances must conform to.")" : { canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) } // **R!**  Profile that all resources must conform to[](terminologies.html#unbound)
  }],
  "definition[](implementationguide-definitions.html#ImplementationGuide.definition "The information needed by an IG publisher tool to publish the whole implementation guide.")" : { // Information needed to build the IG[](terminologies.html#unbound)
    "grouping[](implementationguide-definitions.html#ImplementationGuide.definition.grouping "A logical group of resources. Logical groups can be used when building pages.")" : [{ // Grouping used to present related resources in the IG[](terminologies.html#unbound)
      "name[](implementationguide-definitions.html#ImplementationGuide.definition.grouping.name "The human-readable title to display for the package of resources when rendering the implementation guide.")" : "<string[](datatypes.html#string)>", // **R!**  Descriptive name for the package[](terminologies.html#unbound)
      "description[](implementationguide-definitions.html#ImplementationGuide.definition.grouping.description "Human readable text describing the package.")" : "<string[](datatypes.html#string)>" // Human readable text describing the package[](terminologies.html#unbound)
    }],
    "resource[](implementationguide-definitions.html#ImplementationGuide.definition.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.")" : [{ // **R!**  Resource in the implementation guide[](terminologies.html#unbound)
      "reference[](implementationguide-definitions.html#ImplementationGuide.definition.resource.reference "Where this resource is found.")" : { Reference[](references.html#Reference)(Any[](resourcelist.html)) }, // **R!**  Location of the resource[](terminologies.html#unbound)
      "fhirVersion[](implementationguide-definitions.html#ImplementationGuide.definition.resource.fhirVersion "Indicates the FHIR Version\(s\) this artifact is intended to apply to. If no versions are specified, the resource is assumed to apply to all the versions stated in ImplementationGuide.fhirVersion.")" : ["<code[](datatypes.html#code)>"], // Versions this applies to (if different to IG)[](valueset-FHIR-version.html)
      "name[](implementationguide-definitions.html#ImplementationGuide.definition.resource.name "A human assigned name for the resource. All resources SHOULD have a name, but the name may be extracted from the resource \(e.g. ValueSet.name\).")" : "<string[](datatypes.html#string)>", // Human Name for the resource[](terminologies.html#unbound)
      "description[](implementationguide-definitions.html#ImplementationGuide.definition.resource.description "A description of the reason that a resource has been included in the implementation guide.")" : "<string[](datatypes.html#string)>", // Reason why included in guide[](terminologies.html#unbound)
      // example[x]: Is an example/What is this an example of?. One of these 2:
      "exampleBoolean[](implementationguide-definitions.html#ImplementationGuide.definition.resource.exampleBoolean "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")" : <boolean[](datatypes.html#boolean)>,
      "exampleCanonical[](implementationguide-definitions.html#ImplementationGuide.definition.resource.exampleCanonical "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")" : { canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) },
      "groupingId[](implementationguide-definitions.html#ImplementationGuide.definition.resource.groupingId "Reference to the id of the grouping this resource appears in.")" : "<id[](datatypes.html#id)>" // Grouping this is part of[](terminologies.html#unbound)
    }],
    "page[](implementationguide-definitions.html#ImplementationGuide.definition.page "A page / section in the implementation guide. The root page is the implementation guide home page.")" : { // Page/Section in the Guide[](terminologies.html#unbound)
      // name[x]: Where to find that page. One of these 2:
      "nameUrl[](implementationguide-definitions.html#ImplementationGuide.definition.page.nameUrl "The source address for the page.")" : "<url[](datatypes.html#url)>",
      "nameReference[](implementationguide-definitions.html#ImplementationGuide.definition.page.nameReference "The source address for the page.")" : { Reference[](references.html#Reference)(Binary[](binary.html#Binary)) },
      "title[](implementationguide-definitions.html#ImplementationGuide.definition.page.title "A short title used to represent this page in navigational structures such as table of contents, bread crumbs, etc.")" : "<string[](datatypes.html#string)>", // **R!**  Short title shown for navigational assistance[](terminologies.html#unbound)
      "generation[](implementationguide-definitions.html#ImplementationGuide.definition.page.generation "A code that indicates how the page is generated.")" : "<code[](datatypes.html#code)>", // **R!**  html | markdown | xml | generated[](valueset-guide-page-generation.html)
      "page[](implementationguide-definitions.html#ImplementationGuide.definition.page.page "Nested Pages/Sections under this page.")" : [{ Content as for ImplementationGuide.definition.page }] // Nested Pages / Sections[](terminologies.html#unbound)
    },
    "parameter[](implementationguide-definitions.html#ImplementationGuide.definition.parameter "Defines how IG is built by tools.")" : [{ // Defines how IG is built by tools[](terminologies.html#unbound)
      "code[](implementationguide-definitions.html#ImplementationGuide.definition.parameter.code "apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template.")" : "<code[](datatypes.html#code)>", // **R!**  apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template[](valueset-guide-parameter-code.html)
      "value[](implementationguide-definitions.html#ImplementationGuide.definition.parameter.value "Value for named type.")" : "<string[](datatypes.html#string)>" // **R!**  Value for named type[](terminologies.html#unbound)
    }],
    "template[](implementationguide-definitions.html#ImplementationGuide.definition.template "A template for building resources.")" : [{ // A template for building resources[](terminologies.html#unbound)
      "code[](implementationguide-definitions.html#ImplementationGuide.definition.template.code "Type of template specified.")" : "<code[](datatypes.html#code)>", // **R!**  Type of template specified[](terminologies.html#unbound)
      "source[](implementationguide-definitions.html#ImplementationGuide.definition.template.source "The source location for the template.")" : "<string[](datatypes.html#string)>", // **R!**  The source location for the template[](terminologies.html#unbound)
      "scope[](implementationguide-definitions.html#ImplementationGuide.definition.template.scope "The scope in which the template applies.")" : "<string[](datatypes.html#string)>" // The scope in which the template applies[](terminologies.html#unbound)
    }]
  },
  "manifest[](implementationguide-definitions.html#ImplementationGuide.manifest "Information about an assembled implementation guide, created by the publication tooling.")" : { // Information about an assembled IG[](terminologies.html#unbound)
    "rendering[](implementationguide-definitions.html#ImplementationGuide.manifest.rendering "A pointer to official web page, PDF or other rendering of the implementation guide.")" : "<url[](datatypes.html#url)>", // Location of rendered implementation guide[](terminologies.html#unbound)
    "resource[](implementationguide-definitions.html#ImplementationGuide.manifest.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.")" : [{ // **R!**  Resource in the implementation guide[](terminologies.html#unbound)
      "reference[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.reference "Where this resource is found.")" : { Reference[](references.html#Reference)(Any[](resourcelist.html)) }, // **R!**  Location of the resource[](terminologies.html#unbound)
      // example[x]: Is an example/What is this an example of?. One of these 2:
      "exampleBoolean[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.exampleBoolean "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")" : <boolean[](datatypes.html#boolean)>,
      "exampleCanonical[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.exampleCanonical "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.")" : { canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) },
      "relativePath[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.relativePath "The relative path for primary page for this resource within the IG.")" : "<url[](datatypes.html#url)>" // Relative path for page in IG[](terminologies.html#unbound)
    }],
    "page[](implementationguide-definitions.html#ImplementationGuide.manifest.page "Information about a page within the IG.")" : [{ // HTML page within the parent IG[](terminologies.html#unbound)
      "name[](implementationguide-definitions.html#ImplementationGuide.manifest.page.name "Relative path to the page.")" : "<string[](datatypes.html#string)>", // **R!**  HTML page name[](terminologies.html#unbound)
      "title[](implementationguide-definitions.html#ImplementationGuide.manifest.page.title "Label for the page intended for human display.")" : "<string[](datatypes.html#string)>", // Title of the page, for references[](terminologies.html#unbound)
      "anchor[](implementationguide-definitions.html#ImplementationGuide.manifest.page.anchor "The name of an anchor available on the page.")" : ["<string[](datatypes.html#string)>"] // Anchor available on the page[](terminologies.html#unbound)
    }],
    "image[](implementationguide-definitions.html#ImplementationGuide.manifest.image "Indicates a relative path to an image that exists within the IG.")" : ["<string[](datatypes.html#string)>"], // Image within the IG[](terminologies.html#unbound)
    "other[](implementationguide-definitions.html#ImplementationGuide.manifest.other "Indicates the relative path of an additional non-page, non-image file that is part of the IG - e.g. zip, jar and similar files that could be the target of a hyperlink in a derived IG.")" : ["<string[](datatypes.html#string)>"] // Additional linkable file in IG[](terminologies.html#unbound)
  }
}

```

**Turtle Template**
```

@prefix fhir: <http://hl7.org/fhir/> .[![doco](help.png)](rdf.html "Documentation for this format")


[ a fhir:[**ImplementationGuide**](implementationguide-definitions.html#ImplementationGuide "A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.");
  fhir:nodeRole fhir:treeRoot; # if this is the parser root

  # from Resource[](resource.html): .id[](resource.html#id), .meta[](resource.html#meta), .implicitRules[](resource.html#implicitRules), and .language[](resource.html#language)
  # from DomainResource[](domainresource.html): .text[](narrative.html#Narrative), .contained[](references.html#contained), .extension[](extensibility.html), and .modifierExtension[](extensibility.html#modifierExtension)
  fhir:ImplementationGuide.url[](implementationguide-definitions.html#ImplementationGuide.url "An absolute URI that is used to identify this implementation guide when it is referenced in a specification, model, design or an instance; also called its canonical identifier. This SHOULD be globally unique and SHOULD be a literal address at which at which an authoritative instance of this implementation guide is \(or will be\) published. This URL can be the target of a canonical reference. It SHALL remain the same when the implementation guide is stored on different servers.") [ uri[](datatypes.html#uri) ]; # 1..1 Canonical identifier for this implementation guide, represented as a URI (globally unique)
  fhir:ImplementationGuide.version[](implementationguide-definitions.html#ImplementationGuide.version "The identifier that is used to identify this version of the implementation guide when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the implementation guide author and is not expected to be globally unique. For example, it might be a timestamp \(e.g. yyyymmdd\) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.") [ string[](datatypes.html#string) ]; # 0..1 Business version of the implementation guide
  fhir:ImplementationGuide.name[](implementationguide-definitions.html#ImplementationGuide.name "A natural language name identifying the implementation guide. This name should be usable as an identifier for the module by machine processing applications such as code generation.") [ string[](datatypes.html#string) ]; # 1..1 Name for this implementation guide (computer friendly)
  fhir:ImplementationGuide.title[](implementationguide-definitions.html#ImplementationGuide.title "A short, descriptive, user-friendly title for the implementation guide.") [ string[](datatypes.html#string) ]; # 0..1 Name for this implementation guide (human friendly)
  fhir:[ImplementationGuide.status](implementationguide-definitions.html#ImplementationGuide.status "The status of this implementation guide. Enables tracking the life-cycle of the content \(this element modifies the meaning of other elements\)") [ code[](datatypes.html#code) ]; # 1..1 draft | active | retired | unknown
  fhir:ImplementationGuide.experimental[](implementationguide-definitions.html#ImplementationGuide.experimental "A Boolean value to indicate that this implementation guide is authored for testing purposes \(or education/evaluation/marketing\) and is not intended to be used for genuine usage.") [ boolean[](datatypes.html#boolean) ]; # 0..1 For testing purposes, not real usage
  fhir:ImplementationGuide.date[](implementationguide-definitions.html#ImplementationGuide.date "The date  \(and optionally time\) when the implementation guide was published. The date must change when the business version changes and it must change if the status code changes. In addition, it should change when the substantive content of the implementation guide changes.") [ dateTime[](datatypes.html#dateTime) ]; # 0..1 Date last changed
  fhir:ImplementationGuide.publisher[](implementationguide-definitions.html#ImplementationGuide.publisher "The name of the organization or individual that published the implementation guide.") [ string[](datatypes.html#string) ]; # 0..1 Name of the publisher (organization or individual)
  fhir:ImplementationGuide.contact[](implementationguide-definitions.html#ImplementationGuide.contact "Contact details to assist a user in finding and communicating with the publisher.") [ ContactDetail[](metadatatypes.html#ContactDetail) ], ... ; # 0..* Contact details for the publisher
  fhir:ImplementationGuide.description[](implementationguide-definitions.html#ImplementationGuide.description "A free text natural language description of the implementation guide from a consumer's perspective.") [ markdown[](datatypes.html#markdown) ]; # 0..1 Natural language description of the implementation guide
  fhir:ImplementationGuide.useContext[](implementationguide-definitions.html#ImplementationGuide.useContext "The content was developed with a focus and intent of supporting the contexts that are listed. These contexts may be general categories \(gender, age, ...\) or may be references to specific programs \(insurance plans, studies, ...\) and may be used to assist with indexing and searching for appropriate implementation guide instances.") [ UsageContext[](metadatatypes.html#UsageContext) ], ... ; # 0..* The context that the content is intended to support
  fhir:ImplementationGuide.jurisdiction[](implementationguide-definitions.html#ImplementationGuide.jurisdiction "A legal or geographic region in which the implementation guide is intended to be used.") [ CodeableConcept[](datatypes.html#CodeableConcept) ], ... ; # 0..* Intended jurisdiction for implementation guide (if applicable)
  fhir:ImplementationGuide.copyright[](implementationguide-definitions.html#ImplementationGuide.copyright "A copyright statement relating to the implementation guide and/or its contents. Copyright statements are generally legal restrictions on the use and publishing of the implementation guide.") [ markdown[](datatypes.html#markdown) ]; # 0..1 Use and/or publishing restrictions
  fhir:ImplementationGuide.packageId[](implementationguide-definitions.html#ImplementationGuide.packageId "The NPM package name for this Implementation Guide, used in the NPM package distribution, which is the primary mechanism by which FHIR based tooling manages IG dependencies. This value must be globally unique, and should be assigned with care.") [ id[](datatypes.html#id) ]; # 1..1 NPM Package name for IG
  fhir:ImplementationGuide.license[](implementationguide-definitions.html#ImplementationGuide.license "The license that applies to this Implementation Guide, using an SPDX license code, or 'not-open-source'.") [ code[](datatypes.html#code) ]; # 0..1 SPDX license code for this IG (or not-open-source)
  fhir:ImplementationGuide.fhirVersion[](implementationguide-definitions.html#ImplementationGuide.fhirVersion "The version\(s\) of the FHIR specification that this ImplementationGuide targets - e.g. describes how to use. The value of this element is the formal version of the specification, without the revision number, e.g. \[publication\].\[major\].\[minor\], which is 4.0.1. for this version.") [ code[](datatypes.html#code) ], ... ; # 1..* FHIR Version(s) this Implementation Guide targets
  fhir:ImplementationGuide.dependsOn[](implementationguide-definitions.html#ImplementationGuide.dependsOn "Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guides.") [ # 0..* Another Implementation guide this depends on
    fhir:ImplementationGuide.dependsOn.uri[](implementationguide-definitions.html#ImplementationGuide.dependsOn.uri "A canonical reference to the Implementation guide for the dependency.") [ canonical[](datatypes.html#canonical)(ImplementationGuide[](implementationguide.html#ImplementationGuide)) ]; # 1..1 Identity of the IG that this depends on
    fhir:ImplementationGuide.dependsOn.packageId[](implementationguide-definitions.html#ImplementationGuide.dependsOn.packageId "The NPM package name for the Implementation Guide that this IG depends on.") [ id[](datatypes.html#id) ]; # 0..1 NPM Package name for IG this depends on
    fhir:ImplementationGuide.dependsOn.version[](implementationguide-definitions.html#ImplementationGuide.dependsOn.version "The version of the IG that is depended on, when the correct version is required to understand the IG correctly.") [ string[](datatypes.html#string) ]; # 0..1 Version of the IG
  ], ...;
  fhir:ImplementationGuide.global[](implementationguide-definitions.html#ImplementationGuide.global "A set of profiles that all resources covered by this implementation guide must conform to.") [ # 0..* Profiles that apply globally
    fhir:ImplementationGuide.global.type[](implementationguide-definitions.html#ImplementationGuide.global.type "The type of resource that all instances must conform to.") [ code[](datatypes.html#code) ]; # 1..1 Type this profile applies to
    fhir:ImplementationGuide.global.profile[](implementationguide-definitions.html#ImplementationGuide.global.profile "A reference to the profile that all instances must conform to.") [ canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) ]; # 1..1 Profile that all resources must conform to
  ], ...;
  fhir:ImplementationGuide.definition[](implementationguide-definitions.html#ImplementationGuide.definition "The information needed by an IG publisher tool to publish the whole implementation guide.") [ # 0..1 Information needed to build the IG
    fhir:ImplementationGuide.definition.grouping[](implementationguide-definitions.html#ImplementationGuide.definition.grouping "A logical group of resources. Logical groups can be used when building pages.") [ # 0..* Grouping used to present related resources in the IG
      fhir:ImplementationGuide.definition.grouping.name[](implementationguide-definitions.html#ImplementationGuide.definition.grouping.name "The human-readable title to display for the package of resources when rendering the implementation guide.") [ string[](datatypes.html#string) ]; # 1..1 Descriptive name for the package
      fhir:ImplementationGuide.definition.grouping.description[](implementationguide-definitions.html#ImplementationGuide.definition.grouping.description "Human readable text describing the package.") [ string[](datatypes.html#string) ]; # 0..1 Human readable text describing the package
    ], ...;
    fhir:ImplementationGuide.definition.resource[](implementationguide-definitions.html#ImplementationGuide.definition.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.") [ # 1..* Resource in the implementation guide
      fhir:ImplementationGuide.definition.resource.reference[](implementationguide-definitions.html#ImplementationGuide.definition.resource.reference "Where this resource is found.") [ Reference[](references.html#Reference)(Any[](resourcelist.html)) ]; # 1..1 Location of the resource
      fhir:ImplementationGuide.definition.resource.fhirVersion[](implementationguide-definitions.html#ImplementationGuide.definition.resource.fhirVersion "Indicates the FHIR Version\(s\) this artifact is intended to apply to. If no versions are specified, the resource is assumed to apply to all the versions stated in ImplementationGuide.fhirVersion.") [ code[](datatypes.html#code) ], ... ; # 0..* Versions this applies to (if different to IG)
      fhir:ImplementationGuide.definition.resource.name[](implementationguide-definitions.html#ImplementationGuide.definition.resource.name "A human assigned name for the resource. All resources SHOULD have a name, but the name may be extracted from the resource \(e.g. ValueSet.name\).") [ string[](datatypes.html#string) ]; # 0..1 Human Name for the resource
      fhir:ImplementationGuide.definition.resource.description[](implementationguide-definitions.html#ImplementationGuide.definition.resource.description "A description of the reason that a resource has been included in the implementation guide.") [ string[](datatypes.html#string) ]; # 0..1 Reason why included in guide
      # ImplementationGuide.definition.resource.example[x][](implementationguide-definitions.html#ImplementationGuide.definition.resource.example\[x\] "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") : 0..1 Is an example/What is this an example of?. One of these 2
        fhir:ImplementationGuide.definition.resource.exampleBoolean[](implementationguide-definitions.html#ImplementationGuide.definition.resource.exampleBoolean "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") [ boolean[](datatypes.html#boolean) ]
        fhir:ImplementationGuide.definition.resource.exampleCanonical[](implementationguide-definitions.html#ImplementationGuide.definition.resource.exampleCanonical "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") [ canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) ]
      fhir:ImplementationGuide.definition.resource.groupingId[](implementationguide-definitions.html#ImplementationGuide.definition.resource.groupingId "Reference to the id of the grouping this resource appears in.") [ id[](datatypes.html#id) ]; # 0..1 Grouping this is part of
    ], ...;
    fhir:ImplementationGuide.definition.page[](implementationguide-definitions.html#ImplementationGuide.definition.page "A page / section in the implementation guide. The root page is the implementation guide home page.") [ # 0..1 Page/Section in the Guide
      # ImplementationGuide.definition.page.name[x][](implementationguide-definitions.html#ImplementationGuide.definition.page.name\[x\] "The source address for the page.") : 1..1 Where to find that page. One of these 2
        fhir:ImplementationGuide.definition.page.nameUrl[](implementationguide-definitions.html#ImplementationGuide.definition.page.nameUrl "The source address for the page.") [ url[](datatypes.html#url) ]
        fhir:ImplementationGuide.definition.page.nameReference[](implementationguide-definitions.html#ImplementationGuide.definition.page.nameReference "The source address for the page.") [ Reference[](references.html#Reference)(Binary[](binary.html#Binary)) ]
      fhir:ImplementationGuide.definition.page.title[](implementationguide-definitions.html#ImplementationGuide.definition.page.title "A short title used to represent this page in navigational structures such as table of contents, bread crumbs, etc.") [ string[](datatypes.html#string) ]; # 1..1 Short title shown for navigational assistance
      fhir:ImplementationGuide.definition.page.generation[](implementationguide-definitions.html#ImplementationGuide.definition.page.generation "A code that indicates how the page is generated.") [ code[](datatypes.html#code) ]; # 1..1 html | markdown | xml | generated
      fhir:ImplementationGuide.definition.page.page[](implementationguide-definitions.html#ImplementationGuide.definition.page.page "Nested Pages/Sections under this page.") [ [See ImplementationGuide.definition.page](#ttl-ImplementationGuide.definition.page) ], ... ; # 0..* Nested Pages / Sections
    ];
    fhir:ImplementationGuide.definition.parameter[](implementationguide-definitions.html#ImplementationGuide.definition.parameter "Defines how IG is built by tools.") [ # 0..* Defines how IG is built by tools
      fhir:ImplementationGuide.definition.parameter.code[](implementationguide-definitions.html#ImplementationGuide.definition.parameter.code "apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template.") [ code[](datatypes.html#code) ]; # 1..1 apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template
      fhir:ImplementationGuide.definition.parameter.value[](implementationguide-definitions.html#ImplementationGuide.definition.parameter.value "Value for named type.") [ string[](datatypes.html#string) ]; # 1..1 Value for named type
    ], ...;
    fhir:ImplementationGuide.definition.template[](implementationguide-definitions.html#ImplementationGuide.definition.template "A template for building resources.") [ # 0..* A template for building resources
      fhir:ImplementationGuide.definition.template.code[](implementationguide-definitions.html#ImplementationGuide.definition.template.code "Type of template specified.") [ code[](datatypes.html#code) ]; # 1..1 Type of template specified
      fhir:ImplementationGuide.definition.template.source[](implementationguide-definitions.html#ImplementationGuide.definition.template.source "The source location for the template.") [ string[](datatypes.html#string) ]; # 1..1 The source location for the template
      fhir:ImplementationGuide.definition.template.scope[](implementationguide-definitions.html#ImplementationGuide.definition.template.scope "The scope in which the template applies.") [ string[](datatypes.html#string) ]; # 0..1 The scope in which the template applies
    ], ...;
  ];
  fhir:ImplementationGuide.manifest[](implementationguide-definitions.html#ImplementationGuide.manifest "Information about an assembled implementation guide, created by the publication tooling.") [ # 0..1 Information about an assembled IG
    fhir:ImplementationGuide.manifest.rendering[](implementationguide-definitions.html#ImplementationGuide.manifest.rendering "A pointer to official web page, PDF or other rendering of the implementation guide.") [ url[](datatypes.html#url) ]; # 0..1 Location of rendered implementation guide
    fhir:ImplementationGuide.manifest.resource[](implementationguide-definitions.html#ImplementationGuide.manifest.resource "A resource that is part of the implementation guide. Conformance resources \(value set, structure definition, capability statements etc.\) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.") [ # 1..* Resource in the implementation guide
      fhir:ImplementationGuide.manifest.resource.reference[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.reference "Where this resource is found.") [ Reference[](references.html#Reference)(Any[](resourcelist.html)) ]; # 1..1 Location of the resource
      # ImplementationGuide.manifest.resource.example[x][](implementationguide-definitions.html#ImplementationGuide.manifest.resource.example\[x\] "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") : 0..1 Is an example/What is this an example of?. One of these 2
        fhir:ImplementationGuide.manifest.resource.exampleBoolean[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.exampleBoolean "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") [ boolean[](datatypes.html#boolean) ]
        fhir:ImplementationGuide.manifest.resource.exampleCanonical[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.exampleCanonical "If true or a reference, indicates the resource is an example instance.  If a reference is present, indicates that the example is an example of the specified profile.") [ canonical[](datatypes.html#canonical)(StructureDefinition[](structuredefinition.html#StructureDefinition)) ]
      fhir:ImplementationGuide.manifest.resource.relativePath[](implementationguide-definitions.html#ImplementationGuide.manifest.resource.relativePath "The relative path for primary page for this resource within the IG.") [ url[](datatypes.html#url) ]; # 0..1 Relative path for page in IG
    ], ...;
    fhir:ImplementationGuide.manifest.page[](implementationguide-definitions.html#ImplementationGuide.manifest.page "Information about a page within the IG.") [ # 0..* HTML page within the parent IG
      fhir:ImplementationGuide.manifest.page.name[](implementationguide-definitions.html#ImplementationGuide.manifest.page.name "Relative path to the page.") [ string[](datatypes.html#string) ]; # 1..1 HTML page name
      fhir:ImplementationGuide.manifest.page.title[](implementationguide-definitions.html#ImplementationGuide.manifest.page.title "Label for the page intended for human display.") [ string[](datatypes.html#string) ]; # 0..1 Title of the page, for references
      fhir:ImplementationGuide.manifest.page.anchor[](implementationguide-definitions.html#ImplementationGuide.manifest.page.anchor "The name of an anchor available on the page.") [ string[](datatypes.html#string) ], ... ; # 0..* Anchor available on the page
    ], ...;
    fhir:ImplementationGuide.manifest.image[](implementationguide-definitions.html#ImplementationGuide.manifest.image "Indicates a relative path to an image that exists within the IG.") [ string[](datatypes.html#string) ], ... ; # 0..* Image within the IG
    fhir:ImplementationGuide.manifest.other[](implementationguide-definitions.html#ImplementationGuide.manifest.other "Indicates the relative path of an additional non-page, non-image file that is part of the IG - e.g. zip, jar and similar files that could be the target of a hyperlink in a derived IG.") [ string[](datatypes.html#string) ], ... ; # 0..* Additional linkable file in IG
  ];
]

```

**Changes since Release 3**
[ImplementationGuide](implementationguide.html#ImplementationGuide) |   
---|---  
ImplementationGuide | 
  * Min Cardinality changed from 1 to 0
  * Max Cardinality changed from 1 to *

  
ImplementationGuide.title | 
  * Added Element

  
ImplementationGuide.status | 
  * Change value set from http://hl7.org/fhir/ValueSet/publication-status to http://hl7.org/fhir/ValueSet/publication-status|4.0.1

  
ImplementationGuide.experimental | 
  * No longer marked as Modifier

  
ImplementationGuide.packageId | 
  * **Added Mandatory Element**

  
ImplementationGuide.license | 
  * Added Element

  
ImplementationGuide.fhirVersion | 
  * Min Cardinality changed from 0 to 1
  * Max Cardinality changed from 1 to *
  * Type changed from id to code
  * Add Binding `http://hl7.org/fhir/ValueSet/FHIR-version|4.0.1` (required) 

  
ImplementationGuide.dependsOn | 
  * Renamed from dependency to dependsOn

  
ImplementationGuide.dependsOn.uri | 
  * Moved from ImplementationGuide.dependency to ImplementationGuide.dependsOn
  * Type changed from uri to canonical(ImplementationGuide)

  
ImplementationGuide.dependsOn.packageId | 
  * Added Element

  
ImplementationGuide.dependsOn.version | 
  * Added Element

  
ImplementationGuide.global.type | 
  * Change value set from http://hl7.org/fhir/ValueSet/resource-types to http://hl7.org/fhir/ValueSet/resource-types|4.0.1

  
ImplementationGuide.global.profile | 
  * Type changed from Reference(StructureDefinition) to canonical(StructureDefinition)

  
ImplementationGuide.definition | 
  * Added Element

  
ImplementationGuide.definition.grouping | 
  * Added Element

  
ImplementationGuide.definition.grouping.name | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.grouping.description | 
  * Added Element

  
ImplementationGuide.definition.resource | 
  * Moved from ImplementationGuide.package to ImplementationGuide.definition

  
ImplementationGuide.definition.resource.reference | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.resource.fhirVersion | 
  * Added Element

  
ImplementationGuide.definition.resource.example[x] | 
  * Moved from ImplementationGuide.package.resource.example to example[x]
  * Min Cardinality changed from 1 to 0
  * Add Type canonical(StructureDefinition)

  
ImplementationGuide.definition.resource.groupingId | 
  * Added Element

  
ImplementationGuide.definition.page | 
  * Moved from ImplementationGuide to ImplementationGuide.definition

  
ImplementationGuide.definition.page.name[x] | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.page.generation | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.parameter | 
  * Added Element

  
ImplementationGuide.definition.parameter.code | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.parameter.value | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.template | 
  * Added Element

  
ImplementationGuide.definition.template.code | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.template.source | 
  * **Added Mandatory Element**

  
ImplementationGuide.definition.template.scope | 
  * Added Element

  
ImplementationGuide.manifest | 
  * Added Element

  
ImplementationGuide.manifest.rendering | 
  * Added Element

  
ImplementationGuide.manifest.resource | 
  * **Added Mandatory Element**

  
ImplementationGuide.manifest.resource.reference | 
  * **Added Mandatory Element**

  
ImplementationGuide.manifest.resource.example[x] | 
  * Added Element

  
ImplementationGuide.manifest.resource.relativePath | 
  * Added Element

  
ImplementationGuide.manifest.page | 
  * Added Element

  
ImplementationGuide.manifest.page.name | 
  * **Added Mandatory Element**

  
ImplementationGuide.manifest.page.title | 
  * Added Element

  
ImplementationGuide.manifest.page.anchor | 
  * Added Element

  
ImplementationGuide.manifest.image | 
  * Added Element

  
ImplementationGuide.manifest.other | 
  * Added Element

  
ImplementationGuide.dependency.type | 
  * deleted

  
ImplementationGuide.package | 
  * deleted

  
ImplementationGuide.binary | 
  * deleted

  
ImplementationGuide.page.source | 
  * deleted

  
ImplementationGuide.page.kind | 
  * deleted

  
ImplementationGuide.page.type | 
  * deleted

  
ImplementationGuide.page.package | 
  * deleted

  
ImplementationGuide.page.format | 
  * deleted

  
See the [Full Difference](diff.html) for further information
This analysis is available as [XML](implementationguide.diff.xml) or [JSON](implementationguide.diff.json). 
See [R3 <--> R4 Conversion Maps](implementationguide-version-maps.html) (status = 1 test that all execute ok. All tests pass round-trip testing and 1 r3 resources are invalid (0 errors).)
See the [Profiles & Extensions](implementationguide-profiles.html) and the alternate definitions: Master Definition [XML](implementationguide.profile.xml.html) + [JSON](implementationguide.profile.json.html), [XML](xml.html) [Schema](implementationguide.xsd)/[Schematron](implementationguide.sch) + [JSON](json.html) [Schema](implementationguide.schema.json.html), [ShEx](implementationguide.shex.html) (for [Turtle](rdf.html)) + [see the extensions](implementationguide-profiles.html) & the [dependency analysis](implementationguide-dependencies.html)
###  5.8.3.1 Terminology Bindings [](implementationguide.html#tx "link to here")
Path | Definition | Type | Reference  
---|---|---|---  
ImplementationGuide.status  | The lifecycle status of an artifact. | [Required](terminologies.html#required) |  [PublicationStatus](valueset-publication-status.html)  
ImplementationGuide.jurisdiction  | Countries and regions within which this artifact is targeted for use. | [Extensible](terminologies.html#extensible) |  [Jurisdiction ValueSet](valueset-jurisdiction.html)  
ImplementationGuide.license  | The license that applies to an Implementation Guide (using an SPDX license Identifiers, or 'not-open-source'). The binding is required but new SPDX license Identifiers are allowed to be used (https://spdx.org/licenses/). | [Required](terminologies.html#required) |  [SPDXLicense](valueset-spdx-license.html)  
ImplementationGuide.fhirVersion  
ImplementationGuide.definition.resource.fhirVersion  | All published FHIR Versions. | [Required](terminologies.html#required) |  [FHIRVersion](valueset-FHIR-version.html)  
ImplementationGuide.global.type  | One of the resource types defined as part of this version of FHIR. | [Required](terminologies.html#required) | [Resource Types](valueset-resource-types.html)  
ImplementationGuide.definition.page.generation  | A code that indicates how the page is generated. | [Required](terminologies.html#required) |  [GuidePageGeneration](valueset-guide-page-generation.html)  
ImplementationGuide.definition.parameter.code  | Code of parameter that is input to the guide. | [Required](terminologies.html#required) |  [GuideParameterCode](valueset-guide-parameter-code.html)  
###  5.8.3.2 Constraints [](implementationguide.html#invs "link to here")
**id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)**  
---|---|---|---|---  
**ig-0** |  [Warning](conformance-rules.html#warning) | (base) | Name should be usable as an identifier for the module by machine processing applications such as code generation | name.matches('[A-Z]([A-Za-z0-9_]){0,254}')  
**ig-1** |  [Rule](conformance-rules.html#rule) | ImplementationGuide.definition | If a resource has a groupingId, it must refer to a grouping defined in the Implementation Guide | resource.groupingId.all(%context.grouping.id contains $this)  
**ig-2** |  [Rule](conformance-rules.html#rule) | (base) | If a resource has a fhirVersion, it must be oe of the versions defined for the Implementation Guide | definition.resource.fhirVersion.all(%context.fhirVersion contains $this)  
###  5.8.3.3 Distributing Implementation Guides [](implementationguide.html#packaging "link to here")
Implementation Guides are published through the FHIR Package distribution system. For further details, see the [FHIR Confluence site ![](external.png)](https://confluence.hl7.org/display/FHIR/NPM+Package+Specification). This content may be moved into the specification in a future version. 
###  5.8.3.4 Multi-Version Implementation Guides [](implementationguide.html#versions "link to here")
Most implementation guides target a single version - that is, they describe how to use a particular version, and all the profiles, value sets and examples they contain etc are valid for that particular version. 
In other cases, however, implementation of an implementation guide is not confined to a single version. Typically, the requirement to support multiple versions arises as implementation matures and different implementation communities are stuck at different versions by regulation or market dynamics. Applications may be stuck at different versions of the specification. See [Managing Multiple Versions](versioning.html) for further information about cross-version support. 
For this reason, implementation guides might describe how to use multiple different versions of FHIR for the same purpose. The different versions might have different profiles, extensions, and examples, while sharing common value set definitions, for example. For some reasons, profiles and examples could be common across all versions. And an implementation guide will generally have a lot of common narrative describing the problem, security approaches, and other deployment information irrespective of specific FHIR versions. 
An implementation guide specifies which versions of FHIR it describes in the [ImplementationGuide.fhirVersion](implementationguide-definitions.html#ImplementationGuide.fhirVersion) property: 
```

  "fhirVersion" : ["3.0", "4.0"],

```

This specifies that the implementation guide applies to both [release 3 ![](external.png)](http://hl7.org/fhir/STU3) and [Release 4 ![](external.png)](http://hl7.org/fhir/R4). Note that the patch version (".1" for Release 3) is omitted, since the patch releases never make changes that make any difference to Implementation Guides. 
Note that it is possible to have an Implementation Guide that declares support for one version and imports an Implementation Guide that declares support for a different version. It is up to the importing IG ad/or the tooling that supports Implenentation Guides to determine whether it's safe and/or appropriate to reference the different resources from the new IG, and what to make of this. 
###  5.8.3.5 Default Profiles [](implementationguide.html#default "link to here")
An implementation guide can define default profiles using `ImplementationGuide.global`- these are profiles that apply to any resource that does not otherwise have an explicit profile assigned by the implementation guide. Default profiles are always references to profiles ([StructureDefinition](structuredefinition.html) resources) that are also contained in the resources. By defining default profiles, an implementation guide can save itself from exhaustively defining profiles on every resource type just to profile every reference to a particular resource type. 
Note that a resource can conform to the default profile by conforming to any profile derived from it. 
###  5.8.3.6 Compatibility list [](implementationguide.html#compatibility "link to here")
This table declares the compatibility between the various resources as determined by the Implementation Guide comparison tool: 
_Yet to be done_
##  5.8.4 Search Parameters [](implementationguide.html#search "link to here")
Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.
**Name** | **Type** | **Description** | **Expression** | **In Common**  
---|---|---|---|---  
context | [token](search.html#token) | A use context assigned to the implementation guide | (ImplementationGuide.useContext.value as CodeableConcept) |   
context-quantity | [quantity](search.html#quantity) | A quantity- or range-valued use context assigned to the implementation guide | (ImplementationGuide.useContext.value as Quantity) | (ImplementationGuide.useContext.value as Range) |   
context-type | [token](search.html#token) | A type of use context assigned to the implementation guide | ImplementationGuide.useContext.code |   
context-type-quantity | [composite](search.html#composite) | A use context type and quantity- or range-based value assigned to the implementation guide | On ImplementationGuide.useContext:  
context-type: code  
context-quantity: value.as(Quantity) | value.as(Range) |   
context-type-value | [composite](search.html#composite) | A use context type and value assigned to the implementation guide | On ImplementationGuide.useContext:  
context-type: code  
context: value.as(CodeableConcept) |   
date | [date](search.html#date) | The implementation guide publication date | ImplementationGuide.date |   
depends-on | [reference](search.html#reference) | Identity of the IG that this depends on | ImplementationGuide.dependsOn.uri  
([ImplementationGuide](implementationguide.html)) |   
description | [string](search.html#string) | The description of the implementation guide | ImplementationGuide.description |   
experimental | [token](search.html#token) | For testing purposes, not real usage | ImplementationGuide.experimental |   
global | [reference](search.html#reference) | Profile that all resources must conform to | ImplementationGuide.global.profile  
([StructureDefinition](structuredefinition.html)) |   
jurisdiction | [token](search.html#token) | Intended jurisdiction for the implementation guide | ImplementationGuide.jurisdiction |   
name | [string](search.html#string) | Computationally friendly name of the implementation guide | ImplementationGuide.name |   
publisher | [string](search.html#string) | Name of the publisher of the implementation guide | ImplementationGuide.publisher |   
resource | [reference](search.html#reference) | Location of the resource | ImplementationGuide.definition.resource.reference  
(Any) |   
status | [token](search.html#token) | The current status of the implementation guide | ImplementationGuide.status |   
title | [string](search.html#string) | The human-friendly name of the implementation guide | ImplementationGuide.title |   
url | [uri](search.html#uri) | The uri that identifies the implementation guide | ImplementationGuide.url |   
version | [token](search.html#token) | The business version of the implementation guide | ImplementationGuide.version |   
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:35+1100. [QA Page](qa.html)   
Links: [Search ![](external.png)](http://hl7.org/fhir/search.cfm) | [Version History](history.html) | [Table of Contents](toc.html) | [Credits](credits.html) | [Compare to R3 ![](external.png)](http://services.w3.org/htmldiff?doc1=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fimplementationguide.html&doc2=http%3A%2F%2Fbuild.fhir.org%2Fimplementationguide.html) | [![CC0](cc0.png)](license.html) | [Propose a change ![](external.png)](http://hl7.org/fhir-issues)
