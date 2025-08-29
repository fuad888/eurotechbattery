from .models import Setting

def setting_context(request):
    setting = Setting.objects.first()
    
    return {
        'setting_obj': setting,
    }
