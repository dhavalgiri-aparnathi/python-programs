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
    SELECT * FROM my_table;
"""

db.execute(query)

record = db.fetchall()

for row in record:
    print("\n", row)

con.close()