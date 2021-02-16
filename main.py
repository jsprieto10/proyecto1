from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola mundo y yirleny y anyi!'

@app.route('/cambio')
def git():
    return 'Aprendiendo andamos!'

@app.route('/saludar')
def saludar():
    return 'Hola chicos, desatrasandome estoy!'
    
app.run()
