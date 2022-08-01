from flask import Flask , render_template
from web3 import Web3
import config


app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))


@app.route("/")
def index():
    return "BLOCKSCAN Etherium"


# Transaction 
@app.route("/txn/<hash>")
def transaction(hash):
    transaction = w3.eth.get_transaction(hash)
    return render_template("transaction.html" , hash = hash , transaction = transaction)


# Address
@app.route("/addr/<address>")
def address(address):
    # address_data = we.eth.ad
    return render_template("address.html" , address = address)


# block
@app.route("/block/<blo>")
def block(blo):
    block = w3.eth.get_block_number(blo)
    return block
    # return render_template("block.html" , blo = blo , block=block)

# default
@app.route("/<x>")
def default(x):
    if x == "addr":
        return "Please specify address"
    elif x == "block":
        return "Please specify block number"
    elif x == "txn":
        return "Please specify transaction hash"
    else:
        return "No such page exits on this site plz check your URL"
