--Create Tables
CREATE TABLE IF NOT EXISTS jobs (
            job_id SERIAL PRIMARY KEY,
            job_title VARCHAR(100) NOT NULL
     	)
		
CREATE TABLE IF NOT EXISTS departments (
            department_id SERIAL PRIMARY KEY,
            department_name VARCHAR(100) NOT NULL
        )
CREATE TABLE IF NOT EXISTS employees (
            employee_id SERIAL PRIMARY KEY,
            employee_name VARCHAR(100),
            hire_date TIMESTAMP,
            department_id INT,
            job_id INT,
            FOREIGN KEY (job_id) REFERENCES jobs(job_id),
            FOREIGN KEY (department_id) REFERENCES departments(department_id)
        )



