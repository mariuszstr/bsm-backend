# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motocycle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_speed', models.IntegerField(default=0)),
                ('acceleration', models.IntegerField(default=0)),
                ('setting_front', models.IntegerField(default=0)),
                ('setting_back', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('rider', models.OneToOneField(default=None, to='people.Rider')),
                ('save', models.ForeignKey(to='people.PlayerSave')),
            ],
        ),
    ]
