import json
import unittest
from behave import * 
from utils.transaction import *


testcase = unittest.TestCase('__init__')


@given(u'the transaction block data similar to')
def step_impl(context):
	context.data = json.loads(context.text)


@when(u'the data is passed to transformTransaction')
def step_impl(context):
	context.response = transformTransaction(context.data)


@then(u'the returned data is similar to')
def step_impl(context):
	context.expected = json.loads(context.text)	
	testcase.assertCountEqual(context.response, context.expected)



