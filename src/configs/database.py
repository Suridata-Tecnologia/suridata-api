from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ

connection_url = engine.url.URL.create(
    drivername = 'mysql+pymysql',
    username   = environ.get('DB_USER', 'root'),
    password   = environ.get('DB_PASS', ''),
    host       = environ.get('DB_HOST', '127.0.0.1'),
    database   = environ.get('DB_NAME', 'suridata_portal'),
    port       = 3306,
)
engine = create_engine(connection_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def setup_database():
    Base.metadata.create_all(bind=engine)