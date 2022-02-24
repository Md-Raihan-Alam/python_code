import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
# Delete Record
c.execute("""
DELETE FROM customer WHERE rowid=4
""")
conn.commit()
c.execute("SELECT * FROM customer")
customerData = c.fetchall()
for customerInfo in customerData:
    print(customerInfo)
conn.commit()
conn.close()
