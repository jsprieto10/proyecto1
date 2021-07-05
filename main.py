from flask import Flask, request
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#SQlite 

@app.route('/pelicula', methods=['POST'])
def crear_pelicula():
    #Obtener la información de una petición
    inf = request.get_json()
    nombre = inf["nombre"]
    duracion = inf["duracion"]
    calificacion = inf ["calificacion"]
    anio =inf["anio"]

    #conectarnos a la bd
    con = sqlite3.connect('peliculas.db')
    #insertar en la base de db
    cursorObj = con.cursor()
    entities = (nombre, calificacion, duracion, anio)
    cursorObj.execute('INSERT INTO pelicula(nombre, calificacion, duracion, año) VALUES(?, ?, ?, ?)', entities)

    con.commit()


    # completar la función
    return {"res":"okey"}

@app.route('/pelicula/<nombre>', methods=['DELETE'])
def borrar_pelicula(nombre):
    #completar la función
    #conectarnos a la bd
    con = sqlite3.connect('peliculas.db')
    #insertar en la base de db
    cursorObj = con.cursor()
    print(nombre)
    cursorObj.execute('DELETE FROM pelicula where nombre= ?', [nombre])

    con.commit()


    # completar la función
    return {"res":"okey"}


app.run(debug=True)

