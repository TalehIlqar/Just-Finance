from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("services/<slug:slug>/", views.service_detail, name="service_detail"),
    path("blogs/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("blogs/", views.blog, name="blogs"),
    path("excell/", views.Excell_templateWiev.as_view(), name="excell"),
    path("excell/<int:pk>/", views.ExcellDetail.as_view(), name="excell"),
    path("excell/<int:pk>/<str:status>/", views.ExcellDetail.as_view(), name="excell"),
    path("set_language/<str:lang>/", views.set_language, name="set_language"),
]
