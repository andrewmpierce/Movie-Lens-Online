# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0006_auto_20151007_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
