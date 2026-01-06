import uuid
import random

PROJECT_TYPES = ["sprint", "campaign", "ops", "intake", "goals"]

def generate_projects(teams):
    projects = []
    for team in teams:
        for _ in range(random.randint(3, 6)):
            ptype = random.choice(PROJECT_TYPES)
            projects.append({
                "id": str(uuid.uuid4()),
                "workspace_id": team["workspace_id"],
                "owner_team_id": team["id"],
                "name": f"{ptype.capitalize()} Project",
                "archived": random.random() < 0.3,
                "project_type": ptype
            })
    return projects
