from web3 import Web3


def listTransactions(w3, address):
	"""
	Searches for the transaction history of an address
	inside all the blocks in the network

	param
	w3(string): web3 node connection
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
			print(type(txn))
			if txn['to'] == address or  txn['from'] == address:
				txns.append(transformTransaction(txn))
	return txns



def transformTransaction(txn):
	"""
	Reduces the transaction block to display only
	essentials data

	param
	txn(string): account address

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



