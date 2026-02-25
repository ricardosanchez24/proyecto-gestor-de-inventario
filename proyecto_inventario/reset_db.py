from database_config import Base, engine
# Importamos los modelos para que SQLAlchemy los reconozca
from domain.models import Producto, Usuario 

def resetear_base_de_datos():
    print("Conectando a TiDB y borrando tablas antiguas...")
    # Esto elimina TODAS las tablas registradas
    Base.metadata.drop_all(bind=engine) 
    print("Tablas borradas con éxito.")
    
    print("Creando tablas nuevas con la columna usuario_id...")
    # Esto las vuelve a crear con la estructura actualizada
    Base.metadata.create_all(bind=engine) 
    print("¡Listo! Base de datos reseteada.")

if __name__ == "__main__":
    resetear_base_de_datos()