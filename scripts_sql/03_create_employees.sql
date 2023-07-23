CREATE TABLE IF NOT EXISTS employees (
            employee_id SERIAL PRIMARY KEY,
            employee_name VARCHAR(100),
            hire_date TIMESTAMP,
            department_id INT,
            job_id INT,
            FOREIGN KEY (job_id) REFERENCES jobs(job_id),
            FOREIGN KEY (department_id) REFERENCES departments(department_id)
        )