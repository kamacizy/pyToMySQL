import requests

class API_Caller:
    def __init__(self,url,params):
        self.url = url
        self.params = params

    def api_getter(self):
        res = requests.get(self.url,self.params)
            
    def api_poster(self):
         res = requests.post(self.url,self.params)
            
    def api_putter(self):
        res = requests.put(self.url,self.params)
    
    def api_updater(self):
        res = requests.pa(self.url,self.params)
