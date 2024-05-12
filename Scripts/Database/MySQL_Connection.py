import pymysql



def db_connect():
    db = pymysql.connect(host="db-crypto.c1k48kaimex4.us-east-1.rds.amazonaws.com", 
                        user = "aditya", password="Addi8881212")
    cursor = db.cursor()
    return cursor


