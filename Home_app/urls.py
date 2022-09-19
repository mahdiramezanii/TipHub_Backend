from django.urls import path, re_path
from . import views

app_name = "Home"
urlpatterns = [
    path("", views.HomeView.as_view(), name="Home"),
    path("all_video/", views.AllVideo.as_view(), name="all_video"),
    path("about_us/", views.AboutUs.as_view(), name="about_us"),

]
