import aiohttp

from sqlalchemy import delete

from main.db import get_async_session
from main.settings import settings

from .utils import get_date
from .models import FilmModel


key = settings.imdb_key


class BaseService:

    @classmethod
    async def get_data_from_http_session(cls, endpoint: str) -> dict:
        """Получение данных от endpoint-a через aiohttp session."""
        timeout = aiohttp.ClientTimeout(total=60)
        async with aiohttp.ClientSession() as http_session:
            async with http_session.get(endpoint, timeout=timeout) as response:
                data = await response.json()
                return data


class FilmService(BaseService):

    async def get_top_250_films_list(self) -> list[dict]:
        """Получение топ-250 фильмов."""
        endpoint = f'https://imdb-api.com/en/API/Top250Movies/{key}'
        data = await self.get_data_from_http_session(endpoint)
        return data.get('items')
        # TODO: raise exception and schema

    async def get_one_film(self, film: str) -> dict:
        endpoint = f'https://imdb-api.com/en/API/SearchMovie/{key}/{film}'
        data = await self.get_data_from_http_session(endpoint)
        return data.get('results')[0]
        # TODO: raise exception and schema


class TaskService(BaseService):

    async def add_upcoming_films(self) -> None:
        """
        - Создание сессии с бд
        - Получение данных от endpoint-a
        - Формирование списка фильмов с необходимыми полями
        - Удаление старых фильмов в бд
        - Добавление новых сформированных фильмов
        """
        db_session = get_async_session()
        db_session = await db_session.__anext__()
        endpoint = f'https://imdb-api.com/en/API/ComingSoon/{key}'
        data = await self.get_data_from_http_session(endpoint)

        films = []
        for film in data.get('items'):
            new_film = {}
            new_film['key'] = film.get('id')
            new_film['title'] = film.get('fullTitle')
            new_film['genres'] = film.get('genres')
            new_film['image'] = film.get('image')
            new_film['release_date'] = get_date(
                                    film.get('releaseState'))
            new_film['trailer'] = None
            # TODO: добавить youtube trailer через id
            films.append(FilmModel(**new_film))

        query = delete(FilmModel)
        await db_session.execute(query)
        db_session.add_all(films)
        await db_session.commit()
