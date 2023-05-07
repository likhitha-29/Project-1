import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database="Inventory_Control_Management")
c=mydb.cursor()
manufacture= '''CREATE TABLE Manufacture1(
manufacture_id integer(4) primary key,
no_of_items integer(4),
product varchar(20) not null,
defective_items integer(4)
)'''
goods='''CREATE TABLE Goods1(
goods_id integer(4) primary key not null,
man_date date,
product varchar(20),
color varchar(30),
company varchar(30)
)'''
purchases='''CREATE TABLE Purchase1(
purchase_id integer(4) primary key,
purchase_amount integer(8),
product varchar(20),
store varchar(20),
purchase_date date
)'''
sales='''CREATE TABLE Sale1(
sale_date date,
sale_id integer(4),
profit_margin integer(4),
product varchar(20),
store varchar(20)
)'''
c.execute(manufacture)
c.execute(goods)
c.execute(purchases)
c.execute(sales)