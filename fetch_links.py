# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:50:27 2020

@author: Ewelina
"""

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import sys

url = input('Enter a link: ')

response = urllib.request.urlopen(url)
data = response.read()
doc = BeautifulSoup(data, 'html.parser')

links = doc.select('ol > li')

i = 1

for link in links:
    print(i,  link.get_text())
    i +=1