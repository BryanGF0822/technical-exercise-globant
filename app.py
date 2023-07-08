from psycopg2.extras import execute_batch
from database.db import get_connection
from flask import Flask, jsonify
from config import config
import psycopg2.extras
import psycopg2
import csv

conn = get_connection()

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

@app.route('/')
def hello():
    return "<h1>Hello Glober!</h1> \n <p>This is the technical exercise to join Globant as a Data Engineer Jr.</p>"

def read_csv(file_path, table_name):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    #reemplaza valores en blaco por None    
    data = [[None if value == '' else value for value in row] for row in data]
    return data


@app.route('/jobs', methods=['GET'])
def get_jobs():
    data = read_csv('data/jobs.csv', 'jobs')
    cursor = conn.cursor()
    try:
        insert_query = f"INSERT INTO jobs VALUES (%s, %s)"
        page_size = 1000
        num_rows = len(data)
        rows_inserted = 0

        while rows_inserted < num_rows:
            batch = data[rows_inserted:rows_inserted + page_size]
            execute_batch(cursor, insert_query, batch)
            rows_inserted += len(batch)
            print(f"Filas insertadas: {rows_inserted}/{num_rows}")

        conn.commit()

        print(f"Se insertaron {rows_inserted} filas en lotes de 1 a {page_size}")

        return jsonify({"message": "Datos insertados correctamente"})
    except Exception as e:
        conn.rollback()
        return jsonify({"error": f"Error durante la inserción de datos: {str(e)}"}), 500
    finally:
        cursor.close()

@app.route('/departments', methods=['GET'])
def get_departments():
    data = read_csv('data/departments.csv', 'departments')
    cursor = conn.cursor()
    try:
        insert_query = f"INSERT INTO departments VALUES (%s, %s)"
        page_size = 1000
        num_rows = len(data)
        rows_inserted = 0

        while rows_inserted < num_rows:
            batch = data[rows_inserted:rows_inserted + page_size]
            execute_batch(cursor, insert_query, batch)
            rows_inserted += len(batch)
            print(f"Filas insertadas: {rows_inserted}/{num_rows}")

        conn.commit()

        print(f"Se insertaron {rows_inserted} filas en lotes de 1 a {page_size}")

        return jsonify({"message": "Datos insertados correctamente"})
    except Exception as e:
        conn.rollback()
        return jsonify({"error": f"Error durante la inserción de datos: {str(e)}"}), 500
    finally:
        cursor.close()
        
@app.route('/employees', methods=['GET'])
def get_employees():
    data = read_csv('data/hired_employees.csv', 'employees')
    cursor = conn.cursor()
    try:
        insert_query = f"INSERT INTO employees VALUES (%s, %s, %s, %s, %s)"
        page_size = 1000
        num_rows = len(data)
        rows_inserted = 0

        while rows_inserted < num_rows:
            batch = data[rows_inserted:rows_inserted + page_size]
            execute_batch(cursor, insert_query, batch)
            rows_inserted += len(batch)
            print(f"Filas insertadas: {rows_inserted}/{num_rows}")

        conn.commit()

        print(f"Se insertaron {rows_inserted} filas en lotes de 1 a {page_size}")

        return jsonify({"message": "Datos insertados correctamente"})
    except Exception as e:
        conn.rollback()
        return jsonify({"error": f"Error durante la inserción de datos: {str(e)}"}), 500
    finally:
        cursor.close()

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Error handlers
    app.register_error_handler(404, page_not_found) 
    app.run()
