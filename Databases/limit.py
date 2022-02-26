import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
# limit searching query
# LIMIT must be writted at last
c.execute('SELECT rowid,* FROM customer ORDER BY rowid DESC LIMIT 2')
customerData = c.fetchall()
for customerInfo in customerData:
    print(customerInfo)
conn.commit()
conn.close()
