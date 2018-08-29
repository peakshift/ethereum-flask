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
        "parent_hash": Web3.toHex(block["parentHash"]),
        "mix_hash": Web3.toHex(block["mixHash"]),
        "nonce": Web3.toHex(block["nonce"]),
        "sha3_uncles": Web3.toHex(block["sha3Uncles"]),
        "logs_bloom": Web3.toHex(block["logsBloom"]),
        "transactions_root": Web3.toHex(block["transactionsRoot"]),
        "state_root": Web3.toHex(block["stateRoot"]),
        "receipts_root": Web3.toHex(block["receiptsRoot"]),
        "miner": block["miner"],
        "difficulty": block["difficulty"],
        "total_difficulty": block["totalDifficulty"],
        "extra_data": Web3.toHex(block["extraData"]),
        "size": block["size"],
        "gas_limit": block["gasLimit"],
        "gas_used": block["gasUsed"],
        "timestamp": block["timestamp"],
        "uncles": block["uncles"]
    }
    txns = []
    for txn in block["transactions"]:
        txns.append(Web3.toHex(txn))

    data["transactions"] = txns
    return data
