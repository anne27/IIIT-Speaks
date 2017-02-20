# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('BlogTitle', models.CharField(max_length=140, unique=True)),
                ('BlogDescription', models.CharField(blank=True, null=True, max_length=140)),
                ('Content', models.TextField()),
                ('NumComments', models.IntegerField(blank=True, null=True)),
                ('Publish', models.BooleanField(default=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Slug', models.SlugField(max_length=140, default=None, unique=True)),
                ('Author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-Created'],
            },
        ),
    ]
