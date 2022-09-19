from django.urls import path
from . import views

app_name = "Tutorial"
urlpatterns = [
    path("detail/<int:pk>", views.DetailVideo.as_view(), name="detail"),
    path("category/<int:pk>", views.CategoryVideo, name="category"),
    path("search/", views.Search.as_view(), name="search"),

]
