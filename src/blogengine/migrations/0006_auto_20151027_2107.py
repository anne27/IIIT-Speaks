# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0005_auto_20151026_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='BlogSlug',
            field=models.SlugField(blank=True, max_length=140),
        ),
    ]
