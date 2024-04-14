import json, asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import TimeModel
from django.db import connection

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = await self.get_time()
                await self.send(text_data=json.dumps({"time":data}))
            except Exception as e:
                print(f'에러 발생 : {e}')
                break
            await asyncio.sleep(1)
        
    @sync_to_async
    def get_time(self):
        try:
            result = TimeModel.objects.latest('time').time.strftime('%Y-%m-%d %H:%M:%S.%f')
        finally:
            connection.close()
        return result
    
    async def disconnect(self, close_code):
        pass