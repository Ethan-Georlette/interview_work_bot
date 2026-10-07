import os

from dotenv import load_dotenv
from slack_sdk import WebClient

from app.models import Question


load_dotenv()

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])


def send_question(channel_id: str, question: Question) -> None:
    text = (
        f"🚨 *Interview Task*\n\n"
        f"*Category:* {question.category.value}\n"
        f"*Difficulty:* {question.difficulty}/10\n"
        f"*Estimated time:* {question.estimated_minutes} min\n\n"
        f"{question.question}\n\n"
        f"*Concepts:* {', '.join(question.concepts)}"
    )

    client.chat_postMessage(
        channel=channel_id,
        text=text,
    )
