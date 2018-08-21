from web3 import Web3


def transformBlock(block) -> dict:
	"""
	Transforms the block data

	param
	block(dict): block details

	return
	data(dict): transformed block

	"""
	data = {
		"number": block["number"],
		"hash": Web3.toHex(block["hash"]),
		"parentHash": Web3.toHex(block["parentHash"]),
		"mixHash": Web3.toHex(block["mixHash"]),
		"nonce": Web3.toHex(block["nonce"]),
		"sha3Uncles": Web3.toHex(block["sha3Uncles"]),
		"logsBloom": Web3.toHex(block["logsBloom"]),
		"transactionsRoot": Web3.toHex(block["transactionsRoot"]),
		"stateRoot": Web3.toHex(block["stateRoot"]),
		"receiptsRoot": Web3.toHex(block["receiptsRoot"]),
		"miner": block["miner"],
		"difficulty": block["difficulty"],
		"totalDifficulty": block["totalDifficulty"],
		"extraData": Web3.toHex(block["extraData"]),
		"size": block["size"],
		"gasLimit": block["gasLimit"],
		"gasUsed": block["gasUsed"],
		"timestamp": block["timestamp"],
		"uncles": block["uncles"]
	}
	txns = []
	for txn in block["transactions"]:
		txns.append(Web3.toHex(txn))

	data["transactions"] = txns
	return data