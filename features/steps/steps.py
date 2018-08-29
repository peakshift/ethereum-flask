import json
import unittest
from web3 import Web3
from behave import * 
from utils.block import *
from utils.transaction import *


testcase = unittest.TestCase('__init__')

@given(u'a dictionary')
def step_impl(context):
    context.data = {}


@given(u'property "{property}" HexBytes is "{value}"')
def step_impl(context, property, value):
    context.data[property] = Web3.toBytes(hexstr=value)


@given(u'property "{property}" int is "{value}"')
def step_impl(context, property, value):
    context.data[property] = int(value)


@given(u'property "{property}" string is "{value}"')
def step_impl(context, property, value):
    context.data[property] = str(value)


@given(u'property "{property}" array is empty')
def step_impl(context, property):
    context.data[property] = []


@given(u'property "{property}" array contains')
def step_impl(context, property):
    context.data[property] = []
    for row in context.table:
        context.data[property] = Web3.toBytes(hexstr=row['hash'])


@when(u'the data is passed to the transformBlock function')
def step_impl(context):
    context.response = transformBlock(context.data)


@given(u'the transaction block data similar to')
def step_impl(context):
    context.data = json.loads(context.text)


@when(u'the data is passed to the transformTransaction function')
def step_impl(context):
    context.response = transformTransaction(context.data)


@then(u'the returned data is similar to')
def step_impl(context):
    context.expected = json.loads(context.text)
    testcase.assertCountEqual(context.response, context.expected)




