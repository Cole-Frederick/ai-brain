"""Pydantic models for input schema validation"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum


class ViewType(str, Enum):
    DEAL_FORM = "deal_form"
    CONTACT_VIEW = "contact_view"
    LIST_VIEW = "list_view"
    DASHBOARD = "dashboard"


class Mode(str, Enum):
    VIEW = "view"
    EDIT = "edit"
    CREATE = "create"


class UserRole(str, Enum):
    SALES_REP = "sales_rep"
    MANAGER = "manager"
    ADMIN = "admin"


class Context(BaseModel):
    view: ViewType
    mode: Mode
    recordId: str
    userRole: UserRole


class ActivityType(str, Enum):
    CALL = "call"
    EMAIL = "email"
    WHATSAPP = "whatsapp"
    MEETING = "meeting"
    NOTE = "note"


class DealSnapshot(BaseModel):
    stage: str
    value: Optional[float] = None
    currency: Optional[str] = None
    createdAt: datetime
    lastActivityAt: Optional[datetime] = None
    lastActivityType: Optional[ActivityType] = None
    assignedOwner: str


class MissingField(BaseModel):
    fieldName: str
    required: bool


class BlockingError(BaseModel):
    type: str
    field: str
    reason: str


class ValidationState(BaseModel):
    missingRequiredFields: List[MissingField]
    blockingErrors: List[BlockingError]


class MessageDirection(str, Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"


class Channel(str, Enum):
    EMAIL = "email"
    WHATSAPP = "whatsapp"
    CALL = "call"
    NOTE = "note"


class Message(BaseModel):
    id: str
    timestamp: datetime
    direction: MessageDirection
    channel: Channel
    rawText: str
    summary: Optional[str] = None


class RecentConversation(BaseModel):
    messages: List[Message] = Field(max_length=15)


class CommitmentType(str, Enum):
    CLIENT_PROMISE = "client_promise"
    INTERNAL_DEADLINE = "internal_deadline"
    FOLLOW_UP = "follow_up"


class Commitment(BaseModel):
    extractedAt: datetime
    messageId: str
    type: CommitmentType
    dueDate: datetime
    description: str
    fulfilled: bool


class ExpectedResponseWindow(BaseModel):
    startedAt: datetime
    expectedBy: datetime
    gracePeriodHours: float


class DealHealthEnum(str, Enum):
    HEALTHY = "healthy"
    AT_RISK = "at_risk"
    CRITICAL = "critical"
    INSUFFICIENT_DATA = "insufficient_data"


class LatestSignals(BaseModel):
    dealHealth: DealHealthEnum
    confidence: float
    computedAt: datetime


class PersistedState(BaseModel):
    commitments: Optional[List[Commitment]] = None
    expectedResponseWindow: Optional[ExpectedResponseWindow] = None
    latestSignals: Optional[LatestSignals] = None


class EvaluateInput(BaseModel):
    """Complete input schema for /evaluate endpoint"""
    schemaVersion: str = "1.0"
    timestamp: datetime
    context: Context
    dealSnapshot: DealSnapshot
    validationState: ValidationState
    recentConversation: RecentConversation
    persistedState: PersistedState
