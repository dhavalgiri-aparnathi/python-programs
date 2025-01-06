import mysql.connector as msc

con = msc.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "my_database",
    autocommit = True
)

db = con.cursor()

query = """
    INSERT INTO my_table
    (username, email, password, phone)
    VALUES
    (%s, %s, %s, %s);
"""

values = [
    ("Govind", "govind@gmail.com", "Govind_123", "+91 999 999 9999"),
    ("Madhav", "madhav@gmail.com", "Madhav_123", "+91 000 000 0000"),
    ("Shyam", "shyam@gmail.com", "Shyam_123", "+91 888 888 8888"),
    ("Kishor", "kishor@gmail.com", "Kishor_123", "+91 777 777 7777")
]

db.executemany(query, values)

con.close()