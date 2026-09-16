from datetime import datetime

def validate_date(date_string: str, date_format: str = "%Y-%m-%d") -> tuple[bool, datetime | None]:
    try:
        date = datetime.strptime(date_string, date_format)
        return True, date
    except ValueError:
        return False, None
    
def extract_year_week(date: datetime) -> str:
    iso_calendar = date.isocalendar()
    year_week = f"{iso_calendar[0]}-W{iso_calendar[1]}"
    return year_week