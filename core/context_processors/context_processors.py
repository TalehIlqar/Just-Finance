from core.models import Service, Settings


def get_context_setting(request):
    return {
        "footer_services": Service.objects.all()[:4],
        "default_address": Settings.objects.last().default_address,
        "default_number": Settings.objects.last().default_number,
        "default_email": Settings.objects.last().default_email,
        "sayt_name": Settings.objects.last().name,
        "facebook": Settings.objects.last().facebook,
        "instagram": Settings.objects.last().instagram,
        "whatsapp": Settings.objects.last().whatsapp,
        "linkedin": Settings.objects.last().linkedin,
        "youtube": Settings.objects.last().youtube,
    }