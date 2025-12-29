from flask import Flask, jsonify, request, render_template
from database_config import obtener_conexion
from infrastructure.productos_repository import ProductoRepository
from application.inventario_service import InventarioService

app = Flask(__name__)

conexion = obtener_conexion()
if conexion is None:
	raise RuntimeError("No se pudo establecer la conexión a la base de datos. Revisa `database_config.py`")

repositorio = ProductoRepository(conexion)
servicio = InventarioService(repositorio)


# --- RUTA PARA EL FRONTEND ---
@app.route('/') # <--- NUEVO
def home():
    return render_template('index.html') # Busca el archivo en la carpeta /templates

# --- RUTA PARA VER TODOS LOS PRODUCTOS ---
# (Necesaria para que la tabla cargue todos los datos)
@app.route('/productos', methods=['GET'])
def listar_productos():
    productos = servicio.obtener_todos()
    lista = []
    for p in productos:
        lista.append({
            'id_producto': p.id_producto,
            'nombre_producto': p.nombre_producto,
            'stock': p.stock,
            'precio': float(p.precio),
            'descripcion': p.descripcion
        })
    return jsonify(lista)

@app.route('/productos', methods=['POST','GET'])
def crear_producto():
	try:
		data = request.get_json()
		nombre = data.get('nombre_producto')
		stock = int(data.get('stock', 0))
		precio = float(data.get('precio', 0))
		descripcion = data.get('descripcion', '')
		servicio.agregar_producto(nombre, stock, precio, descripcion)
		return jsonify({'message': 'Producto creado correctamente.'}), 201
	except Exception as e:
		return jsonify({'error': str(e)}), 400


@app.route('/productos/<int:id_producto>', methods=['GET'])
def obtener_producto(id_producto):
	producto = servicio.obtener_producto(id_producto)
	if not producto:
		return jsonify({'error': 'Producto no encontrado.'}), 404
	return jsonify({
		'id_producto': producto.id_producto,
		'nombre_producto': producto.nombre_producto,
		'stock': producto.stock,
		'precio': float(producto.precio),
		'descripcion': producto.descripcion
	})


@app.route('/productos/<int:id_producto>', methods=['PUT'])
def actualizar_producto(id_producto):
	try:
		data = request.get_json()
		nombre = data.get('nombre_producto')
		stock = int(data.get('stock', 0))
		precio = float(data.get('precio', 0))
		descripcion = data.get('descripcion', '')
		servicio.actualizar_producto(id_producto, nombre, stock, precio, descripcion)
		return jsonify({'message': 'Producto actualizado correctamente.'})
	except Exception as e:
		return jsonify({'error': str(e)}), 400


@app.route('/productos/<int:id_producto>', methods=['DELETE'])
def eliminar_producto(id_producto):
	try:
		servicio.eliminar_producto(id_producto)
		return jsonify({'message': 'Producto eliminado correctamente.'})
	except Exception as e:
		return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
	app.run(debug=True)