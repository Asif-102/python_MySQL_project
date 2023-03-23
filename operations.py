import pymysql

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database= "bank"
)

def create_account(name, balance):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name, balance))
    conn.commit()
    cursor.close()