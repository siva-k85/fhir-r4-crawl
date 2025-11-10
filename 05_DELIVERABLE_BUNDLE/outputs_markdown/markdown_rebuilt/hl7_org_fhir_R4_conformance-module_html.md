---
url: https://hl7.org/fhir/R4/conformance-module.html
title: conformance-module.html
source: official_download
extracted: local_file_conversion
mirror_path: conformance-module.html
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


  * **![](conformance.jpg)Conformance**


**This page is part of a downloaded copy of this specification.** This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html)
Work Group [FHIR Infrastructure ![](external.png)](http://www.hl7.org/Special/committees/fiwg/index.cfm) |  [Standards Status](versions.html#std-process): [Informative](versions.html#std-process)  
---|---  
##  5.0 Conformance Module [](conformance-module.html#5.0 "link to here")
The Conformance Module represents metadata about the datatypes, resources and API features of the FHIR specification and can be used to create derived specifications.
  * [CapabilityStatement](capabilitystatement.html)
  * [StructureDefinition](structuredefinition.html)
  * [OperationDefinition](operationdefinition.html)
  * [SearchParameter](searchparameter.html)

| 
  * [CompartmentDefinition](compartmentdefinition.html)
  * [ImplementationGuide](implementationguide.html)
  * [ElementDefinition (datatype)](elementdefinition.html)

| 
  * [Full profiling details](profiling.html)
  * [Detailed conformance rules](conformance-rules.html)

  
---|---|---  
###  5.0.1 Introduction [](conformance-module.html#intro "link to here")
The core FHIR specification describes a set of resources, frameworks and APIs that are used in many different contexts in healthcare. However, there is wide variability between jurisdictions and across the healthcare ecosystem around practices, requirements, regulations, education and what actions are feasible and/or beneficial.
For this reason, the FHIR specification is a "platform specification" - it creates a common platform or foundation on which a variety of different solutions are implemented. As a consequence, this specification usually requires further adaptation to particular contexts of use. 
Typically, these adaptations specify:
  * Rules about which resource elements are or are not used, and what additional elements are added that are not part of the base specification
  * Rules about which of FHIR's RESTful API, messaging and document features are used, and how
  * Rules about which terminologies are used in particular elements
  * Descriptions of how the Resource elements and API features map to local requirements and/or implementations


Note that because of the nature of the healthcare ecosystem, there may be multiple overlapping sets of adaptations - by healthcare domain, by country, by institution, and/or by vendor/implementation.
FHIR provides a set of resources that can be used to represent and share the adaptations listed above in a computable fashion. These resources are collectively called the _conformance resources_. Although these conformance resources can be used in isolation they are typically used in the context of an _Implementation Guide_ or a _Capability Statement_ :
  * _Implementation Guides_ are documents published by a domain, institution or vendor that describe how FHIR is adapted to support a certain use case (or set of use cases). An implementation guide combines a set of conformance resources and supporting narrative into a document for use by implementers.
  * A _capability statements_ use the conformance resources to document how a client or server has implemented FHIR, i.e. which aspects of the specification and API are implemented and how. 


###  5.0.2 Contents [](conformance-module.html#contents "link to here")
The content of an Implementation Guide is described using the [ImplementationGuide](implementationguide.html) resource, while the capability statement is represented by the [CapabilityStatement](capabilitystatement.html) resource. These two resources make use of the complete set of conformance resources to fully capture the set of adaptations they represent. Note that the CapabilityStatement resource is one of the _conformance resources_ , the first just describing the capabilities of a system, while the latter is the set of all conformance resources, including:
  * The [StructureDefinition](structuredefinition.html) defines how a particular structure (Resource, Extension or Data Type) is used to:
    * Describe how existing elements in resources and/or data types are used and identify existing elements that are not used. Exact rules on how to do this can be found in the section on [conformance rules](conformance-rules.html)
    * Define [extensions](extensibility.html) that can be used in resources or data types.
    * Reference the [Value Sets](valueset.html) that specify the content of coded elements, see the [terminology module](terminology-module.html) for more details. 
  * The [MessageDefinition](messagedefinition.html) describes messages that can be sent and received, including the driving event, contents to be exchanged and responsibilities on receipt.
  * The [OperationDefinition](operationdefinition.html) describes additional operations in addition to [those in the base specification](operations.html).
  * The [SearchParameter](searchparameter.html) describes additional search capabilities in addition to those in the base specification 
  * The [CompartmentDefinition](compartmentdefinition.html) describes a logical grouping for resources, used in access control or search


Conformance resources may be used independently, not just within the context of an ImplementationGuide resource or capability statement. See the section [Common use cases](#uses) for examples of such uses.
The conformance resources and their relationships are shown below:
![Image showing the conformance resources](conformance-module-resources.png)
Resources shown with a dotted box are described in other sections of the specification: `ValueSet`, `ConceptMap` and `StructureMap` are from the [section on terminology](terminology-module.html), `TestScript` is part of the section on [Implementer Support](implsupport-module.html).
###  5.0.3 Security and Privacy [](conformance-module.html#secpriv "link to here")
The conformance resources do not represent patient-related data, and as such are less susceptible to data breaching. Some caution is required however:
  * `StructureDefinitions` may contain invariants formulated as structured expressions that are evaluated by external engines (i.e. xpath), which -if improperly sandboxed- could provide low-level access to the system
  * A server may be implemented in such a way that it will automatically support additional search parameters or compartments definitions uploaded to that system. This may result in searches that use large amounts of processing power, expose sensitive patient data, or both.
  * If a server acts as a repository of conformance resources, it should tightly control modifications to its data: updates to conformance resources are usually managed by a review process to ensure backwards compatibility and stability. Worst case, changes to these resources may result in dependent systems running the risk of being misconfigured.


###  5.0.4 Common use Cases [](conformance-module.html#uses "link to here")
Conformance resources are commonly used as part of an [Implementation Guide](implementationguide.html) or [CapabilityStatement](capabilitystatement.html) resource. There are many ways to use the resources independently however, including:
  * An instance of a resource may reference one or more `StructureDefinitions` to claim conformance to the rules laid out in those StructureDefinitions
  * A server may serve `CapabilityStatement` resources, effectively functioning as a discovery endpoint for services within an organization
  * A code-generation tool may use `StructureDefinitions` and `OperationDefinitions` to generate code that represents the structures as classes and operations as remotely callable functions to provide an easier programming model to a software developer. 
  * A server may act as a repository of `NamingSystem` resources, so vendors and implementers can quickly look up the URLs or oids for a given terminology or identifier system.


###  5.0.5 Developmental Roadmap [](conformance-module.html#roadmap "link to here")
A subset of the conformance resources has been tested and used in production tooling and are now normative. These include StructureDefinition and ValueSet. Others, like CapabilityStatement, have been used widely, but not across all elements. As a consequence, these resource have a considerable number of elements marked for "trial use", while other parts are normative and will no longer change in a substantive way.
Other resources are still under development:
  * `ImplementationGuide`: used in the HL7 production tooling but has not received much use outside of these tools yet.
  * `CompartmentDefinition`: was new in STU3, and as such has not undergone much production use


These resources have been mainly used in the tools used to build the FHIR publication, early-adopter implementation guides and the FHIR Foundation conformance resource registry. In future, we expect to see more widespread use of these resources in validation tooling, code-generators and more extensive model-based guide authoring tools.
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:37+1100. [QA Page](qa.html)   
Links: [Search ![](external.png)](http://hl7.org/fhir/search.cfm) | [Version History](history.html) | [Table of Contents](toc.html) | [Credits](credits.html) | [Compare to R3 ![](external.png)](http://services.w3.org/htmldiff?doc1=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fconformance-module.html&doc2=http%3A%2F%2Fbuild.fhir.org%2Fconformance-module.html) | [![CC0](cc0.png)](license.html) | [Propose a change ![](external.png)](http://hl7.org/fhir-issues)
