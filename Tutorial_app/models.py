from django.db import models
from Acount_app.models import User,Techer
from django.utils.text import slugify
from django.urls import reverse
from exeption.utils import jalali_convert
from django.utils import timezone


class Tags(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام تگ")
    created=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name="تگ"
        verbose_name_plural="تگ ها"


    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام دسته بندی")
    created=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی ها"

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category=models.ManyToManyField(Category,related_name="subcategory",verbose_name="نام دسته بندی مرجع")
    name=models.CharField(max_length=30,verbose_name="نام دسته بندی")
    slug=models.SlugField(null=True,blank=True,allow_unicode=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی ها"

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name,allow_unicode=True)
        super(SubCategory, self).save(*args,**kwargs)

    def __str__(self):
        return self.name

class VideoTutorial(models.Model):
    teacher=models.ForeignKey(Techer,on_delete=models.CASCADE,related_name="video_tutorial",verbose_name="مدرس")
    video=models.FileField(upload_to="videototorial/video",verbose_name="ویدیو")
    titel=models.CharField(max_length=100,unique=True,verbose_name="عنوان")
    video_cover=models.FileField(upload_to="videotutorial/iamge",verbose_name="کاور ویدیو")
    video_time=models.TimeField(verbose_name="ویدیو")
    created=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    view=models.IntegerField(default=0,verbose_name="تعداد بازدید")
    discription=models.TextField(verbose_name="توضیحات ویدیو")
    tag=models.ManyToManyField(Tags,related_name="videotutorial",verbose_name="تگ ها")
    category=models.ManyToManyField(SubCategory,related_name="videotutorial",verbose_name="دسته بندی ها")
    slug=models.SlugField(null=True,blank=True,allow_unicode=True)
    is_active=models.BooleanField(default=False,verbose_name="ویدیو فعال هست یا خیر؟")
    special_video=models.BooleanField(verbose_name="مخصوص اعضای ویژه؟")






    class Meta:

        ordering=("-created",)
        verbose_name="ویدیو"
        verbose_name_plural="ویدیوها"

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
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment",verbose_name="کاربر")
    video=models.ForeignKey(VideoTutorial,on_delete=models.CASCADE,related_name="comment",verbose_name="ویدیو")
    parent=models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE,related_name="replay",verbose_name="کامنت مرجع")
    body=models.TextField(verbose_name="متن کامنت")
    created=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")



    class Meta:
        ordering=("created",)
        verbose_name="کامنت"
        verbose_name_plural="کامنت ها"

    def __str__(self):
        return f"{self.user.full_name}, --> {self.body[:15]}"