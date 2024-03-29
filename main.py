from sqlite3.dbapi2 import Cursor
from flask import Flask, request
import sqlite3
from flask_cors import CORS
NOMBRE_BASE_DE_DATOS = 'peliculas.db'

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
    con = sqlite3.connect(NOMBRE_BASE_DE_DATOS)
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
    con = sqlite3.connect(NOMBRE_BASE_DE_DATOS)
    #insertar en la base de db
    cursorObj = con.cursor()
    print(nombre)
    cursorObj.execute('DELETE FROM pelicula where nombre= ?', [nombre])

    con.commit()


    # completar la función
    return {"res":"okey"}


@app.route('/peliculas', methods=['GET'])
def obtener_peliculas():
    con = sqlite3.connect(NOMBRE_BASE_DE_DATOS)
    #Insertar en la base de bd
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM pelicula")
    peliculas = cursorObj.fetchall()
    lista = []
    for pelicula in peliculas:
        objeto = {
          "nombre":pelicula[0], 
          "calificacion":pelicula[1],
          "duracion":pelicula[2],
          "año":pelicula[3],
        }
        lista.append(objeto)
       
    con.close()
    return {"resultado":lista}

app.run(debug=True)

