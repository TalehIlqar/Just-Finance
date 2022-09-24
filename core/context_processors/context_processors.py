from datetime import datetime

from core.models import Service, Setting


def get_context_setting(request):
    return {
        "footer_services": Service.objects.all()[:4],
        "settings": Setting.objects.last(),
        "current_year": datetime.now().year,
    }
