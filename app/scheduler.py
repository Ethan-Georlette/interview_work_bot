# timing for the agent (up\down)
from random import randint
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

from app.agent import generate_question
from app.storage import load_curr_session, load_memory_context

scheduler = BackgroundScheduler()

def question_job():
    session = load_curr_session()
    if session is None or not session.is_active:
        return
    else:
        mem = load_memory_context()
        question = generate_question(mem, session)
        print(question)
        schedule_next_question()


def schedule_next_question():
    minutes = randint(30, 60)
    date=datetime.now() + timedelta(seconds = minutes)
    scheduler.add_job(question_job, "date", run_date=date)
