# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0004_city_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='save',
            field=models.ForeignKey(default=None, blank=True, to='people.PlayerSave', null=True),
        ),
    ]
