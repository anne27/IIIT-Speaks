# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0004_auto_20151026_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='BlogTitle',
            field=models.CharField(max_length=140),
        ),
    ]
