# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:44:44 2018

@author: TZLMYQ
"""

import urllib2

# Request source file
url = 'http://yue.ifeng.com'
request = urllib2.Request(url)      # Write a letter
response = urllib2.urlopen(request)
page = response.read()

# Save source file
webFile = open('webPage.html', 'wb')
webFile.write(page)
webFile.close()

