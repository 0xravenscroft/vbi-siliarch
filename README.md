# SILIARCH

**Adaptive Trusted Hardware and Computing Platform**

VanceBlackwood Industries  
RAVENSCROFT Engineering Research

SILIARCH is a hardware and systems engineering research project focused on device capability models, secure computing and verifiable system behavior.

The project begins with small software components that describe hardware properties and check declared capabilities against defined rules. Later work will investigate RTL verification, firmware assurance and hardware-specific implementations.

## Engineering problem

A device profile can describe a processor, memory capacity or supported interface. That description is useful for configuration and compatibility checks, but it does not prove that the hardware has those properties.

SILIARCH separates three questions:

1. What does the device profile declare?
2. Is the declaration valid and does it meet the stated requirements?
3. What has been established through independent tests, measurements or trusted evidence?

The foundation software addresses data validation first. Hardware measurement and attestation are separate research tasks.

## Foundation implementation

The initial implementation is written in Python and follows the proposed Device Profile v0.1 contract.

The profile format defines five required fields:

| Field | Purpose |
|---|---|
| `schema_version` | Identifies the profile format |
| `device_id` | Identifies a profile without authenticating a physical device |
| `architecture` | Declares the processor architecture |
| `memory_bytes` | Declares memory capacity in bytes |
| `capabilities` | Lists supported interface capabilities |

The repository currently contains:

- `src/siliarch/profile.py` with memory range validation and an initial device profile validator
- `tests/test_profile.py` with unit tests for accepted values, invalid inputs and profile field rules
- Architecture, trust boundary and schema documentation under `docs/`

The memory validator checks integer type and range constraints. The profile validator is still under development and review. Its presence does not mean that the full Device Profile v0.1 processing pipeline is complete.

### Running the tests

From the repository root:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Tests exercise specific software behaviors. They do not establish the authenticity of profile data or verify a physical device. The full set of schema boundary cases and the JSON input layer remain future verification work.

## Development milestones

| Stage | Scope | Status |
|---|---|---|
| F0 | Repository structure, architecture documents and trust boundaries | Foundation documents published |
| F1 | Profile validation, JSON parsing, capability evaluation and CLI | In progress |
| R1 | Secure register controller and RTL verification | Planned |
| H1 | Firmware integrity and hardware assurance research | Planned |
| P1 | Architecture-specific platform adapters | Planned |

The next foundation tasks are to review the profile validator, expand boundary tests, implement duplicate-key-safe JSON parsing and define requirement evaluation.

Milestones are completed only when their acceptance criteria and supporting results have been reviewed.

## Architecture and documentation

SILIARCH keeps data declarations, validation logic, capability evaluation and verification evidence separate. Hardware adapters will be introduced only when a specific target and its test requirements are defined.

| Document | Contents |
|---|---|
| [System Overview](docs/architecture/SYSTEM_OVERVIEW.md) | Proposed components, data flow and module responsibilities |
| [Trust and Evidence](docs/architecture/TRUST_AND_EVIDENCE.md) | Trust boundaries, evidence types and assurance limits |
| [Device Profile v0.1](docs/architecture/DEVICE_PROFILE_V0_1.md) | Field definitions, validation rules and test cases |
| [Engineering Roadmap](docs/ROADMAP.md) | Milestones, expected deliverables and acceptance criteria |
| [ADR-0001](docs/decisions/0001-foundation-first.md) | Decision to begin with a portable capability model |

## Research direction

Planned research includes digital logic, SystemVerilog, FPGA development, embedded firmware, RISC-V and ARM integration, secure boot, device identity, roots of trust, attestation and formal verification.

These areas describe the intended scope of the project. They are not claims of implemented features or verified hardware support.

## Engineering practice

Source code and documentation are edited in Visual Studio Code. Filesystem operations, Git, builds and tests are handled through the terminal.

Changes are kept small and reviewable. Each implementation should have defined inputs, expected behavior, appropriate tests and a clear record of its limitations. Source changes and test changes are committed separately when practical.

A valid profile is not necessarily a truthful profile. A passing software test is not a hardware measurement. A simulation result is not proof of physical implementation.

## Current status

**Foundation development is active. Initial Python validators and unit tests have been published.**

The complete capability evaluator, strict JSON reader, command-line interface, firmware assurance mechanisms and hardware verification modules are not yet delivered. Existing validation code remains subject to technical review and additional tests.

## Scope and licensing

SILIARCH focuses on trusted hardware and computing. General cyber defense, intelligence analysis and quantitative finance are developed in separate research projects.

Security experiments are limited to authorized and controlled environments.

No license has been selected. Public access to this repository does not by itself grant redistribution or reuse rights.
