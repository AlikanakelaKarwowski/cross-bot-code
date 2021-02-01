import sqlite3

db = sqlite3.connect('ban_list.db')
c= db.cursor()
c.execute('''
    CREATE TABLE ban_list(
        entry INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        user_name TEXT,
        reason TEXT,
        date TEXT,
        mod TEXT,
        server TEXT
    )
''')