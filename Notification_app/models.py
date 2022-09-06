from django.db import models
from Acount_app.models import User
from Tutorial_app.models import VideoTutorial
from django.utils.text import slugify
from django.urls import reverse
from exeption.utils import jalali_convert

class Notification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="notification")
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    sender=models.ForeignKey(VideoTutorial,on_delete=models.CASCADE,related_name="notification",null=True,blank=True)
    def get_absulot_url(self):
        return reverse("Notification:notification",kwargs={"id":self.id})

    def __str__(self):
        return f"{self.user.full_name} --> {self.body[:15]}"

    class Meta:
        ordering=("-created",)


class Messgae(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Message")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    sender= models.ForeignKey(User, on_delete=models.CASCADE, related_name="message")


    class Meta:
        ordering=("-created",)


    def to_jalali(self):

        return jalali_convert(self.created)

    def get_absulot_url(self):
        return reverse("Notification:notification", kwargs={"id": self.id})

    def __str__(self):
        return f"{self.user.full_name} --> {self.body[:15]}"