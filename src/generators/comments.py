import uuid
import random
from src.utils.text import comment_text
from src.utils.time import sample_created_at

def generate_comments(tasks, users):
    comments = []
    for task in tasks:
        if random.random() < 0.6:
            continue
        for _ in range(random.randint(1,3)):
            comments.append({
                "id": str(uuid.uuid4()),
                "task_id": task["id"],
                "user_id": random.choice(users)["id"],
                "content": comment_text(),
                "created_at": sample_created_at()
            })
    return comments
