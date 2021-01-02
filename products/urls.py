from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('hot/', views.hot_products, name='hot_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<int:specials_id>/', views.specials_detail, name='specials_detail'),
    path('<int:seasonal_id>/', views.seasonal_detail, name='seasonal_detail'),
    
]
