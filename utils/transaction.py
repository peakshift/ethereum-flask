"""
Interact and read ethereum transactions
"""

def list_transactions(_w3, _address) -> list:
    """
    Searches for the transaction history of an address
    inside all the blocks in the network

    param
    _w3(string): web3 node connection
    _address(string): address for the account whose
    transaction history is being searched for

    return
    txns(list): transaction history of the address given
    """

    blocks = _w3.eth.blockNumber

    txns = []
    for i in range(0, blocks+1):
        block = _w3.eth.getBlock(i, True)
        for txn in block['transactions']:
            if txn['to'] == _address:
                data = transform_transaction(txn)
                del data["to"]
            elif txn['from'] == _address:
                data = transform_transaction(txn)
                del data["from"]
            else:
                continue
            txns.append(data)
    return txns


def transform_transaction(_txn) -> dict:
    """
    Reduces the transaction block to display only
    essentials data

    param
    txn(dict): transaction object

    return
    data(dict): reduced transaction block

    """
    data = {
        "to": _txn["to"],
        "gas": _txn["gas"],
        "from": _txn["from"],
        "value": _txn["value"],
        "gas_price": _txn["gasPrice"],
        "block_number": _txn["blockNumber"]
    }
    return data
