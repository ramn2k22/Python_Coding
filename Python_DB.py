import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="Ram",passwd="Enter_Password", database="Sample") ##Provided that you have Database sample with atleast one Table
mycursor=mydb.cursor()
mycursor.execute("select * from student")
result=mycursor.fetchone()
for i in resul:
    print(i)

for i in mycursor:
    print(i)
mycursor2=mydb.cursor()
mycursor2.execute("select * from Student")
for i in mycursor2:
    print(i)
mycursor3=mydb.cursor()
mycursor3.execute("insert into Student1 values('Ram','VIT'), ('Shyam', 'PIT')")
mycursor3.execute("select * from Student1")
for i in mycursor3:
    print(i)
