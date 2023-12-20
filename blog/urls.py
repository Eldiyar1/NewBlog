from django.contrib import admin
from django.urls import path

from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('products/', views.products_view),
]
