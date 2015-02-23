# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 19:18:00 2015

@author: choog_000
"""

from urllib2 import Request, urlopen, URLError, urllib2
import urllib2

import requests, json

url1 = 'https://www.space-track.org/ajaxauth/login'
url2 = 'https://www.space-track.org/basicspacedata/query/class/boxscore/orderby/COUNTRY%20asc/metadata/true'

daAuth = requests.post(url1,auth=('choogerheyde@gmail.com','DXd0Hh38SG4irCn'))
cookie1 = daAuth.cookies

print daAuth
print cookie1

response = urllib2.Request(url2)
response.add_header('cookie',cookie1)
response2 = urllib2.urlopen(response)

print response2
response2.text


response = requests.get(url2, cookies=cookie1)
response.add_header('cookie',cookie1)
response.text

cookie = daAuth.headers.get('Set-Cookie')

print daAuth
print cookie

request = requests.get(url2, cookies=cookie)
print request.txt


request = Request('https://www.space-track.org/basicspacedata/' +
    'query/class/boxscore/orderby/COUNTRY%20asc/metadata/true')

request.add_header('cookie', cookie)
#print request
#
#response = urllib2.urlopen(request)
#
print request.add_header('cookie', cookie)
#print response

    
try:
    response = urlopen(request)
    data = response.read()
    print data
except URLError, e:
    print 'Did not work. Received an error code:', e

------------------------------------------------
import os
os.chdir('C:\Users\choog_000\Documents\GitHub\SpaceSatellitesDashboard')
os.system('wget  --post-data "identity=choogerheyde@gmail.com&password=DXd0Hh38SG4irCn&query=https://www.space-track.org/basicspacedata/query/class/boxscore" --keep-session-cookies --save-cookies=cookies.txt https://www.space-track.org/ajaxauth/login -O boxscore')

os.system("wget http://www.google.com/")



os.system("wget  --post-data "identity=choogerheyde@gmail.com&password=DXd0Hh38SG4irCn&query=https://www.space-track.org/basicspacedata/query/class/boxscore" --keep-session-cookies --save-cookies=cookies.txt https://www.space-track.org/ajaxauth/login -O boxscore")


import requests, json

#url = 'https://www.space-track.org/ajaxauth/login'
#daAuth = requests.post(url,auth=('choogerheyde@gmail.com','DXd0Hh38SG4irCn'))
#
#print daAuth.json

os.system('wget  --post-data "identity=choogerheyde@gmail.com&password=DXd0Hh38SG4irCn" --keep-session-cookies --save-cookies=cookies.txt https://www.space-track.org/ajaxauth/login -olog')
    
