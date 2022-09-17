from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from core.models import About, HR, FAQ, Service, Blog


# Create your views here.


def index(request):
    context = {
        "title": _("Home"),
    }
    return render(request, "index.html", context)


def about(request):
    context = {
        "title": _("About"),
        "about": About.objects.last(),
        "hr": HR.objects.last(),
        "faqs": FAQ.objects.all(),
    }
    return render(request, "about.html", context)


def contact(request):
    return render(request, "contact.html")


def services(request):
    context = {
        "title": _("Services"),
        "services": Service.objects.all(),
    }
    return render(request, "service.html", context)


def blog(request):
    context = {
        "title": _("Blog"),
        "blogs": Blog.objects.all(),
    }
    return render(request, "blog.html", context)
