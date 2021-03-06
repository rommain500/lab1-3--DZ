# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-23 13:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
from django.db import models
import django.db.models.deletion
from django.utils import timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название отеля')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'db_table': 'hotel',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(upload_to='', verbose_name='Фотография')),
            ],
            options={
                'db_table': 'picture',
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='Дата начала бронирования', default=django.utils.timezone.now)),
                ('date_end', models.DateTimeField(verbose_name='Дата окончания бронирования', default=django.utils.timezone.now)),
                ('person_amount', models.PositiveIntegerField(default=1, verbose_name='Кол-во персон')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Hotel')),
            ],
            options={
                'db_table': 'reserve',
            },
        ),
        migrations.AddField(
            model_name='hotel',
            name='pictures',
            field=models.ManyToManyField(db_table='hotel_pictures', to='hotel.Picture', verbose_name='Фотографии отеля'),
        ),
    ]
