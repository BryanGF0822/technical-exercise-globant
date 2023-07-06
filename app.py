from flask import Flask
import csv
import psycopg2

app = Flask(__name__)

#@app.route('/')
#def hello():
#    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload():
    # Leer archivos CSV y cargar los datos en la base de datos
    # ...
    return 'Data uploaded successfully'

@app.route('/batch_insert', methods=['POST'])
def batch_insert():
    # Procesar la solicitud de inserción por lotes
    # ...
    return 'Batch insert completed'


if __name__ == '__main__':
    app.run(debug=True)
