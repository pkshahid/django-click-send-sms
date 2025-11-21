import requests
from .settings import sms_settings


class ClickSendSMSClient:
    """
    Django-based wrapper for sending SMS using ClickSend REST API
    """

    BASE_URL = "https://rest.clicksend.com/v3/sms/send"

    def __init__(self, username=None, api_key=None):
        self.username = username or sms_settings.USERNAME
        self.api_key = api_key or sms_settings.API_KEY

        if not self.username or not self.api_key:
            raise ValueError("ClickSend credentials are not configured.")

        self.auth = (self.username, self.api_key)

    def send_sms(self, to: str, message: str, sender_id: str = None):
        payload = {
            "messages": [
                {
                    "source": "django click sender",
                    "body": message,
                    "to": to,
                }
            ]
        }

        if sender_id:
            payload["messages"][0]["from"] = sender_id

        res = requests.post(self.BASE_URL, json=payload, auth=self.auth)

        return res.json()

    def send_bulk_sms(self, messages):
        items = []
        for msg in messages:
            entry = {
                "source": "django click sender",
                "body": msg["message"],
                "to": msg["to"]
            }
            if "sender_id" in msg:
                entry["from"] = msg["sender_id"]
            items.append(entry)

        res = requests.post(self.BASE_URL, json={"messages": items}, auth=self.auth)
        return res.json()
