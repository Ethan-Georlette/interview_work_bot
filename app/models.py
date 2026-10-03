# structors for questions and evaluation
from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, field_validator


class QuestionCategory(StrEnum):
    ALGORITHMS = "algorithms"
    LINUX = "linux"
    DEVOPS = "devops"
    DOCKER = "docker"
    KUBERNETES = "kubernetes"
    NETWORKING = "networking"
    SYSTEM_DESIGN = "system_design"


class Question(BaseModel):
    id: str
    topic_key: str
    category: QuestionCategory
    difficulty: int
    question: str
    concepts: list[str]
    estimated_minutes: int
    created_at: datetime

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


    """
    def __init__(self: Question,id: str , category:QuestionCategory ,difficulty: int,question:str,concepts:list[str]
    , estimated_minutes:int,created_at:str):
            self.id = id
            self.category=category
            self.difficulty=difficulty
            self.question= question
            self.concepts=concepts
            self.estimated_minutes=estimated_minutes
            self.created_at=created_at
    def __str__(self):
        return "{\"id\":\""+self.id+"\",\"category\":\""+self.category+\
            "\",\"difficulty\":"+self.difficulty+",\"question\":\""+self.question+\
            "\",\"concepts\":"+self.concepts+",\"estimated_minutes\":"+self.estimated_minutes+\
            ",\"created_at\":\""+self.created_at+"\"}"
    """
