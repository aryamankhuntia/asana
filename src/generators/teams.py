import uuid
import random

TEAM_NAMES = [
    "Core Platform", "Growth Engineering", "Revenue Ops",
    "Customer Enablement", "Design Systems", "IT Operations"
]

def generate_teams(workspace_id, n):
    teams = []
    for _ in range(n):
        teams.append({
            "id": str(uuid.uuid4()),
            "workspace_id": workspace_id,
            "name": random.choice(TEAM_NAMES)
        })
    return teams
