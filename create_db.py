import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29')
print(mydb.connection_id)
c=mydb.cursor()
c.execute('create database Inventory_Control_Management')