# AI Brain - Astrah Orb Intelligence Layer

> The deterministic intelligence core powering deal health evaluation, risk detection, and next-best-action recommendations for the Astrah CRM.

## Overview

The AI Brain is a stateful, deterministic intelligence layer that evaluates deal health without external LLM calls. It operates as a "Living Chief of Staff" - analyzing deal state, conversation patterns, and commitment tracking to provide actionable insights.

**Key Characteristics:**
- **Deterministic** - Same input always produces same output
- **Fast** - <500ms response time target
- **Transparent** - Every decision includes evidence and confidence scoring
- **Stateful** - Persists commitments and signals between evaluations
- **UI-Decoupled** - Pure intelligence layer, no UI logic

## Architecture

```
Platform → [JSON Input] → AI Brain → [JSON Output] → Platform
                              ↓
                    [Persisted State]
```

The Brain receives deal snapshots, conversation history, and validation state, then returns:
- Deal health assessment (healthy/at_risk/critical/insufficient_data)
- Risk signals (silence, stagnation, missed commitments)
- Confidence scoring with explainability
- Single next-best-action recommendation
- State updates to persist

## Core Endpoints

### `/evaluate` (Deterministic)
Primary endpoint for deal health evaluation. **No external LLM calls.**

**Input:** Deal snapshot + recent messages + persisted state  
**Output:** Health decision + signals + next action + state updates  
**Performance:** <500ms, <2KB response

### `/draft` (LLM-Powered)
Generate email/WhatsApp message drafts using external AI.

### `/summarize` (LLM-Powered)
Summarize conversation threads or deal history.

### `/translate` (LLM-Powered)
Translate content between English and Arabic.

## Signal Set (v1)

**Included:**
- Silence Detection (expected/unexpected/grace period)
- Stagnation (stage-based time tracking)
- Risk Drivers (max 3, high-signal only)
- Intent State (engaged/hesitant/unresponsive/unknown)
- Deal Health (aggregated assessment)
- Missing Blockers (validation-based)

**Explicitly Excluded:**
- Fine-grained sentiment scoring
- Automatic actions (no auto-send, auto-update)
- Sales feedback weighting (v1: correction only)
- Predictive close probability
- Multi-deal pattern detection

## State Management

### Persisted Between Evaluations
- Client commitments & promises
- Expected response windows
- Extracted entities (dates, budgets, decision-makers)
- Latest stable signals (for delta detection)
- Evidence pointers (message IDs, timestamps)

### Recomputed Every Time
- Time-based metrics (days since activity, stage duration)
- Silence detection status
- Risk score aggregation
- Next-best-action recommendation
- Deal health (compared to cached for change detection)

## Confidence Scoring

| Level | Score | Criteria |
|-------|-------|----------|
| **High** | 0.8-1.0 | Recent activity (<3 days), complete fields, clear commitments |
| **Medium** | 0.5-0.79 | Activity within 7 days, some missing fields, limited history |
| **Low** | 0.0-0.49 | No recent activity (>7 days), missing critical data, conflicting signals |

**Rule:** Always explain why confidence is not high.

## Design Principles

1. **Intellc

## Integration

### Platform Responsibilities
- Provide complete JSON input per schema
- Manage state persistence (commitments, signals, response windows)
- Handle UI rendering of Brain output
- Derive UI state (canSave, canMoveStage) from Brain output + validation rules

### Brain Responsibilities
- Evaluate deal health deterministically
- Extract commitments from raw message text
- Compute time-based signals
- Provide explainable decisions with evidence
- Return state updates to persist
- **Never perform side effects** (no auto-send, no auto-update)
.