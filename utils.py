import re

def validate_email(value: str) -> bool:
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", value))

def validate_phone(value: str) -> bool:
    return bool(re.match(r"\+7 \d{3} \d{3} \d{2} \d{2}", value))

def validate_date(value: str) -> bool:
    return bool(re.match(r"(\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})", value))