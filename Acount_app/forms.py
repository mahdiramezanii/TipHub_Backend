from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from Acount_app.models import User,Techer
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "نام کاربری خود را وارد کنید"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "password-input", "placeholder": "پسورد خود را وارد کنید"}))




    def clean_username(self):

        if User.objects.filter(username=self.cleaned_data.get('username')).exists():


            return self.cleaned_data.get("username")

        else:
            raise ValidationError("نام کاربری اشتباه است")

    def clean_password(self):

        user=authenticate(username=self.cleaned_data.get("username"),password=self.cleaned_data.get("password"))

        if user is not None:
            return self.cleaned_data.get("password")
        else:
            raise ValidationError("پسورد اشتباه است")


"""class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "text-input", "placeholder": "نام کاربری خود را وارد کنید"
    }))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "email-input", "placeholder": "ایمیل خود را وارد کنید"
    }))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        "class": "password-input", "plaseholder": "لطفا پسورد خود را وارد کنید"
    }))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        "class": "password-input", "plaseholder": "لطفا پسورد خود را مجددا وارد کنید"
    }))

    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("رمز ها شباهت ندارد!")

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data.get("username")).exists():
            raise ValidationError("نام کاربری تکراری است")
        else:
            return self.cleaned_data.get("username")

    def clean_email(self):

        if User.objects.filter(email=self.cleaned_data.get("email")).exists():
            raise ValidationError("ایمیل تکراری است")
        else:
            return self.cleaned_data.get("email")"""


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
    image=forms.ImageField()
    class Meta:
        model=User
        fields=["username","email","image","phone_number","full_name"]



class CreateTeacherForm(forms.Form):

    resume=forms.FileField()
    about_me=forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control"
        })
    )




