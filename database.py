
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = 'niit-master'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'
DB = 'sem7'

# dialect + driver://username:passwor@host:port/database
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
DB_PERCENT="%"

engine = create_engine(
    DB_URI,
    connect_args={},

)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()