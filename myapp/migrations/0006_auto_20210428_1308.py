# Generated by Django 3.0 on 2021-04-28 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='Product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='User',
            new_name='user',
        ),
    ]
