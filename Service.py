from ast import Param
from functools import cache
from this import d
from xmlrpc.client import Fault
from cachetools import Cache
from cv2 import add
from suds.client import Client
from suds.client import Method
from suds.xsd.doctor import Import, ImportDoctor
import requests
import pandas as pd
import numpy as np
import suds
from suds.cache import NoCache



# print(DATA)

class service():
    def Insert(SP,PARA):
        url = 'http://localhost/Data/WebService1.asmx?WSDL'
        imp = Import('http://www.w3.org/2001/XMLSchema')
        doctor = ImportDoctor(imp)
        client = Client(url, doctor=doctor)
        client.set_options(cache=None)
        print(client)
        response = client.service.InsertData(SP,PARA)
        print(response)

    def User_Master(SP,PARA):

                url = 'http://localhost/Data/WebService1.asmx?WSDL'
                imp = Import('http://www.w3.org/2001/XMLSchema')
                #imp.filter.add('http://localhost/IPL_COMMService_STCLAIR/IPL_COMMService.asmx')
                doctor = ImportDoctor(imp)
                client = Client(url, doctor=doctor)
                client.set_options(cache=None)
                print(client)
                response = client.service.User_Master(SP,PARA)
                print(response)

    def Clock_IN_Out(SP,PARA):
                url = 'http://localhost/Data/WebService1.asmx?WSDL'
                imp = Import('http://www.w3.org/2001/XMLSchema')
                #imp.filter.add('http://localhost/IPL_COMMService_STCLAIR/IPL_COMMService.asmx')
                doctor = ImportDoctor(imp)
                client = Client(url, doctor=doctor)
                client.set_options(cache=None)
                print(client)
                response = client.service.Clock_in_Out(SP,PARA)
                print(response)



