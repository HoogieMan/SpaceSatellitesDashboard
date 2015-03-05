# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 19:18:00 2015

@author: choog_000
"""
#Dashboard about Earth's satellites
#Boxscore data: Accounting of man-made objects that have been or are in orbit. 
#Derived from satellite catalog and grouped by country/organization.

import os, json
os.chdir('C:\Users\choog_000\Documents\GitHub\SpaceSatellitesDashboard')

#make API request to Space-Track.org and store the results in a file
os.system('wget  --post-data "identity=choogerheyde@gmail.com&password=DXd0Hh38SG4irCn&query=https://www.space-track.org/basicspacedata/query/class/boxscore/format/csv" --keep-session-cookies --save-cookies=cookies.txt https://www.space-track.org/ajaxauth/login -O boxscore')

#read in the generated file for parsing
daFile = open('boxscore', 'r')
print daFile.read()

data = json.load(daFile)
daFile.close()

print json.daFile

csvFile = csv.writer(open('boxscore.csv','wb+'))

for item in data:
    csvFile.writerow([item['pk'],item['mode']] + item['fields'].values())


----------------------------------------------
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