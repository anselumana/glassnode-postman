import json
import requests
import utils

class GlassnodePostmanGenerator():
    "Glassnode API Postman collection generator."

    def __init__(self, api_key: str):
        self.__api_key = api_key

    def generate_collection(self) -> dict:
        "Returns the Glassnode API Postman collection as a dictionary."
        endpoints = self.__get_endpoints()
        return self.__generate_collection(endpoints)
        
    def __get_endpoints(self) -> dict:
        "Returns all Glassnode API endpoints grouped by domain"
        params = self.__get_params()
        res = requests.get(utils.GLASSNODE_ENDPOINTS_URL, params=params)
        if res.status_code != 200:
            raise Exception(f"Unable to fetch Glassnode API endpoints: API responsed with a {res.status_code} status code.\n{res.text}")
        raw_endpoints = [item["path"] for item in res.json()]
        return self.__get_endpoints_grouped_by_domain(raw_endpoints)
    
    def __generate_collection(self, endpoints: dict) -> dict:
        "Returns the dict representing the Postman JSON collection"
        collection = utils.get_template()
        for domain in sorted(endpoints.keys()):
            folder_name = utils.beautify(domain)
            folder = utils.get_folder(folder_name)
            for endpoint in sorted(endpoints[domain], key=lambda e: e["name"]):
                request = utils.get_request(endpoint)
                folder["item"].append(request)
            collection["item"].append(folder)
        return collection
        
    def __get_endpoints_grouped_by_domain(self, raw_endpoints: list) -> dict:
        "Returns Glassnode API endpoints grouped by domain given the raw list of endpoints"
        endpoints = {}
        for raw_endpoint in raw_endpoints:
            path = str.split(raw_endpoint, "/")[1:]
            domain = path[-2]
            endpoint = {
                "endpoint": raw_endpoint,
                "name": utils.beautify(path[-1]),
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


if __name__ == "__main__":
    # get Glassnode API key
    api_key = utils.get_api_key()
    if not api_key:
        raise Exception("API key not found. Either no .env was found in the root directory or no API_KEY=value was found within it")
    gpg = GlassnodePostmanGenerator(api_key)
    collection = gpg.generate_collection()
    # dump json sorting keys
    out = json.dumps(collection, sort_keys=True)
    # write collection as JSON string to std out
    print(out)