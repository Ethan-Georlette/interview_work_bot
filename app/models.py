# structors for questions and evaluation
from datetime import datetime
from enum import StrEnum
from typing import Self
from uuid import uuid4, UUID

from pydantic import BaseModel, field_validator


class QuestionCategory(StrEnum):
    ALGORITHMS = "algorithms"
    LINUX = "linux"
    DEVOPS = "devops"
    DOCKER = "docker"
    # KUBERNETES = "kubernetes"
    NETWORKING = "networking"
    # SYSTEM_DESIGN = "system_design"


class GeneratedQuestion(BaseModel):
    topic_key: str
    category: QuestionCategory
    difficulty: int
    question: str
    concepts: list[str]
    estimated_minutes: int

    @field_validator("difficulty")
    @classmethod
    def validate_difficulty(cls, value: int) -> int:
        if value < 1 or value > 10:
            raise ValueError("difficulty must be between 1 and 10")

        return value

    @field_validator("estimated_minutes")
    @classmethod
    def validate_estimated_minutes(cls, value: int) -> int:
        if value < 1 or value > 60:
            raise ValueError("time to solve in minutes must be between 1 and 60")
        return value


class Question(GeneratedQuestion):
    id: UUID
    created_at: datetime

    @classmethod
    def from_generated(cls, generated: GeneratedQuestion) -> Self:
        return cls(**generated.model_dump(), id=uuid4(), created_at=datetime.now(),)


class WorkSession(BaseModel):
    id: UUID
    started_at: datetime
    ended_at: datetime | None
    is_active: bool
    questions_asked: int
    slack_channel_id: str
    current_question: Question | None = None
