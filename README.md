# Technical Exercise Globant
Technical exercise to apply for a Junior Data Engineer position at Globant.

## Sección 1: API
En el contexto de una migracion de BD con 3 tablas diferentes (departamentos, trabajos, empleados), se desarrolla una API REST localque debe:
  1. Recibir datos históricos de archivos CSV
  2. Cargar estos archivos en la nueva BD
  3. Ser capaz de insertar transacciones por lotes (1 hasta 1000 filas) con una sola peticion

A continuacion encontramos las instrucciones para la implementacion:
  ### Paso 1: Configuracion inicial
  - Instalar Python
  - Instalar PostgreSQL
  - Instalar Docker Desktop
  - Instalar las bibliotecas necesarias. En este caso, vamos a utilizar Flask (para crear la API REST), Psycopg2 (para conectarse a la base de datos PostgreSQL) y python-decouple
  
  ### Paso 2: Instalamos las dependencias:
  - Ejecutamos los comando necesarios segun las librerias que necesitemos. En este caso vamos a utilizar Flask y PosgreSQL:
    - pip install flask
    - pip install psycopg2

  ### Paso 3: Abrir el proyecto:
  - Podemos utilizar Visual Studio Code para abrir el proyecto
  - En la carpeta raiz del proyecto activamos el ambiente previamente creado utilizando **source venv/Scripts/activate**
  - Para saber si estamos dentro de ambiente debemos verificar en la consola al inicio de aparece entre parantesis el nombre del ambiente --> (env_name)
    
  <img width="436" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/1e29bc4e-da09-4d31-aa38-b05a68eee5f8">
  
  ### Paso 4: Ejecutamos el programa:
  Ahora, podemos ejecutar el programa con el comando --> 'python app.py'
  
  <img width="677" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/10c6f2bb-b36a-45d4-b8f5-7405f6fc5428">

  Para validar que el correcto funcionamiento, vamos al navegador en la ruta --> 'http://localhost:5000' y debe aparece un mensaje de Hello Glober!

  <img width="429" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/0d0d1ba7-ed3f-48da-8140-a1c838a7bf93">

  Ahora, para poder cargar los archivos CSV en la nueva base de datos, realizamos la peticion dependiendo del archivo que queremos subir ya sea /jobs, /departments o /employees. A continuacion te dejo las rutas para cada uno:
  - Jobs: 'http://localhost:5000/jobs'
  - Departments: 'http://localhost:5000/departments'
  - Employees: 'http://localhost:5000/employees'

Al realizar cada uno de las peticiones por primera vez, nos debe aparece un mensaje --> 'Datos insertados correctamente'

<img width="278" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/6f147569-e75b-4457-89f7-94ea05c040d4">

Finalmente, podrémos revisar en nuestro gestor de base de datos, en mi caso estoy utilizando DBeaver y asi podremos visualizar que los datos se estan subiendo correctamente.

<img width="519" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/aafbe046-36ba-41df-af31-b9c0defe1767">

## Sección 2: SQL
A partir de la insercion de data que realizamos anteriormente, vamos a explorar un poco la data.
Debemos saber que antes de utilizar el API REST debemos tener listas las tablas en PostgreSQL que coincidan con los datos proporcionados para el ejercicio, teniendo en cuentes, sus requerimientos y restricciones. A continuacion te dejo las querys para crear la tablas:

<img width="461" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/3fc67594-c4e6-46ff-bfb5-a6b982246951">

Seguido de esto, podemos buscar los nuevos end-point que cumplen con los dos requerimientos que nos proporciona el ejercicio. Acá te dejo las rutas para que puedas visitar y para ejecutar las querys:
  - R1: Number of employees hired for each job and department in 2021 divided by quarter. The table must be ordered alphabetically by department and job.
    - 'http://localhost:5000/jobs/employees/2021/quarters'
    - Esta el query que se envia a traves de la peticion:
      
      <img width="586" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/10718938-a2cf-4fc8-82fc-7941bc231515">
      
    - Nuesto ouput:
        
      <img width="189" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/92c16934-89f9-43c6-b236-1bbd8ee7a69a">

  - R2: List of ids, name and number of employees hired of each department that hired more mployees than the mean of employees hired in 2021 for all the departments, ordered by the number of employees hired (descending).
    - 'http://localhost:5000/departments/more_employees_than_mean'
    - Esta el query que se envia a traves de la peticion:
      
      <img width="629" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/16ce04c1-9787-4407-9c8b-bcdd2a8d746c">
      
    - Nuestro output:
      
      <img width="187" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/a0c869a9-850a-48e9-87e5-ae42336d1200">

## Sesion 3: Bonus Track! Cloud, Testing and Containers.

### Testing
Logramos generar algunos casos de prueba con la libreria "pytest"
- Para ejecutar las pruebas, debemos correr la API REST y luego ingresar al folder llamado "tests" y ejecutar el comando *pytest*. A continuacion encontramos un ejemplo:
    
  <img width="635" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/d498fd07-8901-4874-bc26-baab2fb49350">

### Container
Logramos dockerizar la API. Acontinuacion encuentras los datos para ejecutarlo:
- Ejecuta el comando *docker-compose up*, y veras correr la API desde el contenedor.
  
  ![image](https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/06f2288e-3046-48d6-bf0d-8a8c9960a412)







