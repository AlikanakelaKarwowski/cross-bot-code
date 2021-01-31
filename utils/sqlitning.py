import sqlite3

db = sqlite3.connect('ban_list.db')
c= db.cursor()
c.execute('''
    CREATE TABLE ban_list(
        entry INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        user_name TEXT NOT NULL,
        reason TEXT,
        date TEXT NOT NULL,
        mod TEXT NOT NULL,
        server TEXT
    )
''')