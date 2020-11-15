"""Modules for the Slack Connect Care Bot."""
import os
from pathlib import Path

from dotenv import load_dotenv
from slack_bolt import App


# Load environment variables
ENV_PATH = Path(Path(__file__).parent.parent).joinpath('config/.env')
load_dotenv(dotenv_path=ENV_PATH)


# Initialize the app
APP = App(
    token=os.environ.get('SLACK_APP_TOKEN'),
    signing_secret=os.environ.get('SLACK_SIGNING_SECRET')
)

# Start the app
if __name__ == "__main__":
    APP.start(port=int(os.environ.get("PORT", 3000)))
