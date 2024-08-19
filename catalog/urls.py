from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from catalog.apps import MainappConfig
from catalog.views import products, product_details, contacts, new_product

app_name = MainappConfig.name

urlpatterns = [
    path('', products, name='home'),
    path('products/<int:pk>/', product_details, name='product_details'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('contacts/', contacts, name='contacts'),
    path('new_product/', new_product, name='new_product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
