from core.models import Setting

def global_settings(request):
    setting_obj = Setting.objects.first()
    return {
        "setting_obj": setting_obj
    }
