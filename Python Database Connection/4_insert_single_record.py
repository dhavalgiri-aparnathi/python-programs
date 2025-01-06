import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "my_database",
    autocommit = True
)

db = con.cursor()

username = input("\nEnter username: ")
email = input("\nEnter email: ")
password = input("\nEnter password: ")
phone = input("\nEnter phone: ")

query = """
    INSERT INTO my_table
    (username, email, password, phone)
    VALUES
    (%s, %s, %s, %s);
"""

values = (username, email, password, phone)

db.execute(query, values)

print("\nData Inserted !!!")

con.close()