// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Sender{
    function sendAndDestruct(address _receiver) external payable{
        selfdestruct(payable(_receiver));
    }
}

contract SenderFactory{
    
    function _createSender() internal returns(Sender){
        return new Sender();
    }

    function sendETH(address _to) external payable{
        uint balanceBefore = _to.balance;

        Sender sender = _createSender();
        sender.sendAndDestruct{value: msg.value}(_to);

        require(_to.balance == balanceBefore + msg.value, "Factory: Transfer failed");
    }
}
