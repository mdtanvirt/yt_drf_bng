from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('product/<int:pk>', views.products_details),
]