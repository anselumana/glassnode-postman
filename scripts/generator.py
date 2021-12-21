import requests
import utils
#from pprint import pprint

class GlassnodePostmanGenerator():
    "Glassnode API Postman collection generator."

    def __init__(self, api_key):
        self.__api_key = api_key

    def generate_collection(self):
        "Generates the Glassnode API Postman collection as a JSON file."
        endpoints = self.__get_endpoints()
        return self.__generate_collection(endpoints)
        
    def __get_endpoints(self):
        params = self.__get_params()
        res = requests.get(utils.GLASSNODE_ENDPOINTS_URL, params=params)
        if res.status_code != 200:
            raise Exception(f"Unable to fetch Glassnode API endpoints: API responsed with a {res.status_code} status code.\n{res.text}")
        return self.__get_endpoints_grouped_by_domain(res.json())
    
    def __generate_collection(self, endpoints):
        template = utils.get_template()
        for domain in endpoints:
            folder_name = self.__beautify(domain)
            folder = utils.get_folder(folder_name)
            for endpoint in endpoints[domain]:
                request = utils.get_request(endpoint)
                folder["item"].append(request)
            template["item"].append(folder)
        return template
        
    def __get_endpoints_grouped_by_domain(self, response):
        endpoints = {}
        for item in response:
            raw_endpoint = item["path"]
            path = str.split(raw_endpoint, "/")[1:]
            domain = path[-2]
            endpoint = {
                "endpoint": raw_endpoint,
                "name": self.__beautify(path[-1]),
                "path": path
            }
            if not domain in endpoints:
                endpoints[domain] = []
            endpoints[domain].append(endpoint)
        return endpoints
    
    def __get_params(self):
        return {
            "api_key": self.__api_key
        }
    
    def __beautify(self, string):
        split = str.split(string, "_")
        split = [x.capitalize() for x in split]
        return " ".join(split)