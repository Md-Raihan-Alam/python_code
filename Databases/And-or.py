import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
# AND OR -LOGICAL
c.execute('SELECT * FROM customer WHERE last_name LIKE "sukuna%" AND rowid=5')
print(c.fetchall())
print("....")
c.execute('SELECT * FROM customer WHERE last_name LIKE "sukuna%" OR rowid=1')
print(c.fetchall())
conn.commit()
conn.close()
