from django.urls import path

from . import views

urlpatterns = [
    path("login", views.Login.as_view(), name="login"),
    path("register", views.Register.as_view(), name="register"),
    path("forgotpassword", views.ForgotPassword.as_view(), name="forgotpassword"),
    path("my_videos", views.MyVideos.as_view(), name="my_videos"),
    path("settings", views.Settings.as_view(), name="settings"),
    # path(
    #     "update/<str:username>/", UpdateProfileAPIView.as_view(), name="update_profile"
    # ),
]
