from dotenv import load_dotenv
import os

load_dotenv()

import uuid
from datetime import datetime

from src.db import connect, execute_schema
from src.generators.users import generate_users
from src.generators.teams import generate_teams
from src.generators.projects import generate_projects
from src.generators.sections import generate_sections
from src.generators.tasks import generate_tasks
from src.generators.comments import generate_comments


DB_PATH = os.getenv("DB_PATH", "output/asana_simulation.sqlite")


def insert_many(conn, table, rows):
    if not rows:
        return

    columns = rows[0].keys()
    placeholders = ", ".join(["?"] * len(columns))
    column_names = ", ".join(columns)

    sql = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"
    values = [tuple(row[col] for col in columns) for row in rows]

    conn.executemany(sql, values)


def main():
    conn = connect(DB_PATH)
    execute_schema(conn)

    cursor = conn.cursor()

    # ---- Workspace ----
    workspace_id = str(uuid.uuid4())
    cursor.execute(
        """
        INSERT INTO workspaces (id, name, email_domain, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            workspace_id,
            "Acme SaaS",
            "acme.com",
            datetime.now(),
        ),
    )

    # ---- Users ----
    users = generate_users(450)
    insert_many(cursor, "users", users)

    # Workspace memberships
    workspace_memberships = [
        {
            "workspace_id": workspace_id,
            "user_id": u["id"],
            "role": "member",
            "joined_at": datetime.now(),
        }
        for u in users
    ]
    insert_many(cursor, "workspace_memberships", workspace_memberships)

    # ---- Teams ----
    teams = generate_teams(workspace_id, 32)
    insert_many(cursor, "teams", teams)

    # ---- Team memberships ----
    team_memberships = []
    for team in teams:
        team_users = users.copy()
        import random

        random.shuffle(team_users)
        for u in team_users[: random.randint(4, 10)]:
            team_memberships.append(
                {
                    "team_id": team["id"],
                    "user_id": u["id"],
                    "role": "member",
                    "joined_at": datetime.now(),
                }
            )

    insert_many(cursor, "team_memberships", team_memberships)

    # ---- Projects ----
    projects = generate_projects(teams)

    for p in projects:
        p.pop("project_type", None)

    insert_many(cursor, "projects", projects)

    # ---- Sections ----
    sections = generate_sections(projects)
    insert_many(cursor, "sections", sections)

    # ---- Tasks ----
    tasks = generate_tasks(projects, users, sections)
    insert_many(cursor, "tasks", tasks)

    # ---- Comments ----
    comments = generate_comments(tasks, users)
    insert_many(cursor, "comments", comments)

    conn.commit()
    conn.close()

    print("Simulation database generated successfully.")


if __name__ == "__main__":
    main()
