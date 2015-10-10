# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_person_date_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='save',
            new_name='save_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='save',
            new_name='save_name',
        ),
        migrations.RenameField(
            model_name='rider',
            old_name='save',
            new_name='save_name',
        ),
    ]
