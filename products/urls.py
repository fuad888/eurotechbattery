from django.urls import path
from . import views

urlpatterns = [
    # Hamı məhsullar səhifəsi (slug tələb etmir)
    path("", views.products, name="products"),
    path('details', views.products_details, name='products_details'),
]
