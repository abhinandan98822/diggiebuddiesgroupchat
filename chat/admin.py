from django.contrib import admin

from chat.models import Room, Message,FileModel

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(FileModel)
