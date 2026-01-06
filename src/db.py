import sqlite3

def connect(db_path):
    return sqlite3.connect(db_path)

def execute_schema(conn, schema_path="schema.sql"):
    with open(schema_path, "r") as f:
        conn.executescript(f.read())
    conn.commit()
