from locust.stats import RequestStats
from locust import Locust, TaskSet, task, events
import os
import sys, getopt, argparse
from random import randint,random
import json
from locust.events import EventHook
import requests
import re
import grpc
import service_pb2
import service_pb2_grpc
import time
import xmlrpclib


class GrpcLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(GrpcLocust, self).__init__(*args, **kwargs)

class ApiUser(GrpcLocust):
    
    host = "http://127.0.0.1:50051/"
    min_wait = 100
    max_wait = 1000

    def getEnviron(self,key,default):
            if key in os.environ:
                return os.environ[key]
            else:
                return default

    def on_start(self):
            """
            get token
            :return:
            """
            print "on start"
            self.token = self.getToken()
            self.grpc_endpoint = self.getEnviron('SQUARe_GRPC_ENDPOINT',"127.0.0.1:50051")
            self.data_size = int(self.getEnviron('SELDON_DEFAULT_DATA_SIZE',"784"))           
    

    class task_set(TaskSet):
        
        @task
        def square_root(self):
            channel = grpc.insecure_channel('localhost:50051')
            stub = service_pb2_grpc.SquareServiceStub(channel)
            start_time=time.time()
            try:
                response = stub.SquareNumber(service_pb2.Base(baseNumber = 5))
            except xmlrpclib.Fault as e:
                total_time = int((time.time() - start_time) * 1000)
                events.request_failure.fire(request_type="grpc", name="Square_Service", response_time=total_time, exception=e)
            else:
                total_time = int((time.time() - start_time) * 1000)
                events.request_success.fire(request_type="grpc", name="Square_Service", response_time=total_time, response_length=0)

        # def getToken(self):
        #     consumer_key = self.getEnviron('SELDON_OAUTH_KEY',"oauthkey")
        #     consumer_secret = self.getEnviron('SELDON_OAUTH_SECRET',"oauthsecret")

        #     params = {}
        #     params["consumer_key"] = consumer_key
        #     params["consumer_secret"] = consumer_secret
        #     url = self.oauth_endpoint+"/token"
        #     r = requests.get(url,params=params)
        #     if r.status_code == requests.codes.ok:
        #         j = json.loads(r.text)
        #         print j
        #         return j["access_token"]
        #     else:
        #         print "failed call to get token"
        #         return None


        # def on_start(self):
        #     """
        #     get token
        #     :return:
        #     """
        #     print "on start"
        #     self.oauth_endpoint = self.getEnviron('SELDON_OAUTH_ENDPOINT',"http://127.0.0.1:30015")
        #     self.token = self.getToken()
        #     self.grpc_endpoint = self.getEnviron('SELDON_GRPC_ENDPOINT',"127.0.0.1:30017")
        #     self.data_size = int(self.getEnviron('SELDON_DEFAULT_DATA_SIZE',"784"))            

        # @task
        # def get_prediction(self):
        #     channel = grpc.insecure_channel(self.grpc_endpoint)
        #     stub = seldon_pb2.SeldonStub(channel)
        #     fake_data = [random() for i in range(0,self.data_size)]
        #     data = seldon_pb2.DefaultCustomPredictRequest(values=fake_data)
        #     dataAny = any_pb2.Any()
        #     dataAny.Pack(data)
        #     meta = seldon_pb2.ClassificationRequestMeta(puid=str(randint(0,99999999)))
        #     metadata = [(b'oauth_token', self.token)]
        #     request = seldon_pb2.ClassificationRequest(meta=meta,data=dataAny)
        #     start_time = time.time()
        #     try:
        #         reply = stub.Classify(request,999,metadata=metadata)
        #     except xmlrpclib.Fault as e:
        #         total_time = int((time.time() - start_time) * 1000)
        #         events.request_failure.fire(request_type="grpc", name=HOST, response_time=total_time, exception=e)
        #     else:
        #         total_time = int((time.time() - start_time) * 1000)
        #         events.request_success.fire(request_type="grpc", name=HOST, response_time=total_time, response_length=0)