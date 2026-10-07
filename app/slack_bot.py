# for the slack communication
import os

from dotenv import load_dotenv
from slack_bolt import App

from app.agent import generate_question, ask_ollama_answer
from app.scheduler import schedule_next_question
from app.session import start_session, stop_session
from app.slack_service import send_question, send_solution
from app.storage import (
    load_curr_session,
    save_curr_session, load_memory_context,
)


load_dotenv()

app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.command("/work-start")
def handle_work_start(ack, respond, command):
    ack()
    current_session = load_curr_session()

    if current_session is not None and current_session.is_active:
        respond("A work session is already active.")
        return

    session = start_session(command["channel_id"])
    save_curr_session(session)
    schedule_next_question()

    respond("/work-start")


@app.command("/task")
def handle_task(ack, respond, command):
    ack()
    respond("now task")
    current_session = load_curr_session()
    if current_session is None or not current_session.is_active:
        respond("session is not active")
        return

    mem = load_memory_context()
    question = generate_question(mem, current_session)
    if question is None:
        respond("problem generating question")
        return
    send_question(command["channel_id"], question)
    current_session.current_question = question
    save_curr_session(current_session)


@app.command("/solution")
def handle_solution(ack, respond, command):
    ack()
    respond("answering...")
    curr_session = load_curr_session()
    if curr_session is None or not curr_session.is_active:
        respond("session is not active")
        return
    if curr_session.current_question is None:
        respond("No current question")
        return
    answer = ask_ollama_answer(curr_session.current_question)
    if answer is None:
        respond("unsolvable")

    send_solution(command["channel_id"], curr_session.current_question, answer)


@app.command("/work-stop")
def handle_work_stop(ack, respond):
    ack()

    session = load_curr_session()

    if session is None or not session.is_active:
        respond("There is no active work session.")
        return

    session = stop_session(session)
    save_curr_session(session)

    respond(
        f"Work session stopped. "
        f"Questions asked: {session.questions_asked}"
    )
