from web3 import Web3 #pip install web3
import os
from dotenv import load_dotenv #pip install python-dotenv

load_dotenv()
node_provider=os.environ["NODE_PROVIDER"]

web3_connection=Web3(Web3.HTTPProvider(node_provider))
#are we connect ?
def are_connect():
    print(web3_connection.isConnected())


#this function is show us what is last block
def last_block():
    print(web3_connection.eth.block_number)

#balance function how much eth in our balance
def balance(ETH):
    balance=web3_connection.eth.get_balance(ETH)
    balance_eth=web3_connection.eth.fromWei(balance,"ether")
    print(balance_eth)

