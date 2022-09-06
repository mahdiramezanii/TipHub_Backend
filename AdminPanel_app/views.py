from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView,FormView,View,UpdateView,DeleteView
from Tutorial_app.models import VideoTutorial,SubCategory,Tags
from .forms import CreateVideoForm
from Acount_app.models import Techer
from django.urls import reverse_lazy
from Notification_app.models import Messgae
from Acount_app.models import User
from .mixins import FildesMixin,ActiveTeacher

class DeletVideo(ActiveTeacher,DeleteView):
    model = VideoTutorial
    success_url = reverse_lazy("AdminPanel_app:admin_panel")

class Drafts(ActiveTeacher,ListView):
    template_name = "AdminPanel_app/index.html"
    model = VideoTutorial
    queryset = VideoTutorial.objects.filter(is_active=False)


class EditVideo(ActiveTeacher,UpdateView):
    template_name = "AdminPanel_app/createvideo.html"
    model = VideoTutorial
    fields = ["titel", "discription", "video_time", "video_cover", "video", "category", "tag","is_active","special_video"]
    success_url = reverse_lazy("AdminPanel_app:admin_panel")

class AdminPanelView(ActiveTeacher,ListView):
    template_name = "AdminPanel_app/index.html"
    model = VideoTutorial

    def get_queryset(self):
        v=super().get_queryset()
        return v.filter(teacher__user=self.request.user)



class CreateVideo(ActiveTeacher,View):


    def post(self,request):

        form=CreateVideoForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            return redirect("AdminPanel_app:admin_panel")

        return redirect("AdminPanel_app:create_video")

    def get(self,request):
        form = CreateVideoForm(request.POST,request.FILES)

        return render(request,"AdminPanel_app/createvideo.html",{"form":form})

class MessageView(ActiveTeacher,View):

    def post(self,request):
        message=request.POST.get("message")

        user=User.objects.all()
        for user in user:
            Messgae.objects.create(user=user,sender=request.user,body=message)
        return redirect("AdminPanel_app:message")

    def get(self,request):

        m=Messgae.objects.filter(sender=request.user)
        teacher=Techer.objects.get(user=request.user)
        followers=teacher.followers.all()


        return render(request,"AdminPanel_app/message.html",{"message":m,"followers":followers})

