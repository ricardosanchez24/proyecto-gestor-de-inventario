from proyecto_inventario.domain.models import Producto


class InventarioService:
    def __init__(self, repositorio_productos):
        self.repositorio_productos = repositorio_productos

    def agregar_producto(self, nombre_producto, stock, precio, descripcion):
        nuevo_producto = Producto(nombre_producto, stock, precio, descripcion)
        nuevo_producto.validar_producto()
        self.repositorio_productos.guardar_producto(nuevo_producto)

    def obtener_producto(self, id_producto):
        return self.repositorio_productos.obtener_producto_por_id(id_producto)

    def actualizar_producto(self, id_producto, nombre_producto, stock, precio, descripcion):
        producto_actualizado = Producto(nombre_producto, stock, precio, descripcion, id_producto)
        self.repositorio_productos.actualizar_producto(producto_actualizado)

    def eliminar_producto(self, id_producto):
        self.repositorio_productos.eliminar_producto(id_producto)            