import psycopg2
from psycopg2.extras import RealDictCursor

# Connection string using the credentials from your docker-compose
DB_URL = "postgresql://nikhil_user:mysecretpassword@localhost:5432/task_db"

def get_connection():
    return psycopg2.connect(DB_URL)

def update_task_status(task_id, status, result=None):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE tasks SET status = %s, result = %s WHERE id = %s",
            (status, result, task_id)
        )
    conn.commit()
    conn.close()

def create_task(task_id):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO tasks (id, status) VALUES (%s, %s)",
            (task_id, 'PENDING')
        )
    conn.commit()
    conn.close()