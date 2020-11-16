"""Views for the Slack App."""
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt

from slack_bolt.adapter.django import SlackRequestHandler

from .utils import app


handler = SlackRequestHandler(app=app)


@csrf_exempt
def events(request: HttpRequest):
    """View to direct to the Bolt event handler."""
    return handler.handle(request)
