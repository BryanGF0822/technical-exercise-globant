from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

@app.route('/departments', methods=['GET'])
def obtener_departamentos():
    departamentos = read_csv('data/departments.csv')
    return jsonify(departamentos)

@app.route('/jobs', methods=['GET'])
def obtener_trabajos():
    trabajos = read_csv('data/jobs.csv')
    return jsonify(trabajos)

@app.route('/employees', methods=['GET'])
def obtener_empleados():
    empleados = read_csv('data/hired_employees.csv')
    return jsonify(empleados)

if __name__ == '__main__': 
    app.run(debug=True)
