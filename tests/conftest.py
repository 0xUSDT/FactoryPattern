import pytest
from brownie import accounts


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass





@pytest.fixture(scope="module")
def senderETH(SenderFactory, accounts):
    deployer = accounts[0]
    factory = SenderFactory.deploy({"from": deployer})
    
    return factory

@pytest.fixture(scope="module")
def empty_contract(EmptyContract, accounts):
    deployer = accounts[0]
    empty_contract = EmptyContract.deploy({"from": deployer})
    
    return empty_contract


