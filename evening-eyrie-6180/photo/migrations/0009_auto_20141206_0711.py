# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0008_auto_20141206_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='headshot',
            field=models.ImageField(upload_to=b'profile/author_headshots'),
        ),
        migrations.AlterField(
            model_name='image',
            name='authors',
            field=models.ForeignKey(to='photo.Author', blank=True),
        ),
    ]
