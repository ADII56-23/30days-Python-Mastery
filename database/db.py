import mysql.connector as myconn

mydb = myconn.connect(
    host="localhost",
    user="root",
    password="aditya0000@"
)

print("Connection successful")

mycode=mydb.cursor()
mycode.execute("show databases")
print(mycode.fetchall())

# for x in mycode:
#     print(x)


#dbx=mydb.cursor()
#dbx.execute("use aditya")
#
#
#print("Tables in aditya database:")
#
## dbc1=mydb.cursor()
## dbc1.execute("create table student (id int primary key, name varchar(20), age int)")
#
#dbc2=mydb.cursor()
#dbc2.execute("insert into student values (1,'Alice',20),(2,'Bob',22),(3,'Charlie',19)")
#
#dbs=mydb.cursor()
#dbs.execute("select * from student")
#
#for x in dbs:
#    print(x)