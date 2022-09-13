from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import TemplateView,ListView,DetailView,View
from Tutorial_app.models import VideoTutorial,Category,Comment,SubCategory,Techer
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Notification_app.models import Notification
from Favorite_app.models import Favorite
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from Home_app.mixins import CheckSoecial
from moviepy.video.io.VideoFileClip import VideoFileClip


class HomeView(ListView):
    model = VideoTutorial
    template_name = "Home_app/index.html"
    queryset = VideoTutorial.objects.filter(is_active=True)

class DetailVideo(CheckSoecial,DetailView):
    model = VideoTutorial
    template_name = "Home_app/video_detail.html"

    def get_context_data(self, **kwargs):
        context=super(DetailVideo, self).get_context_data(**kwargs)
        video=VideoTutorial.objects.get(slug=self.object.slug)
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
    def post(self,request,slug):
        user=request.user
        video=VideoTutorial.objects.get(slug=slug)
        body=request.POST.get("body")
        parent_id=request.POST.get("parent_id")
        Comment.objects.create(user=user,video=video,body=body,parent_id=parent_id)

        if parent_id != "":
            lastComment=Comment.objects.filter(id=parent_id).last()
            Notification.objects.create(user=lastComment.user,body="به پیام شما پاسخ داده شد",sender=video)
            Notification.objects.create(user=video.teacher.user,sender=video,body="یک نظر جدید به ویدیو شما اضافه شد")

        else:
            Notification.objects.create(user=video.teacher.user,sender=video, body="یک نظر جدید به ویدیو شما اضافه شد")
        return redirect(reverse("Home:detail_video",kwargs={"slug":slug}))

def CategoryVideo(request,slug):

    sub=SubCategory.objects.get(slug=slug)
    video=sub.videotutorial

    return render(request,"Home_app/CategoryVideo.html",{"video":video,"category1":sub})



class AllVideo(ListView):
    template_name = "Home_app/all_videos.html"
    model = VideoTutorial
    paginate_by = 1
    queryset = VideoTutorial.objects.filter(is_active=True)

class Search(View):

    def get(self,request):
        q=request.GET.get("q")
        page=request.GET.get("page")
        video=VideoTutorial.objects.filter(Q(titel__icontains=q) | Q(discription__icontains=q))

        paginator=Paginator(video,4)

        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request,"Home_app/search_video.html",{"object_list":users})


class AboutUs(ListView):
    template_name = "Home_app/about_us.html"
    model = Techer

    def get_queryset(self):
        teacher=Techer.objects.filter(is_active=True)
        return teacher


def FavorateView(request,slug):


    if request.user.is_authenticated:
        user = request.user
        video = VideoTutorial.objects.get(slug=slug)

        try:
            f = Favorite.objects.get(user=user,video=video)
            f.delete()


        except:

            Favorite.objects.create(user=user, video=video)

        return redirect("Home:detail_video", slug)
    else:
        return redirect("Home:detail_video",slug)




