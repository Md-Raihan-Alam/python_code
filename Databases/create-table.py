import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
# create a table
c.execute("""CREATE TABLE customer(
    first_name text,
    last_name text,
    email text
)""")

# Datatypees
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# commit action
conn.commit()

# close our connection
conn.close()
