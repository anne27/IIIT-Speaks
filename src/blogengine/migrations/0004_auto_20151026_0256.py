# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0003_auto_20151026_0254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Slug',
            new_name='BlogSlug',
        ),
    ]
