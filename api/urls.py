from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

'''urlpatterns = [
    #path('products/', views.product_list.as_view()),
    #path('product/<int:pk>', views.products_details.as_view()),
    path('orders/', views.orders_list),
]'''

router = DefaultRouter()
router.register('product', views.product_list, basename='product')
router.register('order', views.orders_list, basename='order')

urlpatterns = router.urls