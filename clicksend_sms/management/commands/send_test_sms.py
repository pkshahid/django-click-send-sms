from django.core.management.base import BaseCommand
from clicksend_sms.client import ClickSendSMSClient


class Command(BaseCommand):
    help = "Send a test SMS via ClickSend"

    def add_arguments(self, parser):
        parser.add_argument("phone", type=str)
        parser.add_argument("message", type=str)

    def handle(self, *args, **kwargs):
        phone = kwargs["phone"]
        message = kwargs["message"]

        client = ClickSendSMSClient()
        res = client.send_sms(phone, message)

        self.stdout.write(self.style.SUCCESS(str(res)))
