# image_parroter/image_parroter/__init__.py

from .celery import celery_app

# importable from all to all places
__all__ = ('celery_app',)
