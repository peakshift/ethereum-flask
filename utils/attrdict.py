from web3 import Web3


def transformDict(block) -> dict:
	"""
	Transforms a dict of block data with hexstrings to 
	a dict with its byte equivalent

	param
	block(dict): block data with hexstrings

	return
	data(dict): data with byte strings

	"""
	data = {
		"number": block["number"],
		"hash": Web3.toBytes(hexstr=block["hash"]),
		"parentHash": Web3.toBytes(hexstr=block["parentHash"]),
		"mixHash": Web3.toBytes(hexstr=block["mixHash"]),
		"nonce": Web3.toBytes(hexstr=block["nonce"]),
		"sha3Uncles": Web3.toBytes(hexstr=block["sha3Uncles"]),
		"logsBloom": Web3.toBytes(hexstr=block["logsBloom"]),
		"transactionsRoot": Web3.toBytes(hexstr=block["transactionsRoot"]),
		"stateRoot": Web3.toBytes(hexstr=block["stateRoot"]),
		"receiptsRoot": Web3.toBytes(hexstr=block["receiptsRoot"]),
		"miner": block["miner"],
		"difficulty": block["difficulty"],
		"totalDifficulty": block["totalDifficulty"],
		"extraData": Web3.toBytes(hexstr=block["extraData"]),
		"size": block["size"],
		"gasLimit": block["gasLimit"],
		"gasUsed": block["gasUsed"],
		"timestamp": block["timestamp"],
		"uncles": block["uncles"]
	}
	txns = []
	for txn in block["transactions"]:
		txns.append(Web3.toBytes(hexstr=txn))

	data["transactions"] = txns
	return data