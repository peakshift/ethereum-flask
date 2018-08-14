import json
import requests
import unittest
from behave import * 
from utils.block import *
# from utils.transaction import *


testcase = unittest.TestCase('__init__')


@given(u'the AttributeDict')
def step_impl(context):
	context.data = json.loads(context.text)
	print(type(context.data))


@when(u'the AttributeDict is passed to the transformBlock function')
def step_impl(context):
	context.response = transformBlock(context.data)


@then(u'the response data is similar to')
def step_impl(context):
	context.expected = json.loads(context.text)	
	testcase.assertCountEqual(context.response, context.expected)