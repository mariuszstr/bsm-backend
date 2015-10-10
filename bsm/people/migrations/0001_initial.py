# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('training', models.IntegerField(default=0)),
                ('youth_training', models.IntegerField(default=0)),
                ('manager_skill', models.IntegerField(default=0)),
                ('physical_training', models.IntegerField(default=0)),
                ('psychic_training', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=255)),
                ('second_name', models.CharField(default=b'', max_length=255)),
                ('determination', models.IntegerField(default=0)),
                ('ambition', models.IntegerField(default=0)),
                ('professionalism', models.IntegerField(default=0)),
                ('loyalty', models.IntegerField(default=0)),
                ('reflex', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hours', models.IntegerField(default=0)),
                ('user', models.OneToOneField(related_name='ApiUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerSave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('player', models.OneToOneField(default=None, to='people.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.IntegerField(default=0)),
                ('corner', models.IntegerField(default=0)),
                ('pair_raid', models.IntegerField(default=0)),
                ('person', models.OneToOneField(to='people.Person')),
                ('save', models.ForeignKey(to='people.PlayerSave')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='save',
            field=models.ForeignKey(to='people.PlayerSave'),
        ),
        migrations.AddField(
            model_name='coach',
            name='person',
            field=models.OneToOneField(to='people.Person'),
        ),
        migrations.AddField(
            model_name='coach',
            name='save',
            field=models.ForeignKey(to='people.PlayerSave'),
        ),
    ]
