# start stop and work status
from datetime import datetime
from uuid import uuid4


from app.models import WorkSession


def start_session(channel_id: str) -> WorkSession:
    curr_session = WorkSession(id=uuid4(), started_at=datetime.now(), ended_at=None,
                               is_active=True, questions_asked=0, slack_channel_id=channel_id)
    return curr_session


def stop_session(session: WorkSession) -> WorkSession:
    session.is_active = False
    session.ended_at = datetime.now()
    return session
