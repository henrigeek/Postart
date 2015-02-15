# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_auto_20141030_0040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tags',
            new_name='tag',
        ),
    ]
