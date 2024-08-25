from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from catalog.apps import MainappConfig
from catalog.views import ProductListView, ContactsListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView

app_name = MainappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    # path('page/<int:page_number>/', ProductListView.as_view(), name='paginator'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('products/create', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='products_delete'),
    path('blog', ArticleListView.as_view(), name='article_list'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),
    path('article/create', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
