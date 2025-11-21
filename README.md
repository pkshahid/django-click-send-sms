
# Django ClickSend SMS

A lightweight Django app for sending SMS messages through the ClickSend REST API.
Supports single SMS, bulk SMS, Django settings integration, and a test management command.

---

## Features

* Send a single SMS
* Send bulk SMS
* Easy Django integration
* Simple, high-level SMS client
* Optional test command (`send_test_sms`)
* Works with Django 3.2+

---

## Installation

Install using pip:

```
pip install django-clicksend-sms
```

Or install from a local folder:

```
pip install /path/to/django-clicksend-sms/
```

---

## Django Setup

Add the app to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "clicksend_sms",
]
```

Add your ClickSend credentials:

```python
CLICKSEND_USERNAME = "your_clicksend_username"
CLICKSEND_API_KEY = "your_api_key"
```

---

## Usage

### Sending a Single SMS

```python
from clicksend_sms.client import ClickSendSMSClient

def send_otp(phone, otp):
    client = ClickSendSMSClient()
    return client.send_sms(
        to=phone,
        message=f"Your OTP is {otp}"
    )
```

---

### Sending Bulk SMS

```python
from clicksend_sms.client import ClickSendSMSClient

client = ClickSendSMSClient()

messages = [
    {"to": "+1111111111", "message": "Hello User 1"},
    {"to": "+1222222222", "message": "Hello User 2", "sender_id": "MyApp"},
]

response = client.send_bulk_sms(messages)

print(response)
```

---

## Management Command: Send Test SMS

You can quickly test sending an SMS using the built-in Django command.

```
python manage.py send_test_sms <phone> "<message>"
```

Example:

```
python manage.py send_test_sms +11234567890 "Hello from Django!"
```

---

## Package Structure

```
clicksend_sms/
    __init__.py
    apps.py
    client.py
    settings.py
    management/
        commands/
            send_test_sms.py
```

---

## How It Works

### ClickSendSMSClient

This class handles:

* Loading credentials from Django settings
* Formatting message payloads
* Sending requests to ClickSend REST API
* Supporting both single and bulk SMS

---

## Error Handling

Common errors:

* Missing credentials:

```
ValueError: ClickSend credentials are not configured.
```

* Non-JSON API response:

```
{"error": "Invalid JSON response", "status_code": ###}
```

---

## Development

Install in editable mode:

```
pip install -e .
```

Build package for PyPI:

```
python setup.py sdist bdist_wheel
```

Upload:

```
twine upload dist/*
```

---

## License

This project is licensed under the MIT License.
