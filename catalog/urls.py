from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from catalog.apps import MainappConfig
from catalog.views import home, contacts

app_name = MainappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
