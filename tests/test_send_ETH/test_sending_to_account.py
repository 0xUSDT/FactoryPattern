import brownie 
from brownie import accounts
import random

def test_sending_to_account(senderETH):

    sender = accounts[0]
    receiver = accounts[1]

    balance_receiver_before = receiver.balance()

    amount = int(random.randrange(1, 20) * 10**18)

    senderETH.sendETH(receiver, {"from": sender, "value" : amount})

    assert receiver.balance() == balance_receiver_before + amount


def test_sender_balance_decrease(senderETH):
    
    sender = accounts[0]
    receiver = accounts[1]

    balance_sender_before = sender.balance()

    balance_receiver_before = receiver.balance()

    amount = int(random.randrange(1, 20) * 10**18)

    senderETH.sendETH(receiver, {"from": sender, "value" : amount})

    assert receiver.balance() == balance_receiver_before + amount
    assert sender.balance() == balance_sender_before - amount