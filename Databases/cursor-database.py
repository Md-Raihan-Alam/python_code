import sqlite3
conn = sqlite3.connect('customer.db')
# create a cursor
c = conn.cursor()
print(c)
