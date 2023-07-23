import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            host=config('DB_HOST'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            database=config('DB_NAME')
        )
    except DatabaseError as ex:
        print(f'Error connecting to database: {ex}')
        raise ex

def table_exists(cursor, table_name):
    cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
    return cursor.fetchone()[0]

def create_tables(conn):
    create_jobs_table_query = """
    CREATE TABLE IF NOT EXISTS jobs (
        job_id SERIAL PRIMARY KEY,
        job_title VARCHAR(100) NOT NULL
    )
    """
    create_departments_table_query = """
    CREATE TABLE IF NOT EXISTS departments (
        department_id SERIAL PRIMARY KEY,
        department_name VARCHAR(100) NOT NULL
    )
    """
    create_employees_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        employee_id SERIAL PRIMARY KEY,
        employee_name VARCHAR(100),
        hire_date TIMESTAMP,
        department_id INT,
        job_id INT,
        FOREIGN KEY (job_id) REFERENCES jobs(job_id),
        FOREIGN KEY (department_id) REFERENCES departments(department_id)
    )
    """

    try:
        with conn.cursor() as cursor:
            cursor.execute(create_jobs_table_query)
            cursor.execute(create_departments_table_query)
            cursor.execute(create_employees_table_query)
            conn.commit()
        print("Tablas creadas exitosamente.")
    except DatabaseError as ex:
        conn.rollback()
        print(f"Error al crear las tablas: {ex}")

def truncate_tables(conn):
    truncate_employees_query = "TRUNCATE TABLE employees RESTART IDENTITY CASCADE"
    truncate_departments_query = "TRUNCATE TABLE departments RESTART IDENTITY CASCADE"
    truncate_jobs_query = "TRUNCATE TABLE jobs RESTART IDENTITY CASCADE"

    try:
        with conn.cursor() as cursor:
            cursor.execute(truncate_employees_query)
            cursor.execute(truncate_departments_query)
            cursor.execute(truncate_jobs_query)
            conn.commit()
        print("Datos truncados exitosamente.")
    except DatabaseError as ex:
        conn.rollback()
        print(f"Error al truncar los datos: {ex}")