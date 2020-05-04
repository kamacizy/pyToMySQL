import requests

class Machine:
    def __init__(self,url,stock,params):
        self.url = url
        self.stock = stock
        self.params = params

    def api_getter(self):
        res = requests.get(self.url,self.params)
