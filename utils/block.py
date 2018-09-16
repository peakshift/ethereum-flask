"""
Interact and read ethereum blocks
"""

from web3 import Web3


def transform_block(_block) -> dict:
    """
    Transforms the block data

    param
    block(dict): block details

    return
    data(dict): transformed block

    """
    data = {
        "number": _block["number"],
        "hash": Web3.toHex(_block["hash"]),
        "parent_hash": Web3.toHex(_block["parentHash"]),
        "mix_hash": Web3.toHex(_block["mixHash"]),
        "nonce": Web3.toHex(_block["nonce"]),
        "sha3_uncles": Web3.toHex(_block["sha3Uncles"]),
        "logs_bloom": Web3.toHex(_block["logsBloom"]),
        "transactions_root": Web3.toHex(_block["transactionsRoot"]),
        "state_root": Web3.toHex(_block["stateRoot"]),
        "receipts_root": Web3.toHex(_block["receiptsRoot"]),
        "miner": _block["miner"],
        "difficulty": _block["difficulty"],
        "total_difficulty": _block["totalDifficulty"],
        "extra_data": Web3.toHex(_block["extraData"]),
        "size": _block["size"],
        "gas_limit": _block["gasLimit"],
        "gas_used": _block["gasUsed"],
        "timestamp": _block["timestamp"],
        "uncles": _block["uncles"]
    }
    txns = []
    for txn in _block["transactions"]:
        txns.append(Web3.toHex(txn))

    data["transactions"] = txns
    return data
