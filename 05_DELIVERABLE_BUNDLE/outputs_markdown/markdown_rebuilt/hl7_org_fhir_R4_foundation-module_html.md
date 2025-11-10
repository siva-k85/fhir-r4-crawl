---
url: https://hl7.org/fhir/R4/foundation-module.html
title: foundation-module.html
source: official_download
extracted: local_file_conversion
mirror_path: foundation-module.html
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


  * **![](foundation.png)Foundation**


**This page is part of a downloaded copy of this specification.** This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html)
Work Group [FHIR Infrastructure ![](external.png)](http://www.hl7.org/Special/committees/fiwg/index.cfm) |  [Standards Status](versions.html#std-process): [Informative](versions.html#std-process)  
---|---  
##  2.0 Foundation Module [](foundation-module.html#2.0 "link to here")
The Foundation Module is responsible for the overall infrastructure of the FHIR specification. Every implementer works with the content in the foundation module whichever way they use FHIR. 
The Foundation Module maintains most of the basic [documentation](documentation.html) for the FHIR specification. In addition, the Foundation Module includes the following resources: 
**Foundation Framework**
  * [Resource](resource.html)
  * [DomainResource](domainresource.html)
  * [Basic](basic.html)
  * [Binary](binary.html)
  * [Bundle](bundle.html)

|  Content Management Resources.
  * [Questionnaire](questionnaire.html)
  * [QuestionnaireResponse](questionnaireresponse.html)
  * [List](list.html)
  * [Composition](composition.html)
  * [DocumentReference](documentreference.html)
  * [DocumentManifest](documentmanifest.html)

|  Data Exchange Resources.
  * [OperationOutcome](operationoutcome.html)
  * [Parameters](parameters.html)
  * [Subscription](subscription.html)
  * [MessageHeader](messageheader.html)
  * [MessageDefinition](messagedefinition.html)

  
---|---|---  
###  2.0.1 Relationships with other modules [](foundation-module.html#secpriv "link to here")
  * All the other modules depend on the foundation module
  * The [Exchange module](exchange-module.html) builds on the foundation model by defining the recognized methods for exchange of resources
  * The [Terminology module](terminology-module.html) provides the formal basis for using Concepts defined in Code Systems in the definitions
  * The [Conformance module](conformance-module.html) provides the basis for extending the foundation for national and local use
  * The [ Security & Privacy](secpriv-module.html) provides the linking framework to external standards for security and privacy
  * The [Implementation Support module](implsupport-module.html) builds on the foundation to provide testing and reference implementations


###  2.0.2 Developmental Roadmap [](foundation-module.html#roadmap "link to here")
Several components of the foundation module have now reached normative status. The focus over the next 18-24 months as the 5th release of FHIR is prepared is to focus on some of the non-normative elements and move them towards normative status, such as Questionnaire, List, DocumentReference and Subscription. Exactly which resources will be candidates for normative release will be driven, in part, by the degree of implementation - and whether that implementation is communicated back to HL7. 
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:37+1100. [QA Page](qa.html)   
Links: [Search ![](external.png)](http://hl7.org/fhir/search.cfm) | [Version History](history.html) | [Table of Contents](toc.html) | [Credits](credits.html) | [Compare to R3 ![](external.png)](http://services.w3.org/htmldiff?doc1=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Ffoundation-module.html&doc2=http%3A%2F%2Fbuild.fhir.org%2Ffoundation-module.html) | [![CC0](cc0.png)](license.html) | [Propose a change ![](external.png)](http://hl7.org/fhir-issues)
