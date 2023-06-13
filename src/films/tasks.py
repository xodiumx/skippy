import asyncio

from main.celery import celery_app

from .services import TaskService


@celery_app.task
def add_new_films_to_db() -> str:
    """Таска на добавление предстоящих фильмов в бд."""
    service = TaskService()
    asyncio.run(service.add_upcoming_films())
    return 'Films successfully added'
