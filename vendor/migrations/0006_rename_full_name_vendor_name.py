# Generated by Django 4.0.1 on 2022-01-30 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_alter_vendor_category_alter_vendor_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='full_name',
            new_name='name',
        ),
    ]
