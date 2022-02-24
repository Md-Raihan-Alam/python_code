import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
# Query the database and Fetch
c.execute('SELECT * FROM customer')
print("\nFetching One...\n")
# fetching
print(c.fetchone())
print("\nFetching 2 data...\n")
# fetching
print(c.fetchmany(2))
print("\nFetching all....\n")
# fetching
print(c.fetchall())
conn.commit()
conn.close()
