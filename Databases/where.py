import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
# c.execute('SELECT * FROM customer WHERE last_name="Alam"')
# c.execute('SELECT * FROM customer WHERE rowid>=4')
# % here is importatn;note it
c.execute('SELECT * FROM customer WHERE last_name LIKE "sh%"')
print(c.fetchall())
conn.commit()
conn.close()
