# decorators for functions
from app.storage import load_curr_session


def require_active_session(func):
    def wrapper(*args, **kwargs):
        session = load_curr_session()
        if session is not None and session.is_active:
            return func(*args, **kwargs)

        return None
    return wrapper