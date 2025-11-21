from django.conf import settings


class ClickSendSettings:
    @property
    def USERNAME(self):
        return getattr(settings, "CLICKSEND_USERNAME", None)

    @property
    def API_KEY(self):
        return getattr(settings, "CLICKSEND_API_KEY", None)


sms_settings = ClickSendSettings()
