from django.db import connection
cur = connection.cursor()
cur1.execute("SHOW DATABASES")
print(cur1)

 for t in cur1:
    ...:     print(t)
    ...:     

cur1.execute("SELECT * FROM information_schema.tables WHERE table_schema ='rastey';")


 for y in cur1:
    ...:     print(y)


