import os
from utils.block import *
from utils.transaction import *
from flask import Flask, jsonify
from web3 import Web3



app = Flask(__name__)
url = os.environ['server']  # blockchain server
w3 = Web3(Web3.HTTPProvider(url))


@app.route("/tx/<transid>", methods=["GET"])
def get_by_id(transid):
	"""
	Searches for a transaction by ID and returns the 
	sender and the reciever details

	param
	transid(string): transaction hash

	return
	data(dict): filtered transaction block
	"""
	try:
		transaction = w3.eth.getTransaction(transid)
		data = transformTransaction(transaction)
		return jsonify({"data": data}), 200
	except:
		return jsonify({"message": "Invalid Transaction Hash."}), 400 


@app.route("/address/<address>", methods=["GET"])
def get_by_address(address):
	"""
	Returns transactions and balance of an address

	param
	address(string): account address

	return
	balance(int): account balance
	transactions(list): list of transformed transaction blocks
	"""
	try:
		if w3.isAddress(address):
			balance = w3.eth.getBalance(address)
			transactions = listTransactions(w3, address)
			return jsonify({"data":{"balance": balance, "transactions": transactions}}), 200
		return jsonify({"message": "Invalid Ethereum Address."}), 400
	except Exception as e:
		return e 


@app.route("/address/<address>/outgoing", methods=["GET"])
def get_outgoing(address):
	"""
	Returns outgoing transactions of an address

	param
	address(string): account address

	return
	transactions(list): list of transformed outgoing transaction blocks
	"""
	outgoing = []
	try:
		if w3.isAddress(address):
			transactions = listTransactions(w3, address)
			for data in transactions:
				if "to" in data:
					outgoing.append(data)
			return jsonify({"data":{"transactions": outgoing}}), 200
		return jsonify({"message": "Invalid Ethereum Address."}), 400
	except Exception as e:
		return e 


@app.route("/address/<address>/incoming", methods=["GET"])
def get_incoming(address):
	"""
	Returns incoming transactions of an address

	param
	address(string): account address

	return
	transactions(list): list of transformed incoming transaction blocks
	"""
	incoming = []
	try:
		if w3.isAddress(address):
			transactions = listTransactions(w3, address)
			for data in transactions:
				if "from" in data:
					incoming.append(data)
			return jsonify({"data":{"transactions": incoming}}), 200
		return jsonify({"message": "Invalid Ethereum Address."}), 400
	except Exception as e:
		return e 


@app.route("/block/<int:height>", methods=["GET"])
def get_block(height) -> dict :
	"""
	Returns details on a requested block

	param
	height(int): block number

	return
	block(dict): dictionar of block details
	"""
	try:	
		block = w3.eth.getBlock(height)
		details = transformBlock(block)
		return jsonify({"data": details}), 200
	except:
		return jsonify({"message": "We seem to be experiencing some difficulties. Please try again."}), 400


if __name__ == "__main__":
	app.run(debug=True,
		threaded=True,
		host='0.0.0.0',
		port=5000)
