import grpc
import task_pb2
import task_pb2_grpc


def run():
    # 1. Connect to the gRPC server running on localhost:50051
    with grpc.insecure_channel('localhost:50051') as channel:
        # 2. Create a stub (client)
        stub = task_pb2_grpc.TaskServiceStub(channel)

        # 3. Ask the user for a name to send
        name_input = input("Enter a name to process: ")

        # 4. Make the call
        print(f"Sending request for '{name_input}'...")
        response = stub.ProcessData(task_pb2.Request(name=name_input))

    # 5. Print the immediate response from the server
    print("\n--- Server Response ---")
    print(f"Message: {response.message}")
    print(f"Assigned Job ID: {response.job_id}")
    print("\nNote: Your task is now being processed in the background by Celery.")
    print("You can check the Postgres database to see the status update!")


if __name__ == '__main__':
    run()