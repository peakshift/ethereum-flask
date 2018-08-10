import os
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
			print(balance)
			transactions = listTransactions(address)
			print(transactions)
			return jsonify({"data":{"balance": balance, "transactions": transactions}}), 200
		return jsonify({"message": "Invalid Ethereum Address."}), 400
	except Exception as e:
		return e 


if __name__ == "__main__":
	app.run(debug=True,
		threaded=True,
		host='0.0.0.0',
		port=5000)
