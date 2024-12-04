import sqlite3

conn = sqlite3.connect('tasks.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        status INTEGER NOT NULL
    )
''')

conn.commit()
conn.close()
print("Database initialized.")
