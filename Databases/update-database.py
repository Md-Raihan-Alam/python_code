import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
# Update Records
# c.execute("""
# UPDATE customer SET last_name="Shane"
# WHERE first_name="Steph"
# """)
c.execute("""
UPDATE customer SET last_name="Shane"
WHERE rowid=4
""")
conn.commit()
c.execute("SELECT * FROM customer")
customerData = c.fetchall()
for customerInfo in customerData:
    print(customerInfo)
conn.commit()
conn.close()
