from datetime import datetime, date, timedelta


CANON = "%Y-%m-%d"
def parse_iso(text: str) -> date:
    try:
        return datetime.strptime(text, CANON).date()
    except ValueError:
        raise ValueError("invalid date: bad value")

SHOW = "%d %b %Y"
def show(day: date) -> str:
    return day.strftime(SHOW)
    
    
def tenure_days(start: date, end: date) -> int:
    return (end - start).days

def shift(day: date, delta_days: int) -> date:
    return day + timedelta(days=delta_days)


def parse_date(text: str) -> date:
    try:
        d = datetime.strptime(text, CANON).date()
    except ValueError:
        raise ValueError("invalid date: bad value")
    
    if d.isoformat() != text:
        raise ValueError("invalid date: not canonical")
    
    return d


def bucket(signup: str, today: date) -> str:
    signup_date = parse_date(signup)
    
    tenure = tenure_days(signup_date, today)
    
    if tenure < 0:
        raise ValueError("invalid tenure: future signup")
    
    if tenure < 30:
        return "new"
    elif tenure <= 364:
        return "active"
    else:
        return "veteran"
    
        
def age_report(signups: list[str], today: date) -> list[tuple[str, int]]:
    result = {}
    
    for signup in signups:
        parsed = parse_date(signup)
        month = parsed.isoformat()[:7]
        result[month] = result.get(month, 0) + 1
        
    return list(result.items())