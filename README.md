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
