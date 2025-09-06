from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

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

    context = {'form': form}  # context burada yaradılır
    return render(request, 'contact.html', context)
