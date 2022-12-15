import os
from celery import Celery

#                                               or the_forum/
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_forum.settings')
celery_app = Celery('the_forum')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
# celery discovers the tasks alone
celery_app.autodiscover_tasks()
