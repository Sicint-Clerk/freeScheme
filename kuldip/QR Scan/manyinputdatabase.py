import _sqlite3
conn = _sqlite3.connect("library.db")
c = conn.cursor()

c.execute("""create table book(title,author,publisher);""")

list1 = [('A','B',2008),('C','D',2009),('E','F',2010)]

c.executemany("insert into book(title,author,publisher) values (?,?,?)", list1)
sql1 = """select * from book;"""
c.execute(sql1)
print(c.fetchall())
conn.commit()
conn.close()

