from django.urls import path
from . import views

app_name="favorite"
urlpatterns=[
    path("",views.FavoritView.as_view(),name="favorite")
]