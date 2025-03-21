# Generated by Django 5.1.3 on 2024-12-02 19:35

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس')),
                ('Introduction', models.TextField(verbose_name='مقدمه')),
                ('text', models.TextField(verbose_name='بدنه مقاله')),
                ('ingredient', models.TextField(verbose_name='مواد لازم')),
                ('recipe', models.TextField(verbose_name='رسپی')),
                ('pub', models.BooleanField(verbose_name='منتشر شود؟')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='سلاگ')),
                ('Category', models.ManyToManyField(related_name='article', to='product.category', verbose_name='دسته بندی')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]
