from django import forms
from django.forms import ValidationError
from Tutorial_app.models import VideoTutorial
from Acount_app.models import Techer

class CreateVideoForm(forms.ModelForm):

    class Meta:
        model=VideoTutorial
        exclude=("slug","view","teacher")


        widgets={
            "titel":forms.TextInput(attrs={
                "class":"form-control","placeholder":"عنوان ویدیو را وارد کنید"
            }),



            "discription": forms.Textarea(attrs={
                "class": "form-control", "placeholder": "توضیحات ویدیو را وارد کنید"
            }),

            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-label",
            }),

            "special_video": forms.CheckboxInput(attrs={
                "class": "form-check-label",
            }),
            "video_time":forms.TextInput(attrs={
                "placeholder":"تایم ویدیو را وارد کنید"
            })
        }




