from django.urls import path

from . import views


urlpatterns = [
    path("calculator/", views.CalculatorView.as_view(), name="calculator"),
]
