# technical-exercise-globant
Technical exercise to apply for a Junior Data Engineer position at Globant.

## Sección 1: API
En el contexto de una migracion de BD con 3 tablas diferentes (departamentos, trabajos, empleados), se desarrolla una API REST localque debe:
  1. Recibir datos históricos de archivos CSV
  2. Cargar estos archivos en la nueva BD
  3. Ser capaz de insertar transacciones por lotes (1 hasta 1000 filas) con una sola peticion

A continuacion encontramos las instrucciones para la implementacion:
  ### Paso 1: Configuracion inicial
  - Instalar Python en nuestra maquina
  - Instalar las bibliotecas necesarias. En este caso, vamos a utilizar Flask (para crear la API REST) y Psycopg2 (para conectarse a la base de datos PostgreSQL)
  ### Paso 2: Estructura de archivos:
  Creamos lo siguientes archivos.
  - 'app.py': el archivo pricipal de la aplicacion Flask
  - 'data/': un directorio para almacenar los archivos CSV
  ### Paso 3: Configuramos un entorno virtual (opcional):
  - Creamos un entorno virtual para el proyecto (recomendado)
  - Activamos el entorno antes de continuar
  ### Paso 4: Instalamos las dependencias:
  - Ejecutamos los comando necesarios segun las librerias que necesitemos. En este caso vamos a utilizar Flask y PosgreSQL:
    - pip install flask
    - pip install psycopg2
  ### Paso 5: Ejecutamos el programa:
  Para saber si estamos dentro de ambiente debemos verificar en la consola al inicio de aparece entre parantesis el nombre del ambiente --> (env_name)
  
  <img width="436" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/1e29bc4e-da09-4d31-aa38-b05a68eee5f8">

  Ahora, podemos ejecutar el programa con el comando --> 'python app.py'
  
  <img width="677" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/10c6f2bb-b36a-45d4-b8f5-7405f6fc5428">

  Para validar que el correcto funcionamiento, vamos al navegador en la ruta --> 'http://localhost:5000' y debe aparece un mensaje de Hello Word!

  <img width="429" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/0d0d1ba7-ed3f-48da-8140-a1c838a7bf93">

  Ahora, para poder cargar los archivos CSV en la nueva base de datos, realizamos la peticion dependiendo del archivo que queremos subir ya sea /jobs, /departments o /employees. A continuacion te dejo las rutas para cada uno:
  - Jobs: 'http://localhost:5000/jobs'
  - Departments: 'http://localhost:5000/departments'
  - Employees: 'http://localhost:5000/employees'

Al realizar cada uno de las peticiones por primera vez, nos debe aparece un mensaje --> 'Datos insertados correctamente'
<img width="278" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/6f147569-e75b-4457-89f7-94ea05c040d4">

Finalmente, podrémos revisar en nuestro gestor de base de datos, en mi caso estoy utilizando DBeaver y asi podremos visualizar que los datos se estan subiendo correctamente.

<img width="683" alt="image" src="https://github.com/BryanGF0822/technical-exercise-globant/assets/48836505/030c9f0d-2dd8-4603-a6ff-3bf59efc3f54">

  



