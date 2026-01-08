from database_config import Base
from sqlalchemy import String, INTEGER, Column,DECIMAL

class Producto(Base):
    __tablename__ = "productos"
    id_producto = Column(INTEGER, nullable=False, primary_key=True,autoincrement=True)
    nombre_producto = Column(String(55), nullable=False)
    stock = Column(INTEGER, nullable=False)
    precio = Column(DECIMAL(10,2), nullable=False)
    descripcion = Column(String(250))

    def validar_producto(self):
        if not self.nombre_producto:
            raise ValueError("El nombre del producto no puede estar vacío.")
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        return True    
    
    def agg_stock(self, cantidad):
        if self.stock + cantidad < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.stock += cantidad
        return self.stock
    
    def reducir_stock(self, cantidad):
        if self.stock - cantidad < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.stock -= cantidad
        return self.stock
    
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = nuevo_precio
        return self.precio
    
    def __str__(self):
        return f"Producto(id: {self.id_producto}, nombre: {self.nombre_producto}, stock: {self.stock}, precio: {self.precio}, descripcion: {self.descripcion})"
    

class Usuario(Base):
    __tablename__ ="Usuarios"
    id_usuario = Column(INTEGER, nullable=False,primary_key=True,autoincrement=True,unique=True)   
    email = Column(String(250),nullable=False,unique=True)
    password = Column(String(300),nullable=False)
    rol = Column(String(75))