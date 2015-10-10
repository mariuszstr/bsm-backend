# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_auto_20151010_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='save',
            field=models.ForeignKey(blank=True, to='people.PlayerSave', null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='save',
            field=models.ForeignKey(blank=True, to='people.PlayerSave', null=True),
        ),
        migrations.AlterField(
            model_name='league',
            name='save',
            field=models.ForeignKey(blank=True, to='people.PlayerSave', null=True),
        ),
        migrations.AlterField(
            model_name='leagueclass',
            name='save',
            field=models.ForeignKey(blank=True, to='people.PlayerSave', null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='save',
            field=models.ForeignKey(blank=True, to='people.PlayerSave', null=True),
        ),
    ]
