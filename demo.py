import psycopg2

conn = psycopg2.connect('dbname=newdb user=postgres password=picasso0')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS newtb;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE newtb (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

# insert into the table newtb using substitution
cur.execute('INSERT INTO newtb (id, description) VALUES (%s, %s)', (1, 'fantastic'))

# insert into the table newtb  - syntax of "completed BOOLEAN NOT NULL DEFAULT False"
# cur.execute('INSERT INTO newtb (id, description) VALUES (2, true);')


# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()