# SILIARCH

**Adaptive Trusted Hardware and Computing Platform**

RAVENSCROFT INDUSTRIES

SILIARCH is an engineering research project concerned with hardware capability descriptions, portable validation and the evidence required to support trust decisions.

A device profile can declare a processor architecture, memory capacity and available interfaces. Software can check those claims against a defined contract. It cannot establish that the claims are true without independent evidence.

## Objective

Build a portable foundation that can:

1. Validate versioned device profiles without assuming the source is trustworthy.
2. Compare valid declarations with explicit hardware requirements.
3. Record what was checked, how it was checked and what remains unverified.
4. Introduce hardware-specific evidence only when the underlying interfaces and tests are defined.

The current implementation addresses profile validation. Requirement evaluation, evidence records and hardware integration remain future work.

## Current implementation

| Component | Status | Source |
|---|---|---|
| Memory capacity validation | Implemented | [`profile.py`](src/siliarch/profile.py) |
| Device Profile v0.1 validation | Initial implementation under review | [`profile.py`](src/siliarch/profile.py) |
| Validation unit tests | Published, coverage expansion pending | [`test_profile.py`](tests/test_profile.py) |
| Strict JSON input and duplicate-key detection | Planned | [Device Profile v0.1](docs/architecture/DEVICE_PROFILE_V0_1.md) |
| Requirement validation and capability evaluation | Planned | [System Overview](docs/architecture/SYSTEM_OVERVIEW.md) |
| Command-line interface and result records | Planned | [Engineering Roadmap](docs/ROADMAP.md) |

The current validator accepts Python values. It does not read JSON files, inspect hardware, authenticate devices or produce a capability assessment.

### Device Profile v0.1

The contract requires exactly five fields:

| Field | Rule |
|---|---|
| `schema_version` | String equal to `"0.1"` |
| `device_id` | 1 to 64 allowed ASCII characters; begins with a letter or digit |
| `architecture` | One of `arm64`, `riscv64`, `x86_64` |
| `memory_bytes` | Integer from 1 through `2**63 - 1`; booleans rejected |
| `capabilities` | List of unique values from `uart`, `spi` and `i2c` |

Unknown or missing fields are rejected. An empty capability list is valid. The [specification](docs/architecture/DEVICE_PROFILE_V0_1.md) is the authority for the full rules and planned parsing behavior.

## Repository structure

| Path | Responsibility |
|---|---|
| [`src/siliarch/profile.py`](src/siliarch/profile.py) | Applies the profile contract to Python values |
| [`tests/test_profile.py`](tests/test_profile.py) | Imports the validator and checks accepted and rejected inputs |
| [`docs/architecture/DEVICE_PROFILE_V0_1.md`](docs/architecture/DEVICE_PROFILE_V0_1.md) | Defines field types, limits and expected outcomes |
| [`docs/architecture/SYSTEM_OVERVIEW.md`](docs/architecture/SYSTEM_OVERVIEW.md) | Describes component boundaries and the intended data flow |
| [`docs/architecture/TRUST_AND_EVIDENCE.md`](docs/architecture/TRUST_AND_EVIDENCE.md) | Defines trust assumptions and evidence limitations |
| [`docs/ROADMAP.md`](docs/ROADMAP.md) | Tracks milestones and acceptance criteria |
| [`docs/decisions/0001-foundation-first.md`](docs/decisions/0001-foundation-first.md) | Records why work starts with a portable software model |

The specification describes intended behavior. The Python module implements part of that contract. The tests import the Python module and check its observable behavior. The documentation files are not loaded by the application at runtime.

## Run the tests

From the repository root, using Python 3:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py' -v
```

`PYTHONPATH=src` makes the `siliarch` module available for imports. The tests use Python's standard library and require no board or network access.

A passing test run demonstrates behavior for the cases exercised by those tests. It does not establish complete input coverage, hardware authenticity or production readiness.

## Development sequence

The foundation follows the dependency order defined in the [roadmap](docs/ROADMAP.md):

1. Review profile validation and extend boundary tests.
2. Add strict JSON ingestion, including duplicate-key rejection and an input-size policy.
3. Define and validate requirement objects.
4. Implement deterministic capability evaluation.
5. Add a command-line interface and reproducible result records.
6. Begin the RTL secure register controller work as a separate milestone.

## Engineering boundaries

SILIARCH distinguishes a declared property from a validated data structure, a requirement match and a physical measurement. None of these should be described as cryptographic attestation unless the necessary identity, freshness, measurement and trust-policy checks exist.

Later research may cover FPGA and RTL verification, firmware integrity, secure boot, RISC-V and ARM adapters and hardware roots of trust. These capabilities are not implemented by the current Python prototype.

The repository is a research and development project, not a certified security product. Security work is limited to authorized environments.

## License

No license has been selected. Public access to this repository does not by itself grant permission to reuse or redistribute its contents.
