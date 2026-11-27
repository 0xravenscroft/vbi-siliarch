# Trust and Evidence

Status: Design guidance. SILIARCH does not currently measure physical hardware or verify cryptographic attestations.

## Trust boundaries

A correctly formatted device profile can contain inaccurate or deliberately false information. Validation checks the structure of a declaration. It does not authenticate its source.

| Stage | Question answered | What it does not establish |
|---|---|---|
| Declaration | What does the source claim? | Truth or origin of the claim |
| Validation | Does the supplied object conform to the profile contract? | Physical device properties |
| Requirement evaluation | Do valid declared properties meet valid requirements? | Hardware compatibility beyond those claims |
| Measurement | What was observed on specified hardware? | Properties not covered by the method |
| Attestation | Does evidence satisfy a cryptographic verification policy? | General platform security outside that policy |

The published [`profile.py`](../../src/siliarch/profile.py) addresses validation only. [`test_profile.py`](../../tests/test_profile.py) checks selected software behaviors. A passing unit test does not turn a claim into a measurement.

## Input threats and expected handling

| Condition | Expected handling |
|---|---|
| Missing or unrecognized profile field | Reject under the versioned contract |
| Incorrect type or out-of-range value | Reject with an explicit validation error |
| Repeated capability | Reject rather than silently deduplicate |
| Repeated JSON object key | Reject in the planned strict parser |
| Oversized JSON input | Enforce a documented limit before parsing |
| Unverified capability claim | Treat as declared and unverified |
| Missing or contradictory evidence | Record the limitation; do not infer a passing result |
| Replayed attestation evidence | Apply freshness and policy checks when attestation is implemented |

This is an initial design threat model, not a comprehensive security assessment.

## Evidence records

Future assessment records should retain enough information for another engineer to reproduce and evaluate a result:

- Record format version and check identifier
- Source revision and test or tool version
- Input identifier or digest when appropriate
- Execution environment and test conditions
- Expected and observed results
- Outcome, failure details and known limitations

Do not publish passwords, credentials, private keys or sensitive device identifiers in evidence files.

## Verification terms

Use these terms precisely:

- **Declared:** A source asserted a property.
- **Validated:** Data passed the applicable structural contract.
- **Evaluated:** Valid claims were compared with explicit requirements.
- **Simulated:** A model passed identified checks under stated conditions.
- **Measured:** A property was observed on identified hardware using a stated method.
- **Attested:** Cryptographic evidence met a specified verification policy.

These are different kinds of evidence, not interchangeable levels of assurance. A signature alone does not establish secure boot or device integrity. Verification also depends on identity, trust anchors, freshness, measurement meaning and policy.

## Review checklist

Before publishing a security or compatibility result, document the claim, the evidence source, the method, the observed result, the environment, the assumptions and the limits. Unsupported properties remain unverified.

The later firmware work may refer to [NIST SP 800-193, Platform Firmware Resiliency Guidelines](https://csrc.nist.gov/pubs/sp/800/193/final). SILIARCH does not claim compliance.

Related documents: [System Overview](SYSTEM_OVERVIEW.md), [Device Profile v0.1](DEVICE_PROFILE_V0_1.md) and [Engineering Roadmap](../ROADMAP.md).
