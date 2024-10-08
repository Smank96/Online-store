# Generated by Django 5.0.7 on 2024-08-24 04:27
from datetime import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_views_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.SlugField()),
                ('body', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(default=datetime.now, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('views_counter', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
