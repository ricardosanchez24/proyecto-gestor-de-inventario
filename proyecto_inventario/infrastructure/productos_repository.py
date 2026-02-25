from domain.models import Producto

class ProductoRepository:
    def __init__ (self,session):
        self.session = session
        
    def guardar_producto(self, producto):
        self.session.add(producto)
        self.session.commit()
        self.session.refresh(producto)
    
    def obtener_todos_por_usuario(self,id_usuario):
        return self.session.query(Producto).filter(Producto.usuario_id == id_usuario).all()

    def obtener_producto_por_id(self, id_producto,id_usuario):
        return self.session.query(Producto).filter(
            Producto.id_producto == id_producto,
            Producto.usuario_id == id_usuario).first()
    
    def obtener_producto_codigo_barras(self,codigo_barras,id_usuario):
        return self.session.query(Producto).filter(
            Producto.codigo_barras == codigo_barras,
            Producto.usuario_id == id_usuario).first()
    
    def actualizar_producto(self, producto):
        self.session.merge(producto)
        self.session.commit()

    def eliminar_producto(self, id_producto,id_usuario):
        producto_eliminar = self.session.query(Producto).filter(
            Producto.id_producto == id_producto,
            Producto.usuario_id == id_usuario).first()
        if producto_eliminar:
            self.session.delete(producto_eliminar)
            self.session.commit()