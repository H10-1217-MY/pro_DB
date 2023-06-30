import sqlite3

dbname = 'main.db'
conn = sqlite3.connect(dbname)

# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()


# データ検索
cur.execute('SELECT * FROM items')

# 取得したデータはカーソルの中に入る
for row in cur:
    print(row)

conn.close()