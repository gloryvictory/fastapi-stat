# alembic revision --autogenerate -m "Initial commit"
# alembic upgrade <#revision>
# alembic upgrade head


import databases
import sqlalchemy

from src import cfg

# sys.path.append("..")
engine = sqlalchemy.create_engine(cfg.DB_DSN)
database = databases.Database(cfg.DB_DSN)
metadata = sqlalchemy.MetaData(schema=cfg.DB_SCHEMA) # чтобы складывать в одну схему
