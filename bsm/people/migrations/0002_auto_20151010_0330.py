# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playersave',
            name='player',
            field=models.OneToOneField(default=None, blank=True, to='people.Player'),
        ),
    ]
