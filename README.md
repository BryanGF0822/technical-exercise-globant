# Technical Exercise Globant
Technical exercise to apply for a Junior Data Engineer position at Globant.

## Section 1: API
In the context of a database migration with three different tables (departments, jobs, employees), a local REST API has been developed that must:
  1. Receive historical data from CSV files.
  2. Load these files into the new database.
  3. Be able to insert batch transactions (1 to 1000 rows) with a single request.

Below are the instructions for the implementation:
  ### Step 1: Initial Configuration
  - Install Python
  - Install PostgreSQL
  - Install Docker Desktop
  - Install the necessary libraries. In this case, we will use Flask (to create the REST API), Psycopg2 (to connect to the PostgreSQL database), and python-decouple.
  
  ### Step 2: Install Dependencies
  - Run the necessary commands to install the required libraries. In this case, we will use Flask and PostgreSQL:
    - pip install flask
    - pip install psycopg2

  ### Step 3: Open the Project
  - You can use Visual Studio Code to open the project.
  - In the root folder of the project, activate the previously created virtual environment using **source venv/Scripts/activate**
  - To verify if you are within the virtual environment, check if the name of the environment appears in parentheses at the beginning of the console --> (env_name)
    
  <img width="436" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/1e29bc4e-da09-4d31-aa38-b05a68eee5f8">
  
  ### Step 4: Run the Program
  Now, you can run the program using the command --> 'python app.py'
  
  <img width="677" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/10c6f2bb-b36a-45d4-b8f5-7405f6fc5428">

  To verify that it is functioning correctly, open your web browser and go to the URL --> 'http://localhost:5000' and you should see the message "Hello Glober!"

  <img width="429" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/0d0d1ba7-ed3f-48da-8140-a1c838a7bf93">

  To load the CSV files into the new database, make a request to the desired endpoint */jobs*, */departments* or */employees*. Below are the routes for each one:
  - Jobs: 'http://localhost:5000/jobs'
  - Departments: 'http://localhost:5000/departments'
  - Employees: 'http://localhost:5000/employees'

After making each request for the first time, you should receive a message --> "Data inserted correctly."



<img width="278" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/6f147569-e75b-4457-89f7-94ea05c040d4">

Finally, you can check your database management tool (e.g., DBeaver) to verify that the data is being uploaded correctly.

<img width="519" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/aafbe046-36ba-41df-af31-b9c0defe1767">

## Section 2: SQL
After inserting data into the database, we will explore the data a bit. Before using the REST API, make sure to have the PostgreSQL tables set up to match the data provided for the exercise, taking into account their requirements and constraints. Below are the queries to create the tables:

<img width="461" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/3fc67594-c4e6-46ff-bfb5-a6b982246951">

Next, we can search for new endpoints that fulfill the two requirements provided in the exercise. Here are the routes to visit and execute the queries:
  - R1: Number of employees hired for each job and department in 2021 divided by quarter. The table must be ordered alphabetically by department and job.
    - 'http://localhost:5000/jobs/employees/2021/quarters'
      
      <img width="586" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/10718938-a2cf-4fc8-82fc-7941bc231515">
      
    - Ouput:
        
      <img width="189" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/92c16934-89f9-43c6-b236-1bbd8ee7a69a">

  - R2: List of ids, name and number of employees hired of each department that hired more mployees than the mean of employees hired in 2021 for all the departments, ordered by the number of employees hired (descending).
    - 'http://localhost:5000/departments/more_employees_than_mean'
      
      <img width="629" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/16ce04c1-9787-4407-9c8b-bcdd2a8d746c">
      
    - Output:
      
      <img width="187" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/a0c869a9-850a-48e9-87e5-ae42336d1200">

## Section 3: Bonus Track! Cloud, Testing and Containers.

### Testing
We have generated some test cases using the "pytest" library.
- To run the tests, first run the REST API and then go to the "tests" folder and execute the command *pytest*. Here's an example:
    
  <img width="635" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/d498fd07-8901-4874-bc26-baab2fb49350">

### Container
We have containerized the API. Acontinuacion encuentras los datos para ejecutarlo:
- To run it, execute the command *docker-compose up*, and you will see the API running from the container.
  
  ![image](https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/06f2288e-3046-48d6-bf0d-8a8c9960a412)

# Development technologies

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)






