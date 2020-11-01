import psycopg2

conn = psycopg2.connect('dbname=newdb user=postgres password=picasso0')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing newtb2 table
cur.execute("DROP TABLE IF EXISTS newtb3;")

# (re)create the newtb2 table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE newtb3 (
    id integer PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
""")

# String interpolation 1:  %s, passing in a tuple as the 2nd argument in cursor.execute()
cursor.execute('INSERT INTO newtb3 (id, completed) VALUES (%s, %s);', (1, True))

# String interpolation 1:  %s, passing in a tuple as the 2nd argument in cursor.execute()
cursor.execute('INSERT INTO newtb3 (id, completed) VALUES (%s, %s);', (2, True))

# String interpolation 2: named string parameters %(foo)s, passing in a dictionary
SQL = 'INSERT INTO newtb3 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 3,
  'completed': False
}
cursor.execute(SQL, data)

cursor.execute('INSERT INTO newtb3 (id, completed) VALUES (%s, %s);', (4, True))

# Fetch commands

cursor.execute('SELECT * from newtb3;')

# fetch many
result = cursor.fetchmany(2)
print('fetchmany', result)

# fetchone if any left over - not with fetch all
result2 = cursor.fetchone()
print('fetchone', result2)

# fetch all remaining
result = cursor.fetchall()
print('fetchall', result)

cursor.execute('SELECT * from newtb3;')

# fetch all remaining
result = cursor.fetchall()
print('fetchall', result)


# commit, so it does the executions on the db and persists in the db
conn.commit()

conn.close()
cursor.close()