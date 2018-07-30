
from __future__ import print_function

import grpc

import service_pb2
import service_pb2_grpc


def square_root():
    channel = grpc.insecure_channel('localhost:50051')
    stub = service_pb2_grpc.SquareServiceStub(channel)
    response = stub.SquareNumber(service_pb2.Base(baseNumber=5))
    print(response)
    #return response.numberSquared
    
if __name__ == '__main__':
    square_root()

