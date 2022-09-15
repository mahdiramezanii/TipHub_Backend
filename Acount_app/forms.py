from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from Acount_app.models import User, Techer
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "نام کاربری یا ایمیل خود را وارد کنید"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "password-input", "placeholder": "پسورد خود را وارد کنید"}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            raise ValidationError("نام کاربری یا پسورد اشتباه است")



class SignupForm(UserCreationForm):
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        "class": "password-input", "placeholder": "لطفا پسورد خود را وارد کنید"
    }))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        "class": "password-input", "placeholder": "لطفا پسورد خود را مجددا وارد کنید"
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "text-input", "placeholder": "نام کاربری خود را وارد کنید"
            }),
            "email": forms.TextInput(attrs={
                "class": "email-input", "placeholder": "ایمیل خود را وارد کنید"
            }),

            "password1": forms.TextInput(attrs={
                "class": "password-input", "placeholder": "لطفا پسورد خود را وارد کنید"
            }),

            "password2": forms.TextInput(attrs={
                "class": "password-input", "placeholder": " پسورد خود را مجددا وارد کنید"
            }),
        }


class EditUserForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ["username", "email", "image", "phone_number", "full_name"]

        widgets={
            "image":forms.FileInput(attrs={
                "class":"form-control",

            }),

        }


class CreateTeacherForm(forms.Form):
    resume = forms.FileField()
    about_me = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control"
        })
    )
