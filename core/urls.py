from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("services/<int:pk>/", views.service_detail, name="service"),
    path("blog/", views.blog, name="blog"),
]
