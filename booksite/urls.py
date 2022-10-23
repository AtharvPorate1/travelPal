
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('book/', include('bookapp.urls')),
    path('chat/', include('base.urls')),
    path('news/', include('news_api.urls')),
    path('music/', include('music.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
