import json
import requests
import unittest
from behave import * 
from utils.block import *
# from utils.transaction import *


url = "http://localhost:5000"
testcase = unittest.TestCase('__init__')

@when(u'a "GET" request is made to "{resource}"')
def step_impl(context, resource):
	context.response = requests.get(url + resource)


@then(u'the response status is "{code}"')
def step_impl(context, code):
	context.status_code = int(code)


@then(u'the response content type is "{value}"')
def step_impl(context, value):
	assert (context.response.headers["Content-Type"] == value)


@then(u'the response data is similar to')
def step_impl(context):
	context.expected = json.loads(context.text)
	context.results = transformBlock(context.response)
	testcase.assertCountEqual(context.results, context.expected)