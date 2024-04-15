// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Sender{
    constructor(address _to) payable{
        selfdestruct(payable(_to));
    }
}

contract SenderFactory{

    function sendETH(address _to) external payable{
        uint balanceBefore = _to.balance;
        Sender sender = new Sender{value : msg.value}(_to);
        require(_to.balance == balanceBefore + msg.value, "Factory: Transfer failed");
    }
}
