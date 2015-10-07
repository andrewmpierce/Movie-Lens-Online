# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_auto_20151007_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rater',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='stars',
        ),
        migrations.AddField(
            model_name='rating',
            name='stars',
            field=models.IntegerField(default=0),
        ),
    ]
