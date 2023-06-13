from typing import Annotated

from fastapi import APIRouter, Depends, Query

from fastapi_cache.decorator import cache

from .services import FilmService

router = APIRouter(
    prefix='/films',
    tags=['Films']
)


@router.get('/get_tops')
@cache(expire=120)
async def get_top_250(service: FilmService = Depends()) -> list:
    return await service.get_top_250_films_list()


@router.get('/get_film')
async def search_one_film(
    film: Annotated[str, Query(max_length=50)],
    service: FilmService = Depends()) -> dict:
    return await service.get_one_film(film)
