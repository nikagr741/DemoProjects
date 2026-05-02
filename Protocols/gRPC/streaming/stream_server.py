import grpc
import time
from concurrent import futures
import greeter_pb2
import greeter_pb2_grpc


class Greeter(greeter_pb2_grpc.GreeterServicer):
    def StreamGreetings(self, request, context):
        print(f"Received stream request from {request.name}")

        # We will simulate a live feed by sending 5 messages with a delay
        messages = ["Initializing...", "Connecting to database...", "Fetching data...", "Processing...", "Done!"]

        for msg in messages:
            time.sleep(1)  # Simulate some work being done
            yield greeter_pb2.HelloReply(message=f"[{msg}] Hello {request.name}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    print("Streaming Server started on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()