---
url: https://hl7.org/fhir/R4/extensibility.html
title: extensibility.html
source: official_download
extracted: local_file_conversion
mirror_path: extensibility.html
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


  * [![](foundation.png) Foundation](foundation-module.html)
  * **Extensibility**


**This page is part of a downloaded copy of this specification.** This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/directory.html)
  * [Extensibility](#)
  * [Defining Extensions](defining-extensions.html)
  * [Examples](extensibility-examples.html)
  * [Detailed Descriptions](extensibility-definitions.html)
  * [Registry](extensibility-registry.html)


#  2.5.0 Extensibility [](extensibility.html#2.5.0 "link to here")
[FHIR Infrastructure ![](external.png)](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group |  [Maturity Level](versions.html#maturity): Normative |  [Standards Status](versions.html#std-process): [Normative](versions.html#std-process)  
---|---|---  
![](assets/images/ansi-approved.gif) |  This page has been approved as part of an [ANSI ![](external.png)](https://www.ansi.org/) standard. See the [Infrastructure](ansi-infrastructure.html) Package for further details.   
---|---  
This exchange specification is based on generally agreed common requirements across healthcare - covering many jurisdictions, domains, and different functional approaches. It is common for specific implementations to have valid requirements that are not part of these agreed common requirements. Incorporating all valid requirements would make this specification very cumbersome and difficult to implement. Instead, this specification expects that additional valid requirements will be implemented as extensions. 
As such, extensibility is a fundamental part of the design of this specification. Every element in a resource can have extension child elements to represent additional information that is not part of the basic definition of the resource. Applications should not reject resources merely because they contain extensions, though they may need to reject resources because of the specific contents of the extensions. 
Note that, unlike in many other specifications, there can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core simplicity for everyone. 
To make the use of extensions safe and manageable, there is strict governance applied to the definition and use of extensions. Although any implementer can define and use extensions, there is a set of requirements that must be met as part of their use and definition. 
##  2.5.0.1 Extension Element [](extensibility.html#extension "link to here")
Every element in a resource or data type includes an optional "extension" child element that may be present any number of times. This is the content model of the extension as it appears in each resource: 
  * [Structure](#tabs-Extension-struc)
  * [UML](#tabs-Extension-uml)
  * [XML](#tabs-Extension-xml)
  * [JSON](#tabs-Extension-json)
  * [Turtle](#tabs-Extension-ttl)
  * [R3 Diff](#tabs-Extension-diff)
  * [All](#tabs-Extension-all)


**Structure**
[Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") |  [Description & Constraints](formats.html#table "Additional information about the element")[![doco](help16.png)](formats.html#table "Legend for this format")  
---|---|---|---|---  
![.](tbl_spacer.png)![.](icon_element.gif) [Extension](extensibility-definitions.html#Extension "Extension : Optional Extension Element - found in all resources.") |  [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Optional Extensions Element  
+ Rule: Must have either extensions or value[x], not both  
Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource \(for internal references\). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.")  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [url](extensibility-definitions.html#Extension.url "Extension.url : Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](datatypes.html#uri) | identifies the meaning of the extension  
![.](tbl_spacer.png)![.](tbl_vjoin_end.png)![.](icon_datatype.gif) [value[x]](extensibility-definitions.html#Extension.value_x_ "Extension.value\[x\] : Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") |  | 0..1 | [*](datatypes.html#open) | Value of extension  
  
[![doco](help16.png) Documentation for this format](formats.html#table "Legend for this format")  
**UML Diagram** ([Legend](formats.html#uml))
ElementExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeextension : Extension 0..*ExtensionSource of the definition for the extension code - a logical name or a URLurl : uri [1..1]Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list)value[x] : * [0..1]
**XML Template**
```

<[**extension|modifierExtension**](extensibility-definitions.html#Extension "Optional Extension Element - found in all resources.") xmlns="http://hl7.org/fhir" url="identifies the meaning of the extension (uri[](datatypes.html#uri))">
 <!-- from Element: extension[](extensibility.html) -->
 <[**value[x]**](extensibility-definitions.html#Extension.value\[x\] "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")><!-- **0..1** *[](datatypes.html#open) Value of extension[](terminologies.html#unbound) --></value[x]>
</extension|modifierExtension>

```

**JSON Template**
```

{[![doco](help.png)](json.html "Documentation for this format")
  // from Element: extension[](extensibility.html)
  "url[](extensibility-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.")" : "<uri[](datatypes.html#uri)>", // **R!**  identifies the meaning of the extension[](terminologies.html#unbound)
  // value[x]: Value of extension. One of these 50:
  "valueBase64Binary[](extensibility-definitions.html#Extension.valueBase64Binary "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<base64Binary[](datatypes.html#base64Binary)>"
  "valueBoolean[](extensibility-definitions.html#Extension.valueBoolean "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : <boolean[](datatypes.html#boolean)>
  "valueCanonical[](extensibility-definitions.html#Extension.valueCanonical "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<canonical[](datatypes.html#canonical)>"
  "valueCode[](extensibility-definitions.html#Extension.valueCode "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<code[](datatypes.html#code)>"
  "valueDate[](extensibility-definitions.html#Extension.valueDate "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<date[](datatypes.html#date)>"
  "valueDateTime[](extensibility-definitions.html#Extension.valueDateTime "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<dateTime[](datatypes.html#dateTime)>"
  "valueDecimal[](extensibility-definitions.html#Extension.valueDecimal "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : <decimal[](datatypes.html#decimal)>
  "valueId[](extensibility-definitions.html#Extension.valueId "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<id[](datatypes.html#id)>"
  "valueInstant[](extensibility-definitions.html#Extension.valueInstant "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<instant[](datatypes.html#instant)>"
  "valueInteger[](extensibility-definitions.html#Extension.valueInteger "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : <integer[](datatypes.html#integer)>
  "valueMarkdown[](extensibility-definitions.html#Extension.valueMarkdown "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<markdown[](datatypes.html#markdown)>"
  "valueOid[](extensibility-definitions.html#Extension.valueOid "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<oid[](datatypes.html#oid)>"
  "valuePositiveInt[](extensibility-definitions.html#Extension.valuePositiveInt "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<positiveInt[](datatypes.html#positiveInt)>"
  "valueString[](extensibility-definitions.html#Extension.valueString "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<string[](datatypes.html#string)>"
  "valueTime[](extensibility-definitions.html#Extension.valueTime "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<time[](datatypes.html#time)>"
  "valueUnsignedInt[](extensibility-definitions.html#Extension.valueUnsignedInt "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<unsignedInt[](datatypes.html#unsignedInt)>"
  "valueUri[](extensibility-definitions.html#Extension.valueUri "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<uri[](datatypes.html#uri)>"
  "valueUrl[](extensibility-definitions.html#Extension.valueUrl "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<url[](datatypes.html#url)>"
  "valueUuid[](extensibility-definitions.html#Extension.valueUuid "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<uuid[](datatypes.html#uuid)>"
  "valueAddress[](extensibility-definitions.html#Extension.valueAddress "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Address[](datatypes.html#Address) }
  "valueAge[](extensibility-definitions.html#Extension.valueAge "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Age[](datatypes.html#Age) }
  "valueAnnotation[](extensibility-definitions.html#Extension.valueAnnotation "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Annotation[](datatypes.html#Annotation) }
  "valueAttachment[](extensibility-definitions.html#Extension.valueAttachment "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Attachment[](datatypes.html#Attachment) }
  "valueCodeableConcept[](extensibility-definitions.html#Extension.valueCodeableConcept "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { CodeableConcept[](datatypes.html#CodeableConcept) }
  "valueCoding[](extensibility-definitions.html#Extension.valueCoding "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Coding[](datatypes.html#Coding) }
  "valueContactPoint[](extensibility-definitions.html#Extension.valueContactPoint "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { ContactPoint[](datatypes.html#ContactPoint) }
  "valueCount[](extensibility-definitions.html#Extension.valueCount "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Count[](datatypes.html#Count) }
  "valueDistance[](extensibility-definitions.html#Extension.valueDistance "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Distance[](datatypes.html#Distance) }
  "valueDuration[](extensibility-definitions.html#Extension.valueDuration "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Duration[](datatypes.html#Duration) }
  "valueHumanName[](extensibility-definitions.html#Extension.valueHumanName "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { HumanName[](datatypes.html#HumanName) }
  "valueIdentifier[](extensibility-definitions.html#Extension.valueIdentifier "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Identifier[](datatypes.html#Identifier) }
  "valueMoney[](extensibility-definitions.html#Extension.valueMoney "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Money[](datatypes.html#Money) }
  "valuePeriod[](extensibility-definitions.html#Extension.valuePeriod "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Period[](datatypes.html#Period) }
  "valueQuantity[](extensibility-definitions.html#Extension.valueQuantity "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Quantity[](datatypes.html#Quantity) }
  "valueRange[](extensibility-definitions.html#Extension.valueRange "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Range[](datatypes.html#Range) }
  "valueRatio[](extensibility-definitions.html#Extension.valueRatio "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Ratio[](datatypes.html#Ratio) }
  "valueReference[](extensibility-definitions.html#Extension.valueReference "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Reference[](references.html#Reference) }
  "valueSampledData[](extensibility-definitions.html#Extension.valueSampledData "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { SampledData[](datatypes.html#SampledData) }
  "valueSignature[](extensibility-definitions.html#Extension.valueSignature "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Signature[](datatypes.html#Signature) }
  "valueTiming[](extensibility-definitions.html#Extension.valueTiming "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Timing[](datatypes.html#Timing) }
  "valueContactDetail[](extensibility-definitions.html#Extension.valueContactDetail "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { ContactDetail[](metadatatypes.html#ContactDetail) }
  "valueContributor[](extensibility-definitions.html#Extension.valueContributor "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Contributor[](metadatatypes.html#Contributor) }
  "valueDataRequirement[](extensibility-definitions.html#Extension.valueDataRequirement "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { DataRequirement[](metadatatypes.html#DataRequirement) }
  "valueExpression[](extensibility-definitions.html#Extension.valueExpression "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Expression[](metadatatypes.html#Expression) }
  "valueParameterDefinition[](extensibility-definitions.html#Extension.valueParameterDefinition "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { ParameterDefinition[](metadatatypes.html#ParameterDefinition) }
  "valueRelatedArtifact[](extensibility-definitions.html#Extension.valueRelatedArtifact "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { RelatedArtifact[](metadatatypes.html#RelatedArtifact) }
  "valueTriggerDefinition[](extensibility-definitions.html#Extension.valueTriggerDefinition "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { TriggerDefinition[](metadatatypes.html#TriggerDefinition) }
  "valueUsageContext[](extensibility-definitions.html#Extension.valueUsageContext "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { UsageContext[](metadatatypes.html#UsageContext) }
  "valueDosage[](extensibility-definitions.html#Extension.valueDosage "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Dosage[](dosage.html#Dosage) }
  "valueMeta[](extensibility-definitions.html#Extension.valueMeta "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Meta[](resource.html#Meta) }
}

```

**Turtle Template**
```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension[](extensibility.html)
  fhir:Extension.url[](extensibility-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") [ uri[](datatypes.html#uri) ]; # 1..1 identifies the meaning of the extension
  # Extension.value[x][](extensibility-definitions.html#Extension.value\[x\] "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") : 0..1 Value of extension. One of these 50
    fhir:Extension.valueBase64Binary[](extensibility-definitions.html#Extension.valueBase64Binary "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ base64Binary[](datatypes.html#base64Binary) ]
    fhir:Extension.valueBoolean[](extensibility-definitions.html#Extension.valueBoolean "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ boolean[](datatypes.html#boolean) ]
    fhir:Extension.valueCanonical[](extensibility-definitions.html#Extension.valueCanonical "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ canonical[](datatypes.html#canonical) ]
    fhir:Extension.valueCode[](extensibility-definitions.html#Extension.valueCode "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ code[](datatypes.html#code) ]
    fhir:Extension.valueDate[](extensibility-definitions.html#Extension.valueDate "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ date[](datatypes.html#date) ]
    fhir:Extension.valueDateTime[](extensibility-definitions.html#Extension.valueDateTime "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ dateTime[](datatypes.html#dateTime) ]
    fhir:Extension.valueDecimal[](extensibility-definitions.html#Extension.valueDecimal "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ decimal[](datatypes.html#decimal) ]
    fhir:Extension.valueId[](extensibility-definitions.html#Extension.valueId "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ id[](datatypes.html#id) ]
    fhir:Extension.valueInstant[](extensibility-definitions.html#Extension.valueInstant "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ instant[](datatypes.html#instant) ]
    fhir:Extension.valueInteger[](extensibility-definitions.html#Extension.valueInteger "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ integer[](datatypes.html#integer) ]
    fhir:Extension.valueMarkdown[](extensibility-definitions.html#Extension.valueMarkdown "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ markdown[](datatypes.html#markdown) ]
    fhir:Extension.valueOid[](extensibility-definitions.html#Extension.valueOid "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ oid[](datatypes.html#oid) ]
    fhir:Extension.valuePositiveInt[](extensibility-definitions.html#Extension.valuePositiveInt "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ positiveInt[](datatypes.html#positiveInt) ]
    fhir:Extension.valueString[](extensibility-definitions.html#Extension.valueString "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ string[](datatypes.html#string) ]
    fhir:Extension.valueTime[](extensibility-definitions.html#Extension.valueTime "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ time[](datatypes.html#time) ]
    fhir:Extension.valueUnsignedInt[](extensibility-definitions.html#Extension.valueUnsignedInt "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ unsignedInt[](datatypes.html#unsignedInt) ]
    fhir:Extension.valueUri[](extensibility-definitions.html#Extension.valueUri "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ uri[](datatypes.html#uri) ]
    fhir:Extension.valueUrl[](extensibility-definitions.html#Extension.valueUrl "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ url[](datatypes.html#url) ]
    fhir:Extension.valueUuid[](extensibility-definitions.html#Extension.valueUuid "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ uuid[](datatypes.html#uuid) ]
    fhir:Extension.valueAddress[](extensibility-definitions.html#Extension.valueAddress "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Address[](datatypes.html#Address) ]
    fhir:Extension.valueAge[](extensibility-definitions.html#Extension.valueAge "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Age[](datatypes.html#Age) ]
    fhir:Extension.valueAnnotation[](extensibility-definitions.html#Extension.valueAnnotation "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Annotation[](datatypes.html#Annotation) ]
    fhir:Extension.valueAttachment[](extensibility-definitions.html#Extension.valueAttachment "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Attachment[](datatypes.html#Attachment) ]
    fhir:Extension.valueCodeableConcept[](extensibility-definitions.html#Extension.valueCodeableConcept "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ CodeableConcept[](datatypes.html#CodeableConcept) ]
    fhir:Extension.valueCoding[](extensibility-definitions.html#Extension.valueCoding "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Coding[](datatypes.html#Coding) ]
    fhir:Extension.valueContactPoint[](extensibility-definitions.html#Extension.valueContactPoint "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ ContactPoint[](datatypes.html#ContactPoint) ]
    fhir:Extension.valueCount[](extensibility-definitions.html#Extension.valueCount "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Count[](datatypes.html#Count) ]
    fhir:Extension.valueDistance[](extensibility-definitions.html#Extension.valueDistance "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Distance[](datatypes.html#Distance) ]
    fhir:Extension.valueDuration[](extensibility-definitions.html#Extension.valueDuration "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Duration[](datatypes.html#Duration) ]
    fhir:Extension.valueHumanName[](extensibility-definitions.html#Extension.valueHumanName "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ HumanName[](datatypes.html#HumanName) ]
    fhir:Extension.valueIdentifier[](extensibility-definitions.html#Extension.valueIdentifier "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Identifier[](datatypes.html#Identifier) ]
    fhir:Extension.valueMoney[](extensibility-definitions.html#Extension.valueMoney "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Money[](datatypes.html#Money) ]
    fhir:Extension.valuePeriod[](extensibility-definitions.html#Extension.valuePeriod "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Period[](datatypes.html#Period) ]
    fhir:Extension.valueQuantity[](extensibility-definitions.html#Extension.valueQuantity "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Quantity[](datatypes.html#Quantity) ]
    fhir:Extension.valueRange[](extensibility-definitions.html#Extension.valueRange "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Range[](datatypes.html#Range) ]
    fhir:Extension.valueRatio[](extensibility-definitions.html#Extension.valueRatio "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Ratio[](datatypes.html#Ratio) ]
    fhir:Extension.valueReference[](extensibility-definitions.html#Extension.valueReference "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Reference[](references.html#Reference) ]
    fhir:Extension.valueSampledData[](extensibility-definitions.html#Extension.valueSampledData "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ SampledData[](datatypes.html#SampledData) ]
    fhir:Extension.valueSignature[](extensibility-definitions.html#Extension.valueSignature "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Signature[](datatypes.html#Signature) ]
    fhir:Extension.valueTiming[](extensibility-definitions.html#Extension.valueTiming "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Timing[](datatypes.html#Timing) ]
    fhir:Extension.valueContactDetail[](extensibility-definitions.html#Extension.valueContactDetail "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ ContactDetail[](metadatatypes.html#ContactDetail) ]
    fhir:Extension.valueContributor[](extensibility-definitions.html#Extension.valueContributor "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Contributor[](metadatatypes.html#Contributor) ]
    fhir:Extension.valueDataRequirement[](extensibility-definitions.html#Extension.valueDataRequirement "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ DataRequirement[](metadatatypes.html#DataRequirement) ]
    fhir:Extension.valueExpression[](extensibility-definitions.html#Extension.valueExpression "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Expression[](metadatatypes.html#Expression) ]
    fhir:Extension.valueParameterDefinition[](extensibility-definitions.html#Extension.valueParameterDefinition "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ ParameterDefinition[](metadatatypes.html#ParameterDefinition) ]
    fhir:Extension.valueRelatedArtifact[](extensibility-definitions.html#Extension.valueRelatedArtifact "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ RelatedArtifact[](metadatatypes.html#RelatedArtifact) ]
    fhir:Extension.valueTriggerDefinition[](extensibility-definitions.html#Extension.valueTriggerDefinition "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ TriggerDefinition[](metadatatypes.html#TriggerDefinition) ]
    fhir:Extension.valueUsageContext[](extensibility-definitions.html#Extension.valueUsageContext "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ UsageContext[](metadatatypes.html#UsageContext) ]
    fhir:Extension.valueDosage[](extensibility-definitions.html#Extension.valueDosage "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Dosage[](dosage.html#Dosage) ]
    fhir:Extension.valueMeta[](extensibility-definitions.html#Extension.valueMeta "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Meta[](resource.html#Meta) ]
]

```

**Changes since Release 3**
[Extension](extensibility.html#Extension) |   
---|---  
Extension.value[x] | 
  * Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage

  
See the [Full Difference](diff.html) for further information
**Structure**
[Name](formats.html#table "The logical name of the element") | [Flags](formats.html#table "Information about the use of the element") | [Card.](formats.html#table "Minimum and Maximum # of times the the element can appear in the instance") | [Type](formats.html#table "Reference to the type of the element") |  [Description & Constraints](formats.html#table "Additional information about the element")[![doco](help16.png)](formats.html#table "Legend for this format")  
---|---|---|---|---  
![.](tbl_spacer.png)![.](icon_element.gif) [Extension](extensibility-definitions.html#Extension "Extension : Optional Extension Element - found in all resources.") |  [I](conformance-rules.html#constraints "This element has or is affected by some invariants")[N](versions.html#std-process "Standards Status = Normative") |  | [Element](element.html) | Optional Extensions Element  
+ Rule: Must have either extensions or value[x], not both  
Elements defined in Ancestors: [id](element.html#Element "Unique id for the element within a resource \(for internal references\). This may be any string value that does not contain spaces."), [extension](element.html#Element "May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.")  
![.](tbl_spacer.png)![.](tbl_vjoin.png)![.](icon_primitive.png) [url](extensibility-definitions.html#Extension.url "Extension.url : Source of the definition for the extension code - a logical name or a URL.") |  | 1..1 | [uri](datatypes.html#uri) | identifies the meaning of the extension  
![.](tbl_spacer.png)![.](tbl_vjoin_end.png)![.](icon_datatype.gif) [value[x]](extensibility-definitions.html#Extension.value_x_ "Extension.value\[x\] : Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") |  | 0..1 | [*](datatypes.html#open) | Value of extension  
  
[![doco](help16.png) Documentation for this format](formats.html#table "Legend for this format")  
**UML Diagram** ([Legend](formats.html#uml))
ElementExtensions - as described for all elements: additional information that is not part of the basic definition of the resource / typeextension : Extension 0..*ExtensionSource of the definition for the extension code - a logical name or a URLurl : uri [1..1]Value of extension - must be one of a constrained set of the data types (see [Extensibility](extensibility.html) for a list)value[x] : * [0..1]
**XML Template**
```

<[**extension|modifierExtension**](extensibility-definitions.html#Extension "Optional Extension Element - found in all resources.") xmlns="http://hl7.org/fhir" url="identifies the meaning of the extension (uri[](datatypes.html#uri))">
 <!-- from Element: extension[](extensibility.html) -->
 <[**value[x]**](extensibility-definitions.html#Extension.value\[x\] "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")><!-- **0..1** *[](datatypes.html#open) Value of extension[](terminologies.html#unbound) --></value[x]>
</extension|modifierExtension>

```

**JSON Template**
```

{[![doco](help.png)](json.html "Documentation for this format")
  // from Element: extension[](extensibility.html)
  "url[](extensibility-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.")" : "<uri[](datatypes.html#uri)>", // **R!**  identifies the meaning of the extension[](terminologies.html#unbound)
  // value[x]: Value of extension. One of these 50:
  "valueBase64Binary[](extensibility-definitions.html#Extension.valueBase64Binary "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<base64Binary[](datatypes.html#base64Binary)>"
  "valueBoolean[](extensibility-definitions.html#Extension.valueBoolean "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : <boolean[](datatypes.html#boolean)>
  "valueCanonical[](extensibility-definitions.html#Extension.valueCanonical "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<canonical[](datatypes.html#canonical)>"
  "valueCode[](extensibility-definitions.html#Extension.valueCode "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<code[](datatypes.html#code)>"
  "valueDate[](extensibility-definitions.html#Extension.valueDate "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<date[](datatypes.html#date)>"
  "valueDateTime[](extensibility-definitions.html#Extension.valueDateTime "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<dateTime[](datatypes.html#dateTime)>"
  "valueDecimal[](extensibility-definitions.html#Extension.valueDecimal "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : <decimal[](datatypes.html#decimal)>
  "valueId[](extensibility-definitions.html#Extension.valueId "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<id[](datatypes.html#id)>"
  "valueInstant[](extensibility-definitions.html#Extension.valueInstant "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<instant[](datatypes.html#instant)>"
  "valueInteger[](extensibility-definitions.html#Extension.valueInteger "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : <integer[](datatypes.html#integer)>
  "valueMarkdown[](extensibility-definitions.html#Extension.valueMarkdown "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<markdown[](datatypes.html#markdown)>"
  "valueOid[](extensibility-definitions.html#Extension.valueOid "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<oid[](datatypes.html#oid)>"
  "valuePositiveInt[](extensibility-definitions.html#Extension.valuePositiveInt "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<positiveInt[](datatypes.html#positiveInt)>"
  "valueString[](extensibility-definitions.html#Extension.valueString "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<string[](datatypes.html#string)>"
  "valueTime[](extensibility-definitions.html#Extension.valueTime "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<time[](datatypes.html#time)>"
  "valueUnsignedInt[](extensibility-definitions.html#Extension.valueUnsignedInt "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<unsignedInt[](datatypes.html#unsignedInt)>"
  "valueUri[](extensibility-definitions.html#Extension.valueUri "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<uri[](datatypes.html#uri)>"
  "valueUrl[](extensibility-definitions.html#Extension.valueUrl "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<url[](datatypes.html#url)>"
  "valueUuid[](extensibility-definitions.html#Extension.valueUuid "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : "<uuid[](datatypes.html#uuid)>"
  "valueAddress[](extensibility-definitions.html#Extension.valueAddress "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Address[](datatypes.html#Address) }
  "valueAge[](extensibility-definitions.html#Extension.valueAge "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Age[](datatypes.html#Age) }
  "valueAnnotation[](extensibility-definitions.html#Extension.valueAnnotation "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Annotation[](datatypes.html#Annotation) }
  "valueAttachment[](extensibility-definitions.html#Extension.valueAttachment "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Attachment[](datatypes.html#Attachment) }
  "valueCodeableConcept[](extensibility-definitions.html#Extension.valueCodeableConcept "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { CodeableConcept[](datatypes.html#CodeableConcept) }
  "valueCoding[](extensibility-definitions.html#Extension.valueCoding "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Coding[](datatypes.html#Coding) }
  "valueContactPoint[](extensibility-definitions.html#Extension.valueContactPoint "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { ContactPoint[](datatypes.html#ContactPoint) }
  "valueCount[](extensibility-definitions.html#Extension.valueCount "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Count[](datatypes.html#Count) }
  "valueDistance[](extensibility-definitions.html#Extension.valueDistance "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Distance[](datatypes.html#Distance) }
  "valueDuration[](extensibility-definitions.html#Extension.valueDuration "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Duration[](datatypes.html#Duration) }
  "valueHumanName[](extensibility-definitions.html#Extension.valueHumanName "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { HumanName[](datatypes.html#HumanName) }
  "valueIdentifier[](extensibility-definitions.html#Extension.valueIdentifier "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Identifier[](datatypes.html#Identifier) }
  "valueMoney[](extensibility-definitions.html#Extension.valueMoney "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Money[](datatypes.html#Money) }
  "valuePeriod[](extensibility-definitions.html#Extension.valuePeriod "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Period[](datatypes.html#Period) }
  "valueQuantity[](extensibility-definitions.html#Extension.valueQuantity "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Quantity[](datatypes.html#Quantity) }
  "valueRange[](extensibility-definitions.html#Extension.valueRange "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Range[](datatypes.html#Range) }
  "valueRatio[](extensibility-definitions.html#Extension.valueRatio "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Ratio[](datatypes.html#Ratio) }
  "valueReference[](extensibility-definitions.html#Extension.valueReference "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Reference[](references.html#Reference) }
  "valueSampledData[](extensibility-definitions.html#Extension.valueSampledData "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { SampledData[](datatypes.html#SampledData) }
  "valueSignature[](extensibility-definitions.html#Extension.valueSignature "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Signature[](datatypes.html#Signature) }
  "valueTiming[](extensibility-definitions.html#Extension.valueTiming "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Timing[](datatypes.html#Timing) }
  "valueContactDetail[](extensibility-definitions.html#Extension.valueContactDetail "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { ContactDetail[](metadatatypes.html#ContactDetail) }
  "valueContributor[](extensibility-definitions.html#Extension.valueContributor "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Contributor[](metadatatypes.html#Contributor) }
  "valueDataRequirement[](extensibility-definitions.html#Extension.valueDataRequirement "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { DataRequirement[](metadatatypes.html#DataRequirement) }
  "valueExpression[](extensibility-definitions.html#Extension.valueExpression "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Expression[](metadatatypes.html#Expression) }
  "valueParameterDefinition[](extensibility-definitions.html#Extension.valueParameterDefinition "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { ParameterDefinition[](metadatatypes.html#ParameterDefinition) }
  "valueRelatedArtifact[](extensibility-definitions.html#Extension.valueRelatedArtifact "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { RelatedArtifact[](metadatatypes.html#RelatedArtifact) }
  "valueTriggerDefinition[](extensibility-definitions.html#Extension.valueTriggerDefinition "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { TriggerDefinition[](metadatatypes.html#TriggerDefinition) }
  "valueUsageContext[](extensibility-definitions.html#Extension.valueUsageContext "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { UsageContext[](metadatatypes.html#UsageContext) }
  "valueDosage[](extensibility-definitions.html#Extension.valueDosage "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Dosage[](dosage.html#Dosage) }
  "valueMeta[](extensibility-definitions.html#Extension.valueMeta "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).")" : { Meta[](resource.html#Meta) }
}

```

**Turtle Template**
```

@prefix fhir: <http://hl7.org/fhir/> .

[
 # from Element: Element.extension[](extensibility.html)
  fhir:Extension.url[](extensibility-definitions.html#Extension.url "Source of the definition for the extension code - a logical name or a URL.") [ uri[](datatypes.html#uri) ]; # 1..1 identifies the meaning of the extension
  # Extension.value[x][](extensibility-definitions.html#Extension.value\[x\] "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") : 0..1 Value of extension. One of these 50
    fhir:Extension.valueBase64Binary[](extensibility-definitions.html#Extension.valueBase64Binary "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ base64Binary[](datatypes.html#base64Binary) ]
    fhir:Extension.valueBoolean[](extensibility-definitions.html#Extension.valueBoolean "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ boolean[](datatypes.html#boolean) ]
    fhir:Extension.valueCanonical[](extensibility-definitions.html#Extension.valueCanonical "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ canonical[](datatypes.html#canonical) ]
    fhir:Extension.valueCode[](extensibility-definitions.html#Extension.valueCode "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ code[](datatypes.html#code) ]
    fhir:Extension.valueDate[](extensibility-definitions.html#Extension.valueDate "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ date[](datatypes.html#date) ]
    fhir:Extension.valueDateTime[](extensibility-definitions.html#Extension.valueDateTime "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ dateTime[](datatypes.html#dateTime) ]
    fhir:Extension.valueDecimal[](extensibility-definitions.html#Extension.valueDecimal "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ decimal[](datatypes.html#decimal) ]
    fhir:Extension.valueId[](extensibility-definitions.html#Extension.valueId "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ id[](datatypes.html#id) ]
    fhir:Extension.valueInstant[](extensibility-definitions.html#Extension.valueInstant "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ instant[](datatypes.html#instant) ]
    fhir:Extension.valueInteger[](extensibility-definitions.html#Extension.valueInteger "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ integer[](datatypes.html#integer) ]
    fhir:Extension.valueMarkdown[](extensibility-definitions.html#Extension.valueMarkdown "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ markdown[](datatypes.html#markdown) ]
    fhir:Extension.valueOid[](extensibility-definitions.html#Extension.valueOid "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ oid[](datatypes.html#oid) ]
    fhir:Extension.valuePositiveInt[](extensibility-definitions.html#Extension.valuePositiveInt "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ positiveInt[](datatypes.html#positiveInt) ]
    fhir:Extension.valueString[](extensibility-definitions.html#Extension.valueString "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ string[](datatypes.html#string) ]
    fhir:Extension.valueTime[](extensibility-definitions.html#Extension.valueTime "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ time[](datatypes.html#time) ]
    fhir:Extension.valueUnsignedInt[](extensibility-definitions.html#Extension.valueUnsignedInt "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ unsignedInt[](datatypes.html#unsignedInt) ]
    fhir:Extension.valueUri[](extensibility-definitions.html#Extension.valueUri "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ uri[](datatypes.html#uri) ]
    fhir:Extension.valueUrl[](extensibility-definitions.html#Extension.valueUrl "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ url[](datatypes.html#url) ]
    fhir:Extension.valueUuid[](extensibility-definitions.html#Extension.valueUuid "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ uuid[](datatypes.html#uuid) ]
    fhir:Extension.valueAddress[](extensibility-definitions.html#Extension.valueAddress "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Address[](datatypes.html#Address) ]
    fhir:Extension.valueAge[](extensibility-definitions.html#Extension.valueAge "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Age[](datatypes.html#Age) ]
    fhir:Extension.valueAnnotation[](extensibility-definitions.html#Extension.valueAnnotation "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Annotation[](datatypes.html#Annotation) ]
    fhir:Extension.valueAttachment[](extensibility-definitions.html#Extension.valueAttachment "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Attachment[](datatypes.html#Attachment) ]
    fhir:Extension.valueCodeableConcept[](extensibility-definitions.html#Extension.valueCodeableConcept "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ CodeableConcept[](datatypes.html#CodeableConcept) ]
    fhir:Extension.valueCoding[](extensibility-definitions.html#Extension.valueCoding "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Coding[](datatypes.html#Coding) ]
    fhir:Extension.valueContactPoint[](extensibility-definitions.html#Extension.valueContactPoint "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ ContactPoint[](datatypes.html#ContactPoint) ]
    fhir:Extension.valueCount[](extensibility-definitions.html#Extension.valueCount "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Count[](datatypes.html#Count) ]
    fhir:Extension.valueDistance[](extensibility-definitions.html#Extension.valueDistance "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Distance[](datatypes.html#Distance) ]
    fhir:Extension.valueDuration[](extensibility-definitions.html#Extension.valueDuration "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Duration[](datatypes.html#Duration) ]
    fhir:Extension.valueHumanName[](extensibility-definitions.html#Extension.valueHumanName "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ HumanName[](datatypes.html#HumanName) ]
    fhir:Extension.valueIdentifier[](extensibility-definitions.html#Extension.valueIdentifier "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Identifier[](datatypes.html#Identifier) ]
    fhir:Extension.valueMoney[](extensibility-definitions.html#Extension.valueMoney "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Money[](datatypes.html#Money) ]
    fhir:Extension.valuePeriod[](extensibility-definitions.html#Extension.valuePeriod "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Period[](datatypes.html#Period) ]
    fhir:Extension.valueQuantity[](extensibility-definitions.html#Extension.valueQuantity "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Quantity[](datatypes.html#Quantity) ]
    fhir:Extension.valueRange[](extensibility-definitions.html#Extension.valueRange "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Range[](datatypes.html#Range) ]
    fhir:Extension.valueRatio[](extensibility-definitions.html#Extension.valueRatio "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Ratio[](datatypes.html#Ratio) ]
    fhir:Extension.valueReference[](extensibility-definitions.html#Extension.valueReference "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Reference[](references.html#Reference) ]
    fhir:Extension.valueSampledData[](extensibility-definitions.html#Extension.valueSampledData "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ SampledData[](datatypes.html#SampledData) ]
    fhir:Extension.valueSignature[](extensibility-definitions.html#Extension.valueSignature "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Signature[](datatypes.html#Signature) ]
    fhir:Extension.valueTiming[](extensibility-definitions.html#Extension.valueTiming "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Timing[](datatypes.html#Timing) ]
    fhir:Extension.valueContactDetail[](extensibility-definitions.html#Extension.valueContactDetail "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ ContactDetail[](metadatatypes.html#ContactDetail) ]
    fhir:Extension.valueContributor[](extensibility-definitions.html#Extension.valueContributor "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Contributor[](metadatatypes.html#Contributor) ]
    fhir:Extension.valueDataRequirement[](extensibility-definitions.html#Extension.valueDataRequirement "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ DataRequirement[](metadatatypes.html#DataRequirement) ]
    fhir:Extension.valueExpression[](extensibility-definitions.html#Extension.valueExpression "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Expression[](metadatatypes.html#Expression) ]
    fhir:Extension.valueParameterDefinition[](extensibility-definitions.html#Extension.valueParameterDefinition "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ ParameterDefinition[](metadatatypes.html#ParameterDefinition) ]
    fhir:Extension.valueRelatedArtifact[](extensibility-definitions.html#Extension.valueRelatedArtifact "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ RelatedArtifact[](metadatatypes.html#RelatedArtifact) ]
    fhir:Extension.valueTriggerDefinition[](extensibility-definitions.html#Extension.valueTriggerDefinition "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ TriggerDefinition[](metadatatypes.html#TriggerDefinition) ]
    fhir:Extension.valueUsageContext[](extensibility-definitions.html#Extension.valueUsageContext "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ UsageContext[](metadatatypes.html#UsageContext) ]
    fhir:Extension.valueDosage[](extensibility-definitions.html#Extension.valueDosage "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Dosage[](dosage.html#Dosage) ]
    fhir:Extension.valueMeta[](extensibility-definitions.html#Extension.valueMeta "Value of extension - must be one of a constrained set of the data types \(see \[Extensibility\]\(extensibility.html\) for a list\).") [ Meta[](resource.html#Meta) ]
]

```

**Changes since Release 3**
[Extension](extensibility.html#Extension) |   
---|---  
Extension.value[x] | 
  * Add Types canonical, url, uuid, ContactDetail, Contributor, DataRequirement, Expression, ParameterDefinition, RelatedArtifact, TriggerDefinition, UsageContext, Dosage

  
See the [Full Difference](diff.html) for further information
Notes: 
  * The `url` is a mandatory attribute / property and identifies a retrievable [extension definition](defining-extensions.html) that defines the content and meaning of the extension
  * The `url` SHALL be a URL, not a URN (e.g. not an OID or a UUID), and it SHALL be the canonical URL of a StructureDefinition that defines the extension. Except for child extensions defined within complex extensions, the URL SHALL be an absolute URL. 
  * The structure definitions for the extension SHOULD be available to consumers of an instance. The preferred mechanisms for achieving this availability are the direct resolvability of the extension's canonical URL and/or the publishing of the extension definition on a registry that is available and known to those systems that will be consuming the instances containing the extension
  * An extension SHALL have either a value (i.e. a value[x] element) or sub-extensions, but not both. If present, the value[x] element SHALL have content (value attribute or other elements)
  * If it is not safe for an application processing the content of the resource to ignore the extension it SHALL be represented using a [Modifier Extension](#isModifier) rather than an `extension` element
  * There are a few resources (ones that do not specialize [DomainResource](domainresource.html)) where extensions are not allowed on the root element, but extensions can appear elsewhere through the resource
  * The _value[x]_ element has an actual name of "value" and then the TitleCased name of one of these defined types, and its contents are those as defined for that type: 
    * valueBase64Binary: [base64Binary](datatypes.html#base64Binary)
    * valueBoolean: [boolean](datatypes.html#boolean)
    * valueCanonical: [canonical](datatypes.html#canonical)
    * valueCode: [code](datatypes.html#code) (only if the extension definition provides a [fixed](terminologies.html#code) binding to a suitable set of codes)
    * valueDate: [date](datatypes.html#date)
    * valueDateTime: [dateTime](datatypes.html#dateTime)
    * valueDecimal: [decimal](datatypes.html#decimal)
    * valueId: [id](datatypes.html#id)
    * valueInstant: [instant](datatypes.html#instant)
    * valueInteger: [integer](datatypes.html#integer)
    * valueMarkdown: [markdown](datatypes.html#markdown)
    * valueOid: [oid](datatypes.html#oid)
    * valuePositiveInt: [positiveInt](datatypes.html#positiveInt)
    * valueString: [string](datatypes.html#string)
    * valueTime: [time](datatypes.html#time)
    * valueUnsignedInt: [unsignedInt](datatypes.html#unsignedInt)
    * valueUri: [uri](datatypes.html#uri)
    * valueUrl: [url](datatypes.html#url)
    * valueUuid: [uuid](datatypes.html#uuid)
    * valueAddress: [Address](datatypes.html#Address)
    * valueAge: [Age](datatypes.html#Age)
    * valueAnnotation: [Annotation](datatypes.html#Annotation)
    * valueAttachment: [Attachment](datatypes.html#Attachment)
    * valueCodeableConcept: [CodeableConcept](datatypes.html#CodeableConcept)
    * valueCoding: [Coding](datatypes.html#Coding)
    * valueContactPoint: [ContactPoint](datatypes.html#ContactPoint)
    * valueCount: [Count](datatypes.html#Count)
    * valueDistance: [Distance](datatypes.html#Distance)
    * valueDuration: [Duration](datatypes.html#Duration)
    * valueHumanName: [HumanName](datatypes.html#HumanName)
    * valueIdentifier: [Identifier](datatypes.html#Identifier)
    * valueMoney: [Money](datatypes.html#Money)
    * valuePeriod: [Period](datatypes.html#Period)
    * valueQuantity: [Quantity](datatypes.html#Quantity)
    * valueRange: [Range](datatypes.html#Range)
    * valueRatio: [Ratio](datatypes.html#Ratio)
    * valueReference: [Reference](references.html#Reference) - a reference to another resource
    * valueSampledData: [SampledData](datatypes.html#SampledData)
    * valueSignature: [Signature](datatypes.html#Signature)
    * valueTiming: [Timing](datatypes.html#Timing)
    * valueContactDetail: [ContactDetail](metadatatypes.html#ContactDetail)
    * valueContributor: [Contributor](metadatatypes.html#Contributor)
    * valueDataRequirement: [DataRequirement](metadatatypes.html#DataRequirement)
    * valueExpression: [Expression](metadatatypes.html#Expression)
    * valueParameterDefinition: [ParameterDefinition](metadatatypes.html#ParameterDefinition)
    * valueRelatedArtifact: [RelatedArtifact](metadatatypes.html#RelatedArtifact)
    * valueTriggerDefinition: [TriggerDefinition](metadatatypes.html#TriggerDefinition)
    * valueUsageContext: [UsageContext](metadatatypes.html#UsageContext)
    * valueDosage: [Dosage](dosage.html#Dosage)
    * valueMeta: [Meta](resource.html#Meta)


Here is an example of an extension in XML ([see definition](extension-iso21090-en-use.html)): 
```

<name>
  <extension url="http://hl7.org/fhir/StructureDefinition/iso-21090-EN-use" >
    <valueCode value="I" />
  </extension>
  <text value="Chief Red Cloud"/>
</name>

```

In this example the name with text = "Chief Red Cloud" is extended to have a name use code of "Indigenous" (defined in ISO 21090, but very rarely used in practice). 
In JSON, extensions are represented similarly: 
```

{
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/iso-21090-EN-use",
    "valueCode" : "I"
  }],
  "text" : "Chief Red Cloud"
}

```

Making the types explicit in the representation means that all systems can read and write (and therefore store and/or exchange) extensions correctly without needing to access the definition of the extension. 
Note that the JSON representation for extensions on primitive data types is handled differently. See [Representing primitive types in JSON](json.html#primitive) for further information. 
Extensions can also contain extensions, either because the extension definition itself defines complex content - that is, a nested tree of values in the extension - or because the extension is extended with an additional extension defined separately. 
In the case where an extension defines complex content, the identity of the parts of the extension are local/relative to the reference to the extension definition. 
As an example, consider extending a patient with information about citizenship ([see definition](extension-patient-citizenship.html)) containing 2 fields: code and period. In XML: 
```

<Patient>
  <extension url="http://hl7.org/fhir/StructureDefinition/patient-citizenship" >
    <extension url="code" >
      <valueCodeableConcept>
        <coding>
          <system value="urn:iso:std:iso:3166" />
          <code value="DE" />
        </coding>
      </valueCodeableConcept>
    </extension>
    <extension url="period" >
      <valuePeriod>
        <start value="2009-03-14" />
      </valuePeriod>
    </extension>
  </extension>
  <!-- other data for patient -->
</Patient>

```

Or in JSON: 
```

{
  "resourceType" : "Patient",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/patient-citizenship",
    "extension" : [{
      "url" : "code",
      "valueCodeableConcept" : {
          "coding" : [{
             "system" : "urn:iso:std:iso:3166",
             "code" : "DE"
          }]
       }
    }, {
      "url" : "period",
      "valuePeriod" : {
         "start" : "2009-03-14"
      }
    }]
	}]
}

```

This extension can be extended again, by adding a "passport-number" extension: 
The passport number is defined as a separate extension (e.g. by an implementing organization, not in this specification) rather than part of the official citizenship extension. The URL of the extension is thus different. In XML: 
```


<Patient>
  <extension url="http://hl7.org/fhir/StructureDefinition/patient-citizenship" >
    <extension url="code" >
      <valueCodeableConcept>
        <coding>
          <system value="urn:iso:std:iso:3166" />
          <code value="DE" />
        </coding>
      </valueCodeableConcept>
    </extension>
    <extension url="period" >
      <valuePeriod>
        <start value="2009-03-14" />
      </valuePeriod>
    </extension>
    <extension url="http://acme.org/fhir/StructureDefinition/passport-number" >
        <valueString value="12345ABC" />
      </extension>
    <!-- other data for patient -->
  </extension>
</Patient>

```

or in JSON: 
```


{
  "resourceType" : "Patient",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/patient-citizenship",
    "extension" : [{
      "url" : "code",
      "valueCodeableConcept" : {
        "coding" : [{
          "system" : "urn:iso:std:iso:3166",
          "code" : "DE"
        }]
      }
    },{
      "url" : "period",
      "valuePeriod" : {
        "start" : "2009-03-14"
      }
    },
		{
      "url": "http://acme.org/fhir/StructureDefinition/passport-number",
      "valueString": "12345ABC"
    }]
  }]
}

```

Note that this passport number extension is shown here as an example defined by a fake organization, and not appropriate for re-use by implementers. 
##  2.5.0.2 Modifier Extensions [](extensibility.html#modifierExtension "link to here")
There are some cases where the information provided in an extension modifies the meaning of the element that contains it. Typically, this means information that qualifies or negates the primary meaning of the element that contains it. Some examples: 
  * A flag on a [Patient.contact] indicating they are **not** to be contacted - i.e. a next of kin for record-keeping purposes only
  * Using the [Condition](condition.html) resource to record an assertion that a patient has a family history of the condition rather than the condition itself
  * Asserting that a performer was **not** actually involved in a [Procedure](procedure.html)
  * Asserting an additional subsumption relationship on a concept in a [value set](valueset.html)


Such extensions are known as "modifier extensions". For further information, see [the definition of what makes an element - or an extension - a modifier](conformance-rules.html#modifier). If modifier extensions are present, an application is restricted in its ability to safely process the resource unless it knows what the extension means for its own use of the data. 
Implementers SHOULD avoid the use of modifier extensions where possible. Any use should be carefully considered against its possible downstream consequences. Inclusion of modifier extensions in an instance would be expected to significantly limit the ability of other systems to process the instance. However, implementers are often forced into these situations by the business arrangements around the use of resources, so this specification creates a framework for handling such cases. Implementers who are introducing an extension and are uncertain whether the extension should be marked as a modifier are encouraged to raise the question on [chat.fhir.org ![](external.png)](http://chat.fhir.org). 
This specification allows for such modifier elements to be included at the base of a resource or in any elements that do not have a data type (e.g. the elements that correspond to classes in the resource UML diagrams), and on a [few specially selected data types](datatypes.html#modifiers). Other data types and elements inside data types SHALL NOT have modifier extensions, and extensions SHALL NOT have modifier extensions internally (except for the reusable structures allowed to appear in extensions, listed above). 
Note that complex extensions are allowed to have elements in the complex extension that are marked [Is-Modifier = true](conformance-rules.html#isModifier), which means that these elements modify the extension value itself. Internal extensions like this marked "Is-Modifier" are still represented using the `extension` element, not `modifierExtension` because the impact of the modifier element is expected to be known by applications that understand the containing extension. 
Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). Is-modifier elements not defined as part of an extension's definition cannot be conveyed. 
In XML, these modifier elements are represented using an element named `modifierExtension`, which has same content as the `extension` element documented above: 
Example: There's no element on [MedicationRequest](medicationrequest.html) to write an "anti-prescription" - an instruction not to take a medication for a particular period. Classical clinical recording systems do not record this as a prescription - but one particular system does, and these "anti-prescription" records need to be shared within the institution where this happens as they are an important part of the workflow. Hence, applications are allowed to extend a resource with data like this: 
```

<MedicationRequest>
  <modifierExtension url="http://example.org/fhir/StructureDefinition/anti-prescription">
    <valueBoolean value="true"/>
  </modifierExtension>
  <!-- ... other content ... -->
</MedicationRequest>

```

Or in JSON: 
```

{
  "resourceType" : "MedicationRequest",
  "modifierExtension" : [{
    "url" : "http://example.org/fhir/StructureDefinition/anti-prescription",
    "valueBoolean" : true
  }],
  .. other content ...
}

```

Implementations processing the data in resources SHALL check for modifiers anywhere they could appear, and if a modifier extension is present on a data element that the application 'processes', SHALL do one of these things: 
  1. recognize the modifier extension, and understand the impact of the extension when using the data
  2. reject instances that contain the modifier extension
  3. treat such instances as "for rendering purposes only" - i.e. check that the narrative status = `extensions` or `generated`, display the narrative and don't process the discrete data
  4. Ask for a human to check the modifier extension before proceeding to process the data
  5. carry a warning concerning the data along with any action or output that results from processing the data to inform users that it has not fully understood the source information


Processing the data of a resource typically means copying or filtering data out of a resource for use in another context (display to a human, decision support, exchange in another format where not all information is included, or storing it for this kind of use). Servers and background processes that simply move whole resources around unchanged are not "processing the data of the resource", and therefore these applications are not required to check for unknown modifier extensions. 
**#1** : When an application understands this extension, it means that some developer has provided appropriate instructions for what to do with the data contained in it because of the existence of the modifier extension or has determined that the modifier does not impact on the system's computational functions. Note that this assessment needs to be repeated each time a system's computational behavior changes 
**#2** : This means that implementations are not inherently required to "support" a modifier extension in any meaningful way - they can achieve this understanding by rejecting instances that contain this extension (a server, for instance, could return a HTTP 422 status code with an [OperationOutcome](operationoutcome.html) if a client PUTs or POSTs a modifier extension it does not know). Applications might also be able to ignore a modifier extension if they know that it is safe to do so in their own context, though this would not usually be the case. 
Implementations SHALL ensure that they do not process data containing unrecognized modifier extensions. Note that implementations might be able to be sure, due to their implementation environment (e.g. specific trading partner agreement), that modifier extensions will never occur, and can therefore meet the requirement to check for modifiers at the design stage. However, since integration and deployment options often change, applications SHOULD always check for modifier extensions when processing resources. 
**#3** : One way to warn the user is to download the extension definition from the given URL, and then use the defined display name to present the extension to the user. An error message could look something like this: 
![](modifier-extension-warning.png)
Note that the narrative of the resource SHALL contain modifying information, so it is safe to show this to the user as an expression of the resource's content. A warning dialog box could be extended to offer the user the choice to see the original narrative. 
Here is the prescription example from above with narrative: 
```

<MedicationRequest xmlns="http://hl7.org/fhir">
  <text>
    <status value="generated"/>
    <div xmlns="http://www.w3.org/1999/xhtml">
      <p><b>Note: This prescription is an instruction NOT to take a medication</b></p>
      <!-- snip actual narrative -->
    </div>
  </text>
  <!-- ...data... -->
  <modifierExtension url="http://example.org/fhir/StructureDefinition/anti-prescription">
    <valueBoolean value="true"/>
  </modifierExtension>
  <!-- ...data... -->
</MedicationRequest>

```

An application only needs to concern itself with modifier extensions on elements that it processes. Take, for example, a case where a procedure resource has a modifier extension on one of the `performer` elements indicating that they did not participate in the procedure. If an application is not using the performer details at all, the fact that one of the performers has a modifier extension is irrelevant and the application is free to ignore it. If the application does process the performers, and it sees the modifier extension, it must act in one of the ways outlined above. 
[Implementation Guides](implementationguide.html) might place limitations on the appearance of modifier extensions within instances that comply with the implementation guide. 
###  2.5.0.2.1 Summary: Conformance Rules for Modifier Extensions [](extensibility.html#Summary "link to here")
  * A Modifier Extension SHALL only modify the element which contains it and/or that element's children
  * It SHALL always be safe to show the narrative to humans; any modifier extension SHALL be represented in the narrative
  * Applications SHALL always ensure unrecognized modifier extensions are not present when processing the data from any element that might have carry modifier extensions
  * If a Modifier Extension that an application does not understand is present, the application SHALL refuse to process the resource or affected element, or SHALL provide an appropriate warning to its users


###  2.5.0.2.2 Special Case: Missing data [](extensibility.html#Special-Case "link to here")
In some cases, implementers might find that they do not have appropriate data for an element with minimum cardinality = 1. In this case, the element must be present, but unless the resource or a profile on it has made the actual value of the primitive data type mandatory, it is possible to provide an extension that explains why the primitive value is not present: 
```

<uri>
  <extension url="http://hl7.org/fhir/StructureDefinition/data-absent-reason">
    <valueCode="unknown"/>
  </extension>
</uri>

```

In this example, instead of a value, a [data missing code](general-extensions.html) is provided. Note that it is not required that this particular extension be used. This extension is **not** a modifier extension, because the primitive data type has no value. 
It is not valid to create a fictional piece of data for the primitive value, and then add an extension indicating that the data has been constructed to meet the data rules. This would be both a bad idea as well as a modifier extension, which is not allowed on simple data types. 
##  2.5.0.3 Exchanging Extensions [](extensibility.html#exchange "link to here")
_Note: This section describes the use of "non-modifier extensions", except where "modifier extensions" are explicitly mentioned (see[Modifier Extensions](#isModifier) above for details)._
Extensions are a way of allowing local requirements to be reflected in a resource using a common information based approach so that all systems can confidently process them using the same tools. However, when it comes to processing the information, applications will be constrained in their ability to handle extensions by the degree to which they are informed about them. 
While the structured definition of an extension should always be available (see below for details), the mere availability of a definition does not automatically mean that applications know how to handle them correctly - generally, human decisions are required to determine how the data in extensions should be handled, along with the implicit obligations that surround the information. 
For this reason, local requirements that manifest as extensions are an obstacle to integration and interoperability. The more the requirements are shared (i.e. regional or national scale), the less of an obstacle the extensions (and the requirements they represent) will represent. The consistent representation, definition and registration of extensions that this specification defines cannot resolve that problem - it only provides a framework within which such local variations can be handled more easily. 
When it comes to deploying applications that support local requirements, situations will very likely arise where different applications exchanging information with each other are supporting different sets of extensions. This specification defines some basic rules that are intended to make management of these situations easier, but it cannot resolve them. 
  * When exchanging resources, systems SHOULD retain unknown extensions when they are capable of doing so (just as they SHOULD retain core elements when they are capable of doing so)
  * If a system modifies a resource it SHOULD remove any extensions that it does not understand from the modified element and its descendants, because it cannot know whether the modifications it has made might invalidate the value of the unknown extension
  * Systems that drop existing elements are considered to be "[processing the containing element](#processing)"
  * A system SHALL NOT modify a resource or element that contains "modifier" extensions it doesn't understand
  * Applications SHOULD ignore extensions that they do not recognize if they are not "modifier" extensions


The degree to which a system can retain unknown extensions is a function of the type of system it is: a general purpose FHIR server, or a middleware engine would be expected to retain all extensions, while an application that manages patient registration through a user interface can only retain extensions to the degree that the information in them is part of the set managed by the user. Other applications will fall somewhere between these two extremes. 
###  2.5.0.3.1 Summary: Handling extensions [](extensibility.html#Summary2 "link to here")
Use the following rules as a guideline for handling resources: 
  * When writing extensions, make sure they are defined and published
  * When reading, navigating through or searching on elements that can have modifier extensions, check whether there are any modifier extensions present
  * When reading elements, read and process the extensions you know and use, and ignore other extensions **except for modifier extensions**
  * Retain extensions whenever you can


®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:37+1100. [QA Page](qa.html)   
Links: [Search ![](external.png)](http://hl7.org/fhir/search.cfm) | [Version History](history.html) | [Table of Contents](toc.html) | [Credits](credits.html) | [Compare to R3 ![](external.png)](http://services.w3.org/htmldiff?doc1=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fextensibility.html&doc2=http%3A%2F%2Fbuild.fhir.org%2Fextensibility.html) | [![CC0](cc0.png)](license.html) | [Propose a change ![](external.png)](http://hl7.org/fhir-issues)
