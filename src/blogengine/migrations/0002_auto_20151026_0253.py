# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Slug',
            field=models.SlugField(unique=True, max_length=140),
        ),
    ]
