from django.db import models
from django.db.models.functions import Now


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True, verbose_name='Категория товара')
    category_description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование товара')
    product_description = models.TextField(verbose_name='Описание')
    product_picture = models.ImageField(upload_to='products_images', blank=True, null=True, verbose_name='Фото')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(verbose_name='Дата создания', db_default=Now())
    updated_at = models.DateTimeField(verbose_name='Дата изменения', db_default=Now())

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.product_name


class Contacts(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    phone_number = models.CharField(max_length=12, verbose_name='Phone')
    message = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
