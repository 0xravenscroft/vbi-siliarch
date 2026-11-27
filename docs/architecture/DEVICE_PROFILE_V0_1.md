# Device Profile v0.1

Status: Specification published. Initial Python validation is available; strict JSON input and capability assessment are not yet implemented.

## Purpose

A device profile is a structured declaration of device properties. It is not a hardware inventory, authenticated identity or measurement record.

Version 0.1 defines the first portable input contract for SILIARCH. All input is untrusted until it passes the applicable validation rules.

## Profile format

```json
{
  "schema_version": "0.1",
  "device_id": "lab-board-01",
  "architecture": "riscv64",
  "memory_bytes": 65536,
  "capabilities": ["uart", "spi"]
}
```

This is fictional test data.

| Field | Type | Rule |
|---|---|---|
| `schema_version` | String | Exactly `"0.1"` |
| `device_id` | String | 1 to 64 ASCII characters; first is a letter or digit; remaining characters may be letters, digits, periods, underscores or hyphens |
| `architecture` | String | Exactly one of `arm64`, `riscv64`, `x86_64` |
| `memory_bytes` | Integer | From 1 through 9,223,372,036,854,775,807 inclusive |
| `capabilities` | Array of strings | Zero or more unique values from `uart`, `spi`, `i2c` |

All five fields are mandatory. Additional fields are rejected. An empty `capabilities` array is allowed. Boolean values are invalid for `memory_bytes` even though Python treats booleans as a subtype of integers.

The `device_id` is a declared identifier, not proof of a unique physical device.

## Input parsing requirements

The current [Python validator](../../src/siliarch/profile.py) receives Python objects. It does not parse JSON text.

The planned JSON reader must:
- Reject malformed JSON.
- Reject duplicate object keys instead of keeping the first or last value.
- Enforce a documented byte-size limit before parsing untrusted files.
- Pass the decoded object to the profile validator without inventing missing values.

Parsing and validation are separate boundaries. A JSON document that parses successfully can still fail the profile contract.

## Requirement example

```json
{
  "architecture": "riscv64",
  "min_memory_bytes": 32768,
  "required_capabilities": ["uart"]
}
```

This object illustrates a proposed requirement format. Its validation rules and evaluator have not yet been implemented.

## Assessment outcomes

| Outcome | Meaning |
|---|---|
| Invalid input | The profile or requirement violates its contract |
| Match | Valid declared properties satisfy validated requirements |
| No match | Valid declared properties fail at least one validated requirement |

Invalid input is not a no-match result. A match does not establish the truth of the declaration.

## Required tests

The foundation test plan includes:

1. Accept a complete valid profile.
2. Reject missing and unknown fields.
3. Reject unsupported schema versions.
4. Enforce identifier character and length boundaries.
5. Reject boolean, zero, negative and oversized memory values.
6. Reject unsupported or repeated capabilities.
7. Accept an empty capability list.
8. Reject duplicate keys in the planned JSON reader.
9. Return Match for a valid profile that meets a valid requirement.
10. Return No match for a valid profile missing a required capability.

The initial tests in [`tests/test_profile.py`](../../tests/test_profile.py) cover a subset of these cases. The full set is not yet complete.

Tests must be repeatable without network access or physical hardware.

## Implementation order

1. Review and complete pure profile validation.
2. Extend boundary and negative tests.
3. Add strict JSON input handling.
4. Define and validate requirement objects.
5. Implement deterministic comparison.
6. Add a small CLI and evidence-aware result format.

Related documents: [System Overview](SYSTEM_OVERVIEW.md), [Trust and Evidence](TRUST_AND_EVIDENCE.md) and [Engineering Roadmap](../ROADMAP.md).
