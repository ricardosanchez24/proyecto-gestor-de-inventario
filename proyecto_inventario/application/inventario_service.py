from domain.models import Producto


class InventarioService:
    def __init__(self, repositorio_productos):
        self.repositorio_productos = repositorio_productos

    def agregar_producto(self, nombre_producto, stock, precio, descripcion):
        nuevo_producto = Producto(
            nombre_producto=nombre_producto,
            stock=stock,
            precio=precio,
            descripcion=descripcion
        )
        nuevo_producto.validar_producto()
        self.repositorio_productos.guardar_producto(nuevo_producto)
    
    def obtener_todos(self):
        return self.repositorio_productos.obtener_todos()

    def obtener_producto(self, id_producto):
        return self.repositorio_productos.obtener_producto_por_id(id_producto)

    def actualizar_producto(self, id_producto, nombre_producto, stock, precio, descripcion):
        producto_actualizado = Producto(
            id_producto=id_producto, # Importante pasar el ID aquí
            nombre_producto=nombre_producto,
            stock=stock,
            precio=precio,
            descripcion=descripcion
        )
        self.repositorio_productos.actualizar_producto(producto_actualizado)

    def eliminar_producto(self, id_producto):
        self.repositorio_productos.eliminar_producto(id_producto)            