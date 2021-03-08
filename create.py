import sqlite3
conn = sqlite3.connect('videos.db')


c = conn.cursor()

# Create table
c.execute('''CREATE TABLE videos
             (nombre text, calificacion int, duracion int, año int)''')


# Insert a row of data
c.execute("INSERT INTO videos VALUES ('Lectura Publica de Las Escrituras',5,345,2019)")


conn.commit()
conn.close()

