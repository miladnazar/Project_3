pragma solidity ^0.7.4;

contract project3 {
    struct Portfolio {
        string [2][] assets;            
    }
    
    mapping(uint => Portfolio) public portfolios;
    
    constructor() public {

    }

    // how to parse JSON object, and where?
    function buildPortfolio(uint id) public returns(bool) {
        Portfolio tmp=Portfolio();
        portfolios[id]=tmp;
        return true;
    }
    
    function() external payable {
        // fallback function
    }
    
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
