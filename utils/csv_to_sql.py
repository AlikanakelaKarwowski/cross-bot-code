import sqlite3
import csv

conn = sqlite3.connect('./ban_list.db')

sql = """
  INSERT OR IGNORE INTO ban_list(user_id, user_name, reason, date, mod, server)
                   VALUES(?,?,?,?,?,?)
"""
cur = conn.cursor()
with open('banned_users.txt', 'r', encoding="utf8") as f:
    data = csv.reader(f)
    for i,row in enumerate(data):
      print(row)
      if i > 10:
        break
    cur.executemany(sql, data)
    conn.commit()