import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database="Inventory_Control_Management")
c=mydb.cursor()
x='update Goods1 g,Manufacture1 m set manufacture_id=110,no_of_items=50,m.product="Mobiles",defective_items=4 where m.product="Toys" AND g.product="Toys" AND g.color="Red"'
c.execute(x)
mydb.commit()