from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from django.views.generic import DetailView

from core.models import About, HR, FAQ, ApplicationCategory, Service, Blog, Settings


# Create your views here.


def index(request):
    context = {
        "title": _("Home"),
        "about": About.objects.last(),
        "hr": HR.objects.last(),
        "faqs": FAQ.objects.all(),
        "services": Service.objects.all()[:3],
        "blogs": Blog.objects.all()[:3],
        "applicationcategory": ApplicationCategory.objects.all(),
        "settings": Settings.objects.last(),
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
    context = {
        "title": _("Contact"),
        "applicationcategory": ApplicationCategory.objects.all(),
    }
    return render(request, "contact.html", context)


def services(request):
    context = {
        "title": _("Services"),
        "services": Service.objects.all(),
    }
    return render(request, "service.html", context)


def service_detail(request, pk):
    context = {
        "title": _("Service Detail"),
        "service": Service.objects.get(pk=pk),
    }
    return render(request, "components/../templates/service-detail.html", context)


def blog(request):
    context = {
        "title": _("Blog"),
        "blogs": Blog.objects.all(),
    }
    return render(request, "blog.html", context)


def blog_detail(request, slug):
    context = {
        "title": _("Blog Detail"),
        "blog": Blog.objects.get(slug=slug),
    }
    return render(request, "components/../templates/blog-detail.html", context)
