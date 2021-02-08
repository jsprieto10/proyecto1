from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola mundo y yirleny y anyi!'


@app.route('/saludar/<nombre>')
def saludo(nombre):
    return f"hola, {nombre}"


app.run()