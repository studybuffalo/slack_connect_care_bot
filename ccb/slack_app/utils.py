"""Modules for the Slack Connect Care Bot."""
from django.conf import settings
from slack_bolt import App


# Initialize the app
app = App(
    token=settings.SLACK_APP_TOKEN,
    signing_secret=settings.SLACK_SIGNING_SECRET,
)


@app.event('app_home_opened')
def open_modal(client, event, logger):
  try:
    # view.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Welcome to your _App's Home_* :tada:"
            }
          },
          {
            "type": "divider"
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app."
            }
          },
          {
            "type": "actions",
            "elements": [
              {
                "type": "button",
                "text": {
                  "type": "plain_text",
                  "text": "Click me!"
                }
              }
            ]
          }
        ]
      }
    )

  except Exception as e:
    logger.error(f"Error opening modal: {e}")

@app.message('beep')
def say_boop(message, say):
    say('boop!')
