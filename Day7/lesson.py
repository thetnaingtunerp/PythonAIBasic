# pip install flask
import sqlite3
from flask import Flask, render_template,request,redirect

app = Flask(__name__)

conn = sqlite3.connect('mydb.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS contacts
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 phone TEXT,
                 address TEXT
                 )
            """)



@app.route('/home')
def homepage():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    items = c.execute("SELECT * FROM contacts")
    rows = items.fetchall()

    # conn.close()
    print(rows)
    return render_template('home.html', item=rows)

@app.route('/save', methods=('GET','POST'))
def savedata():
    name = request.args.get('cname')
    phone = request.args.get('phone')
    address = request.args.get('address')
    
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, phone, address) VALUES (?, ?, ?)",
          (name, phone, address))
    conn.commit()
    conn.close() 
    return redirect('/home')

@app.route('/delete/<int:id>', methods=('GET','POST'))
def delete_data(id):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/home')

@app.route('/edit/<int:id>', methods=('GET','POST'))
def edit_data(id):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    items = c.execute("SELECT * FROM contacts WHERE id =?",(id,))
    rows = items.fetchone()
    return render_template('page2.html', data = rows)
    
@app.route('/update/<int:id>', methods=('GET','POST'))
def updat_data(id):
    name = request.args.get('cname')
    phone = request.args.get('phone')
    address = request.args.get('address')
    
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    items = c.execute("UPDATE contacts SET name=?, phone=?, address=? WHERE id= ?",(name,phone,address,id))
    conn.commit()
    conn.close()
    
    return redirect('/home')
    


conn.commit()
conn.close()

if __name__ == '__main__':
    app.run()