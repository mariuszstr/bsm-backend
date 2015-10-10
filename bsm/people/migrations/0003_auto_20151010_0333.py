# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20151010_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playersave',
            name='player',
            field=models.OneToOneField(null=True, default=None, blank=True, to='people.Player'),
        ),
    ]
