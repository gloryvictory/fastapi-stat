from fastapi import APIRouter, Depends, HTTPException

from src.lstat.models import TEST_M
from src.lstat.services import files_get_all_count, stat_get_all, stat_create_item

router_stat = APIRouter(
    # prefix="/lstat",
    tags=["Статистика"]
)


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
async def create_item(item: TEST_M):
    content = await stat_create_item(item)
    return content
