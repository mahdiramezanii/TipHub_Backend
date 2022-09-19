from django.shortcuts import redirect
from django.views.generic  import ListView,DetailView
from .models import Favorite
from Acount_app.mixin import CheckLogin
from Tutorial_app.models import VideoTutorial

class FavoritView(CheckLogin,ListView):
    template_name = "Favorite_app/favorite.html"
    model = Favorite
    def get_context_data(self,**kwargs):

        context=super(FavoritView,self).get_context_data(**kwargs)
        favorite_video=Favorite.objects.filter(user=self.request.user)

        context["video"]=favorite_video


        return context


def LikeVideo(request,pk):


    if request.user.is_authenticated:
        user = request.user
        video = VideoTutorial.objects.get(id=pk)

        try:
            f = Favorite.objects.get(user=user,video=video)
            f.delete()


        except:

            Favorite.objects.create(user=user, video=video)

        return redirect("Tutorial:detail", pk)
    else:
        return redirect("Tutorial:detail",pk)