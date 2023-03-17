from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE CREDENTIALS
user = 'root'
password = '1234'
host = 'localhost'
port = '3310'
database = 'apiRestTest'

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
