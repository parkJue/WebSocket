from django.apps import AppConfig
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def update_time_value():
    from .models import TimeModel
    try:
        obj = TimeModel.objects.get(pk=1)
    except TimeModel.DoesNotExist:
        obj = TimeModel(pk=1)
    obj.save()

class WebsocketAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'websocket_app'

    def ready(self):
        if self.name == 'websocket_app':
            scheduler = BackgroundScheduler()
            scheduler.add_job(update_time_value, 'interval', seconds=1)
            scheduler.start()