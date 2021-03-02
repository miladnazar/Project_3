from pathlib import Path

import requests
import json
import os
from dotenv import load_dotenv

from web3.auto import w3

# // Read api keys from .json or .xml
headers = {
    "Content-Type":"application/json",
    "pinata_api_key":"",
    "pinata_secret_api_key":""
}

def initContract():
    load_dotenv()
    with open(Path("Project3_ABI.json")) as json_file:
        abi = json.load(json_file)
    return w3.eth.contract(address=os.getenv("PROJECT3_ADDRESS"), abi=abi)

def convertDataToJSON():
    # json.dumps()
    return -1

def pinJSONtoIPFS(json):
    request = requests.post("https://api.pinata.cloud/pinning/pinJSONtoIPFS",
                            data=json,
                            headers=headers)

    ipfs_hash = request.json()["IpfsHash"]
    return f"ipfs://{ipfs_hash}"
