from utils import validate_date, validate_email, validate_phone

# Определение типа поля
def determine_field_type(value: str) -> str:
    if validate_date(value):
        return "date"
    elif validate_phone(value):
        return "phone"
    elif validate_email(value):
        return "email"
    else:
        return "text"