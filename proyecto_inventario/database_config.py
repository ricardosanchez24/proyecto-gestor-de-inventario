import mysql.connector

def obtener_conexion():
    try:
        datos_config = {
            'user': 'root',
            'password': '123456789',
            'host': 'localhost',
            'database': 'gestor_inventario', 
            #'auth_plugin': 'mysql_native_password' 

                            }
        conexion = mysql.connector.connect(**datos_config)
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None