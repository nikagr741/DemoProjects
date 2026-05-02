import grpc
from concurrent import futures
import uuid
import task_pb2
import task_pb2_grpc
from database import create_task
from worker import long_running_task



class TaskProcessor(task_pb2_grpc.TaskServiceServicer):
    def ProcessData(self, request, context):
        # 1. Generate a unique Job ID
        job_id = str(uuid.uuid4())
        print(f"Received request for name: {request.name}. Assigning Job ID: {job_id}")

        try:
            # 2. Save initial state to Postgres (Source of Truth)
            create_task(job_id)

            # 3. Trigger the background worker (via Redis)
            # .delay() is the Celery magic that makes this asynchronous
            long_running_task.delay(job_id)

            return task_pb2.Response(
                message=f"Hello {request.name}, your request is being processed!",
                job_id=job_id
            )
        except Exception as e:
            print(f"Error starting task: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Failed to initialize task in database.')
            return task_pb2.Response()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_pb2_grpc.add_TaskServiceServicer_to_server(TaskProcessor(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC Producer Server started on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()