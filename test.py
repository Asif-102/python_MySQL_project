import pymysql

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

print(conn)