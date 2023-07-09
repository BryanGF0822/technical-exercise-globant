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


SELECT d.department_id, d.department_name, COUNT(*) AS num_employees
        FROM departments d
        INNER JOIN employees e ON e.department_id = d.department_id
        WHERE EXTRACT(YEAR FROM e.hire_date) = 2021
        GROUP BY d.department_id, d.department_name
        HAVING COUNT(*) > (SELECT AVG(num_employees) FROM (SELECT COUNT(*) AS num_employees FROM employees WHERE EXTRACT(YEAR FROM hire_date) = 2021 GROUP BY department_id) AS subquery)
        ORDER BY num_employees DESC


