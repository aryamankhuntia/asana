import uuid
import random
from faker import Faker

fake = Faker()

def generate_users(n):
    users = []
    for _ in range(n):
        uid = str(uuid.uuid4())
        users.append({
            "id": uid,
            "name": fake.name(),
            "email": fake.unique.email(),
            "role": random.choices(
                ["ic", "manager", "exec"],
                weights=[0.75, 0.2, 0.05]
            )[0]
        })
    return users
