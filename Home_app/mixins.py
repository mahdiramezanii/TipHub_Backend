from Tutorial_app.models import VideoTutorial
from django.shortcuts import redirect
class CheckSoecial:

    def dispatch(self,request,pk):
        video=VideoTutorial.objects.get(id=pk)
        teacher=video.teacher.id

        if video.special_video == True:
            if request.user.is_authenticated:
                if request.user.is_specialuser() or request.user.is_admin or request.user.id == teacher:
                    return super(CheckSoecial,self).dispatch(request,pk)
                else:
                    return redirect("Home:Home")
            return redirect("Home:Home")
        else:
            return super(CheckSoecial,self).dispatch(request,pk)