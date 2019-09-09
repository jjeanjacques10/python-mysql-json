# -*- coding: utf-8 -*-

import mysql.connector
import json

mydb = mysql.connector.connect(
  host="",
  user="",
  passwd="",
  database="",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

with open('convertcsv.json') as f:    
    data = json.load(f)

sql = "INSERT INTO `wp_it_trends`.`automacao` (`Posto`,`Probabilidade`,`CBO2002`,`Ocupacao`) VALUES (%s, %s, %s, %s)"

for i in data:
    val = (i["Posto"], i["Probabilidade"], i["CBO 2002"], i[u"Ocupação"])
    mycursor.execute(sql, val)
    mydb.commit()
print(mycursor.rowcount, " record inserted.")