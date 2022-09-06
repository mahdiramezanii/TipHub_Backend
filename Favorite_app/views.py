from django.shortcuts import render
from django.views.generic  import ListView,DetailView
from .models import Favorite
from Acount_app.mixin import CheckLogin
class FavoritView(CheckLogin,ListView):
    template_name = "Favorite_app/favorite.html"
    model = Favorite
    def get_context_data(self,**kwargs):

        context=super(FavoritView,self).get_context_data(**kwargs)
        favorite_video=Favorite.objects.filter(user=self.request.user)

        context["video"]=favorite_video

        return context