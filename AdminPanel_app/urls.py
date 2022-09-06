from django.urls import path,re_path
from . import views

app_name="AdminPanel_app"
urlpatterns=[
    path("",views.AdminPanelView.as_view(),name="admin_panel"),
    path("drafts",views.Drafts.as_view(),name="admin_panel_drafts"),
    path("create_video/",views.CreateVideo.as_view(),name="create_video"),
    re_path(r'edit/(?P<slug>[-\w]+)/', views.EditVideo.as_view(), name="edit_video"),
    re_path(r'delet/(?P<slug>[-\w]+)/', views.DeletVideo.as_view(), name="delet_video"),
    path("message/",views.MessageView.as_view(),name="message")
]