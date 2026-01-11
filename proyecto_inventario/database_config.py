import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

db_url = os.environ.get('DATABASE_URL')

if not db_url:
    db_url = "mysql+pymysql://2H3RDvaTTfeiDqR.root:9QOIPNSg1l2wDmxF@gateway01.us-east-1.prod.aws.tidbcloud.com:4000/test?ssl_ca=/etc/ssl/certs/ca-certificates.crt&ssl_verify_cert=true&ssl_verify_identity=true"

#db_url = 'mysql+pymysql://root:123456789@localhost/gestor_inventario'
engine = create_engine(db_url, pool_pre_ping=True) # hace la conexion con la base de datos
SessionLocal = sessionmaker(bind=engine) # crea una fabrica de sesiones no las sesiones en si
Base = declarative_base() # crear un cajon de etiquetas para que sqlalchemy sepa que codigo tiene que traducir a sql