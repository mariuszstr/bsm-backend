# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20151010_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='save',
            field=models.ForeignKey(blank=True, to='people.PlayerSave', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='save',
            field=models.ForeignKey(blank=True, to='people.PlayerSave', null=True),
        ),
        migrations.AlterField(
            model_name='rider',
            name='save',
            field=models.ForeignKey(blank=True, to='people.PlayerSave', null=True),
        ),
    ]
