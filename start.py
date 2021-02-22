import sqlite3
conn = sqlite3.connect('peliculas.db')


c = conn.cursor()

# Create table
c.execute('''CREATE TABLE pelicula
             (nombre text, calificacion int, duracion int, año int)''')


# Insert a row of data
c.execute("INSERT INTO pelicula VALUES ('Up, una aventura de altura',5,136,2009)")


conn.commit()
conn.close()
