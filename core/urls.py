from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
]

admin.site.site_header = "Intropixel"
admin.site.site_title = "Intropixel Admin Panel"
admin.site.index_title = "Welcome to Intropixel Admin Panel"
