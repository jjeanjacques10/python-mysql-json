# -*- coding: utf-8 -*-
import json

with open('convertcsv.json') as f:    
    data = json.load(f)

for i in data:
    print("-------------------------------------")
    print(i["Posto"])
    print(i["Probabilidade"])
    print(i[u"Ocupação"])
    print(i["CBO 2002"])