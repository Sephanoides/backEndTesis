# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:22:45 2021

@author: Hugo
"""
import random


usuarios = 'usuarios del conjunto de datos'
items = 'ítems del conjunto de datos'

recomendaciones = {}

for u in usuarios:
    recomendaciones[u] = {}
    for i in items:
        recomendaciones[u][i] = random.randrange(1,5)
        
        
