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


# @app.route('/employees/2021/quarters', methods=['GET'])
# def get_employees_by_quarter():
#     cursor = conn.cursor()
#     try:
#         query = """
#         SELECT d.department_name, j.job_title, EXTRACT(QUARTER FROM e.hire_date) AS quarter, COUNT(*) AS num_employees
#         FROM employees e
#         INNER JOIN departments d ON e.department_id = d.department_id
#         INNER JOIN jobs j ON e.job_id = j.job_id
#         WHERE EXTRACT(YEAR FROM e.hire_date) = 2021
#         GROUP BY d.department_name, j.job_title, quarter
#         ORDER BY d.department_name, j.job_title
#         """
#         cursor.execute(query)
#         result = cursor.fetchall()

#         data = []
#         for row in result:
#             department_name, job_title, quarter, num_employees = row
#             data.append({
#                 "department_name": department_name,
#                 "job_title": job_title,
#                 "quarter": int(quarter),
#                 "num_employees": int(num_employees)
#             })

#         return jsonify(data)
#     except Exception as e:
#         return jsonify({"error": f"Error al obtener los datos: {str(e)}"}), 500
#     finally:
#         cursor.close()

@app.route('/employees/2021/quarters', methods=['GET'])
def get_employees_by_quarter():
    cursor = conn.cursor()
    try:
        query = """
        SELECT d.department_name, j.job_title,
               COUNT(CASE WHEN EXTRACT(QUARTER FROM e.hire_date) = 1 THEN 1 ELSE NULL END) AS q1,
               COUNT(CASE WHEN EXTRACT(QUARTER FROM e.hire_date) = 2 THEN 1 ELSE NULL END) AS q2,
               COUNT(CASE WHEN EXTRACT(QUARTER FROM e.hire_date) = 3 THEN 1 ELSE NULL END) AS q3,
               COUNT(CASE WHEN EXTRACT(QUARTER FROM e.hire_date) = 4 THEN 1 ELSE NULL END) AS q4
        FROM employees e
        INNER JOIN departments d ON e.department_id = d.department_id
        INNER JOIN jobs j ON e.job_id = j.job_id
        WHERE EXTRACT(YEAR FROM e.hire_date) = 2021
        GROUP BY d.department_name, j.job_title
        ORDER BY d.department_name, j.job_title
        """
        cursor.execute(query)
        result = cursor.fetchall()

        data = []
        for row in result:
            department_name, job_title, q1, q2, q3, q4 = row
            data.append({
                "department_name": department_name,
                "job_title": job_title,
                "Q1": int(q1),
                "Q2": int(q2),
                "Q3": int(q3),
                "Q4": int(q4)
            })

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Error al obtener los datos: {str(e)}"}), 500
    finally:
        cursor.close()


@app.route('/departments/more_employees_than_mean', methods=['GET'])
def get_departments_with_more_employees_than_mean():
    cursor = conn.cursor()
    try:
        query = """
        SELECT d.department_id, d.department_name, COUNT(*) AS num_employees
        FROM departments d
        INNER JOIN employees e ON e.department_id = d.department_id
        WHERE EXTRACT(YEAR FROM e.hire_date) = 2021
        GROUP BY d.department_id, d.department_name
        HAVING COUNT(*) > (SELECT AVG(num_employees) FROM (SELECT COUNT(*) AS num_employees FROM employees WHERE EXTRACT(YEAR FROM hire_date) = 2021 GROUP BY department_id) AS subquery)
        ORDER BY num_employees DESC
        """
        cursor.execute(query)
        result = cursor.fetchall()

        data = []
        for row in result:
            department_id, department_name, num_employees = row
            data.append({
                "department_id": int(department_id),
                "department_name": department_name,
                "num_employees": int(num_employees)
            })

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Error al obtener los datos: {str(e)}"}), 500
    finally:
        cursor.close()

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Error handlers
    app.register_error_handler(404, page_not_found) 
    app.run()
