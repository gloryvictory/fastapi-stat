from fastapi import APIRouter, Depends, HTTPException

from src.lstat.services import files_get_all_count, stat_get_all


router_stat = APIRouter(
    # prefix="/lstat",
    tags=["Статистика"]
)


# @router_files.get(path='/count',
#                   status_code=200,
#                   name='Получить количество Файлов',
#                   tags=['Файлы'],
#                   description='Получает количество Файлов')
# async def get_count():
#     content = await files_get_all_count()
#     return content


@router_stat.get(path="/",
                 status_code=200,
                 name='Получить список статистики',
                 tags=['Статистика'],
                 description='Получает список статистики'
                 )
async def get_all():
    content = await stat_get_all()
    return content
