from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, "public/index.html")


class Templates(View):
    def get(self, request):
        return render(request, "public/templates.html")


class EditTemplate(View):
    def get(self, request):
        return render(request, "public/edit_template.html")


class Pricing(View):
    def get(self, request):
        return render(request, "public/pricing.html")


class Faqs(View):
    def get(self, request):
        return render(request, "public/faqs.html")


class Contact(View):
    def get(self, request):
        return render(request, "public/contact.html")
