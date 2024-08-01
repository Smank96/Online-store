from django.urls import path, include
from catalog.apps import MainappConfig
from catalog.views import home, contacts

app_name = MainappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
