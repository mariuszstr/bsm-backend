# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_auto_20151010_0438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='save',
            new_name='save_name',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='save',
            new_name='save_name',
        ),
        migrations.RenameField(
            model_name='league',
            old_name='save',
            new_name='save_name',
        ),
        migrations.RenameField(
            model_name='leagueclass',
            old_name='save',
            new_name='save_name',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='save',
            new_name='save_name',
        ),
    ]
