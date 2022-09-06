from django.shortcuts import render,redirect
from django.views.generic.base import View
from .models import Notification

class NotificationView(View):

    def get(self,request,id):
        notification=Notification.objects.get(id=id)
        re=notification.sender.get_absulot_url()
        notification.delete()
        return redirect(re)
