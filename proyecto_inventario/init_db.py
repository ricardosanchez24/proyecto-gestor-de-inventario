from database_config import Base, engine
from domain.models import Producto


def inicializar_base_datos():
    Base.metadata.create_all(bind=engine) #esto dice  toma todos los modelos registrados en base y crea sus tablas en el motor (engine) si no existen
    print("Base de datos iniciada")

if __name__ == "__main__":
    inicializar_base_datos()  