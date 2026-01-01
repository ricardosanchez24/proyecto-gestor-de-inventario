import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



db_url = 'mysql+pymysql://root:123456789@localhost/gestor_inventario'
engine = create_engine(db_url) # hace la conexion con la base de datos
SessionLocal = sessionmaker(bind=engine) # crea una fabrica de sesiones no las sesiones en si
Base = declarative_base() # crear un cajon de etiquetas para que sqlalchemy sepa que codigo tiene que traducir a sql