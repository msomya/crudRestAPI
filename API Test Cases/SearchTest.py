#!/usr/bin/python

import requests
import pprint
import json

urlToTest = "http://msomya.pythonanywhere.com/api/production/search/?"

#Test case when both the parameters are given
data = "item=Electronics IT&&year=2014-15"
response = requests.get(urlToTest+data)
jsonRes = response.json()
pprint.pprint(jsonRes)
print "HTTP Status Code Returned: ", response.status_code

#Test case when only year is given 
data = {'year':'2014-15'}
data = "year=2014-15"
response = requests.get(urlToTest+data)
jsonRes = response.json()
pprint.pprint(jsonRes)
print "HTTP Status Code Returned: ", response.status_code

#Test case when only item is given 
data = "item=Electronics IT"
response = requests.get(urlToTest+data)
jsonRes = response.json()
pprint.pprint(jsonRes)
print "HTTP Status Code Returned: ", response.status_code
