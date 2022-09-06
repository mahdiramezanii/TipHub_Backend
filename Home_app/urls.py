from django.urls import path, re_path
from . import views

app_name = "Home"
urlpatterns = [
    path("", views.HomeView.as_view(), name="Home"),
    re_path(r'detail/(?P<slug>[-\w]+)/', views.DetailVideo.as_view(), name="detail_video"),
    re_path(r'category/(?P<slug>[-\w]+)/', views.CategoryVideo, name="category"),
    path("all_video/", views.AllVideo.as_view(), name="all_video"),
    path("search/", views.Search.as_view(), name="search"),
    path("about_us/", views.AboutUs.as_view(), name="about_us"),
    re_path(r'favorite/(?P<slug>[-\w]+)/', views.FavorateView, name="favorite"),
]
