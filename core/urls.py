from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("blog/", views.blog, name="blog"),
    # path("", views.BaseIndexView.as_view(), name="index"),
    # path("about/", views.AboutView.as_view(), name="about"),
    # path("contact/", views.ContactView.as_view(), name="contact"),
]