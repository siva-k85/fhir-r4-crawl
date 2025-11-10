---
url: https://hl7.org/fhir/R4/documents.html
title: documents.html
source: official_download
extracted: local_file_conversion
mirror_path: documents.html
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


  * [![](exchange.png) Exchange](exchange-module.html)
  * **Documents**


**This page is part of a downloaded copy of this specification.** This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html)
#  3.3 FHIR Documents [](documents.html#3.3 "link to here")
[FHIR Infrastructure ![](external.png)](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group |  [Maturity Level](versions.html#maturity): 3 |  [Standards Status](versions.html#std-process): [Trial Use](versions.html#std-process)  
---|---|---  
FHIR resources can be used to build documents that represent a composition: a coherent set of information that is a statement of healthcare information, including clinical observations and services. A document is an immutable set of resources with a fixed presentation that is authored and/or attested by humans, organizations and devices. 
Documents built in this fashion may be exchanged between systems and persisted in document storage and management systems, including systems such as IHE XDS. 
Applications claiming conformance to this framework claim to be conformant to "FHIR documents" (see [Conformance](conformance-rules.html)). 
FHIR documents may be 'clinical' (focused on patient healthcare information) but may also serve non-clinical purposes (e.g. FHIR Implementation guides, practice guidelines, patient handouts, etc.) HL7 will develop profiles in the future giving additional guidance on appropriate representation of clinical documents in general as well as specific types of clinical documents (e.g. Consolidated CDA). 
Note that FHIR defines both this document format and a [document reference resource](documentreference.html). FHIR documents are for documents that are authored and assembled in FHIR, while the document reference resource is for general references to pre-existing documents. 
  * [Example discharge summary](document-example-dischargesummary.html): [XML](document-example-dischargesummary.xml.html) or [JSON](document-example-dischargesummary.json.html)


##  3.3.1 Document Content [](documents.html#content "link to here")
All documents have the same structure: a [Bundle](bundle.html) of resources of [type](bundle-definitions.html#Bundle.type) "document" that has a [Composition](composition.html) resource as the first resource in the bundle, followed by a series of other resources, referenced from the `Composition` resource, that provide supporting evidence for the document. The bundle gathers all the content of the document into a single XML or JSON document which may be signed and managed as required. The resources include both human readable and computer processable portions. In addition, the bundle may include [CSS stylesheets ![](external.png)](http://www.w3.org/Style/CSS/Overview.en.html), [Provenance](provenance.html) statements and a signature. 
The composition resource is the foundation of the clinical document. It: 
  * provides identity and its purpose, and sets the context of the document
  * carries key information such as the subject and author, and who attests to the document
  * divides the document up into a series of sections, each with their own narrative


Resources referenced by the Composition as listed below SHALL be included in the bundle when the document is assembled: 
  * [Composition.subject](composition-definitions.html#Composition.subject)
  * [Composition.encounter](composition-definitions.html#Composition.encounter)
  * [Composition.author](composition-definitions.html#Composition.author)
  * [Composition.attester.party](composition-definitions.html#Composition.attester.party)
  * [Composition.custodian](composition-definitions.html#Composition.custodian)
  * [Composition.event.detail](composition-definitions.html#Composition.event.detail)
  * [Composition.section.author](composition-definitions.html#Composition.section.author)
  * [Composition.section.focus](composition-definitions.html#Composition.section.focus)
  * [Composition.section.entry](composition-definitions.html#Composition.section.entry)


Other resources that these referenced resources refer to may also be included in the bundle if the document construction system chooses to do so. Including these additional resources will make the document bigger but will save applications from needing to retrieve the linked resources if they need them while processing the document. Thus, whether these linked resources should be included or not depends on the implementation environment. 
The document bundle SHALL include only: 
  1. The Composition resource, and any resources directly or indirectly (e.g. recursively) referenced from it
  2. A Binary resource containing a stylesheet (as described below)
  3. Provenance Resources that have a target of Composition or another resource included in the document


There are two key identifiers in the document: 
  * The document identifier (mandatory). This is found in _Bundle.identifier_ and is globally unique for this instance of the document, and is never re-used, including for other documents derived from the same composition
  * The Composition identifier (optional). This is found in _Composition.identifier_ , and is the same for all documents that are derived from this composition


The document has several dates in it: 
  * The document date (mandatory). This is found in _Bundle.meta.lastUpdated_ and identifies when the document bundle was assembled from the underlying resources
  * The Composition date (mandatory). This is found in _Composition.date_ , which is when the author wrote the document logically
  * The Attestation dates (optional). This is found in _Composition.attester.time_ and is when the document was witnessed by the attesters. This would usually be at the same time as the composition date or afterwards
  * The Composition last modified time (optional). This is found in _Composition.meta.lastUpdated_ for the composition and is the last date of change of the composition. This must be >= the composition date


Document Bundles may be signed using digital signatures following the rules laid out in the [digital signatures](signatures.html) page. The signature SHOULD be provided by a listed attester of the document and the signature SHOULD contain a [KeyInfo element ![](external.png)](http://www.w3.org/TR/xmldsig-core/#sec-KeyInfo) that contains a KeyName element whose value is a URI that matches the [fullUri](bundle-definitions.html#Bundle.entry.fullUri) for the matching attester resource. 
Once assembled into a bundle, the document is immutable - its content can never be changed, and the document id can never be reused. Note that the document may be represented in either XML or JSON and interconverted between these or have its character encoding changed, all the while remaining the same document. However, the directly referenced content within the document and the presentation of the document cannot change substantially (such that it changes the clinical meaning of the content). Any additional documents derived from the same composition SHALL have a different document id. 
###  3.3.1.1 Document Presentation [](documents.html#presentation "link to here")
When the document is presented for human consumption, applications SHOULD present the collated narrative portions in order: 
  1. The [subject resource](composition-definitions.html#Composition.subject) Narrative
  2. The [Composition](composition.html) resource Narrative
  3. The [section.text](composition-definitions.html#Composition.section.text) Narratives


The presentation of the document is called the 'attested content' of the document. Additional resources can be included in the bundle (e.g. resources referenced from the List that represent the section.content SHOULD be in the bundle, and other additional resources they reference can be included), but these (and any narrative) are not attested content. Specifically, the `Composition.attester` attests to the presented form of the document. 
The Composition resource narrative should summarize the important parts of the document header that are required to establish clinical context for the document (other than the subject, which is displayed in its own right). To actually build the combined narrative, simply append all the narrative <div> fragments together. 
If the document is presented in a different order from that given above, it might not represent the original attested content. Implementation Guides may restrict document narrative and display behavior further. 
The [XML Tools reference implementation](downloads.html#refimpl) includes a XSLT transform that converts an XML document into browser-ready XHTML. 
In addition to the [basic style rules about Narratives](narrative.html#css), which must be followed, a document can reference or contain one or more stylesheets that contains additional styles that apply to the collated narrative. This is done by asserting stylesheet links on the feed: 
```

<Bundle xmlns="http://hl7.org/fhir">
  <!-- metadata and type -->
  <link>
    <relation value="stylesheet"/>
    <url value="[uri]"/>
  </link>
</Bundle>

```

The `url` can be an absolute reference to a CSS stylesheet or a relative reference to a Binary resource that carries a CSS stylesheet. Stylesheet references can only refer to a CSS stylesheet - other forms of stylesheet are not acceptable. 
Relative (internal) references SHOULD be used for stylesheets, because the viewer may be unable to resolve external content at the time of viewing, due to technical problems or local policy decisions. 
Any stylesheet referenced or used SHALL NOT alter the presentation in such a way that it changes the clinical meaning of the content. 
Unless otherwise agreed in local trading partner agreements, applications displaying the collated narrative SHOULD use the stylesheets specified by the document (see [security note](security.html#stylesheet)). Parties entering into a trading agreement to do otherwise should consider the implications this action will have on their long-term scope for document exchange very carefully. If the parties agree to use stylesheets that are not contained in the document, then it may be that they will never be able to share their documents safely in a more general context, such as a regional or national EHR or a global personal health record. 
##  3.3.2 Document Profiles [](documents.html#profiles "link to here")
[Document profiles](profiling.html) are used to describe documents for a particular purpose. Document profiles may make rules about: 
  * The content of the Composition resource, including
  * The structure of the sections in the composition
  * Which resources are to be included in the bundle along with the resources that are directly referenced in the Document resource


Applications should consider publishing [Capability Statements](capabilitystatement.html) that identify document types they support. Documents can identify a profile that they conform to by placing a profile identifier in the `Bundle.meta.profile` element - see [Profile Tags](resource.html#meta) for a discussion of the utility of this. 
##  3.3.3 Document Handling Obligations [](documents.html#obligations "link to here")
The authors/constructors and processors of Clinical Documents, whether human or software, have obligations that they must satisfy. 
###  3.3.3.1 Author/Constructor Obligations [](documents.html#3.3.3.1 "link to here")
A document constructor is an application that creates a document. An author is a human, organization or device that uses the constructor to create a document. Between them, the constructor and the author may create new content resources and/or assemble already existing content resources while performing their tasks. They also have the following responsibilities: 
  * To assure that the document SHALL contain valid composition that conforms to the rules described here and that only links to other valid resources
  * To assure that the content of document SHALL conform to any declared [Profiles](profiling.html) (see below).
  * Ensure that the attesters are properly aware of the presentation of the document to which they are attesting


###  3.3.3.2 Processor Obligations [](documents.html#3.3.3.2 "link to here")
A document processor is an application and/or human user that receives documents and extracts data from them or makes decisions because of them. The documents may be received directly from a document constructor, accessed via a document management system or forwarded by a third party. The document processor is responsible for ensuring that received documents are processed and/or rendered in accordance to this specification. A document processor has the obligation to assure that the following rules are followed: 
  * When storing/transmitting a document, any method may be used as long as the bundled document can be (re-)assembled with sufficient integrity to validate a digital signature
  * When presenting the narrative of the document, the rules described above SHALL be followed
  * Resources or data from the document may be extracted for additional uses, but such data is no longer considered to be attested by the document author
  * Wherever the data from the document is displayed to a user, there SHOULD always be a way for the user to access a presentation of the original document


In addition to these obligations, document receivers SHOULD carefully track the source of documents for new documents that supersede existing documents, particularly when the documents represent compositions that have been retracted. When documents have been replaced, they SHOULD either withdraw data extracted from superseded documents or warn users when they view the document or data taken from it. 
##  3.3.4 Document End-Points [](documents.html#bundle "link to here")
There are several different RESTful end-points used when working with documents. The use of the various end-points can best be described by considering the consequences of posting to them: 
**End-Point** | **Type of Content** | **Description**  
---|---|---  
[baseurl]/Bundle | Document Bundle | This works like a normal end-point for managing a type of resource, but it works with whole document bundles - i.e. a read operation returns a bundle, an update gets a bundle and a search returns a bundle of bundles. Note that if documents are POSTed using a [create](http.html#create) interaction the Bundle.id will change, but the Bundle.identifier will not. See [Serving Bundles using the RESTful API](bundle.html#rest) for further comment  
[baseurl]/Composition | Composition Resource | The normal end-point for managing composition resources. This can be used while building a document or after breaking a document up into its constituent resources or when using compositions separately from documents  
[[baseurl]/Binary](binary.html) | Document Bundle | Just store the entire document as a sequence of bytes and return exactly that sequence when requested. There is no way to find content in the /Binary end-point, so usually this would be associated with a [Document Reference](documentreference.html) so that applications can find and process the document, though this is not required  
[[baseurl]](http.html#transaction) (e.g. a transaction) | Document Bundle | Ignore the fact that the bundle is a document and process all of the resources that it contains as individual resources. Clients SHOULD not expect that a server that receives a document submitted using this method will be able to reassemble the document exactly. (Even if the server can reassemble the document (see below), the result cannot be expected to be in the same order, etc. Thus a document signature will very likely be invalid.). See [Accepting other Bundle types](http.html#other-bundles) for further details  
Note: While these end-points are defined for use with document-related resources and document bundles, it is not necessary to use them. Documents may be transferred between systems using any method desired. In addition, servers and/or specifications may define additional [operations](operations.html) for handling documents beyond the options described above. 
###  3.3.4.1 Generating a Document [](documents.html#3.3.4.1 "link to here")
A client can ask a server to generate a fully bundled document from a composition resource. For details, see [Generate Document Operation](composition-operations.html). 
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:37+1100. [QA Page](qa.html)   
Links: [Search ![](external.png)](http://hl7.org/fhir/search.cfm) | [Version History](history.html) | [Table of Contents](toc.html) | [Credits](credits.html) | [Compare to R3 ![](external.png)](http://services.w3.org/htmldiff?doc1=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fdocuments.html&doc2=http%3A%2F%2Fbuild.fhir.org%2Fdocuments.html) | [![CC0](cc0.png)](license.html) | [Propose a change ![](external.png)](http://hl7.org/fhir-issues)
