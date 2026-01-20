# AI Brain - Astra Orb Intelligence Layer

## Overview

The AI Brain is a stateful, deterministic intelligence layer that evaluates deal health without external LLM calls. It operates as a "Living Chief of Staff" - analyzing deal state, conversation patterns, and commitment tracking to provide actionable insights.


**Key Characteristics:**
- **Deterministic** - Same input always produces same output
- **Fast** - <500ms response time target
- **Transparent** - Every decision includes evidence and confidence scoring
- **Stateful** - Persists commitments and signals between evaluations
- **UI-Decoupled** - Pure intelligence layer, no UI logic
