"""Modules for the Slack Connect Care Bot."""
from django.conf import settings

from slack_bolt import App
from slack_bolt.error import BoltError


# Initialize the app
app = App(
    token=settings.SLACK_APP_TOKEN,
    signing_secret=settings.SLACK_SIGNING_SECRET,
)


@app.event('app_home_opened')
def open_modal(client, event, logger):
    """Function to generate an app home page."""
    try:
        # Publish a view
        client.views_publish(
            user_id=event['user'],
            view={
                'type': 'home',
                'callback_id': 'home_view',
                'blocks': [
                    {
                        'type': 'section',
                        'text': {
                            'type': 'mrkdwn',
                            'text': '*Welcome to your _App\'s Home_* :tada:'
                        },
                    },
                    {
                        'type': 'divider'
                    },
                    {
                        'type': 'section',
                        'text': {
                            'type': 'mrkdwn',
                            'text': (
                                'This button won\'t do much for now but you '
                                'can set up a listener for it using the '
                                '`actions()` method and passing its unique '
                                '`action_id`. See an example in the '
                                '`examples` folder within your Bolt app.'
                            ),
                        }
                    },
                    {
                        'type': 'actions',
                        'elements': [
                            {
                                'type': 'button',
                                'text': {
                                    'type': 'plain_text',
                                    'text': 'Click me!'
                                }
                            }
                        ]
                    }
                ]
            }
        )
    except BoltError as error:
        logger.error('Error opening modal: {}'.format(error))


@app.message('beep')
def say_boop(message, say):  # pylint: disable=unused-argument
    """Function to trigger a beep boop response."""
    say('boop!')
