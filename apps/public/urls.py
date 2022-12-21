from django.urls import path

from . import views

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("templates", views.templates.as_view(), name="templates"),
    path("pricing", views.pricing.as_view(), name="pricing"),
    path("faqs", views.faqs.as_view(), name="faqs"),
    path("contact", views.contact.as_view(), name="contact"),
    # path(
    #     "update/<str:username>/", UpdateProfileAPIView.as_view(), name="update_profile"
    # ),
]
