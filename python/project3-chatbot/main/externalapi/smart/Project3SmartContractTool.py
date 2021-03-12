from python.src.main.lib.interfaces.SmartContractTool import SmartContractTool

class Project3SmartContractTool(SmartContractTool):

    def __init__(self, contract_address):
        super().__init__("Project3PortfolioBuilderSmartContract", "Project3PortfolioBuilderSmartContract_ABI.json", contract_address)

    def call(self, id, portfolio_str):
        self.__contract.functions.registerPortfolioStr(id, portfolio_str).call()

    def get_portfolio_str(self, id):
        return self.__contract.functions.getPortfolioStr(id).call()
