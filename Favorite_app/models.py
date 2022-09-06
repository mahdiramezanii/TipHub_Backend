from django.db import models
from Acount_app.models import User
from Tutorial_app.models import VideoTutorial

class Favorite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="favorite")
    video=models.ForeignKey(VideoTutorial,on_delete=models.CASCADE,related_name="favorite")
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user.username

