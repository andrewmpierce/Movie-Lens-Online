# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20151007_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=1, choices=[('M', 'M'), ('F', 'F'), ('O', 'O'), ('X', 'X')], default='X'),
        ),
    ]
