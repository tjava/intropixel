from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("templates", views.Templates.as_view(), name="templates"),
    path("edit_template", views.EditTemplate.as_view(), name="edit_template"),
    path("pricing", views.Pricing.as_view(), name="pricing"),
    path("faqs", views.Faqs.as_view(), name="faqs"),
    path("contact", views.Contact.as_view(), name="contact"),
    # path(
    #     "update/<str:username>/", UpdateProfileAPIView.as_view(), name="update_profile"
    # ),
]
