from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import activate, gettext_lazy as _
from core.models import About, HR, FAQ, ApplicationCategory, Service, Blog, Setting


def index(request):
    context = {
        "title": _("Home"),
        "about": About.objects.last(),
        "hr": HR.objects.last(),
        "faqs": FAQ.objects.all(),
        "services": Service.objects.all()[:3],
        "blogs": Blog.objects.all()[:3],
        "applicationcategory": ApplicationCategory.objects.all(),
        "settings": Setting.objects.last(),
    }
    return render(request, "pages/index.html", context)


def about(request):
    context = {
        "title": _("About"),
        "about": About.objects.last(),
        "hr": HR.objects.last(),
        "faqs": FAQ.objects.all(),
    }
    return render(request, "pages/about.html", context)


def contact(request):
    context = {
        "title": _("Contact"),
        "applicationcategory": ApplicationCategory.objects.all(),
    }
    return render(request, "pages/contact.html", context)


def services(request):
    context = {
        "title": _("Services"),
        "services": Service.objects.all(),
    }
    return render(request, "pages/services.html", context)


def service_detail(request, slug):
    context = {
        "title": _("Service Detail"),
        "service": Service.objects.get(slug=slug),
    }
    return render(request, "pages/service-detail.html", context)


def blog(request):
    context = {
        "title": _("Blog"),
        "blogs": Blog.objects.all(),
    }
    return render(request, "pages/blogs.html", context)


def blog_detail(request, slug):
    context = {
        "title": _("Blog Detail"),
        "blog": Blog.objects.get(slug=slug),
    }
    return render(request, "pages/blog-detail.html", context)


def set_language(request, lang):
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    activate(lang)
    return response
