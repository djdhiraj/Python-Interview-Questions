from django.db import connection
cur = connection.cursor()
cur1.execute("SHOW DATABASES")
print(cur1)

 for t in cur1:
    ...:     print(t)
    ...:     
cur1.execute("SELECT COUNT(*) from information_schema.tables where table_schema = 'rastey'")
cur1.execute("SELECT * FROM information_schema.tables WHERE table_schema ='rastey';")

myresult = cur1.fetchall()
# commit after create, update, and delete tables in database
mydb.commit()
 for y in cur1:
    ...:     print(y)













