from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import  FAQ

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Müraciətiniz uğurla göndərildi!')
            return redirect('contact') 
        else:
            messages.error(request, 'Zəhmət olmasa, formu düzgün doldurun!')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'faqs': FAQ.objects.all()  # istəsən FAQ-ları da buradan göndərə bilərsən
    }
    return render(request, 'contact.html', context)


def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})