import requests
import json
import os

from web3.auto import w3

// Read api keys from .json or .xml
headers = {
    "Content-Type":"application/json",
    "pinata_api_key":"",
    "pinata_secret_api_key":""
}

def initContract():
    # CryptoFax.json
    # return w3.eth.contract(address="", abi="json.load()")
    return -1

def convertDataToJSON():
    # json.dumps()
    return -1

def pinJSONtoIPFS(json):
    request = requests.post("https://api.pinata.cloud/pinning/pinJSONtoIPFS",
                            data=json,
                            headers=headers)

    ipfs_hash = request.json()["IpfsHash"]
    return f"ipfs://{ipfs_hash}"
