from flask import Flask, jsonify, request, render_template
from database_config import SessionLocal
from infrastructure.productos_repository import ProductoRepository
from application.inventario_service import InventarioService

app = Flask(__name__)

# --- RUTA PARA EL FRONTEND ---
@app.route('/') # <--- NUEVO
def home():
    return render_template('index.html') # Busca el archivo en la carpeta /templates

# --- RUTA PARA VER TODOS LOS PRODUCTOS ---
# (Necesaria para que la tabla cargue todos los datos)
@app.route('/productos', methods=['GET'])
def listar_productos():
	session = SessionLocal()
	repo = ProductoRepository(session)
	servicio = InventarioService(repo)
	try:
		productos = servicio.obtener_todos()
		
		lista_final = []
		for p in productos:
				lista_final.append({
					'id_producto': p.id_producto,
					'nombre_producto': p.nombre_producto,
					'stock': p.stock,
					'precio': float(p.precio), # Importante convertir Decimal a float
					'descripcion': p.descripcion
				})
		return jsonify(lista_final)
	finally:
			session.close()

@app.route('/productos', methods=['POST','GET'])
def crear_producto():
	session = SessionLocal()
	repo = ProductoRepository(session)
	servicio = InventarioService(repo)
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
	finally:
		session.close()


@app.route('/productos/<int:id_producto>', methods=['GET'])
def obtener_producto(id_producto):
	session = SessionLocal()
	repo = ProductoRepository(session)
	servicio = InventarioService(repo)
	try:
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
	finally:
		session.close()



@app.route('/productos/<int:id_producto>', methods=['PUT'])
def actualizar_producto(id_producto):
	session = SessionLocal()
	repo = ProductoRepository(session)
	servicio = InventarioService(repo)

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
	finally:
		session.close()


@app.route('/productos/<int:id_producto>', methods=['DELETE'])
def eliminar_producto(id_producto):
	session = SessionLocal()
	repo = ProductoRepository(session)
	servicio = InventarioService(repo)

	try:
		servicio.eliminar_producto(id_producto)
		return jsonify({'message': 'Producto eliminado correctamente.'})
	except Exception as e:
		return jsonify({'error': str(e)}), 400
	finally:
		session.close()


if __name__ == '__main__':
	app.run(debug=True)