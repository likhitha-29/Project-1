import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database="Inventory_Control_Management")
c=mydb.cursor()
f='select profit_margin from Sale1 s join Goods1 g on s.product=g.product where s.product="wooden table" AND store="MyCare" And company="SS Export"'
c.execute(f)
dis=c.fetchall()
for x in dis:
    print(x)