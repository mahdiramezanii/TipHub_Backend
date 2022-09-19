from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from Home_app.mixins import CheckSoecial
from django.views.generic import DetailView,View
from Tutorial_app.models import VideoTutorial,Category,SubCategory,Comment
from Favorite_app.models import Favorite
from Notification_app.models import Notification,Messgae
from django.shortcuts import redirect
from django.urls import reverse



class DetailVideo(CheckSoecial,DetailView):
    model = VideoTutorial
    template_name = "Tutorial_app/video_detail.html"

    def get_context_data(self, **kwargs):
        context=super(DetailVideo, self).get_context_data(**kwargs)
        video=VideoTutorial.objects.get(id=self.object.id)
        video.view+=1
        video.save()

        #chcke like
        if self.request.user.is_authenticated:
            if Favorite.objects.filter(user=self.request.user,video=video).exists():
                context["is_like"]=True
            else:
                context["is_like"]=False

        #زcomment pagination
        _comment=Comment.objects.filter(video=video)
        paginator=Paginator(_comment,2)
        page=self.request.GET.get("page")
        context["comment"]=paginator.get_page(page)

        return context

    #create comment an notification
    def post(self,request,pk):
        user=request.user
        video=VideoTutorial.objects.get(id=pk)
        body=request.POST.get("body")
        parent_id=request.POST.get("parent_id")
        Comment.objects.create(user=user,video=video,body=body,parent_id=parent_id)

        if parent_id != "":
            lastComment=Comment.objects.filter(id=parent_id).last()
            Notification.objects.create(user=lastComment.user,body="به پیام شما پاسخ داده شد",sender=video)
            Notification.objects.create(user=video.teacher.user,sender=video,body="یک نظر جدید به ویدیو شما اضافه شد")

        else:
            Notification.objects.create(user=video.teacher.user,sender=video, body="یک نظر جدید به ویدیو شما اضافه شد")
        return redirect(reverse("Tutorial:detail_video",kwargs={"pk":pk}))

def CategoryVideo(request,pk):

    sub=SubCategory.objects.get(id=pk)
    video=sub.videotutorial

    return render(request,"Tutorial_app/CategoryVideo.html",{"video":video,"category1":sub})



class Search(View):

    def get(self,request):
        q=request.GET.get("q")
        page=request.GET.get("page")
        video=VideoTutorial.objects.filter(Q(titel__icontains=q) | Q(discription__icontains=q) | Q(teacher__slug__icontains=q))

        paginator=Paginator(video,4)

        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request,"Tutorial_app/search_video.html",{"object_list":users})