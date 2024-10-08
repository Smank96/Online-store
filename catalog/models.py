from datetime import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from users.models import User


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
    created_at = models.DateTimeField(verbose_name='Дата создания', default=datetime.now)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', default=datetime.now)
    views_counter = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    owner = models.ForeignKey(User, verbose_name="Создатель", blank=True, null=True, on_delete=models.SET_NULL)

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


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(null=False, unique=True)
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog', null=True, blank=True, verbose_name='Изображение')
    created_at = models.DateTimeField(verbose_name='Дата создания', default=datetime.now)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    views_counter = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def get_absolute_url(self):
        return reverse('catalog:article_detail', kwargs={'slug': self.slug})


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Продукт', null=True, blank=True)
    version_number = models.PositiveIntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_active = models.BooleanField(default=False, verbose_name='Признак текущей версии')

    class Meta:
        verbose_name = 'Версия товара'
        verbose_name_plural = 'Версии товаров'

    def __str__(self):
        return f"Версия: {self.version_number} - {self.version_name}"
