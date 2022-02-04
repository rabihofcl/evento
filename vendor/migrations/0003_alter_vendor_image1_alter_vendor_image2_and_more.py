# Generated by Django 4.0.1 on 2022-02-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_vendor_image1_vendor_image2_vendor_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='image1',
            field=models.FileField(blank=True, upload_to='media/showcase/'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='image2',
            field=models.FileField(blank=True, upload_to='media/showcase/'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='image3',
            field=models.FileField(blank=True, upload_to='media/showcase/'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='image4',
            field=models.FileField(blank=True, upload_to='media/showcase/'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='image5',
            field=models.FileField(blank=True, upload_to='media/showcase/'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='image6',
            field=models.FileField(blank=True, upload_to='media/showcase/'),
        ),
    ]
