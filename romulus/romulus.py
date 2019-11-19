from flask import Flask
import grpc
import rome_pb2_grpc
import rome_pb2

app = Flask(__name__)

channel = grpc.insecure_channel('alexander:5000')
stub = rome_pb2_grpc.RomanServiceStub(channel)


@app.route('/')
def hello_world():
    msg = rome_pb2.HelloRequest(content="Hello from romulus (grpc)")
    rpc = stub.SayHello(msg)
    return rpc.content


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
