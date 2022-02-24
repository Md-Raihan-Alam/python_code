import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
many_customers = [
    ('alcurd', 'shank', 'saiyan@gmail.com'),
    ('Steph', 'Shock', 'step@gmail.com'),
    ('mystogun', 'sukuna', 'mystogum@gmail.com'),
]
# insert multiple values
c.executemany("INSERT INTO customer VALUES(?,?,?)", many_customers)
print("Command execute successfully")
conn.commit()
conn.close()
