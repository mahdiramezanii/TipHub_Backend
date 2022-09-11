from django.db import models
from Acount_app.models import User
from Tutorial_app.models import VideoTutorial
from django.utils.text import slugify
from django.urls import reverse
from exeption.utils import jalali_convert

class Notification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="notification",verbose_name="نام کاربری")
    body=models.TextField(verbose_name="متن اعلان")
    created=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    is_active=models.BooleanField(default=True)
    sender=models.ForeignKey(VideoTutorial,on_delete=models.CASCADE,related_name="notification",null=True,blank=True,verbose_name="فعال هست یا خیر")
    def get_absulot_url(self):
        return reverse("Notification:notification",kwargs={"id":self.id})


    def __str__(self):
        return f"{self.user.full_name} --> {self.body[:15]}"

    class Meta:
        ordering=("-created",)
        verbose_name="اعلان"
        verbose_name_plural="اعلانات"


class Messgae(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Message",verbose_name="کاربر")
    body = models.TextField(verbose_name="متن پیام")
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    is_active = models.BooleanField(default=True,verbose_name="فعال هست یا خیر")
    sender= models.ForeignKey(User, on_delete=models.CASCADE, related_name="message",verbose_name="ارسال کننده پیام")


    class Meta:
        ordering=("-created",)
        verbose_name="پیام"
        verbose_name_plural="پیام ها"


    def to_jalali(self):

        return jalali_convert(self.created)

    def get_absulot_url(self):
        return reverse("Notification:notification", kwargs={"id": self.id})

    def __str__(self):
        return f"{self.user.full_name} --> {self.body[:15]}"