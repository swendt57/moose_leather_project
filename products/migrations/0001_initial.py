# Generated by Django 3.0.3 on 2020-03-02 20:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('other_info', models.CharField(blank=True, default='', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_consignment', models.BooleanField(default=False)),
                ('commission_percent', models.DecimalField(decimal_places=2, default=0.25, max_digits=2)),
                ('image', models.ImageField(default='images/no_image.png', upload_to='images', validators=[products.models.Item.validate_image])),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
