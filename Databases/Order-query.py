import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
# Order query ->Ascending=ASC
conn.commit()
c.execute("SELECT rowid,* FROM customer ORDER BY rowid")
customerData = c.fetchall()
for customerInfo in customerData:
    print(customerInfo)
# Dsecending
c.execute("SELECT rowid,* FROM customer ORDER BY rowid DESC")
customerData = c.fetchall()
for customerInfo in customerData:
    print(customerInfo)
# Alphabetic
c.execute("SELECT rowid,* FROM customer ORDER BY last_name")
customerData = c.fetchall()
for customerInfo in customerData:
    print(customerInfo)
# Alphabetic Dsecending
c.execute("SELECT rowid,* FROM customer ORDER BY last_name DESC")
customerData = c.fetchall()
for customerInfo in customerData:
    print(customerInfo)
conn.commit()
conn.close()
