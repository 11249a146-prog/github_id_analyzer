def number(value):
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return "0"

def short_date(value):
    return (value or "")[:10]
