# Generated by Django 4.0.1 on 2022-01-24 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50)),
                ('full_name', models.CharField(blank=True, max_length=50)),
                ('profile_picture', models.ImageField(blank=True, upload_to='vendorprofile')),
                ('place', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('pincode', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_amount', models.CharField(blank=True, max_length=10)),
                ('subscription_date', models.DateField(auto_now=True)),
                ('expiry_date', models.DateField(auto_now=True)),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]
