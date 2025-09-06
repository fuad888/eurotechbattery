from django.shortcuts import render
from about.models import Aboutpage,About,team


# Create your views here.

def about(request):
    about_page = Aboutpage.objects.first()
    about_info = About.objects.first()
    team_members = team.objects.all()
    context = {
        'about_page': about_page,
        'about_info': about_info,
        'team_members': team_members,
    }
    return render(request, 'about.html', context)