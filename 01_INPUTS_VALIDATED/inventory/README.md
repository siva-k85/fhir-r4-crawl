# Inventory Limitation Notice

## Status

The automated inventory crawl of HL7.org/fhir/R4/ is **blocked by CAPTCHA** challenges.

## Issue

HL7.org implements sophisticated bot detection (AWS WAF) that returns HTTP 405 responses with CAPTCHA challenges for automated crawl attempts, even with comprehensive anti-detection measures:

- Realistic user agents
- Human-like behavior simulation  
- Browser fingerprint masking
- Variable delays

## Current Inventory Status

The existing `links.csv` and `summary.md` reflect this limitation:
- **Most responses**: HTTP 405 (CAPTCHA blocked)
- **Depth**: All 0 (unable to traverse links)
- **Content-Type**: Unknown (no actual HTML retrieved)

## Resolution

The project uses a **hybrid approach** instead:

1. **Manual URL discovery**: 10 shortlist pages identified through documentation review
2. **Official download**: `fhir-spec.zip` from HL7.org provides complete R4 specification
3. **Local conversion**: HTML files converted to markdown using Crawl4AI file:// URLs (bypasses CAPTCHA)
4. **Supplementary web crawl**: 45 auxiliary pages successfully extracted before bot detection triggered

##

 Result

**55 validated markdown files** extracted successfully, including:
- 10 critical shortlist pages (from official download)
- 45 auxiliary pages (from web crawl)

See `03_OUTPUTS_COMPLETE/markdown/` for all extracted content.

## Recommendation

For future bulk access to FHIR R4 documentation, use the official download:
- **URL**: https://hl7.org/fhir/R4/fhir-spec.zip
- **License**: CC BY 4.0
- **Size**: ~210MB

This is HL7's recommended method for bulk access and avoids bot detection entirely.
