Feature: Ethereum Flask
As a ___ 
I want ___
So that ___


Scenario: Transform a transaction block data to python dict
Given the transaction block below
"""
AttributeDict({
	'hash': HexBytes('0x9459c8a1caae335fb5f2018a54ae7db0d8d9a0066b0df495d7778321f40a93e7'), 
	'nonce': 1, 
	'blockHash': HexBytes('0xf475f7209f0c6349d621ce1a2c5589be65990d15987baa7489df41a86eff9828'), 
	'blockNumber': 5, 
	'transactionIndex': 0, 
	'from': '0x4a78bA434908DDd69F55B804f7A79eB4CB4A3831', 
	'to': '0xaA431B5228c0875747f3076185959f004a9699aC', 
	'value': 1234567, 
	'gas': 121000, 
	'gasPrice': 1, 
	'input': '0x0', 
	'v': 27, 
	'r': HexBytes('0x4edcd013e60c2969cdd8cb01fb1ab7356dbd42fb172a3cf4ed1f4567508e7369'), 
	's': HexBytes('0x2ca92ec0cb70be79077891b81025f207f7a25ce651ab35accbd3fed8c7e70041')
})
"""
When the data is passed to transformTransaction
Then the returned data is similar to:
"""
{
	"to": "0xaA431B5228c0875747f3076185959f004a9699aC",
	"from": "0x4a78bA434908DDd69F55B804f7A79eB4CB4A3831",
	"gas": 121000,
	"value": 1234567,
	"gas_price": 1,
	"block_number": 5
}
"""

