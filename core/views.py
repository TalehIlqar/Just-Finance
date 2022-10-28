from django.conf import settings
from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import activate, gettext_lazy as _

from django.views.generic import ListView

from calculator.models import SectorType
from core.models import About, HR, FAQ, ApplicationCategory, Service, Blog, Excell_template, ServiceFAQ


def index(request):
    context = {
        "title": _("Home"),
        "about": About.objects.last(),
        "hr": HR.objects.last(),
        "faqs": FAQ.objects.all(),
        "services": Service.objects.all()[:4],
        "blogs": Blog.objects.filter(is_pin=False)[:2],
        "blogs_pin": Blog.objects.filter(is_pin=True)[:1],
        "applicationcategory": ApplicationCategory.objects.all(),
        "media_url": settings.MEDIA_URL,
        "sector_types": SectorType.objects.all(),
    }
    return render(request, "pages/v2index.html", context)


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
        "about" : About.objects.last(),
    }
    return render(request, "pages/contact.html", context)


def services(request):
    context = {
        "title": _("Services"),
        "services": Service.objects.all(),
    }
    return render(request, "pages/v2services.html", context)


def service_detail(request, slug):
    context = {
        "title": _("Service Detail"),
        "service": Service.objects.get(slug=slug),
        "servicesfaq": ServiceFAQ.objects.filter(service=Service.objects.get(slug=slug)),

    }   
    return render(request, "pages/v2service-detail.html", context)


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


class Excell_templateWiev(ListView):
    model = Excell_template
    template_name = "pages/v2excel.html"
    context_object_name = "excell_template"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        # context["excell"] = Excell_template.objects.all()
        context = super().get_context_data(**kwargs)
        context["title"] = _("Excell Template")
        context["excell_template"] = Excell_template.objects.all()
        context["categories"] = ApplicationCategory.objects.all()
        category = self.request.GET.get("category_id")
        search = self.request.GET.get("search_excel")
        if search:
            context["excell_template"] = Excell_template.objects.filter(title__icontains=search)
        if category:
            context["excell_template"] = Excell_template.objects.filter(category__id=category)
        if category and search:
            context["excell_template"] = Excell_template.objects.filter(title__icontains=search, category__id=category)
        
        context["search"] = search
        context["selected_category"] = category
        return context


class ExcellDetail(ListView):
    def get(self, request, pk, status=None):
        try:
            excell = Excell_template.objects.get(pk=pk)
        except:
            return "File does not exist"
        response = FileResponse(open(excell.file.path, 'rb'))
        if status == 'download':
            response['Content-Disposition'] = 'attachment; filename=%s' % excell.file.name
        elif status == 'show':
            response['Content-Disposition'] = 'inline; filename=%s' % excell.file.name
        return response
