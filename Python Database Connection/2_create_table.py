import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "my_database",
    autocommit = True
)

db = con.cursor()

db.execute("""
    CREATE TABLE my_table (
        id INT(11) PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(150) NOT NULL,
        password VARCHAR(150) NOT NULL
    );           
""")

con.close()