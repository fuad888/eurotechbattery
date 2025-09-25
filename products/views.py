from django.shortcuts import render, get_object_or_404
from .models import Products, Category, ParentCategory
from django.core.paginator import Paginator

def products(request):
    products_qs = Products.objects.all()
    parent_categories = ParentCategory.objects.all()
    categories = Category.objects.all()

    # Parent filter
    parent_slug = request.GET.get("parent")
    if parent_slug:
        products_qs = products_qs.filter(parent_category__slug=parent_slug)
        categories = categories.filter(parent__slug=parent_slug)

    # Category filter
    category_slug = request.GET.get("category")
    if category_slug:
        products_qs = products_qs.filter(category__slug=category_slug)

    # Sort
    sort = request.GET.get("sort")
    if sort == "price_asc":
        products_qs = products_qs.order_by("price")
    elif sort == "price_desc":
        products_qs = products_qs.order_by("-price")
    elif sort == "newest":
        products_qs = products_qs.order_by("-created_at")
    elif sort == "oldest":
        products_qs = products_qs.order_by("created_at")
    else:
        products_qs = products_qs.order_by("-created_at")  # default

    # Pagination
    paginator = Paginator(products_qs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "products.html", {
        "page_obj": page_obj,
        "categories": categories,
        "sort": sort,
        "category_slug": category_slug,
        "parent": parent_categories,
        "parent_slug": parent_slug,
    })
