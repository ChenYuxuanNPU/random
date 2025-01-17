"""
测试关系型数据库的部分字段插入
"""

import sqlite3

conn = sqlite3.connect(
    fr"C:\Users\1012986131\Desktop\python\random\test_db.db"
)
c = conn.cursor()

c.execute(f"create table test(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, age integer)")

c.execute(f"insert into test(name) values('123')")

c.execute(f'insert into test(age) values(18)')
c.execute(f'insert into test(age) values(19)')

c.execute(f'delete from test where age = 18')

c.execute(f'delete from test')

c.execute(f'insert into test(age) values(19)')
c.execute(f'insert into test(name,age) values("name1",19)')

c.execute(f"select * from test")
result = c.fetchall()

print(result)

conn.close()
