from django.db import models
from Acount_app.models import User,Techer
from django.utils.text import slugify
from django.urls import reverse
from exeption.utils import jalali_convert
from django.utils import timezone


class Tags(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category=models.ManyToManyField(Category,related_name="subcategory")
    name=models.CharField(max_length=30)
    slug=models.SlugField(null=True,blank=True,allow_unicode=True)
    created=models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name,allow_unicode=True)
        super(SubCategory, self).save(*args,**kwargs)

    def __str__(self):
        return self.name

class VideoTutorial(models.Model):
    teacher=models.ForeignKey(Techer,on_delete=models.CASCADE,related_name="video_tutorial")
    video=models.FileField(upload_to="videototorial/video")
    titel=models.CharField(max_length=100,unique=True)
    video_cover=models.FileField(upload_to="videotutorial/iamge")
    video_time=models.TimeField()
    created=models.DateTimeField(auto_now_add=True)
    view=models.IntegerField(default=0)
    discription=models.TextField()
    tag=models.ManyToManyField(Tags,related_name="videotutorial")
    category=models.ManyToManyField(SubCategory,related_name="videotutorial")
    slug=models.SlugField(null=True,blank=True,allow_unicode=True)
    is_active=models.BooleanField(default=False)
    special_video=models.BooleanField()




    class Meta:

        ordering=("-created",)

    def to_jalali(self):

        return jalali_convert(self.created)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.titel,allow_unicode=True)

        super(VideoTutorial,self).save(*args,**kwargs)

    def get_absulot_url(self):

        return reverse("Home:detail_video",kwargs={"slug":self.slug})

    def __str__(self):
        return f"{self.teacher.user.full_name} --> {self.titel}"



class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment")
    video=models.ForeignKey(VideoTutorial,on_delete=models.CASCADE,related_name="comment")
    parent=models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE,related_name="replay")
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering=("created",)

    def __str__(self):
        return f"{self.user.full_name}, --> {self.body[:15]}"