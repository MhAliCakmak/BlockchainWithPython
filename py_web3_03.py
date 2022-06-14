from dotenv import load_dotenv #pip install python-dotenv
from web3 import Web3 #pip install web3
import os
import json


#if you have spesific information like node_provider ,you should create a .env file than you write your environment variable.

load_dotenv()
node_provider=os.environ["NODE_PROVIDER"]
web3_connection=Web3(Web3.HTTPProvider(node_provider))

global_gas=4500000
global_gas_price=web3_connection.toWei(8,"gwei")
#Are we connect ?
def are_connect():
    return web3_connection.isConnected()

def get_nonce(address):
    return web3_connection.eth.get_transaction_count(address)

def eth_transfer(sender,receiver,signature,amount_eth):
    transcation_body={
        'nonce':get_nonce(sender),
        "to":receiver,
        'value':web3_connection.toWei(amount_eth,'ether'),
        "gas":global_gas,
        "gasPrice":global_gas_price}
      
    

    
    signed_transaction=web3_connection.eth.account.sign_transaction(transcation_body,signature)
    result=web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result


print(eth_transfer(os.environ["ADDRESS_1"],os.environ["ADDRESS_2"],os.environ["PRIVATE_KEY_1"],2))