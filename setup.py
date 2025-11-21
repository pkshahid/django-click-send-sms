from setuptools import setup, find_packages

setup(
    name="django-clicksend-sms",
    version="1.0.3",
    description="Django app for sending SMS using ClickSend API",
    author="Mohammed Shahid",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=3.2",
        "requests>=2.25",
    ],
)
