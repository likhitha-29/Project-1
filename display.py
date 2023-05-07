import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database="Inventory_Control_Management")
c=mydb.cursor()
f="select no_of_items from Manufacture1 m join Goods1 g on g.product=m.product where m.product='wooden chair' and g.man_date='2023-04-01'"
c.execute(f)
dis=c.fetchall()
for x in dis:
    print(x)