#!/usr/bin/python

import requests
import pprint
import json

urlToTest = "http://msomya.pythonanywhere.com/api/production/search/?"

#Test case when both the parameters are given
data = "item=Consumer Electronics&&year=2007-08"
response = requests.delete(urlToTest+data)
print "HTTP Status Code Returned: ", response.status_code

