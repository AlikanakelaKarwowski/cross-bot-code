import sqlite3
import pandas as pd

conn = sqlite3.connect(r'/cross-bot-code/ban_list.db')

ban_data = pd.read_csv('/cross-bot-code/banned_users.txt')
ban_data.to_sql('banned', conn, if_exists='replace', index=False)

cur = conn.cursor()
for row in cur.execute('SELECT * FROM banned'):
    print(row)

conn.close()
