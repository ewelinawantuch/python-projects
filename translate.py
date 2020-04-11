# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:42:41 2020

@author: Ewelina
"""


from googletrans import Translator

def main():
    translator = Translator()
    result = translator.translate("Jak się masz?", dest='de')
    print(result.text)
    
main()