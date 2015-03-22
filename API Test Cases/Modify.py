#!/usr/bin/python

import requests
import pprint
import json

urlToTest = "http://msomya.pythonanywhere.com/api/production/search/"
data = {'item':'Electronics IIT', 'year':'2015-16', 'data':'288'}
response = requests.put(urlToTest, data=json.dumps(data))
#jsonRes = response.json()
#pprint.pprint(jsonRes)
print "HTTP Status Code Returned: ", response.status_code

