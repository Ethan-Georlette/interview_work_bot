# read and write to the json
from pathlib import Path

from app.models import Question, WorkSession


DATA_DIR = Path(__file__).parent.parent / "data"
QUESTIONS_FILE = DATA_DIR / "questions.jsonl"
SESSION_FILE = DATA_DIR / "current_session.json"

# __________________ question part _____________________


def save_question(question: Question) -> None:
    try:
        with open(QUESTIONS_FILE, "a", encoding="utf-8") as file:
            file.write(question.model_dump_json() + "\n")
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


# ___________________________session part __________________

def save_curr_session(session: WorkSession) -> None:
    try:
        with open(SESSION_FILE, "w", encoding="utf-8") as file:
            file.write(session.model_dump_json())
    except OSError as error:
        print(f"Could not write session: {error}")


def load_curr_session() -> WorkSession | None:
    try:
        with open(SESSION_FILE, "r", encoding="utf-8") as file:
            line = file.read()
            session = WorkSession.model_validate_json(line)
            return session
    except OSError as error:
        print(f"could not read from file: {error}")
        return None
