---
url: https://hl7.org/fhir/R4/compartmentdefinition-practitioner.html
title: Unknown
crawled: unknown
depth: 0
---

[![logo fhir](https://hl7.org/fhir/R4/assets/images/fhir-logo-www.png) ](http://hl7.org/fhir)
**Release 4**
[ ![visit the hl7 website](https://hl7.org/fhir/R4/assets/images/hl7-logo.png) ](http://www.hl7.org)
[![Search FHIR](https://hl7.org/fhir/R4/assets/images/search.png)](http://hl7.org/fhir/search.cfm)
[FHIR](https://hl7.org/fhir/R4/index.html)
  * [Home](https://hl7.org/fhir/R4/index.html)
  * [Getting Started](https://hl7.org/fhir/R4/modules.html)
  * [Documentation](https://hl7.org/fhir/R4/documentation.html)
  * [Resources](https://hl7.org/fhir/R4/resourcelist.html)
  * [Profiles](https://hl7.org/fhir/R4/profilelist.html)
  * [Extensions](https://hl7.org/fhir/R4/extensibility-registry.html)
  * [Operations](https://hl7.org/fhir/R4/operationslist.html)
  * [Terminologies](https://hl7.org/fhir/R4/terminologies-systems.html)


  * [![](https://hl7.org/fhir/R4/conformance.jpg) Conformance](https://hl7.org/fhir/R4/conformance-module.html)
  * [CompartmentDefinition](https://hl7.org/fhir/R4/compartmentdefinition.html)
  * **Example Instance**


This page is part of the FHIR Specification (v4.0.1: R4 - Mixed [Normative](https://confluence.hl7.org/display/HL7/HL7+Balloting "Normative Standard") and [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use")) in it's permanent home (it will always be available at this URL). The current version which supercedes this version is [5.0.0](http://hl7.org/fhir/index.html). For a full list of available versions, see the [Directory of published versions ![](https://hl7.org/fhir/R4/external.png)](http://hl7.org/fhir/directory.html). Page versions: [R5](http://hl7.org/fhir/R5/compartmentdefinition-practitioner.html) [R4B](http://hl7.org/fhir/R4B/compartmentdefinition-practitioner.html) **R4** [R3](http://hl7.org/fhir/STU3/compartmentdefinition-practitioner.html)
# Compartment Practitioner
[FHIR Infrastructure](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group |  [Maturity Level](https://hl7.org/fhir/R4/versions.html#maturity): N/A |  [Standards Status](https://hl7.org/fhir/R4/versions.html#std-process):[Trial Use](https://hl7.org/fhir/R4/versions.html#std-process)  
---|---|---  
Formal URI | http://hl7.org/fhir/compartment/Practitioner  
---|---  
Description | The set of resources associated with a particular practitioner  
Identity | There is an instance of the practitioner compartment for each Practitioner resource, and the identity of the compartment is the same as the Practitioner  
Membership | The practitioner compartment includes any resources where the resource is explicitly linked to a Practitioner (usually as author, but other kinds of linkage exist)  
Formal Definition |  [CompartmentDefinition](https://hl7.org/fhir/R4/compartmentdefinition.html)resource: [XML](https://hl7.org/fhir/R4/compartmentdefinition-practitioner.xml.html) or [JSON](https://hl7.org/fhir/R4/compartmentdefinition-practitioner.json.html)  
Resource based membership rules: 
The following resources may be in this compartment: 
**Resource** | **Inclusion Criteria**  
---|---  
[Account](https://hl7.org/fhir/R4/account.html) | subject  
[AdverseEvent](https://hl7.org/fhir/R4/adverseevent.html) | recorder  
[AllergyIntolerance](https://hl7.org/fhir/R4/allergyintolerance.html) | recorder or asserter  
[Appointment](https://hl7.org/fhir/R4/appointment.html) | actor  
[AppointmentResponse](https://hl7.org/fhir/R4/appointmentresponse.html) | actor  
[AuditEvent](https://hl7.org/fhir/R4/auditevent.html) | agent  
[Basic](https://hl7.org/fhir/R4/basic.html) | author  
[CarePlan](https://hl7.org/fhir/R4/careplan.html) | performer  
[CareTeam](https://hl7.org/fhir/R4/careteam.html) | participant  
[ChargeItem](https://hl7.org/fhir/R4/chargeitem.html) | enterer or performer-actor  
[Claim](https://hl7.org/fhir/R4/claim.html) | enterer or provider or payee or care-team  
[ClaimResponse](https://hl7.org/fhir/R4/claimresponse.html) | requestor  
[ClinicalImpression](https://hl7.org/fhir/R4/clinicalimpression.html) | assessor  
[Communication](https://hl7.org/fhir/R4/communication.html) | sender or recipient  
[CommunicationRequest](https://hl7.org/fhir/R4/communicationrequest.html) | sender or recipient or requester  
[Composition](https://hl7.org/fhir/R4/composition.html) | subject or author or attester  
[Condition](https://hl7.org/fhir/R4/condition.html) | asserter  
[CoverageEligibilityRequest](https://hl7.org/fhir/R4/coverageeligibilityrequest.html) | enterer or provider  
[CoverageEligibilityResponse](https://hl7.org/fhir/R4/coverageeligibilityresponse.html) | requestor  
[DetectedIssue](https://hl7.org/fhir/R4/detectedissue.html) | author  
[DeviceRequest](https://hl7.org/fhir/R4/devicerequest.html) | requester or performer  
[DiagnosticReport](https://hl7.org/fhir/R4/diagnosticreport.html) | performer  
[DocumentManifest](https://hl7.org/fhir/R4/documentmanifest.html) | subject or author or recipient  
[DocumentReference](https://hl7.org/fhir/R4/documentreference.html) | subject or author or authenticator  
[Encounter](https://hl7.org/fhir/R4/encounter.html) | practitioner or participant  
[EpisodeOfCare](https://hl7.org/fhir/R4/episodeofcare.html) | care-manager  
[ExplanationOfBenefit](https://hl7.org/fhir/R4/explanationofbenefit.html) | enterer or provider or payee or care-team  
[Flag](https://hl7.org/fhir/R4/flag.html) | author  
[Group](https://hl7.org/fhir/R4/group.html) | member  
[Immunization](https://hl7.org/fhir/R4/immunization.html) | performer  
[Invoice](https://hl7.org/fhir/R4/invoice.html) | participant  
[Linkage](https://hl7.org/fhir/R4/linkage.html) | author  
[List](https://hl7.org/fhir/R4/list.html) | source  
[Media](https://hl7.org/fhir/R4/media.html) | subject or operator  
[MedicationAdministration](https://hl7.org/fhir/R4/medicationadministration.html) | performer  
[MedicationDispense](https://hl7.org/fhir/R4/medicationdispense.html) | performer or receiver  
[MedicationRequest](https://hl7.org/fhir/R4/medicationrequest.html) | requester  
[MedicationStatement](https://hl7.org/fhir/R4/medicationstatement.html) | source  
[MessageHeader](https://hl7.org/fhir/R4/messageheader.html) | receiver or author or responsible or enterer  
[NutritionOrder](https://hl7.org/fhir/R4/nutritionorder.html) | provider  
[Observation](https://hl7.org/fhir/R4/observation.html) | performer  
[Patient](https://hl7.org/fhir/R4/patient.html) | general-practitioner  
[PaymentNotice](https://hl7.org/fhir/R4/paymentnotice.html) | provider  
[PaymentReconciliation](https://hl7.org/fhir/R4/paymentreconciliation.html) | requestor  
[Person](https://hl7.org/fhir/R4/person.html) | practitioner  
[PractitionerRole](https://hl7.org/fhir/R4/practitionerrole.html) | practitioner  
[Procedure](https://hl7.org/fhir/R4/procedure.html) | performer  
[Provenance](https://hl7.org/fhir/R4/provenance.html) | agent  
[QuestionnaireResponse](https://hl7.org/fhir/R4/questionnaireresponse.html) | author or source  
[RequestGroup](https://hl7.org/fhir/R4/requestgroup.html) | participant or author  
[ResearchStudy](https://hl7.org/fhir/R4/researchstudy.html) | principalinvestigator  
[RiskAssessment](https://hl7.org/fhir/R4/riskassessment.html) | performer  
[Schedule](https://hl7.org/fhir/R4/schedule.html) | actor  
[ServiceRequest](https://hl7.org/fhir/R4/servicerequest.html) | performer or requester  
[Specimen](https://hl7.org/fhir/R4/specimen.html) | collector  
[SupplyDelivery](https://hl7.org/fhir/R4/supplydelivery.html) | supplier or receiver  
[SupplyRequest](https://hl7.org/fhir/R4/supplyrequest.html) | requester  
[VisionPrescription](https://hl7.org/fhir/R4/visionprescription.html) | prescriber  
A resource is in this compartment if the nominated search parameter (or chain) refers to the patient resource that defines the compartment. 
The following resources are never in this compartment: 
  * [ActivityDefinition](https://hl7.org/fhir/R4/activitydefinition.html)
  * [Binary](https://hl7.org/fhir/R4/binary.html)
  * [BiologicallyDerivedProduct](https://hl7.org/fhir/R4/biologicallyderivedproduct.html)
  * [BodyStructure](https://hl7.org/fhir/R4/bodystructure.html)
  * [Bundle](https://hl7.org/fhir/R4/bundle.html)
  * [CapabilityStatement](https://hl7.org/fhir/R4/capabilitystatement.html)
  * [CatalogEntry](https://hl7.org/fhir/R4/catalogentry.html)
  * [ChargeItemDefinition](https://hl7.org/fhir/R4/chargeitemdefinition.html)
  * [CodeSystem](https://hl7.org/fhir/R4/codesystem.html)
  * [CompartmentDefinition](https://hl7.org/fhir/R4/compartmentdefinition.html)
  * [ConceptMap](https://hl7.org/fhir/R4/conceptmap.html)
  * [Consent](https://hl7.org/fhir/R4/consent.html)
  * [Contract](https://hl7.org/fhir/R4/contract.html)
  * [Coverage](https://hl7.org/fhir/R4/coverage.html)
  * [Device](https://hl7.org/fhir/R4/device.html)
  * [DeviceDefinition](https://hl7.org/fhir/R4/devicedefinition.html)
  * [DeviceMetric](https://hl7.org/fhir/R4/devicemetric.html)
  * [DeviceUseStatement](https://hl7.org/fhir/R4/deviceusestatement.html)
  * [EffectEvidenceSynthesis](https://hl7.org/fhir/R4/effectevidencesynthesis.html)
  * [Endpoint](https://hl7.org/fhir/R4/endpoint.html)
  * [EnrollmentRequest](https://hl7.org/fhir/R4/enrollmentrequest.html)
  * [EnrollmentResponse](https://hl7.org/fhir/R4/enrollmentresponse.html)
  * [EventDefinition](https://hl7.org/fhir/R4/eventdefinition.html)
  * [Evidence](https://hl7.org/fhir/R4/evidence.html)
  * [EvidenceVariable](https://hl7.org/fhir/R4/evidencevariable.html)
  * [ExampleScenario](https://hl7.org/fhir/R4/examplescenario.html)
  * [FamilyMemberHistory](https://hl7.org/fhir/R4/familymemberhistory.html)
  * [Goal](https://hl7.org/fhir/R4/goal.html)
  * [GraphDefinition](https://hl7.org/fhir/R4/graphdefinition.html)
  * [GuidanceResponse](https://hl7.org/fhir/R4/guidanceresponse.html)
  * [HealthcareService](https://hl7.org/fhir/R4/healthcareservice.html)
  * [ImagingStudy](https://hl7.org/fhir/R4/imagingstudy.html)
  * [ImmunizationEvaluation](https://hl7.org/fhir/R4/immunizationevaluation.html)
  * [ImmunizationRecommendation](https://hl7.org/fhir/R4/immunizationrecommendation.html)
  * [ImplementationGuide](https://hl7.org/fhir/R4/implementationguide.html)
  * [InsurancePlan](https://hl7.org/fhir/R4/insuranceplan.html)
  * [Library](https://hl7.org/fhir/R4/library.html)
  * [Location](https://hl7.org/fhir/R4/location.html)
  * [Measure](https://hl7.org/fhir/R4/measure.html)
  * [MeasureReport](https://hl7.org/fhir/R4/measurereport.html)
  * [Medication](https://hl7.org/fhir/R4/medication.html)
  * [MedicationKnowledge](https://hl7.org/fhir/R4/medicationknowledge.html)
  * [MedicinalProduct](https://hl7.org/fhir/R4/medicinalproduct.html)
  * [MedicinalProductAuthorization](https://hl7.org/fhir/R4/medicinalproductauthorization.html)
  * [MedicinalProductContraindication](https://hl7.org/fhir/R4/medicinalproductcontraindication.html)
  * [MedicinalProductIndication](https://hl7.org/fhir/R4/medicinalproductindication.html)
  * [MedicinalProductIngredient](https://hl7.org/fhir/R4/medicinalproductingredient.html)
  * [MedicinalProductInteraction](https://hl7.org/fhir/R4/medicinalproductinteraction.html)
  * [MedicinalProductManufactured](https://hl7.org/fhir/R4/medicinalproductmanufactured.html)
  * [MedicinalProductPackaged](https://hl7.org/fhir/R4/medicinalproductpackaged.html)
  * [MedicinalProductPharmaceutical](https://hl7.org/fhir/R4/medicinalproductpharmaceutical.html)
  * [MedicinalProductUndesirableEffect](https://hl7.org/fhir/R4/medicinalproductundesirableeffect.html)
  * [MessageDefinition](https://hl7.org/fhir/R4/messagedefinition.html)
  * [MolecularSequence](https://hl7.org/fhir/R4/molecularsequence.html)
  * [NamingSystem](https://hl7.org/fhir/R4/namingsystem.html)
  * [ObservationDefinition](https://hl7.org/fhir/R4/observationdefinition.html)
  * [OperationDefinition](https://hl7.org/fhir/R4/operationdefinition.html)
  * [OperationOutcome](https://hl7.org/fhir/R4/operationoutcome.html)
  * [Organization](https://hl7.org/fhir/R4/organization.html)
  * [OrganizationAffiliation](https://hl7.org/fhir/R4/organizationaffiliation.html)
  * [PlanDefinition](https://hl7.org/fhir/R4/plandefinition.html)
  * [Questionnaire](https://hl7.org/fhir/R4/questionnaire.html)
  * [RelatedPerson](https://hl7.org/fhir/R4/relatedperson.html)
  * [ResearchDefinition](https://hl7.org/fhir/R4/researchdefinition.html)
  * [ResearchElementDefinition](https://hl7.org/fhir/R4/researchelementdefinition.html)
  * [ResearchSubject](https://hl7.org/fhir/R4/researchsubject.html)
  * [RiskEvidenceSynthesis](https://hl7.org/fhir/R4/riskevidencesynthesis.html)
  * [SearchParameter](https://hl7.org/fhir/R4/searchparameter.html)
  * [Slot](https://hl7.org/fhir/R4/slot.html)
  * [SpecimenDefinition](https://hl7.org/fhir/R4/specimendefinition.html)
  * [StructureDefinition](https://hl7.org/fhir/R4/structuredefinition.html)
  * [StructureMap](https://hl7.org/fhir/R4/structuremap.html)
  * [Subscription](https://hl7.org/fhir/R4/subscription.html)
  * [Substance](https://hl7.org/fhir/R4/substance.html)
  * [SubstanceNucleicAcid](https://hl7.org/fhir/R4/substancenucleicacid.html)
  * [SubstancePolymer](https://hl7.org/fhir/R4/substancepolymer.html)
  * [SubstanceProtein](https://hl7.org/fhir/R4/substanceprotein.html)
  * [SubstanceReferenceInformation](https://hl7.org/fhir/R4/substancereferenceinformation.html)
  * [SubstanceSourceMaterial](https://hl7.org/fhir/R4/substancesourcematerial.html)
  * [SubstanceSpecification](https://hl7.org/fhir/R4/substancespecification.html)
  * [Task](https://hl7.org/fhir/R4/task.html)
  * [TerminologyCapabilities](https://hl7.org/fhir/R4/terminologycapabilities.html)
  * [TestReport](https://hl7.org/fhir/R4/testreport.html)
  * [TestScript](https://hl7.org/fhir/R4/testscript.html)
  * [ValueSet](https://hl7.org/fhir/R4/valueset.html)
  * [VerificationResult](https://hl7.org/fhir/R4/verificationresult.html)


See [ information about compartments](https://hl7.org/fhir/R4/compartmentdefinition.html). 
®© HL7.org 2011+. FHIR Release 4 (Technical Correction #1) (v4.0.1) generated on Fri, Nov 1, 2019 09:37+1100. [QA Page](https://hl7.org/fhir/R4/qa.html)   
Links: [Search](http://hl7.org/fhir/search.cfm) | [Version History](https://hl7.org/fhir/R4/history.html) | [Table of Contents](https://hl7.org/fhir/R4/toc.html) | [Credits](https://hl7.org/fhir/R4/credits.html) | [Compare to R3](https://www.fhir.org/perl/htmldiff.pl?oldfile=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fcompartmentdefinition-practitioner.html&newfile=http%3A%2F%2Fhl7.org%2Ffhir%2FR4%2Fcompartmentdefinition-practitioner.html) | [![CC0](https://hl7.org/fhir/R4/cc0.png)](https://hl7.org/fhir/R4/license.html) | [Propose a change](http://hl7.org/fhir-issues)
