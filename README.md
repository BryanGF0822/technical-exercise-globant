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
