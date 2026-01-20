"""Pydantic models for output schema validation"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum


class DealHealthEnum(str, Enum):
    HEALTHY = "healthy"
    AT_RISK = "at_risk"
    CRITICAL = "critical"
    INSUFFICIENT_DATA = "insufficient_data"


class ConfidenceLevelEnum(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Confidence(BaseModel):
    score: float = Field(ge=0.0, le=1.0)
    level: ConfidenceLevelEnum
    reason: str


class Decision(BaseModel):
    dealHealth: DealHealthEnum
    riskFlag: bool
    confidence: Confidence


class SilenceTypeEnum(str, Enum):
    EXPECTED = "expected"
    UNEXPECTED = "unexpected"
    GRACE_PERIOD = "grace_period"


class SilenceSignal(BaseModel):
    detected: bool
    type: SilenceTypeEnum
    daysSinceLastActivity: float


class StagnationSignal(BaseModel):
    detected: bool
    daysInCurrentStage: float


class RiskTypeEnum(str, Enum):
    SILENCE = "silence"
    MISSED_COMMITMENT = "missed_commitment"
    STAGNATION = "stagnation"
    MISSING_DATA = "missing_data"
    INACTIVITY = "inactivity"


class RiskSeverityEnum(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RiskDriver(BaseModel):
    type: RiskTypeEnum
    severity: RiskSeverityEnum
    description: str


class IntentStateEnum(str, Enum):
    ENGAGED = "engaged"
    HESITANT = "hesitant"
    UNRESPONSIVE = "unresponsive"
    UNKNOWN = "unknown"


class Signals(BaseModel):
    silence: SilenceSignal
    stagnation: StagnationSignal
    riskDrivers: List[RiskDriver] = Field(max_length=3)
    intentState: IntentStateEnum


class Evidence(BaseModel):
    messageId: str
    timestamp: datetime
    relevance: str


class Explainability(BaseModel):
    why: str = Field(max_length=200)
    missingData: List[str]
    whatWouldChange: Optional[str] = Field(None, max_length=150)
    evidence: List[Evidence]


class ActionTypeEnum(str, Enum):
    CALL = "call"
    EMAIL = "email"
    WHATSAPP = "whatsapp"
    UPDATE_FIELD = "update_field"
    SCHEDULE_MEETING = "schedule_meeting"
    ESCALATE = "escalate"
    NONE = "none"


class UrgencyEnum(str, Enum):
    IMMEDIATE = "immediate"
    TODAY = "today"
    THIS_WEEK = "this_week"
    LOW = "low"


class NextBestAction(BaseModel):
    action: ActionTypeEnum
    reason: str = Field(max_length=150)
    urgency: UrgencyEnum


class CommitmentType(str, Enum):
    CLIENT_PROMISE = "client_promise"
    INTERNAL_DEADLINE = "internal_deadline"
    FOLLOW_UP = "follow_up"


class NewCommitment(BaseModel):
    extractedAt: datetime
    messageId: str
    type: CommitmentType
    dueDate: datetime
    description: str
    fulfilled: bool


class UpdatedExpectedResponseWindow(BaseModel):
    startedAt: datetime
    expectedBy: datetime
    gracePeriodHours: float


class SignalsToCache(BaseModel):
    dealHealth: DealHealthEnum
    confidence: float
    computedAt: datetime


class StateUpdates(BaseModel):
    newCommitments: Optional[List[NewCommitment]] = None
    updatedExpectedResponseWindow: Optional[UpdatedExpectedResponseWindow] = None
    signalsToCache: Optional[SignalsToCache] = None


class EvaluateOutput(BaseModel):
    """Complete output schema for /evaluate endpoint"""
    schemaVersion: str = "1.0"
    timestamp: datetime
    decision: Decision
    signals: Signals
    explainability: Explainability
    nextBestAction: NextBestAction
    stateUpdates: StateUpdates


