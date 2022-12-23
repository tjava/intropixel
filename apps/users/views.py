from django.shortcuts import render
from django.views import View

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "users/login.html")


class Register(View):
    def get(self, request):
        return render(request, "users/register.html")


class MyVideos(View):
    def get(self, request):
        return render(request, "users/my_videos.html")


class Settings(View):
    def get(self, request):
        return render(request, "users/settings.html")


class ForgotPassword(View):
    def get(self, request):
        return render(request, "users/forgotpassword.html")
