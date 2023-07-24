# Utiliza la imagen de Python como base
FROM python:3.8

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala las dependencias del proyecto (psycopg2 y Flask)
RUN pip install --no-cache-dir -r requirements.txt

# Configuración de las variables de entorno para la base de datos
ENV SECRET_KEY=Al3x4nd3r$
ENV DB_HOST=localhost
ENV DB_NAME=globant_db
ENV DB_USER=postgres
ENV DB_PASSWORD=password

# Expone el puerto en el que la aplicación Flask estará escuchando
EXPOSE 5000

# Agrega el comando para esperar a que la base de datos esté disponible antes de iniciar la aplicación Flask
CMD bash -c "while !</dev/tcp/$DB_HOST/5432; do sleep 1; done; python app.py"


