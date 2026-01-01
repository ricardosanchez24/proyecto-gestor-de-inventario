from domain.models import Producto

class ProductoRepository:
    def __init__ (self,session):
        self.session = session
        

    def guardar_producto(self, producto):
        self.session.add(producto)
        self.session.commit()
        self.session.refresh(producto)
    
    def obtener_todos(self):
        return self.session.query(Producto).all()

    def obtener_producto_por_id(self, id_producto):
        return self.session.query(Producto).filter(Producto.id_producto == id_producto).first()
    
    def actualizar_producto(self, producto):
        self.session.merge(producto)
        self.session.commit()

    def eliminar_producto(self, id_producto):
        producto_eliminar = self.session.query(Producto).filter(Producto.id_producto == id_producto).first()
        if producto_eliminar:
            self.session.delete(producto_eliminar)
            self.session.commit()