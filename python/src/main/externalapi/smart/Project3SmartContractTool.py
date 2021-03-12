from python.src.main.lib.interfaces.SmartContractTool import SmartContractTool

class Project3SmartContractTool(SmartContractTool):

    def __init__(self, contract_address):
        super().__init__("Project3PortfolioBuilderSmartContract", "Project3PortfolioBuilderSmartContract_ABI.json", contract_address)

    def call(self, id, contract_address, portfolio_name, portfolio_str):
        # TODO Change the date
        return self.__contract.functions.registerPortfolio(False, id,
                "http://portfolio-uri", contract_address,
                "1/1/2021", portfolio_name, portfolio_str).call()
        # self.__contract.functions.registerPortfolioStr(id, portfolio_str).call()

# registerPortfolio(bool generate_token_id, uint token_id,
# string memory portfolio_uri, address owner,
# string memory date, string memory name, string memory portfolio_string) public returns(uint)



    def get_portfolio_str(self, id):
        return self.__contract.functions.getPortfolioStr(id).call()
