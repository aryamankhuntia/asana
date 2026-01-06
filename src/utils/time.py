import random
from datetime import datetime, timedelta

NOW = datetime.now()

def random_workday(start, end):
    while True:
        dt = start + timedelta(seconds=random.randint(0, int((end-start).total_seconds())))
        if dt.weekday() < 5:
            return dt

def sample_created_at(months_back=6):
    start = NOW - timedelta(days=30 * months_back)
    return random_workday(start, NOW)

def sample_due_date(created_at, project_type):
    if random.random() > 0.75:
        return None

    if project_type == "sprint":
        delta = random.randint(7, 21)
    elif project_type == "campaign":
        delta = random.randint(14, 56)
    else:
        delta = random.randint(14, 90)

    return created_at.date() + timedelta(days=delta)

def sample_completed_at(created_at, due_date=None):
    if random.random() > 0.65:
        return None

    base = created_at + timedelta(days=random.randint(1, 14))
    if due_date and random.random() < 0.2:
        base = datetime.combine(due_date, datetime.min.time()) + timedelta(days=random.randint(1,5))
    return base
