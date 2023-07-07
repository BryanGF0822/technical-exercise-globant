from flask import Flask, jsonify
import csv
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="guapi_db",
    user="bryan",
    password="password"
)

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! --> This is the technical exercise to join Globant as a Data Engineer Jr.'

# def read_csv(file_path):
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         data = list(reader)
#     return data

def read_csv(file_path, table_name):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        cursor = conn.cursor()
        try:
            for row in reader:
                insert_query = f"INSERT INTO {table_name} VALUES ({','.join(['%s']*len(row))})"
                cursor.execute(insert_query, row)
            conn.commit()
        except Exception as e:
            conn.rollback()  # Revertir cualquier cambio realizado en la transacción
            print("Error during data insertion:", e)
        finally:
            cursor.close()

    # Después de cargar los datos, se debe realizar una nueva consulta para obtener los datos desde la base de datos
    cursor = conn.cursor()
    select_query = f"SELECT * FROM {table_name}"
    cursor.execute(select_query)
    data = cursor.fetchall()
    cursor.close()

    # Devuelve los datos cargados desde la base de datos
    return data


@app.route('/departments', methods=['GET'])
def get_departments():
    departments = read_csv('data/departments.csv', 'departments')
    return jsonify(departments)

@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = read_csv('data/jobs.csv', 'jobs')
    return jsonify(jobs)

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = read_csv('data/hired_employees.csv', 'employees')
    return jsonify(employees)

if __name__ == '__main__': 
    app.run(debug=True)
