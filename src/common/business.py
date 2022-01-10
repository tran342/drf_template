import random
import string
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR

import requests
from django.conf import settings
from django.utils import timezone


def get_now():
    now = timezone.now()
    # if not timezone.is_naive(now):
    #     now = timezone.make_naive(now, timezone.utc)

    return now


def generate_random_code(n: int):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))


def generate_random_code_2(n: int):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


def generate_random_digit(n: int):
    return ''.join(random.choices(string.digits, k=n))


def round_currency(amount: Decimal) -> Decimal:
    return amount.quantize(Decimal('.01'), ROUND_HALF_UP)


def strip_currency(amount: Decimal) -> Decimal:
    return amount.quantize(Decimal('.01'), ROUND_FLOOR)


def send_slack_msg(txt, channel):
    requests.post(settings.SLACK_ALERT['URL'], json={
        "channel": channel,
        "username": "alert-bot",
        "text": txt,
        "icon_url": "http://www.hopabot.com/img/intro-carousel/f2.png"
    }, headers={'Content-type': 'application/json'})


def send_slack_data_alert(txt):
    send_slack_msg(txt, "#data-alert")
