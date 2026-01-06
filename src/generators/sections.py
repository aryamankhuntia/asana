import uuid

DEFAULT_SECTIONS = ["To Do", "In Progress", "Done"]

def generate_sections(projects):
    sections = []
    for p in projects:
        for i, name in enumerate(DEFAULT_SECTIONS):
            sections.append({
                "id": str(uuid.uuid4()),
                "project_id": p["id"],
                "name": name,
                "order_index": i
            })
    return sections
