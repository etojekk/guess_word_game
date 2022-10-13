from sqlalchemy import create_engine, MetaData
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import fastapy_word_parser.new_create_test.db.credentials as cr

SQLALCHEMY_DATABASE_URL = (f'postgresql+psycopg2://{cr.name}:{cr.password}@localhost:5432/fastapitest')


engine = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=NullPool)

base = declarative_base()

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

base.metadata.create_all(engine)

metadata = MetaData(engine)





