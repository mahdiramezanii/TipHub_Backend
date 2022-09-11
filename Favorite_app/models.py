from django.db import models
from Acount_app.models import User
from Tutorial_app.models import VideoTutorial

class Favorite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="favorite",verbose_name="نام کاربری")
    video=models.ForeignKey(VideoTutorial,on_delete=models.CASCADE,related_name="favorite",verbose_name="ویدیو")
    created=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name="علاقه مندی"
        verbose_name_plural="علاقه مندی ها"
    def __str__(self):

        return self.user.username

