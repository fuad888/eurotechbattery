from django.urls import path
from . import views

urlpatterns = [
    # Hamı məhsullar səhifəsi (slug tələb etmir)
    path("products/", views.products, name="products"),

    # # Tək məhsul səhifəsi (slug tələb olunur)
    # path("products/<slug:slug>/", views.product_detail, name="product_detail"),

    # # Kateqoriyaya görə məhsullar
    # path("category/<slug:slug>/", views.category_products, name="category_products"),
]
