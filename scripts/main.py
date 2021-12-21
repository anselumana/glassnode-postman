import os
import json
from generator import GlassnodePostmanGenerator
from utils import get_api_key

if __name__ == "__main__":
    path = os.getcwd() + os.sep + "postman" + os.sep + "glassnode-api.postman_collection.json"
    api_key = get_api_key()
    generator = GlassnodePostmanGenerator(api_key)
    collection = generator.generate_collection()
    with open(path, "w") as file:
        file.write(json.dumps(collection))
    print(f"Glassnode API Postman collection successfully generated.\nSaved to \"{path}\"")