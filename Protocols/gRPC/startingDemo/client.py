import grpc
import greeter_pb2
import greeter_pb2_grpc

def run():
    # Connect to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        # Call the remote method
        response = stub.SayHello(greeter_pb2.HelloRequest(name='Nikhil'))
    print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()