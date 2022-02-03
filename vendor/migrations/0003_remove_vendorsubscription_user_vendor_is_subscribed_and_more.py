# Generated by Django 4.0.1 on 2022-01-29 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_remove_vendorsubscription_vendor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorsubscription',
            name='user',
        ),
        migrations.AddField(
            model_name='vendor',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vendorsubscription',
            name='subscription_type',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendorsubscription',
            name='vendor',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor'),
            preserve_default=False,
        ),
    ]