import sqlite3
conn = sqlite3.connect("customer.db")
c = conn.cursor()
c.execute("INSERT INTO customer VALUES ('Alcurd','Shank','alcurd@gmail.com')")
conn.commit()
conn.close()
