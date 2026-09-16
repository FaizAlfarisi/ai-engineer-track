from datetime import datetime

def parse_date(date_string: str, date_format: str = "%Y-%m-%d") -> tuple[str | None, datetime | None]:
    try:
        date_obj = datetime.strptime(date_string, date_format)
        canonical_str = date_obj.strftime(date_format)
        
        if date_string != canonical_str:
            return None, None
        
        return canonical_str, date_obj
    except ValueError:
        return None, None
    
def extract_year_week(date: datetime) -> str:
    iso_calendar = date.isocalendar()
    year_week = f"{iso_calendar.year}-W{iso_calendar.week:02d}"
    return year_week