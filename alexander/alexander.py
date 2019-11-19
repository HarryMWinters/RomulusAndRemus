import grpc
import logging
from concurrent import futures

import rome_pb2_grpc
import rome_pb2


class RomanServicer(rome_pb2_grpc.RomanServiceServicer):
    def __init__(self):
        self.call_count = 0

    def SayHello(self, request, context):
        print("SayHello called.")
        self.call_count += 1
        msg = f"SayHello called on servicer. Call count: {self.call_count}"
        response = rome_pb2.HelloResponse(content=msg)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rome_pb2_grpc.add_RomanServiceServicer_to_server(
        RomanServicer(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    logging.debug("Starting Alexander...")
    serve()
