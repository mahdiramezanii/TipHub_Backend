from django.contrib import admin
from .models import Notification,Messgae

@admin.register(Notification)
class Notification(admin.ModelAdmin):
    pass
@admin.register(Messgae)
class Message(admin.ModelAdmin):
    pass