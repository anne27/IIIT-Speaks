# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0006_auto_20151027_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='BlogTitle',
            field=models.CharField(unique=True, max_length=140),
        ),
    ]
