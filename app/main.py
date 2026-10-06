# entering point
from app.scheduler import scheduler, schedule_next_question
from app.session import start_session
from app.storage import save_curr_session


if __name__ == "__main__":
    session = start_session()
    save_curr_session(session)

    scheduler.start()
    schedule_next_question()

    input("Scheduler running. Press Enter to stop...\n")

    scheduler.shutdown()