# sqlite3
import sqlite3
# Create a connection to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''
          INSERT INTO contact(name, phone, address)
          VALUES('Aung Aung', '1234567890', 'Yangon')
          ''')


conn.commit()#save changes
conn.close()#close connection