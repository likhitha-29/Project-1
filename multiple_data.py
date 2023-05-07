import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database ='Inventory_Control_Management')
c=mydb.cursor()
z='insert into Manufacture1(manufacture_id,no_of_items,product,defective_items) values(%s,%s,%s,%s)'
a=[(100,20,'Toy Car',0),(101,15,'wooden chair',3),(102,20,'Toys',2),(103,20,'Shoes',3),(104,50,'perfumes',5),
   (105,30,'Watches',3),(106,45,'wooden table',8)]
c.executemany(z,a)
x='insert into Goods1(goods_id,man_date,product,color,company) values(%s,%s,%s,%s,%s)'
b=[(500,'2023-04-12','wooden table','brown','SS Export'),(501,'2023-04-01','wooden chair','brown','EVOK'),
   (502,'2023-02-14','Toys','Red','Mattel'),(503,'2023-01-01','Toys','Blue','Mattel'),
   (504,'2023-05-14','Watches','RoseGold','Titan'),(505,'2023-01-15','Shoes','Black','Puma'),
   (506,'2023-02-28','perfumes',' ','Bloom'),(507,'2022-11-22','Toy Car','Blue','Mattel')]
c.executemany(x,b)
y='insert into Purchase1(purchase_id,purchase_amount,product,store,purchase_date) values(%s,%s,%s,%s,%s)'
d=[(200,500,'Toys','MyKids','2023-03-14'),(201,2000,'Watches','MyCare','2023-05-01'),
   (202,1000,'perfumes','MyCare','2023-04-03'),(203,5000,'wooden chair','ORay','2023-05-01'),
   (204,2500,'Shoes','MyKids','2023-03-01'),(205,750,'Toy Car','MyKids','2023-03-02'),
   (206,3000,'wooden table','MyCare','2023-03-06')]
c.executemany(y,d)
w='insert into Sale1(sale_date,sale_id,profit_margin,product,store) values(%s,%s,%s,%s,%s)'
e=[('2023-03-06',1000,500,'wooden table','MyCare'),('2023-03-02',1001,300,'Toy Car','MyKids'),
   ('2023-03-01',1002,300,'Shoes','MyKids'),('2023-04-03',1003,700,'perfumes','MyCare'),
   ('2023-05-01',1004,500,'wooden chair','ORay'),('2023-05-01',1005,200,'watches','MyCare'),
   ('2023-03-14',1006,100,'Toys','MyKids')]
c.executemany(w,e)
mydb.commit()
print("Data inserted successfully")