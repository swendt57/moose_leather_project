# Generated by Django 3.0.3 on 2020-03-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_info',
        ),
        migrations.AddField(
            model_name='order',
            name='address1',
            field=models.CharField(default='TBD', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='address2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='TBD', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='postal_code',
            field=models.CharField(default='TBD', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='TBD', max_length=25),
        ),
    ]
