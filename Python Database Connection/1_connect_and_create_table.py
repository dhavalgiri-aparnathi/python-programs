import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    autocommit = True
)

db = con.cursor()
db.execute("""
    CREATE DATABASE IF NOT EXISTS my_database;           
""")

con.close()