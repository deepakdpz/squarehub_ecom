# Generated by Django 5.0.3 on 2024-04-06 03:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_basketitem_is_order_placed'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('payment_mode', models.CharField(choices=[('online', 'online'), ('cod', 'cod')], default='cod', max_length=100)),
                ('user_id', models.CharField(max_length=200, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('order_ confirmed', 'Order confirmed'), ('dispatched', 'Dispatched'), ('in_transit', 'In transit'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='order_confirmd', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('basket_item_object', models.ManyToManyField(to='shop.basketitem')),
                ('user_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myorders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
