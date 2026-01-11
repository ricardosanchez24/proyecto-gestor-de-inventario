#imagen base
FROM python:3.14-slim

#directorio de trabajo
WORKDIR /app

#copiar las dependencias
COPY requirements.txt

#instala las librerias
RUN pip install --no-cache-dir- -r requirements.txt

#copia el resto del codigo (index,database,etc)
COPY . .

#puerto de Flask
EXPOSE 5000

#comando de ejecucion
CMD ["python","app.py"]