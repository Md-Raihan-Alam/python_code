import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
c.execute('SELECT * FROM customer')
customersData = c.fetchall()
# formating fetch
for customerInfo in customersData:
    print(customerInfo)
    print(customerInfo[0]+" | "+customerInfo[1]+" | "+customerInfo[2])
conn.commit()
conn.close()
