 import pymysql
db_connection=pymysql.connect(
    host="localhost",
    user="root",
    passwd="yokesh",
    database="db"
)
my_database=db_connection.cursor()
print("connected successfully")
##insert
sql_statement='INSERT INTO student(username,password)value(%s,%s)'
values=("yokesh","375684758")
my_database.execute(sql_statement,values)
db_connection.commit()

##Read
sql_statement="SELECT*FROM student"
my_database.execute(sql_statement)
output=my_database.fetchall()
for x in output:
    print(x)
    
####update
sql_statement="UPDATE student SET password='1111' where username ='java'"
my_database.execute(sql_statement)
db_connection.commit()

####Delete
sql_query="DELETE FROM student where username='python'"
my_database.execute(sql_query)
db_connection.commit()
print("row(s)deleted successfully")

