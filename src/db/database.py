from sqlalchemy import create_engine, MetaData
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import db.credentials as cr

SQLALCHEMY_DATABASE_URL = (f'postgresql+psycopg2://{cr.name}:{cr.password}@{cr.host}:5432/fastapi_test')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

base = declarative_base()

metadata = MetaData(engine)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

base.metadata.create_all(engine)







