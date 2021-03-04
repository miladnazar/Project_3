// SPDX-License-Identifier: MIT
pragma solidity ^0.7.4;
pragma experimental ABIEncoderV2;
/*
{
    “id”:1,
    “date”:“2021-01-02”,
    “assets”: [
        {
            “asset_name”:“TSLA”,
            “allocation”:100
        },
        {
            “asset_name”:“AAPL”,
            “allocation”:50
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

    mapping(uint => Portfolio) public portfolios;

    constructor() {}

    function registerPortfolio_testing(uint id) public returns(string memory) {
        return "This is a test.";
    }

    function registerPortfolio(uint id, Portfolio memory portfolio) public returns(bool) {
      /** @dev Registers a suggested portfolio allocation.
        * @param id The portfolio id.
        * @param portfolio The recommended portfolio allocations.
        * @return result Success indicator.
        */
        portfolios[id] = portfolio;
        return true;
    }

    // NOTES
    // Receive JSON object to contract
    // Store struct on chain
    // Error checking to revert changes, if invalid values are found in JSON
}
