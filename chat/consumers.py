# this is simple working channel

# import asyncio
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.exceptions import StopConsumer

# class MySyncConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         print("web connected")
#         await self.accept()

#     async def disconnect(self, event):
#         print("web disconnect", event)
#         raise StopConsumer

#     async def receive(self, text_data):
#         print("web received", text_data)
#         for i in range(5):
#             await asyncio.sleep(1)  
#             await self.send(text_data=str(i))


# chat app with default group name (static group name)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):


    def websocket_connect(self,event):
        print('websocket connect',event)
        print("channel layer",self.channel_layer)
        print("channelname",self.channel_name)
        async_to_sync (self.channel_layer.group_add)('coders',self.channel_name)


        self.send({

            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        print("msg recieved from client",event['text'])
        async_to_sync(self.channel_layer.group_send)('coders',{

            'type':'chat.message',
            'message':event['text']
        })
    

    def chat_message(self,event):
        print('event.........',event)
        self.send({

            'type':'websocket.send',
            'text':event['message']
        })



    def websocket_disconnect(self,event):
        print('diconnected',event)

        async_to_sync (self.channel_layer.group_discard)('coders',self.channel_name)
        raise StopConsumer()