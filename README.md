# SILIARCH

**Adaptive Trusted Hardware and Computing Platform**

VanceBlackwood Industries  
RAVENSCROFT Engineering Research

SILIARCH is a hardware and systems engineering research project focused on device capability models, secure computing and reproducible verification.

The work begins with a narrow but important problem. A device can declare its processor architecture, memory capacity and available interfaces, but a declaration is not proof of the underlying hardware. SILIARCH builds the software foundations needed to assess those declarations without confusing them with measurements or trusted evidence.

## Engineering objective

Develop a portable framework for describing hardware capabilities, enforcing explicit data contracts and evaluating device requirements.

The project separates three concerns:

1. **Declaration**: What properties does a device profile claim?
2. **Evaluation**: Is the profile valid and does it satisfy defined requirements?
3. **Evidence**: Which properties have been established through independent tests, measurements or attestation?

These concerns have different trust boundaries. A structurally valid profile may still contain false claims. Software validation cannot establish device identity or physical integrity.

## Foundation implementation

The first milestone uses Python to establish a small and testable Device Profile v0.1 model.

| Field | Meaning | Contract |
|---|---|---|
| `schema_version` | Profile format | Must equal `0.1` |
| `device_id` | Declared profile identifier | 1 to 64 permitted ASCII characters |
| `architecture` | Processor architecture | `arm64`, `riscv64` or `x86_64` |
| `memory_bytes` | Declared memory capacity | Integer from 1 to `2**63 - 1` |
| `capabilities` | Declared interfaces | Unique entries from `uart`, `spi` and `i2c` |

All five fields are required. Unexpected fields are rejected. The complete field rules are maintained in the [Device Profile v0.1 specification](docs/architecture/DEVICE_PROFILE_V0_1.md).

### Published components

| File | Responsibility |
|---|---|
| [`src/siliarch/profile.py`](src/siliarch/profile.py) | Memory range checks and an initial device profile validator |
| [`tests/test_profile.py`](tests/test_profile.py) | Unit tests for accepted inputs, rejected inputs and selected schema rules |
| [`docs/architecture/SYSTEM_OVERVIEW.md`](docs/architecture/SYSTEM_OVERVIEW.md) | Planned processing flow and component boundaries |
| [`docs/architecture/TRUST_AND_EVIDENCE.md`](docs/architecture/TRUST_AND_EVIDENCE.md) | Trust assumptions and limits of verification evidence |

The validation functions operate on supplied Python values. The JSON input layer, duplicate-key detection, requirement evaluator and command-line interface are not yet implemented.

The profile validator remains under review. Additional boundary tests and code cleanup are required before treating the Device Profile v0.1 implementation as complete.

### Run the tests

From the repository root:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The tests check defined software behaviors. Passing tests do not authenticate a profile, inspect a physical board or establish hardware security.

## Architecture

SILIARCH is being developed as a set of components with clear responsibilities.

| Component | Responsibility | Status |
|---|---|---|
| Device profile validation | Enforce field names, types and permitted values | Initial implementation |
| Structured input | Read JSON without silently accepting ambiguous data | Planned |
| Capability evaluation | Compare validated claims with explicit requirements | Planned |
| Evidence records | Preserve test context, results and limitations | Planned |
| Hardware adapters | Collect platform-specific observations | Future research |
| Trust and attestation | Evaluate identity and integrity evidence against a policy | Future research |

A capability match will mean that supplied data meets a requirement. It will not mean that the physical device has been verified.

## Engineering roadmap

| Milestone | Focus | Status |
|---|---|---|
| F0 | Repository foundation, architecture and trust documentation | Published |
| F1 | Profile validation, strict JSON parsing, capability evaluation and CLI | In progress |
| R1 | Secure register controller and SystemVerilog verification | Planned |
| H1 | Firmware integrity and hardware assurance research | Planned |
| P1 | ARM and RISC-V platform adapters | Planned |

Immediate F1 priorities are validator review, boundary testing, duplicate-key-safe JSON parsing and deterministic requirement evaluation.

A milestone is complete only when its acceptance criteria can be checked against reproducible results.

## Research direction

Long-term research includes computer architecture, digital logic, FPGA and RTL engineering, embedded firmware, RISC-V and ARM systems, secure boot, device identity, hardware roots of trust, attestation and formal verification.

These are research objectives, not claims of implemented features, certified assurance or verified platform compatibility. Hardware-specific support will require its own implementation and test evidence.

## Development practice

Source code and technical documents are edited in Visual Studio Code. File operations, Git commands, builds and tests run in the integrated terminal.

Changes should be focused, reviewable and supported by appropriate tests. Source and test updates are committed separately when practical. Architectural decisions and known limitations are documented alongside the implementation.

Reproducibility matters more than feature count. Each result should make clear what was tested, under which assumptions and what remains unverified.

## Documentation

- [Engineering Roadmap](docs/ROADMAP.md)
- [System Overview](docs/architecture/SYSTEM_OVERVIEW.md)
- [Trust and Evidence](docs/architecture/TRUST_AND_EVIDENCE.md)
- [Device Profile v0.1](docs/architecture/DEVICE_PROFILE_V0_1.md)
- [ADR-0001: Start with a Portable Capability Model](docs/decisions/0001-foundation-first.md)

## Current status

Foundation documentation, initial Python validation code and unit tests are published. Full profile validation coverage and the capability evaluation pipeline are still in development.

No physical hardware measurement, secure boot implementation, cryptographic attestation or production security assurance is claimed.

## Scope and licensing

SILIARCH focuses on trusted hardware and computing. General cyber defense, intelligence analysis and quantitative finance are maintained as separate research areas.

Security experiments are restricted to authorized and controlled environments.

No license has been selected. Public repository access does not itself grant permission to reuse or redistribute the source.
