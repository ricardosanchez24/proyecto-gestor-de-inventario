from domain.models import Usuario
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
from datetime import timedelta, datetime

class AutenticacionServices:
    def __init__(self,usuarios_repository):
        self.usuarios_repository = usuarios_repository

    def registrar_usuario(self, email, password, rol):
        #validar
        buscar_usuario = self.usuarios_repository.buscar_usuario_email(email)
        if buscar_usuario:
            raise ValueError("Error, el usuario ya existe")
        #encriptar contraseña
        password_hash = generate_password_hash(password)
        #registrar usuario    
        nuevo_usuario = Usuario(
            email = email,
            password = password_hash,
            rol = rol
        )
        self.usuarios_repository.guardar_usuario(nuevo_usuario)


    def login(self,email,password):
        #buscar y validar usuario
        usuario = self.usuarios_repository.buscar_usuario_email(email)
        if not usuario:
            return None
        if not check_password_hash(usuario.password,password): #checkea el password del usuario y lo compara con el password que le enviaron
            return None
        #guardamos la info del usuario si todo sale bien
        payload = {
            'user_id': usuario.id_usuario,
            'rol': usuario.rol,
            'now': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        #creamos el token con la info del usuario,nuestra llave secreta y escogiendo el algoritmo de encriptacion
        token = jwt.encode(payload,'SECRET_KEY',algorithm='HS256')
        #retornamos el token
        return token         