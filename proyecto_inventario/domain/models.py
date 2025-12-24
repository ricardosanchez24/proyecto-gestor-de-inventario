class Producto:
    def __init__ (self, nombre_producto, stock, precio, descripcion, id_producto=None):
        self.nombre_producto = nombre_producto
        self.stock = stock
        self.precio = precio
        self.descripcion = descripcion
        self.id_producto = id_producto

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