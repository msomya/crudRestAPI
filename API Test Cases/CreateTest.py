#!/usr/bin/python

import requests
import pprint
import json

urlToTest = "http://msomya.pythonanywhere.com/api/production/"
data = {'item':'Electronics IT', 'year':'2014-15', 'data':'280611'}
response = requests.post(urlToTest, data=json.dumps(data))
jsonRes = response.json()
pprint.pprint(jsonRes)
print "HTTP Status Code Returned: ", response.status_code

