# read and write to the json
from app.models import Question

from pathlib import Path

DATA_DIR = Path(__file__).parent.parent/"data"
QUESTIONS_FILE = DATA_DIR / "questions.jsonl"


def save_question(question: Question) -> None:
    try:
        with open(QUESTIONS_FILE, "a", encoding="utf-8") as file:
            file.write(question.model_dump_json()+"\n")
    except OSError as error:
        print(f"Could not write question: {error}")


def load_memory_context() -> list[str]:
    try:
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
            topic_keys: list[str] = []
            for line in file:
                question = Question.model_validate_json(line)
                topic_keys.append(question.topic_key)
            return topic_keys
    except OSError as error:
        print(f"could not read from file: {error}")
        return []
