from django.contrib import admin
from catalog.models import Category, Product, Contacts, Article, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category', 'views_counter')
    list_filter = ('category',)
    search_fields = ('product_name', 'product_description')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'message')
    search_fields = ('name', 'message')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'preview', 'slug', 'created_at', 'is_published', 'views_counter')
    search_fields = ('title', 'body')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'is_active')
    search_fields = ('product',)
