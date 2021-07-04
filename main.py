from flask import Flask, request
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/pelicula', methods=['POST'])
def crear_pelicula():
    
    return

@app.route('/pelicula/<nombre>', methods=['DELETE'])
def borrar_pelicula(nombre):
    
    
    return


app.run(debug=True)

