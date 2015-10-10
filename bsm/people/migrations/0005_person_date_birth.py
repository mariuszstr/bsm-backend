# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20151010_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date_birth',
            field=models.DateField(null=True, blank=True),
        ),
    ]
