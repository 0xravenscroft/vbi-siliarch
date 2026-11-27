# Engineering Roadmap

Status: Foundation documentation and initial Python validation are published. The first end-to-end capability assessment is not complete.

This roadmap records dependencies, deliverables and acceptance criteria. Dates are planning targets, not release commitments.

## F0. Repository foundation

**Goal:** Establish a reviewable repository, initial architecture and explicit trust boundaries.

Published:
- [System Overview](architecture/SYSTEM_OVERVIEW.md)
- [Trust and Evidence](architecture/TRUST_AND_EVIDENCE.md)
- [Device Profile v0.1](architecture/DEVICE_PROFILE_V0_1.md)
- [ADR-0001](decisions/0001-foundation-first.md)

Remaining review: verify links, reconcile documentation with implementation and record reproducible local checks.

**Exit criteria:** A clean checkout has the documented files, working links and an understandable Git history.

## F1. Device capability prototype

**Goal:** Determine whether a valid, declared device profile satisfies a separately validated requirement.

| Order | Work item | Status |
|---|---|---|
| 1 | Define Device Profile v0.1 | Specification published |
| 2 | Validate fields, types and ranges | Initial Python implementation published |
| 3 | Test valid, invalid and boundary values | Initial unit tests published; more cases required |
| 4 | Read JSON with duplicate-key rejection and bounded input size | Planned |
| 5 | Define and validate requirement objects | Planned |
| 6 | Evaluate declared capabilities deterministically | Planned |
| 7 | Provide a minimal CLI and reproducible result output | Planned |
| 8 | Record test environment and limitations | Planned |

The current code is in [`src/siliarch/profile.py`](../src/siliarch/profile.py). Its test suite is in [`tests/test_profile.py`](../tests/test_profile.py).

Review priorities:
- Keep one implementation of each validator and avoid repeated checks.
- Test identifier length and character boundaries, numeric limits and every allowed capability.
- Reject malformed JSON and repeated object keys before validation.
- Keep invalid input distinct from a valid profile that does not meet requirements.
- Document exactly what a match does and does not prove.

**Exit criteria:** All contract cases are reproducible, invalid inputs fail clearly, requirement evaluation produces consistent outcomes and no result implies physical device verification.

## R1. Secure register controller

**Goal:** Specify and verify a small RTL register block.

Deliverables: access-control rules, reset and clock semantics, SystemVerilog module, testbench, selected assertions and waveform review.

**Exit criteria:** Reproducible simulation with documented assumptions, assertions and coverage limits. Physical implementation is a separate claim.

## H1. Firmware assurance research

**Goal:** Evaluate firmware integrity, device identity and secure boot design options in controlled environments.

**Exit criteria:** Experiments record their threat model, trust assumptions, method, evidence and limitations.

## P1. Platform adapters

**Goal:** Investigate selected ARM and RISC-V hardware without coupling the portable core to a specific board.

**Exit criteria:** Each supported target has an implemented adapter, reproducible compatibility tests and a documented support boundary.

## Development practice

Every change should identify the problem, affected files, dependency changes and a method of verification. Keep source, tests and documentation changes reviewable. Do not mark a milestone complete on the basis of a commit message alone.

Code and tests are written in English. Local experiments and hardware-specific claims require evidence before they appear as supported features.

See [System Overview](architecture/SYSTEM_OVERVIEW.md) and [Trust and Evidence](architecture/TRUST_AND_EVIDENCE.md) for architectural and assurance boundaries.
