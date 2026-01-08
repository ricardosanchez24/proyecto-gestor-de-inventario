from domain.models import Usuario

class UsuarioRepository:
    def __init__(self,session):
        self.session = session

    def guardar_usuario(self,usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def listar_todos_usuarios(self):
       return self.session.query(Usuario).all()
    
    def buscar_usuario_email(self,email):
        return self.session.query(Usuario).filter(Usuario.email == email).first()
    
    def actualizar_usuario(self,usuario):
        self.session.merge(usuario)
        self.session.commit

    def eliminar_usuario(self,usuario):
        self.session.delete(usuario)
        self.session.commit