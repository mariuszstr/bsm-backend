# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('speedway_popularity', models.IntegerField(default=0)),
                ('population', models.IntegerField(default=0)),
                ('wealth', models.IntegerField(default=0)),
                ('save', models.ForeignKey(to='people.PlayerSave')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('speedway_popularity', models.IntegerField(default=0)),
                ('population', models.IntegerField(default=0)),
                ('wealth', models.IntegerField(default=0)),
                ('save', models.ForeignKey(to='people.PlayerSave')),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('ability', models.IntegerField(default=0)),
                ('country', models.ForeignKey(to='league.Country')),
                ('save', models.ForeignKey(to='people.PlayerSave')),
            ],
        ),
        migrations.CreateModel(
            name='LeagueClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('ability', models.IntegerField(default=0)),
                ('number_of_promotions', models.IntegerField(default=0)),
                ('number_of_drop', models.IntegerField(default=0)),
                ('number_of_promotions_match', models.IntegerField(default=0)),
                ('number_of_drop_match', models.IntegerField(default=0)),
                ('league_script', models.TextField(default=b'')),
                ('match_script', models.TextField(default=b'')),
                ('last_class', models.ForeignKey(related_name='class_last_class', default=None, to='league.LeagueClass')),
                ('league', models.ForeignKey(to='league.League')),
                ('next_class', models.ForeignKey(related_name='class_next_class', default=None, to='league.LeagueClass')),
                ('save', models.ForeignKey(to='people.PlayerSave')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('matches', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('league', models.ForeignKey(to='league.League')),
                ('league_class', models.ForeignKey(to='league.LeagueClass')),
                ('save', models.ForeignKey(to='people.PlayerSave')),
            ],
        ),
    ]
