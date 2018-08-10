import os
from web3 import Web3


url = os.environ['server']  # blockchain server
w3 = Web3(Web3.HTTPProvider(url))


def listTransactions(address):
	"""
	Searches for the transaction history of an address
	inside all the blocks in the network

	param
	address(string): address for the account whose
	transaction history is being searched for

	return
	txns(list): transaction history of the address given
	"""

	blocks = w3.eth.blockNumber

	txns = []
	for i in range(0,blocks+1):
		block = w3.eth.getBlock(i, True)
		for txn in block['transactions']:
			if txn['to'] == address:
				data = transformTransaction(txn)
				del data["to"]
			elif txn['from'] == address:
				data = transformTransaction(txn)
				del data["from"]
			else:
				continue
			txns.append(data)
	return txns



def transformTransaction(txn):
	"""
	Reduces the transaction block to display only
	essentials data

	param
	txn(dict): transaction object

	return
	data(dict): reduced transaction block

	"""
	data = {
		"to": txn["to"],
		"gas": txn["gas"], 
		"from": txn["from"],
		"value": txn["value"],
		"gas_price": txn["gasPrice"], 
		"block_number": txn["blockNumber"]
	}
	return data



def blockTransform(block):
	"""
	Transforms the block data

	param
	block(dict): block details

	return
	data(dict): transformed block

	"""
	data = {
		"number": block["number"],
	    "hash": w3.toHex(block["hash"]),
	    "parentHash": w3.toHex(block["parentHash"]),
	    "mixHash": w3.toHex(block["mixHash"]),
	    "nonce": w3.toHex(block["nonce"]),
	    "sha3Uncles": w3.toHex(block["sha3Uncles"]),
	    "logsBloom": w3.toHex(block["logsBloom"]),
	    "transactionsRoot": w3.toHex(block["transactionsRoot"]),
	    "stateRoot": w3.toHex(block["stateRoot"]),
	    "receiptsRoot": w3.toHex(block["receiptsRoot"]),
	    "miner": block["miner"],
	    "difficulty": block["difficulty"],
	    "totalDifficulty": block["totalDifficulty"],
	    "extraData": w3.toHex(block["extraData"]),
	    "size": block["size"],
	    "gasLimit": block["gasLimit"],
	    "gasUsed": block["gasUsed"],
	    "timestamp": block["timestamp"],
	    "uncles": block["uncles"]
	}
	txns = []
	for txn in block["transactions"]:
		txns.append(w3.toHex(txn))

	data["transactions"] = txns
	return data