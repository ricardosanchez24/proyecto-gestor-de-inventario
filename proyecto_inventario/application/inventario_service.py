from domain.models import Producto


class InventarioService:
    def __init__(self, repositorio_productos):
        self.repositorio_productos = repositorio_productos

    def agregar_producto(self, nombre_producto, stock, precio, descripcion,codigo_barras,usuario_id):
        nuevo_producto = Producto(
            nombre_producto=nombre_producto,
            stock=stock,
            precio=precio,
            descripcion=descripcion,
            codigo_barras=codigo_barras,
            usuario_id=usuario_id
        )
        nuevo_producto.validar_producto()
        self.repositorio_productos.guardar_producto(nuevo_producto)
    
    def obtener_todos(self,usuario_id):
        return self.repositorio_productos.obtener_todos_por_usuario(usuario_id)

    def obtener_producto(self, id_producto,usuario_id):
        return self.repositorio_productos.obtener_producto_por_id(id_producto,usuario_id)
    
    def obtener_producto_codigo_barras(self,codigo_barras,usuario_id):
        return self.repositorio_productos.obtener_producto_codigo_barras(codigo_barras,usuario_id)

    def actualizar_producto(self, id_producto, nombre_producto, stock, precio, descripcion,codigo_barras,usuario_id):

        producto_existente = self.repositorio_productos.obtener_producto_por_id(id_producto,usuario_id)

        if not producto_existente:
            raise ValueError("Producto no encontrado o no tienes los permisos necesarios para modificarlo")

        producto_actualizado = Producto(
            id_producto=id_producto, # Importante pasar el ID aquí
            nombre_producto=nombre_producto,
            stock=stock,
            precio=precio,
            descripcion=descripcion,
            codigo_barras=codigo_barras,
            usuario_id=usuario_id
        )
        self.repositorio_productos.actualizar_producto(producto_actualizado)

    def eliminar_producto(self, id_producto,usuario_id):
        self.repositorio_productos.eliminar_producto(id_producto,usuario_id)  

    def modificar_stock(self, id_producto, cantidad,usuario_id):
        # 1. Buscar el producto
        producto = self.repositorio_productos.obtener_producto_por_id(id_producto,usuario_id)
        if not producto:
            raise ValueError("Producto no encontrado")

        # 2. Modificar el stock usando la lógica del Dominio
        if cantidad > 0:
            producto.agg_stock(cantidad)
        elif cantidad < 0:
            # Enviamos el valor positivo a reducir_stock (ej: -1 se convierte en 1)
            producto.reducir_stock(abs(cantidad))
        
        # 3. Guardar cambios
        self.repositorio_productos.actualizar_producto(producto)              