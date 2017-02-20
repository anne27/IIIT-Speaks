# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0002_auto_20151026_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Slug',
            field=models.SlugField(max_length=140),
        ),
    ]
