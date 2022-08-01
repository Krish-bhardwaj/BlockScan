import config

from web3 import Web3

w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))

t1w3 = Web3(Web3.HTTPProvider(config.INFURA_RINKEBY_URL))

t2w3 = Web3(Web3.HTTPProvider(config.INFURA_ROPSTEN_URL))

t3w3 = Web3(Web3.HTTPProvider(config.INFURA_KOVAN_URL))

t4w3 = Web3(Web3.HTTPProvider(config.INFURA_GORLI_URL))

print(w3.eth.block_number)
print(f"Mainnet : {w3.eth.block_number}")
print(f"Rinkeby : {t1w3.eth.block_number}")
print(f"Ropsten : {t2w3.eth.block_number}")
print(f"Kovan   : {t3w3.eth.block_number}")
print(f"Gorli   : {t4w3.eth.block_number}")

# print(w3.eth.get_block('latest'))

wallet_address = ["0x4f401e3Cd7bF9293bEA676b4431352Caa876Dfda" , 
                  "0xEA1A4Fe1f376267D4Ed7C88D47891Bb1891e12B8" ,
                  "0xC24fF1aa6838dfbbaB70a25E08D59c73bA3294c9" ,
                  "0xa8094A6fAd4CA3f86D8b0Ae311b551E5b8fa7c3F" ,
                  "0x81b8A8098C06aA146D93eB9ad31910a234c47C8C" ,
                  "0x85Ca9191caCee9F41A816b65095a7728a6AbaeA6" ]

for i in wallet_address:
    balance_mainnet = w3.eth.get_balance(i)

    balance_testnet_rinkeby = t1w3.eth.get_balance(i)
    balance_testnet_ropsten = t2w3.eth.get_balance(i)
    balance_testnet_kovan = t3w3.eth.get_balance(i)
    balance_testnet_gorli = t4w3.eth.get_balance(i)

    
    balance_mainnet_in_eth = w3.fromWei(balance_mainnet, 'ether')

    balance_testnet_1_in_eth = w3.fromWei(balance_testnet_rinkeby, 'ether')
    balance_testnet_2_in_eth = w3.fromWei(balance_testnet_ropsten, 'ether')
    balance_testnet_3_in_eth = w3.fromWei(balance_testnet_kovan, 'ether')
    balance_testnet_4_in_eth = w3.fromWei(balance_testnet_gorli, 'ether')
    
    print(f"Wallet : {i}")
    
    print(f"Mainnet : {balance_mainnet_in_eth}")
    
    print(f"Rinkeby : {balance_testnet_1_in_eth}")
    print(f"Ropsten : {balance_testnet_2_in_eth}")
    print(f"Kovan   : {balance_testnet_3_in_eth}")
    print(f"Gorli   : {balance_testnet_4_in_eth}")
