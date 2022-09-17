from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Create your views here.


def index(request):
    context = {
        "title": _("Home"),
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        "title": _("About"),
    }
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'service.html')


def blog(request):
    return render(request, 'blog.html')
