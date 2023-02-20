from datetime import datetime

from pydantic import BaseModel


class TEST_S(BaseModel):
    id: int
    fl_db: str
    fl_name: str
    fl_title: str
    fl_count:int
    fl_guid: str
    fl_date: datetime

    class Config:
        orm_mode = True

