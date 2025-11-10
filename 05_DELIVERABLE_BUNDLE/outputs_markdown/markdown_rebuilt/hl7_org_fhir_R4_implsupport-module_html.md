---
url: https://hl7.org/fhir/R4/implsupport-module.html
title: implsupport-module.html
source: official_download
extracted: local_file_conversion
mirror_path: implsupport-module.html
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


  * **![](implsupport.png)Implementation Support**


**This page is part of a downloaded copy of this specification.** This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html)
Work Group [FHIR Infrastructure ![](external.png)](http://www.hl7.org/Special/committees/fiwg/index.cfm) & [Application Implementation and Design ![](external.png)](http://www.hl7.org/Special/committees/java/index.cfm) |  [Standards Status](versions.html#std-process): [Informative](versions.html#std-process)  
---|---  
##  7.0 Implementation Support Module [](implsupport-module.html#7.0 "link to here")
###  7.0.1 Introduction [](implsupport-module.html#intro "link to here")
This section provides information which will be useful for FHIR implementers, including information about available libraries, tools, and other similar resources, as well as where to seek help. 
###  7.0.2 Index [](implsupport-module.html#index "link to here")
In addition to the content below, a number of implementation resources can be found on the [Downloads Page](./downloads.html). 
This module also contains some specific documentation that relates to issues commonly encountered by developers: 
  * [Testing FHIR](testing.html) + [TestScript](testscript.html) + [TestReport](testreport.html)
  * [Validating Resources](validation.html)
  * [Mapping Language](mapping-language.html) ([Tutorial](mapping-tutorial.html) & [StructureMap](structuremap.html))
  * [FHIRPath](fhirpath.html)
  * [Common Usages](usecases.html)
  * [Version Management Policy](versions.html)

| 
  * [Clinical Safety Considerations](safety.html)
  * [How FHIR fits into an EHR](ehr-fm.html)
  * [Managing Resource Identity](managing.html)
  * [Interaction Patterns](pushpull.html)
  * [Update Rules](updates.html)
  * [Clinical Examples](integrated-examples.html)

| 
  * [Comparisons:](comparison.html)
    * [v2](comparison-v2.html) &
    * [v3 Messaging](comparison-v3.html)
    * [CDA](comparison-cda.html) + [CDA on FHIR](cda-intro.html)
    * [Other Specifications](comparison-other.html)

  
---|---|---  
###  7.0.3 Security and Privacy [](implsupport-module.html#secpriv "link to here")
For more general considerations, see [the Security and Privacy module](secpriv-module.html). 
###  7.0.4 Common Use Cases [](implsupport-module.html#uses "link to here")
####  7.0.4.1 For Client Developers and Testers: Reference Servers [](implsupport-module.html#7.0.4.1 "link to here")
The following reference servers have been created by the FHIR team and made available to help implementers test their code. While the reference servers are not considered to be a normative part of the FHIR specification, the maintainers make every effort to ensure that they are fully compliant. 
Note that there are a large number of servers available for testing that are not listed here. A full list is available on the HL7 Confluence system [here ![](external.png)](https://confluence.hl7.org/display/FHIR/Public+Test+Servers). 
Server Name | Maintainer | Link  
---|---|---  
Healthintersections | Grahame Grieve | [http://fhir3.healthintersections.com.au/ ![](external.png)](http://fhir3.healthintersections.com.au/)  
Spark | Furore Informatica | [http://spark.furore.com/ ![](external.png)](http://spark.furore.com/)  
HAPI | University Health Network / James Agnew | [http://fhirtest.uhn.ca/ ![](external.png)](http://fhirtest.uhn.ca/)  
sqlonfhir | Telstra Health / Brian Postlethwaite | [http://sqlonfhir-stu3.azurewebsites.net/fhir ![](external.png)](http://sqlonfhir-stu3.azurewebsites.net/fhir)  
####  7.0.4.2 For Developers: Reference Implementations (Libraries) [](implsupport-module.html#7.0.4.2 "link to here")
The following reference implementations are made available under an open-source license. These libraries may be used by developers to quickly add FHIR capabilities to their applications. 
Language | Library | Link | License  
---|---|---|---  
.NET / C# | FHIR .NET API | [https://github.com/ewoutkramer/fhir-net-api ![](external.png)](https://github.com/ewoutkramer/fhir-net-api) | BSD-3  
Java | HAPI FHIR | [http://hapifhir.io ![](external.png)](http://hapifhir.io) | Apache 2.0  
Swift | Swift FHIR | [https://github.com/smart-on-fhir/Swift-FHIR ![](external.png)](https://github.com/smart-on-fhir/Swift-FHIR) | Apache 2.0  
JavaScript | fhir.js | [https://github.com/smart-on-fhir/fhir.js ![](external.png)](https://github.com/smart-on-fhir/fhir.js) | MIT  
Python | Client Py | [https://github.com/smart-on-fhir/client-py ![](external.png)](https://github.com/smart-on-fhir/client-py) | Apache 2.0  
Pascal | FHIR Pascal | [http://hl7.org/fhir/downloads.html ![](external.png)](http://hl7.org/fhir/downloads.html) | BSD-3  
####  7.0.4.3 For Profilers [](implsupport-module.html#for_profilers "link to here")
A number of tools are available to profilers wishing to create profiles for use in their implementations. A current list of tools can be found [here ![](external.png)](https://confluence.hl7.org/pages/viewpage.action?pageId=35718864#ProfileTooling-Editing&AuthoringProfiles) on HL7 Confluence. (See the [conformance module](./conformance-module.html) for information on profiling.) 
####  7.0.4.4 For Testers [](implsupport-module.html#for_testers "link to here")
A number of tools are available to solution testers who want to test FHIR implementations for conformance to the FHIR specification. A current list of such tools can be found [here ![](external.png)](https://confluence.hl7.org/display/FHIR/Testing+Platforms). 
###  7.0.5 Getting Help [](implsupport-module.html#help "link to here")
The following are a few ways that implementers can seek help as they work with FHIR: 
  * [FHIR Chat Channel / Zulip ![](external.png)](http://chat.fhir.org/) (maintained by fhir.org)
  * [FHIR Community Forum ![](external.png)](http://community.fhir.org/) (maintained by fhir.org)
  * [StackOverflow ![](external.png)](http://stackoverflow.com/questions/tagged/hl7_fhir) (General tech community, use the tag `hl7_fhir`)


###  7.0.6 Developmental Roadmap [](implsupport-module.html#roadmap "link to here")
The reference servers and reference implementations generally try to keep up to date with recent changes to the FHIR specification. Each server may have multiple endpoints which are held to a specific version of the specification, but generally there will also be endpoints available for testing which conform to a very recent build. 
Efforts are now underway to create a curated collection of quality test data which can be used by FHIR implementers to help test their applications. This collection will be made available when it is ready. 
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:37+1100. [QA Page](qa.html)   
Links: [Search ![](external.png)](http://hl7.org/fhir/search.cfm) | [Version History](history.html) | [Table of Contents](toc.html) | [Credits](credits.html) | [Compare to R3 ![](external.png)](http://services.w3.org/htmldiff?doc1=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fimplsupport-module.html&doc2=http%3A%2F%2Fbuild.fhir.org%2Fimplsupport-module.html) | [![CC0](cc0.png)](license.html) | [Propose a change ![](external.png)](http://hl7.org/fhir-issues)
