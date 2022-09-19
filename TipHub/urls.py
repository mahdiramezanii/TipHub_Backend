"""TipHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Home_app.urls")),
    path("acount/", include("Acount_app.urls")),
    path('accounts/', include('allauth.urls')),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='Acount_app/password/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="Acount_app/password/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='Acount_app/password/password_reset_complete.html'),
         name='password_reset_complete'),
    path("tutorial/", include("Tutorial_app.urls")),
    path("notification/",include("Notification_app.urls")),
    path("favorite/",include("Favorite_app.urls")),
    path("admin_panel/",include("AdminPanel_app.urls")),
    path("detail/",include("Tutorial_app.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
