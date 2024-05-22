import pymysql



def db_connect():
    db = pymysql.connect(host="db-crypto.c9wekkiy8fip.us-east-2.rds.amazonaws.com", 
                        user = "admin", password="Addi8881212")
    cursor = db.cursor()
    return cursor, db


# a,b = db_connect()
# a.execute('''USE CRYPTO''')
# print(a.execute('''SELECT COUNT(*) FROM BITCOIN'''))
# print(a.execute('''SELECT * FROM BITCOIN'''))

# rows = a.fetchall()

# # Print each row
# for row in rows:
#     print(row)

