from flask import Flask, jsonify, request, render_template
from database_config import SessionLocal,Base,engine
from infrastructure.productos_repository import ProductoRepository
from application.inventario_service import InventarioService
from infrastructure.usuarios_repository import UsuarioRepository
from application.autenticacion_service import AutenticacionServices
import jwt # para decodificar el token guardian
from functools import wraps # para crear el decorador
import os

app = Flask(__name__)
# CONFIGURAR LA CLAVE SECRETA	            CLAVE             CLAVE TEMPORAL POR SI NO SE ENCUENTRA LA CLAVE
app.config['SECRET_KEY'] = os.environ.get('CLAVE_SECRETA','CLAVE-TEMPORAL')
# forzando la creacion de tablas
with app.app_context():
	print("Intentando crear tablas en tiDB...")
	try:
		Base.metadata.create_all(bind=engine)
		print("Tablas creadas exitosamente")
	except Exception as e:
		print(f"Error al crear las tablas {e}")

#creacion de token personalizado
def token_requerido(f):
	@wraps(f)
	def decorador(*args,**kwargs):
		token = None

		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		else:
			return jsonify({'menssage': 'token no encontrado'}),400

		try:
			data = jwt.decode(token, app.config['SECRET KEY'],algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			return jsonify({'menssage': 'el token a expirado'}), 401
		except jwt.InvalidTokenError:
			return jsonify({'menssage': 'token invalido'}), 401
		
		return f(*args,**kwargs)

	return decorador			

# --- RUTA PARA EL FRONTEND ---
@app.route('/') # <--- NUEVO
def home():
    return render_template('index.html') # Busca el archivo en la carpeta /templates

# Rutas para mostrar las VISTAS (Páginas HTML)
@app.route('/ingresar') #login
def view_login():
    return render_template('login.html')

@app.route('/registrarse') # registro
def view_registro():
    return render_template('registro.html')

@app.route("/registro", methods = ['GET','POST'])
def registrar_usuario():
	session = SessionLocal()
	repo = UsuarioRepository(session)
	servicio = AutenticacionServices(repo)

	try:
		data = request.get_json()
		email = data['email']
		password = data['password']
		rol = data['rol']
		servicio.registrar_usuario(email,password,rol)
		return jsonify({'menssage': 'Usuario registrado con exito'}),200
	except Exception as e:
		return jsonify({'Error': str(e)}),400
	finally:
		session.close()	

@app.route('/login', methods = ['GET','POST'])
def login():
	session = SessionLocal()
	repo = UsuarioRepository(session)
	servicio = AutenticacionServices(repo)

	try:
		data = request.get_json()
		email = data['email']
		password = data['password']
		token = servicio.login(email,password)
		return jsonify({'token': token}), 200
	except Exception as e:
		return jsonify({'Error': str(e)}), 400
	finally:
		session.close()	

# --- RUTA PARA VER TODOS LOS PRODUCTOS ---
# (Necesaria para que la tabla cargue todos los datos)
@app.route('/productos', methods=['GET'])
@token_requerido
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
@token_requerido
def crear_producto():
	session = SessionLocal()
	repo = ProductoRepository(session)
	servicio = InventarioService(repo)
	try:
		data = request.get_json()
		nombre_producto = data.get('nombre_producto')
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
@token_requerido
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
@token_requerido
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
@token_requerido
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

@app.route('/productos/<int:id_producto>/stock', methods=['PATCH'])
@token_requerido
def actualizar_stock(id_producto):
    session = SessionLocal()
    repo = ProductoRepository(session)
    servicio = InventarioService(repo)
    
    try:
        data = request.get_json()
        cantidad = int(data.get('cantidad', 0)) # Puede ser 1 o -1
        
        servicio.modificar_stock(id_producto, cantidad)
        return jsonify({'message': 'Stock actualizado'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()		


if __name__ == '__main__':
	

	port = int(os.environ.get("PORT", 10000))
	app.run(host='0.0.0.0', port=port)			
	#app.run(debug=True)