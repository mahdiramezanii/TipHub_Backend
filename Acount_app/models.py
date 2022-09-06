from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):

        user = self.create_user(
            email,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username=models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    image = models.FileField(upload_to="user/image", default="defult/index.jpg", blank=True, null=True)
    is_teacher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    full_name=models.CharField(max_length=50)
    special_user=models.DateTimeField(default=timezone.now())


    objects = MyUserManager()

    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.email

    def is_specialuser(self):

        if self.special_user>timezone.now():
            return True
        return False

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Techer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="teacher")
    about_me=models.TextField()
    followers=models.ManyToManyField(User,related_name="followers",null=True,blank=True)
    slug=models.SlugField(null=True,blank=True,allow_unicode=True)
    resume=models.FileField(upload_to="teacher/cv",null=True,blank=True)
    is_active=models.BooleanField(default=False)


    def save(self,*args,**kwargs ):

        self.slug=slugify(self.user.full_name,allow_unicode=True)

        super(Techer,self).save(*args,**kwargs)

    def get_absolut_url(self):

        return reverse("Acount_app:profile_teacher",kwargs={"pk":self.id,"slug":self.slug})

    def teacher_active(self):

        if self.is_active == True:

            return True
        else:
            return False

    def __str__(self):
        return self.user.username
