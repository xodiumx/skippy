from __future__ import absolute_import

from celery import Celery
from celery.schedules import crontab

from .settings import settings

packages = ['films']

celery_app = Celery(__name__)
celery_app.conf.broker_url = settings.celery_broker
celery_app.conf.result_backend = settings.celery_result_backend

celery_app.autodiscover_tasks(packages=packages, force=True)

celery_app.conf.beat_schedule = {
    'update_upcoming_films': {
        'task': 'films.tasks.add_new_films_to_db',
        'schedule': crontab(minute='*/1'),
    },
}
celery_app.conf.timezone = 'UTC'
