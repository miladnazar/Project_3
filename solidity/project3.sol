pragma solidity ^0.7.4;
pragma experimental ABIEncoderV2;

/*
{
    "id":1,
    "date":"2021-01-02",
    "assets": [
        {
            "asset_name":"TSLA",
            "allocation":100
        },
        {
            "asset_name":"AAPL",
            "allocation":50
        }
    ]
}
*/

contract project3 {
    
    struct Portfolio {
        string industries;
        //string [2][] industries;
        string date;
        uint id;          
    }
    
    struct CustomerMetrics {
        uint risk;
        uint unitial_investment;
        string[] industries_preferences;
        uint investing_duration;
        
    }
    
    
        
    struct PerformanceData { 
        fixed annualized_return;
        fixed sharpe_ratio;
        fixed volatility;
    }
    
    struct IndustryData { 
        fixed annualized_return;
        fixed sharpe_ratio;
        fixed volatility;
    }
        
    
    mapping(uint => Portfolio) public portfolios;
    
    
    constructor() public {}
    // constructor (string[] memory industry_return_data, string[] memory industry_volatility_data, string[] memory industry_sharperatio_data) public {
    // }

    // how to parse JSON object, and where?
    function buildPortfolio(uint id, CustomerMetrics memory metrics, IndustryData memory industry_data, string[] memory portfolios_info) public returns(Portfolio memory) {
      /** @dev Builds a suggested portfolio allocation based on customer requirements.
        * @param id portfolio id 
        * @param metrics the customer investment requirements
        * @param industry_data industry specific performance data
        * @param portfolios_info any additional portfolio parameters
        * @return portfolio the recommended portfolio allocations
        */
        //Portfolio portfolio=Portfolio();
        //risk = metrics.risk; 
        //industries = metrics.industries_preferences;
        //performanceData = filterIndustires(performanceData, industries);
        //performanceData = filterRisk(performanceData, risk);
        //portfolio = buildFromSharpeRatio(performanceData);
        //portfolios[id]=portfolio;
        return Portfolio("", "", 0);
    }
    
    //function filterIndustires(PerformanceData performanceData, string[] industries) public returns(PerformanceData) {
    //}   
    //function filterRisk(PerformanceData performanceData, string[] risk) public returns(PerformanceData) {
    //}
    //function buildFromSharpeRatio(PerformanceData performanceData, uint numIndustries) public returns(Portfolio){
    //}
   
      
    
    //function() external payable {
        // fallback function
    //}
    
    /*
    // This function will convert an uint type value to string type
    // Will be used to store into dynamic Portfolio array
    function uintToString(uint v) constant returns (string str) {
        uint maxlength = 100;
        bytes memory reversed = new bytes(maxlength);
        uint i = 0;
        while (v != 0) {
            uint remainder = v % 10;
            v = v / 10;
            reversed[i++] = byte(48 + remainder);
        }
        bytes memory s = new bytes(i + 1);
        for (uint j = 0; j <= i; j++) {
            s[j] = reversed[i - j];
        }
        str = string(s);
    }
    
    // This function will convert a string type value to an uint type
    // Will be used to read from Porfolio dynamic array (if needed)
    function stringToUint(string s) constant returns (uint result) {
        bytes memory b = bytes(s);
        uint i;
        result = 0;
        for (i = 0; i < b.length; i++) {
            uint c = uint(b[i]);
            if (c >= 48 && c <= 57) {
                result = result * 10 + (c - 48);
            }
        }
    }
    
    function stringToUint(string s) constant returns (uint) {
        bytes memory b = bytes(s);
        uint result = 0;
        for (uint i = 0; i < b.length; i++) { // c = b[i] was not needed
            if (b[i] >= 48 && b[i] <= 57) {
                result = result * 10 + (uint(b[i]) - 48); // bytes and int are not compatible with the operator -.
            }
        }
        return result; // this was missing
    }

    function uintToString(uint v) constant returns (string) {
        uint maxlength = 100;
        bytes memory reversed = new bytes(maxlength);
        uint i = 0;
        while (v != 0) {
            uint remainder = v % 10;
            v = v / 10;
            reversed[i++] = byte(48 + remainder);
        }
        bytes memory s = new bytes(i); // i + 1 is inefficient
        for (uint j = 0; j < i; j++) {
            s[j] = reversed[i - j - 1]; // to avoid the off-by-one error
        }
        string memory str = string(s);  // memory isn't implicitly convertible to storage
        return str;
    }
    */
    
    // NOTES 
    // Receive JSON object to contract
    // Store struct on chain
    
    // Error checking to revert changes, if invalid values are found in JSON
    
    //  function buildPortfolio(price_prediction, valuation, customer_metrics) public returns(portfolio_type portfolio) {
    //  }
}

