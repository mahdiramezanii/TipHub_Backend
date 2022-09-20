from django.views.generic import TemplateView,ListView,DetailView,View
from Tutorial_app.models import VideoTutorial,Category,Comment,SubCategory,Techer



class HomeView(ListView):
    model = VideoTutorial
    template_name = "Home_app/index.html"
    queryset = VideoTutorial.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        most_view_video = VideoTutorial.objects.filter(view__gt=50,is_active=True)[:6]
        context["most_view"] = most_view_video
        return context

class MostViewVideo(ListView):
    model = VideoTutorial
    template_name = "Home_app/all_videos.html"
    queryset = VideoTutorial.objects.filter(view__gt=50,is_active=True)
    paginate_by = 2



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







