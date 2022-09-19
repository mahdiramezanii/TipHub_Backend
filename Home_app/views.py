from django.shortcuts import render,redirect
from django.views.generic import ListView
from Tutorial_app.models import VideoTutorial,Techer



class HomeView(ListView):
    model = VideoTutorial
    template_name = "Home_app/index.html"
    queryset = VideoTutorial.objects.filter(is_active=True)

class AllVideo(ListView):
    template_name = "Home_app/all_videos.html"
    model = VideoTutorial
    paginate_by = 1
    queryset = VideoTutorial.objects.filter(is_active=True)

    def get_context_data(self,**kwargs):
        context=super(AllVideo, self).get_context_data(**kwargs)
        Most_viewed_video=VideoTutorial.objects.filter()



class AboutUs(ListView):
    template_name = "Home_app/about_us.html"
    model = Techer

    def get_queryset(self):
        teacher=Techer.objects.filter(is_active=True)
        return teacher







