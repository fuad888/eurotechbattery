from django.shortcuts import render, get_object_or_404
from .models import Products, Category
from django.core.paginator import Paginator

# Hamı məhsullar səhifəsi
def products(request):
    all_products = Products.objects.all()
    paginator = Paginator(all_products, 10)  # hər səhifədə 10 məhsul
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()  # filter üçün lazımdır
    return render(request, 'products.html', {
        'page_obj': page_obj,
        'categories': categories
    })

# Tək məhsul səhifəsi
def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'product_detail.html', {'product': product})

# Kateqoriyaya görə məhsullar
def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Products.objects.filter(category=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})
