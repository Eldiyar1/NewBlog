from django.urls import path

from post import views

urlpatterns = [
    path('', views.main_view),
    path('products/', views.products_view),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('products/create/', views.product_create),
    path('categories/', views.categories_view),
    path('categories/create/', views.category_create_view),
    path('hashtags/', views.hashtags_view),
]