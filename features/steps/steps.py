from web3 import Web3
import json
import unittest
from behave import * 
from utils.transaction import *
from web3.utils.datastructures import AttributeDict


testcase = unittest.TestCase('__init__')


@given(u'the transaction block below')
def step_impl(context):
	context.data = AttributeDict(context.text)
	print(type(context.data))


@when(u'the data is passed to transformTransaction')
def step_impl(context):
	context.response = transformTransaction(context.data)


@then(u'the returned data is similar to')
def step_impl(context):
	context.expected = json.loads(context.text)	
	testcase.assertCountEqual(context.response, context.expected)



