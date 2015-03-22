#!/usr/bin/python

import requests
import pprint

urlToTest = "http://msomya.pythonanywhere.com/api/production/"
response = requests.get(urlToTest)
jsonRes = response.json()
pprint.pprint(jsonRes)
print "HTTP Status Code Returned: ", response.status_code

