# ADR-0001: Start with a Portable Capability Model

Status: Accepted
Date: 2026-11-11

## Context

SILIARCH will investigate device capabilities, platform-specific interfaces, firmware integrity and hardware verification. These areas need a shared vocabulary for declarations, requirements and evidence.

Starting with hardware integrations before defining that vocabulary would make defects difficult to isolate and tests difficult to reproduce.

## Options considered

1. **Start with FPGA and RTL work.** This would introduce hardware simulation early, but leave the data contract and assessment rules unresolved.
2. **Build the full platform architecture first.** This would establish interfaces for components without validated requirements.
3. **Start with a portable capability model.** This would allow field rules, failure handling and requirement matching to be tested independently of any board.

## Decision

Choose option 3.

Use Python and its standard library for the initial profile model, validation and requirement assessment. Keep parsing, validation, evaluation and evidence recording as separate responsibilities.

The first implementation must not imply that checking a declaration verifies a physical device. RTL experiments, firmware work and platform adapters will be introduced as independently testable components.

## Consequences

**Benefits**
- Small changes with observable behavior
- Early validation of type, range and malformed-input rules
- Clear separation between declared properties and evidence
- No dependency on a specific board or hardware toolchain

**Trade-offs**
- Hardware verification begins after the portable contract is understood
- The first model cannot authenticate devices
- Hardware experiments may require contract and interface revisions

## Review trigger

Revisit this decision when an implemented hardware adapter, RTL experiment or assurance requirement demonstrates that the portable contract cannot represent a necessary property or result.

Related documents: [System Overview](../architecture/SYSTEM_OVERVIEW.md), [Trust and Evidence](../architecture/TRUST_AND_EVIDENCE.md) and [Engineering Roadmap](../ROADMAP.md).
