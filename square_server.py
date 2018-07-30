from concurrent import futures
import time

import grpc

import service_pb2
import service_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Square(service_pb2_grpc.SquareServiceServicer):

    def SquareNumber(self, request, context):
        return service_pb2.NumberSquared(numberSquared=request.baseNumber*request.baseNumber)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_SquareServiceServicer_to_server(Square(), server)
    print("Running on port localhost:50051")
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
