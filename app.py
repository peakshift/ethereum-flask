"""
Bootstrap flask application
"""

import os
from web3 import Web3
from flask import Flask, jsonify
from utils.block import transform_block
from utils.transaction import list_transactions, transform_transaction

APP = Flask(__name__)
URL = os.environ['server']  # blockchain server
W3 = Web3(Web3.HTTPProvider(URL))


@APP.route("/tx/<transid>", methods=["GET"])
def get_by_id(transid) -> dict:
    """
    Searches for a transaction by ID and returns the
    sender and the reciever details

    param
    transid(string): transaction hash

    return
    data(dict): filtered transaction block
    """
    try:
        transaction = W3.eth.getTransaction(transid)
        data = transform_transaction(transaction)
        return jsonify({"data": data}), 200
    except ValueError:
        return jsonify({"message": "Invalid Transaction Hash."}), 400


@APP.route("/address/<address>", methods=["GET"])
def get_by_address(address) -> dict:
    """
    Returns transactions and balance of an address

    param
    address(string): account address

    return
    balance(int): account balance
    transactions(list): list of transformed transaction blocks
    """
    try:
        if W3.isAddress(address):
            balance = W3.eth.getBalance(address)
            transactions = list_transactions(W3, address)
            return jsonify({"data":{"balance": balance, "transactions": transactions}}), 200
        return jsonify({"message": "Invalid Ethereum Address."}), 400
    except ValueError as error:
        return jsonify({"message": error}), 400


@APP.route("/address/<address>/outgoing", methods=["GET"])
def get_outgoing(address) -> dict:
    """
    Returns outgoing transactions of an address

    param
    address(string): account address

    return
    transactions(list): list of transformed outgoing transaction blocks
    """
    outgoing = []
    try:
        if W3.isAddress(address):
            transactions = list_transactions(W3, address)
            for data in transactions:
                if "to" in data:
                    outgoing.append(data)
            return jsonify({"data":{"transactions": outgoing}}), 200
        return jsonify({"message": "Invalid Ethereum Address."}), 400
    except ValueError as error:
        return jsonify({"message": error}), 400


@APP.route("/address/<address>/incoming", methods=["GET"])
def get_incoming(address) -> dict:
    """
    Returns incoming transactions of an address

    param
    address(string): account address

    return
    transactions(list): list of transformed incoming transaction blocks
    """
    incoming = []
    try:
        if W3.isAddress(address):
            transactions = list_transactions(W3, address)
            for data in transactions:
                if "from" in data:
                    incoming.append(data)
            return jsonify({"data":{"transactions": incoming}}), 200
        return jsonify({"message": "Invalid Ethereum Address."}), 400
    except ValueError as error:
        return jsonify({"message": error}), 400


@APP.route("/block/<int:height>", methods=["GET"])
def get_block(height) -> dict:
    """
    Returns details on a requested block

    param
    height(int): block number

    return
    block(dict): dictionary of block details
    """
    try:
        block = W3.eth.getBlock(height)
        details = transform_block(block)
        return jsonify({"data": details}), 200
    except ValueError:
        return jsonify({"message": "Something went wrong. Please try again."}), 400


if __name__ == "__main__":
    APP.run(debug=True,
            threaded=True,
            host='0.0.0.0',
            port=5000)
