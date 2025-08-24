import re
from django.core.exceptions import ValidationError

BLOCKED_NUMBERS = [
    "09000000000",
    "09100000000",
    "09111111111",
    "09222222222",
    "09333333333",
    "09444444444",
    "09555555555",
    "09666666666",
    "09777777777",
    "09888888888",
    "09999999999",
]

VALID_PREFIXES = [
    *[f"091{i}" for i in range(0, 10)],
    *[f"099{i}" for i in range(0, 5)],

    *[f"090{i}" for i in range(1, 6)],
    *[f"093{i}" for i in range(0, 10)],
    "0941",

    "0920", "0921", "0922",
    "0998", "0999"
]


def validate_phone(phone):
    if not re.match(r"^\d{11}$", phone):
        raise ValidationError("شماره تلفن باید دقیقاً 11 رقم باشد")

    if phone in BLOCKED_NUMBERS:
        raise ValidationError("این شماره قابل استفاده نیست")

    if not any(phone.startswith(prefix) for prefix in VALID_PREFIXES):
        raise ValidationError("پیش‌شماره نامعتبر است")

    return phone

