from Acount_app.models import Techer
from django.shortcuts import redirect
class FildesMixin():

    def dispatch(self,request,*args,**kwargs):

        if request.user.is_superuser:
            self.fields=["taecher","titel","discription","video_time","vidoe_cover","video","category","tag"]

        else:
            self.fields = ["titel", "discription", "video_time", "vidoe_cover", "video", "category", "tag"]

        return super().dispatch(request, *args, **kwargs)

class ActiveTeacher:

    def dispatch(self,request,*args,**kwargs):


        if request.user.is_authenticated:
            user = request.user
            teacher = Techer.objects.get(user=user)

            if teacher.is_active == True:

                return super().dispatch(request,*args,**kwargs)

            else:
                return redirect("Home:Home")
        return redirect("Home:Home")
