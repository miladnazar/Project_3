// SPDX-License-Identifier: MIT
pragma solidity ^0.7.4;
pragma experimental ABIEncoderV2;

contract project3 {

    struct Portfolio {
        string industries;
        //string [2][] industries;
        string date;
        uint id;
    }

    mapping(uint => string) public portfolio_strings;
    mapping(uint => Portfolio) public portfolios;

    constructor() {}

    // -------------------------------------------------------------------------
    // String-based portfolio map functions
    // -------------------------------------------------------------------------

    function registerPortfolioString(uint id, string memory portfolio_str) public returns(bool) {
      /** @dev Registers a portfolio allocation in string form.
        * @param id The portfolio id.
        * @param portfolio The recommended portfolio allocations in string form.
        * @return result True if success; false if string is empty.
        */
        // TODO Error handling - return fals if empty string.
        portfolio_strings[id] = portfolio_str;
        return true;
    }

    function getPortfolioString(uint id) public returns(string memory) {
      /** @dev Retrieves a previously-registered portfolio allocation.
        * @param id The portfolio id.
        * @return portfolio The recommended portfolio allocations in string form; empty string if no portfolio registered with the id.
        */
        // TODO Error handling.
        return portfolio_strings[id];
    }

    // -------------------------------------------------------------------------
    // Struct-based portfolio map functions
    // -------------------------------------------------------------------------

    function registerPortfolio(uint id, Portfolio memory portfolio) public returns(bool) {
      /** @dev Registers a portfolio allocation.
        * @param id The portfolio id.
        * @param portfolio The recommended portfolio allocation.
        * @return result Success indicator.
        */
        portfolios[id] = portfolio;
        return true;
    }

    function getPortfolio(uint id) public returns(Portfolio memory) {
      /** @dev Retrieves a previously-registered portfolio allocation.
        * @param id The portfolio id.
        * @return portfolio The recommended portfolio allocation.
        */
        return portfolios[id];
    }

    // NOTES
    // Receive JSON object to contract
    // Store struct on chain
    // Error checking to revert changes, if invalid values are found in JSON

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

}
