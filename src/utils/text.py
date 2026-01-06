import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2] / "text_pools"

def load_pool(filename):
    path = BASE_DIR / filename
    return [line.strip() for line in path.read_text().splitlines() if line.strip()]

ENGINEERING_TITLES = load_pool("task_titles_engineering.txt")
MARKETING_TITLES = load_pool("task_titles_marketing.txt")
COMMENTS = load_pool("comments.txt")
PROJECT_NAMES = load_pool("project_names.txt")

def task_title(task_type="engineering"):
    if task_type == "marketing":
        return random.choice(MARKETING_TITLES)
    return random.choice(ENGINEERING_TITLES)

def comment_text():
    return random.choice(COMMENTS)

def project_name():
    return random.choice(PROJECT_NAMES)
