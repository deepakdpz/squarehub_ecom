# Generated by Django 5.0.3 on 2024-04-08 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='order_id',
        ),
    ]
