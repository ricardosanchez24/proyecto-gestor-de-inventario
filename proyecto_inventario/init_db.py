from database_config import obtener_conexion


def inicializar_base_datos():
    try:
        conexion = obtener_conexion()
        if conexion is None:
            return "No se pudo establecer la conexión a la base de datos."
        
        cursor = conexion.cursor()

        consultas_sql = '''
        CREATE TABLE IF NOT EXISTS productos (
            id_producto INT AUTO_INCREMENT PRIMARY KEY,
            nombre_producto VARCHAR(100) NOT NULL,
            descripcion TEXT,
            precio DECIMAL(10, 2) NOT NULL,
            stock INT NOT NULL
        );'''

        cursor.execute(consultas_sql)
        conexion.commit()
        cursor.close()
        conexion.close()
        return "Base de datos inicializada correctamente."

    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")    

if __name__ == "__main__":
    inicializar_base_datos()  