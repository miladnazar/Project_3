import json
from pathlib import Path

from web3.auto import w3


class SmartContractTool:

    def __init__(self, contract_name, contract_abi_file_path, contract_address):
        self.__contract_name = contract_name
        self.__contract_abi_file_path = contract_abi_file_path
        self.__contract_address = contract_address
        self.__contract = self.__initContract(contract_abi_file_path, contract_address)

    # --------------------------------------------------------------------------
    # Functional Interface
    # --------------------------------------------------------------------------

    def call(self):
        return None

    # --------------------------------------------------------------------------
    # Helper Functions
    # --------------------------------------------------------------------------

    def __initContract(self, contract_abi_file_path, contract_address):
        with open(Path(contract_abi_file_path)) as json_file:
            abi = json.load(json_file)
        return w3.eth.contract(address=contract_address, abi=abi)
