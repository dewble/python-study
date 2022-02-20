import json
import requests
import sys

from settings import incoming_webhook_url

sys.path.insert(0, '/Users/dewble/Workspace/python/study/')



def send_slack_template(incoming_webhook_url, message):
    payload = {'type': 'mrkdwn', 'text': message}
    message_json = json.dumps(payload)
    requests.post(incoming_webhook_url, data=message_json)



message = 'slack test message'
send_slack_template(incoming_webhook_url, message)