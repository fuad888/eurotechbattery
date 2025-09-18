import random
from django.shortcuts import render
from products.models import Products, Category
from about.models import About

def home(request):
    latest_products = Products.objects.all().order_by('-created_at')[:3]  # son 3 məhsul
    about = About.objects.first()  # şirkət haqqında məlumat
    categories = Category.objects.all()

    # Random product
    product_count = Products.objects.count()
    random_product = None
    if product_count > 0:
        random_index = random.randint(0, product_count - 1)
        random_product = Products.objects.all()[random_index]

    context = {
        'latest_products': latest_products,
        'about': about,
        'categories': categories,
        'random_product': random_product,
    }
    return render(request, 'index.html', context)
