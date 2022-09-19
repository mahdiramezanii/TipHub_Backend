from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import TemplateView,ListView,DetailView,View
from Tutorial_app.models import VideoTutorial,Category,Comment,SubCategory,Techer
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Notification_app.models import Notification
from Favorite_app.models import Favorite
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from Home_app.mixins import CheckSoecial
from moviepy.video.io.VideoFileClip import VideoFileClip


class HomeView(ListView):
    model = VideoTutorial
    template_name = "Home_app/index.html"
    queryset = VideoTutorial.objects.filter(is_active=True)





class AllVideo(ListView):
    template_name = "Home_app/all_videos.html"
    model = VideoTutorial
    paginate_by = 1
    queryset = VideoTutorial.objects.filter(is_active=True)




class AboutUs(ListView):
    template_name = "Home_app/about_us.html"
    model = Techer

    def get_queryset(self):
        teacher=Techer.objects.filter(is_active=True)
        return teacher







