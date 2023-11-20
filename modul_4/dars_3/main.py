import psycopg2

con = psycopg2.connect(database="lesson_3",
                       user="postgres",
                       password="1",
                       host="localhost",
                       port=5432)

cur = con.cursor()

query = """
    select * from student
"""
cur.execute(query)
print(cur.fetchall())

