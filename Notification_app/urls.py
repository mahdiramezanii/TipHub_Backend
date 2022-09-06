from django.urls import path
from . import views

app_name="Notification"
urlpatterns=[
    path("notification/<int:id>",views.NotificationView.as_view(),name="notification")
]