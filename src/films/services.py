import aiohttp

from main.settings import settings


key = settings.imdb_key


class FilmService:

    async def get_top_250_films_list() -> list[dict]:
        """Получение топ-250 фильмов."""
        timeout = aiohttp.ClientTimeout(total=60)
        endpoint = f'https://imdb-api.com/en/API/Top250Movies/{key}'

        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint, timeout=timeout) as response:
                data = await response.json()
                return data.get('items')
        # TODO: raise exception and schema

    async def get_one_film(film: str) -> dict:
        timeout = aiohttp.ClientTimeout(total=60)
        endpoint = f'https://imdb-api.com/en/API/SearchMovie/{key}/{film}'

        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint, timeout=timeout) as response:
                data = await response.json()
                return data.get('results')[0]
        # TODO: raise exception and schema