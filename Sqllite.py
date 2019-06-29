import sqlite3
import psycopg2

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Store (item TEXT UNIQUE, quantity INTEGER)")
    conn.commit()
    conn.close()

def insert(item,quantity):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Store VALUES (?,?)", (item, quantity))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(item,quantity):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE Store SET quantity=? WHERE item=?",(quantity,item))
    conn.commit()
    conn.close()


update("Wine", 12)
print(view())