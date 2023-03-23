import pymysql

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

mycursor = conn.cursor()

sql_command =   """
                    CREATE DATABASE bank;
                """
mycursor.execute(sql_command)