// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;


contract EmptyContract{
    function empty() external pure returns(string memory){
        return "I am an empty contract";
    }
}