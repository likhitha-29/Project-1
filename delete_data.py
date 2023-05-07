import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database="Inventory_Control_Management")
c=mydb.cursor()
f='delete from Manufacture1 where defective_items>=1'
c.execute(f)
mydb.commit()