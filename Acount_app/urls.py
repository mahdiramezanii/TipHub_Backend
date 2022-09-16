from django.urls import path,re_path
from . import views

app_name = "Acount_app"
urlpatterns = [
    path("", views.ProfileUser.as_view(), name="profile"),
    path("edit_profile", views.ProfileEdit.as_view(), name="profile_edit"),
    path("login/", views.LoginView.as_view(), name="Login"),
    path("logout/", views.LogoutView.as_view(), name="Logout"),
    path("register/", views.RegisterView.as_view(), name='Register'),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
    path("password_reset", views.PasswordResetRequest.as_view(), name="password_reset"),
    re_path(r'^profile/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)',views.ProfileTeacher.as_view(), name="profile_teacher"),
    path("create_teacher",views.CreateTeacher.as_view(),name="create_teacher")

]
