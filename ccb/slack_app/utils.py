"""Modules for the Slack Connect Care Bot."""
from django.conf import settings
from slack_bolt import App


# Initialize the app
APP = App(
    token=settings.SLACK_APP_TOKEN,
    signing_secret=settings.SLACK_SIGNING_SECRET,
)
