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
    ALTER TABLE my_table ADD COLUMN phone VARCHAR(30) NOT NULL;          
""")

con.close()