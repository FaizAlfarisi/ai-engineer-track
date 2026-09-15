from datetime import datetime

def validate_date(date_string: str, date_format: str = "%Y-%m-%d") -> bool:
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False