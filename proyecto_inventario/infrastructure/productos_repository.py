from domain.models import Producto

class ProductoRepository:
    def __init__ (self,conexion):
        self.conexion = conexion

    def guardar_producto(self, producto):
        cursor = self.conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre_producto, stock, precio, descripcion) VALUES (%s, %s, %s, %s)",
            (producto.nombre_producto, producto.stock, producto.precio, producto.descripcion)
        )
        self.conexion.commit()
        cursor.close()
    
    def obtener_todos(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        cursor.close()
        productos = []
        for d in datos:
            # Recuerda el orden corregido: id, nombre, stock, precio, descripcion
            productos.append(Producto(d[1], d[4], d[3], d[2], d[0])) 
        return productos


    def obtener_producto_por_id(self, id_producto):
        cursor = self.conexion.cursor()
        cursor.execute(
            "SELECT * FROM productos WHERE id_producto = %s", (id_producto,)
        ) 
        datos = cursor.fetchone() #fetch es para obtener un solo registro en forma de tupla
        cursor.close()
        if datos:
            return Producto(datos[1], datos[4], datos[3], datos[2], datos[0])
        return None
    
    def actualizar_producto(self, producto):
        cursor = self.conexion.cursor()
        cursor.execute(
            "UPDATE productos SET nombre_producto = %s, stock = %s, precio = %s, descripcion = %s WHERE id_producto = %s",
            (producto.nombre_producto, producto.stock, producto.precio, producto.descripcion, producto.id_producto)
        )
        self.conexion.commit()
        cursor.close()

    def eliminar_producto(self, id_producto):
        cursor = self.conexion.cursor()
        cursor.execute(
            "DELETE FROM productos WHERE id_producto = %s", (id_producto,)
        )    
        self.conexion.commit()
        cursor.close()