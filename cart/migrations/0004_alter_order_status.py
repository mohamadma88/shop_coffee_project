# Generated by Django 5.1.3 on 2025-03-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_order_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'در حال پرداخت'), ('Processing', 'در حال پردازش'), ('Shipped', 'در حال ارسال'), ('Delivered', 'تحویل داده شده')], default='Pending', max_length=100),
        ),
    ]
