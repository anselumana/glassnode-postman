from dotenv import dotenv_values

GLASSNODE_ENDPOINTS_URL = "https://api.glassnode.com/v2/metrics/endpoints"

def get_template() -> dict:
    return {
        "info": {
            "_postman_id": "9c236aa8-b6ff-4975-9c03-9f402044d0a6",
            "name": "Glassnode API",
            "description": "Non-official Glassnode API Postman collection. API Docs: https://docs.glassnode.com/api. Github repository: https://github.com/anselumana/glassnode-postman. Issues: https://github.com/anselumana/glassnode-postman/issues",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": []
    }

def get_folder(name) -> dict:
    return {
        "name": name,
        "item": []
    }

def get_request(endpoint) -> dict:
    host = "{{url}}"
    return {
        "name": endpoint["name"],
        "request": {
            "method": "GET",
            "header": [
                {
                    "key": "Content-Type",
                    "value": "application/json",
                    "type": "text"
                }
            ],
            "url": {
                "raw": host + "/" + "/".join(endpoint["path"]),
                "host": [
                    host
                ],
                "path": endpoint["path"],
                "query": [
                    {
                        "key": "a",
                        "value": "BTC",
                        "description": "Asset symbol",
                        "disabled": False
                    },
                    {
                        "key": "s",
                        "value": "0",
                        "description": "Since (unix timestamp)",
                        "disabled": True
                    },
                    {
                        "key": "u",
                        "value": "1640115478",
                        "description": "Until (unix timestamp)",
                        "disabled": True
                    },
                    {
                        "key": "i",
                        "value": "24h",
                        "description": "Frequency interval [10m, 1h, 24h, 1w, 1month]",
                        "disabled": True
                    },
                    {
                        "key": "f",
                        "value": "JSON",
                        "description": "Format [JSON, CSV]",
                        "disabled": True
                    },
                    {
                        "key": "timestamp_format",
                        "value": "unix",
                        "description": "Timestamp format [unix, humanized]",
                        "disabled": True
                    }
                ]
            },
            "description": ""
        },
        "response": []
    }
    
def beautify(value: str) -> str:
    split = str.split(value, "_")
    split = [x.capitalize() for x in split]
    return " ".join(split)

def get_api_key() -> str:
    """
    Returns the Glassnode api key found in the .env file in the root directory.
    """
    config = dotenv_values()
    return config.get("API_KEY")