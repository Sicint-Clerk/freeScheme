import _sqlite3
conn = _sqlite3.connect('sample.db')
c = conn.cursor()
c.execute("Delete from emp where staff_number=23")
print(conn.total_changes)
conn.commit()
print(c.fetchall())
conn.close()