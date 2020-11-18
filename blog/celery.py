from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('blog')
app.config_from_object('django.config.settings', namespace= 'CELERY')
app.autodiscover_tasks()