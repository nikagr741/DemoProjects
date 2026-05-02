import time
import psycopg2
from celery import Celery

# 1. Initialize Celery
# 'localhost' works if you run the worker in your terminal.
# Use 'redis' if running the worker inside a Docker container.
app = Celery('worker', broker='redis://localhost:6379/0')


def update_task_status(task_id, status, result=None):
    """Updates the PostgreSQL database with the current task state."""
    conn = None
    try:
        # DB Connection: Use localhost:5432 for external workers
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="task_db",
            user="nikhil_user",
            password="mysecretpassword"
        )
        cur = conn.cursor()

        # Execute the update
        cur.execute(
            "UPDATE tasks SET status = %s, result = %s WHERE id = %s",
            (status, result, task_id)
        )

        # IMPORTANT: Changes are not saved without a commit!
        conn.commit()
        cur.close()
        print(f"[{task_id}] Database updated to: {status}")

    except Exception as e:
        print(f"❌ Database Update Error: {e}")
    finally:
        if conn:
            conn.close()


@app.task
def long_running_task(task_id):
    """The background task picked up by Celery."""
    print(f"🚀 Starting task: {task_id}")

    # Step A: Mark as Processing
    update_task_status(task_id, 'PROCESSING')

    # Step B: Simulate heavy work (The 10-second delay)
    print(f"⌛ Working on {task_id}...")
    time.sleep(10)

    # Step C: Mark as Completed
    update_task_status(task_id, 'COMPLETED', result="Success: Data processed.")

    print(f"✅ Task {task_id} finished!")
    return True