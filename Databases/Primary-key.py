import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
c.execute('SELECT rowid,* FROM customer')  # simple row id
customerData = c.fetchall()
for customerInfo in customerData:
    print(customerInfo)
conn.commit()
conn.close()
