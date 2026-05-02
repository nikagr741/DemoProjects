from celery import Celery

# The first argument 'worker' MUST match the filename 'worker.py'
app = Celery('worker', broker='redis://localhost:6379/0')

@app.task
def long_running_task(task_id):
    print(f"Processing {task_id}")
    return True