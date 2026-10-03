# entering_point

from app.models import Question, QuestionCategory
from app.storage import save_question


question = Question(
    id="test-1",
    category=QuestionCategory.DOCKER,
    difficulty=5,
    question="How does Docker bridge networking work?",
    concepts=["bridge", "networking", "dns"],
    estimated_minutes=15,
    created_at="2026-09-30",
)

save_question(question)
