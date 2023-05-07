import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29')
print(mydb.connection_id)