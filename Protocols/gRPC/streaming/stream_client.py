import grpc
import greeter_pb2
import greeter_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)

        print("Opening stream...")
        # The call returns an iterator
        response_iterator = stub.StreamGreetings(greeter_pb2.HelloRequest(name='Nikhil'))

        for response in response_iterator:
            print(f"Received from stream: {response.message}")


if __name__ == '__main__':
    run()