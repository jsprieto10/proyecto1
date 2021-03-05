import sqlite3
conn = sqlite3.connect('canciones.db')


c = conn.cursor()

# Create table
c.execute('''CREATE TABLE canciones
             (nombre text, duracion int,  album text, año int)''')

# Insert a row of data
c.execute("INSERT INTO canciones VALUES ('Tu',5,'libertad',2017)")

conn.commit()
conn.close()