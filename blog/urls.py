from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('products/', views.products_view),
    path('hashtags/', views.hashtags_view),
    path('categories/', views.categories_view),
    path('product/<int:product_id>/', views.product_detail_view),
    path('hashtags/', views.hashtags_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

