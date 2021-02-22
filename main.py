from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hola mundo, Yirleny y Anyi! estas son las rutas que puedes explorar: <br/>\
<ul>\
<li>/cambio</li> \
<li>/saludar</li>\
<li>/saludar/ACA_PONES_TU_NOMBRE</li>\
</ul></p>'

@app.route('/cambio')
def git():
    return 'Aprendiendo andamos!'

@app.route('/saludar')
def saludar():
    return 'Hola chicos, desatrasandome estoy! <b>ahora entra a la ruta 127.0.0.1:500/saludar/TUNOMBRE</b>'

@app.route('/saludar/<nombre>')
def saludar_nombre(nombre):
    return f'<h2>Hola {nombre}!</h2> <p>Ya pudiste bajar mis cambios en el repo :)</p>'

@app.route('/pelicula', methods=['POST'])
def crear_pelicula():
    
    conn = sqlite3.connect('peliculas.db')
    body = request.json
    
    c = conn.cursor()
    # Insert a row of data
    c.execute("INSERT INTO pelicula VALUES (?,?,?,?)", (body["nombre"], body["calificacion"], body["duracion"], body["año"]))

    conn.commit()
    return {"respuesta": "ok"}

@app.route('/pelicula/<nombre>', methods=['DELETE'])
def borrar_pelicula(nombre):
    
    conn = sqlite3.connect('peliculas.db')

    c = conn.cursor()
    # Insert a row of data
    c.execute("DELETE FROM pelicula where nombre=?", [nombre])
    conn.commit()
    return {"respuesta": "ok"}

app.run(debug=True)
