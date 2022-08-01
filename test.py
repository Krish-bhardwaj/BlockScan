import config

from web3 import Web3

w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))

print(f"Mainnet : {w3.eth.block_number}")
# print(w3.eth.get_block('latest'))

wallet = "0x4f401e3Cd7bF9293bEA676b4431352Caa876Dfda"

balance_mainnet = w3.eth.get_balance(wallet)

balance_mainnet_in_eth = w3.fromWei(balance_mainnet, 'ether')

print(f"Balance : {balance_mainnet_in_eth}")

transaction = w3.eth.get_transaction("0x3fe548cc523418a1d0f89934f1b753858082198c47c228b5c6765a0e120a558c")

print(transaction)