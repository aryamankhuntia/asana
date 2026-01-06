import uuid
import random
from src.utils.time import sample_created_at, sample_due_date, sample_completed_at
from src.utils.text import task_title

def generate_tasks(projects, users, sections):
    tasks = []
    for _ in range(30000):
        project = random.choice(projects)
        section = random.choice([s for s in sections if s["project_id"] == project["id"]])
        creator = random.choice(users)
        assignee = None if random.random() < 0.18 else random.choice(users)

        created_at = sample_created_at()
        due = sample_due_date(created_at, project.get("project_type", "ops"))
        completed_at = sample_completed_at(created_at, due)

        tasks.append({
            "id": str(uuid.uuid4()),
            "project_id": project["id"],
            "section_id": section["id"],
            "title": task_title(),
            "status": "completed" if completed_at else random.choice(["not_started", "in_progress"]),
            "priority": random.choice(["low", "medium", "high"]),
            "assignee_id": assignee["id"] if assignee else None,
            "created_by_user_id": creator["id"],
            "created_at": created_at,
            "due_date": due,
            "completed_at": completed_at
        })
    return tasks
