from django.contrib import admin
from django.urls import path

from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_view),
    path('current_date/', views.current_date_view),
    path('goodby/', views.goodby_view,),

]
