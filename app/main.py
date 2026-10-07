# entering point
import os

from dotenv import load_dotenv
from slack_bolt.adapter.socket_mode import SocketModeHandler

from app.scheduler import scheduler
from app.slack_bot import app


if __name__ == "__main__":
    load_dotenv()

    scheduler.start()

    handler = SocketModeHandler(
        app,
        os.environ["SLACK_APP_TOKEN"],
    )

    handler.start()
