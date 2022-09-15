from django.shortcuts import render,redirect
from django.views.generic.base import View
from .models import Notification,Messgae

class NotificationView(View):

    def get(self,request,id):
        notification=Notification.objects.get(id=id)
        re=notification.sender.get_absulot_url()
        notification.delete()
        return redirect(re)

class MessageView(View):
    def get(self,request,id):
        message=Messgae.objects.get(id=id)

        message.delete()
        return redirect("Home:Home")

