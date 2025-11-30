from django.shortcuts import render, get_object_or_404
from .models import Products, Category, ParentCategory
from django.core.paginator import Paginator

# products/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products, Category, ParentCategory

def products(request):
    # Bütün ParentCategory-ləri alırıq (əsas səhifə üçün)
    parent_categories = ParentCategory.objects.all()

    # Bütün Category-ləri alırıq (filtrləmə üçün)
    categories = Category.objects.all()

    # Məhsulları alırıq
    products_qs = Products.objects.all()

    # GET parametrləri
    parent_slug = request.GET.get("parent")
    category_slug = request.GET.get("category")

    # 1. ParentCategory filtri
    if parent_slug:
        # ParentCategory ilə əlaqəli məhsullar
        products_qs = products_qs.filter(parent_category__slug=parent_slug)
        # O parentə aid Category-ləri göstər
        categories = categories.filter(parent__slug=parent_slug)

    # 2. Category filtri (prioritetli)
    if category_slug:
        products_qs = products_qs.filter(category__slug=category_slug)

    # Sıralama
    sort = request.GET.get("sort", "")
    if sort == "price_asc":
        products_qs = products_qs.order_by("price")
    elif sort == "price_desc":
        products_qs = products_qs.order_by("-price")
    elif sort == "newest":
        products_qs = products_qs.order_by("-created_at")
    elif sort == "oldest":
        products_qs = products_qs.order_by("created_at")
    else:
        products_qs = products_qs.order_by("-created_at")

    # Pagination
    paginator = Paginator(products_qs, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Kontekst
    context = {
        "page_obj": page_obj,
        "categories": categories,
        "parent_categories": parent_categories,  # BURADA OLMALIDIR!
        "parent_slug": parent_slug,
        "category_slug": category_slug,
    }

    return render(request, "products.html", context)


def products_details(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'products_details.html', {'product': product})