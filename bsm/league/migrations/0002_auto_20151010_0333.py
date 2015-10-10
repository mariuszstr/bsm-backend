# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leagueclass',
            name='last_class',
            field=models.ForeignKey(related_name='class_last_class', default=None, blank=True, to='league.LeagueClass', null=True),
        ),
        migrations.AlterField(
            model_name='leagueclass',
            name='next_class',
            field=models.ForeignKey(related_name='class_next_class', default=None, blank=True, to='league.LeagueClass', null=True),
        ),
    ]
