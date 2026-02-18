import sqlite3
import datetime as dt


db = sqlite3.connect('todo.db')

cr = db.cursor()

cr.execute(''' CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL,
    priority TEXT NOT NULL,
    Tags TEXT NOT NULL,
    CREATED_AT TEXT NOT NULL)''')


cr.execute("SELECT * FROM todo")
print(cr.fetchall())