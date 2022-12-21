from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class index(View):
    def get(self, request):
        return render(request, "public/index.html")


class templates(View):
    def get(self, request):
        return render(request, "public/templates.html")


class pricing(View):
    def get(self, request):
        return render(request, "public/pricing.html")


class faqs(View):
    def get(self, request):
        return render(request, "public/faqs.html")


class contact(View):
    def get(self, request):
        return render(request, "public/contact.html")
