import psycopg2

conn = psycopg2.connect('dbname=newdb user=postgres password=picasso0')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing newtb2 table
cur.execute("DROP TABLE IF EXISTS newtb2;")

# (re)create the newtb2 table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE newtb2 (
    id integer PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
""")

# String interpolation 1:  %s, passing in a tuple as the 2nd argument in cursor.execute()
cursor.execute('INSERT INTO newtb2 (id, completed) VALUES (%s, %s);', (1, True))

# String interpolation 2: named string parameters %(foo)s, passing in a dictionary
SQL = 'INSERT INTO newtb2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)


# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()