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

lists = doc.find_all('ol')
for list in lists:
   i = 1
   list_items = list.find_all('li')
   for y in list_items:
       print(i, y.get_text()) 
       i += 1
