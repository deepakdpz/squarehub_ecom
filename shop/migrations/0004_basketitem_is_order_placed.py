# Generated by Django 5.0.3 on 2024-04-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_basketitem_basket_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='is_order_placed',
            field=models.BooleanField(default=False),
        ),
    ]