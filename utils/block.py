import os
from web3 import Web3


url = os.environ['server']  # blockchain server
w3 = Web3(Web3.HTTPProvider(url))


def blockTransform(block) -> dict:
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