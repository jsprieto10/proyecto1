from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola mundo y yirleny y anyi!'

@app.route('/cambio')
def git():
    return 'Aprendiendo andamos!'

@app.route('/saludar/<nombre>')
def saludo(nombre):
    return f"hola, {nombre}"

@app.route('/Saludar1/<Apellido>')
def saludo1(apellido):
    return f"Su apellido es: , {Apellido}"

app.run()
