import sqlite3

guild_db = sqlite3.connect('guild.db')
guild_c= guild_db.cursor()
guild_c.execute('''
    CREATE TABLE IF NOT EXISTS guild(
        bot_id INTEGER PRIMARY KEY AUTOINCREMENT,
        guild_id TEXT NOT NULL,
        prefix CHARACTER(1) NOT NULL,
        ban_perm TEXT NOT NULL,
        clown_id TEXT,
        uwu_flag INT 
    )
''')