# from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, TEXT, BIGINT
from datetime import datetime
from typing import Optional

import ormar


from src.database import database, metadata

# from uuid import uuid4 as uuid
# uid: uuid = ormar.UUID(primary_key=True, default=uuid)


# metadata = MetaData()
class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class BaseClass(ormar.Model):
    class Meta(MainMeta):
        abstract = True
        # tablename = "Fields"
        pass

    id: Optional[int] = ormar.Integer(primary_key=True)
    fl_db: str = ormar.String(max_length=255, index=True)
    fl_name: str = ormar.String(max_length=255, index=True)
    fl_title: str = ormar.String(max_length=255, index=True)
    fl_count:int = ormar.BigInteger()
    fl_guid: str = ormar.String(max_length=255, index=True)
    fl_date: Optional[datetime] = ormar.DateTime(default=datetime.now)


class TEST_M(BaseClass):
    class Meta(MainMeta):
        tablename = "TEST"
        pass


