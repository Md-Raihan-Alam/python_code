import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
# delete the whole table
c.execute('DROM TABLE customer')
conn.commit()
conn.close()
