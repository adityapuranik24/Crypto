import pymysql



db = pymysql.connect(host="market-db.c9wekkiy8fip.us-east-2.rds.amazonaws.com", 
                     user = "admin", password="Addi8881212")

cursor = db.cursor()
print(cursor.execute("select version()"))