import random
from django.shortcuts import render
from products.models import Products, ParentCategory
from about.models import About
from Home.models import Homepage
import random

def home(request):
    latest_products = Products.objects.all().order_by('-created_at')[:3]
    about = About.objects.first()
    categories = ParentCategory.objects.all()
    home = Homepage.objects.first()

    # Random product
    products = list(Products.objects.all())
    random_product = random.choice(products) if products else None

    context = {
        'latest_products': latest_products,
        'about': about,
        'categories': categories,
        'random_product': random_product,
        'home': home,
    }
    return render(request, 'index.html', context)

