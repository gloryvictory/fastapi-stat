from fastapi import APIRouter, Depends, HTTPException

from src.lstat.models import LSTAT_M
from src.lstat.services import stat_get_all, stat_create_item, stat_get_all_by_name

# prefix="/lstat",
router_stat = APIRouter(tags=["Статистика"])


@router_stat.get(path="/",
                 status_code=200,
                 name='Получить список статистики',
                 tags=['Статистика'],
                 description='Получает список статистики'
                 )
async def get_all():
    content = await stat_get_all()
    return content


@router_stat.post(path="/",
                  status_code=201,
                  name='Заполнить табличку статистики',
                  tags=['Статистика'],
                  description='Заполнить табличку статистики'
                  )
async def create_item(item: LSTAT_M):
    content = await stat_create_item(item)
    return content


@router_stat.get(path="/{fl_name}",
                 status_code=200,
                 name='Получить список по конкретному слою',
                 tags=['Статистика'],
                 description='Получает список статистики по конкретному слою. Пример: http://<server>:<port>/api/v1/lstat/db.user.table'
                 )
async def get_all(fl_name: str):
    content = await stat_get_all_by_name(fl_name)
    return content
