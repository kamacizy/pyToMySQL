import requests

class API_Caller:
    def __init__(self,url,params):
        self.url = url
        self.params = params

    def api_getter(self):
        res = requests.get(self.url,self.params)
        if res.status_code >= 200 and res.status_code < 300:
            return res.json()
        else:
            return "Failed with status code: {0}".format(res.status_code)

    def api_poster(self):
        res = requests.post(self.url,self.params)
        if res.status_code >= 200 and res.status_code < 300:
            return res.json()
        else:
            return "Failed with status code: {0}".format(res.status_code)

            
    def api_putter(self):
        res = requests.put(self.url,self.params)
        if res.status_code >= 200 and res.status_code < 300:
            return res.json()
        else:
            return "Failed with status code: {0}".format(res.status_code)

    
    def api_updater(self):
        res = requests.pa(self.url,self.params)
        if res.status_code >= 200 and res.status_code < 300:
            return res.json()
        else:
            return "Failed with status code: {0}".format(res.status_code)

