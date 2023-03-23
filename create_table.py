import pymysql

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database= "bank"
)

mycursor = conn.cursor()

sql_command =   """
                    CREATE TABLE accounts (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(100) NOT NULL,
                        balance DECIMAL(10, 2) NOT NULL
                    );
                """

mycursor.execute(sql_command)