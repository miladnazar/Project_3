// SPDX-License-Identifier: MIT
pragma solidity ^0.5.4;
pragma experimental ABIEncoderV2;
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";

contract Project3PortfolioBuilderSmartContract is ERC721Full {

    constructor() ERC721Full("PortfolioCoin", "PFC") public { }

    struct Portfolio {
        string date;
        string name;
        string portfolio_string; // for testing
    }

    using Counters for Counters.Counter;
    Counters.Counter token_ids;

    mapping(uint => Portfolio) public portfolios;

    event PortfolioEvent(uint token_id, string portfolio_uri);

    // -------------------------------------------------------------------------
    // Struct-based portfolio map functions
    // -------------------------------------------------------------------------

    function registerPortfolio(bool generate_token_id, uint token_id,
            string memory portfolio_uri, address owner,
            string memory date, string memory name, string memory portfolio_string) public returns(uint) {

      /** @dev Registers a portfolio allocation.
        * @param id The portfolio id.
        * @param portfolio The recommended portfolio allocation.
        * @return result Success indicator.
        */

        if (generate_token_id) {
            token_ids.increment();
            token_id = token_ids.current();
        }

        // _mint(owner,token_id);  // TODO
        // _setTokenURI(token_id, portfolio_uri);  // TODO

        portfolios[token_id] = Portfolio(date, name, portfolio_string);

        // emit PortfolioEvent(token_id, portfolio_uri);

        return token_id;
    }

    function getLastTokenID() public returns (uint) {
        return token_ids.current();
    }

    function testGetPortfoioString() public returns (string memory) {
        return "AAPL: 45";
    }

    // experimental, for testing
    function registerPortfolioTesting(uint token_id, string memory portfolio_uri, string memory tester) public returns(string memory) {
        portfolios[token_id].portfolio_string = tester;
        emit PortfolioEvent(token_id,portfolio_uri);
        return portfolios[token_id].portfolio_string; // for testing
    }

    function getPortfolio(uint token_id) public returns(Portfolio memory) {
      /** @dev Retrieves a previously-registered portfolio allocation.
        * @param id The portfolio id.
        * @return portfolio The recommended portfolio allocation.
        */
        return portfolios[token_id];
    }

    function getPortfolioString(uint token_id) public returns(string memory) {
      /** @dev Retrieves a previously-registered portfolio allocation.
        * @param id The portfolio id.
        * @return portfolio The recommended portfolio allocation.
        */
        Portfolio memory portfolio = portfolios[token_id];
        return portfolio.portfolio_string;
    }

}
