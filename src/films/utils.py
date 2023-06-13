from datetime import datetime


def get_date(date: str) -> str:
    """Функция преобразования даты."""
    date_format = '%b %d, %Y'
    return datetime.strptime(date, date_format)
