from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('users/', include('users.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)