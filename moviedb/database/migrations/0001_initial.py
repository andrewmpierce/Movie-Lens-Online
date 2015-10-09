# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('movie_id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('rater_id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(default='X', max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'X')])),
                ('zipcode', models.PositiveSmallIntegerField()),
                ('occupation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('stars', models.PositiveSmallIntegerField()),
                ('movie', models.ForeignKey(to='database.Movie')),
                ('rater', models.ForeignKey(to='database.Rater')),
            ],
        ),
    ]
