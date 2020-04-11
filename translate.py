# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:42:41 2020

@author: Ewelina
"""


from googletrans import Translator
import requests

def googletrans():
    translator = Translator()
    result = translator.translate("Jak się masz?", dest='de')
    print(result.text)
    
def piratetrans(text):
    url = 'https://api.funtranslations.com/translate/pirate.json'
    data = {'text': text}
    
    response = requests.post(url, data=data)
    print(type(response.text))
    
piratetrans('Hello,  sir')
