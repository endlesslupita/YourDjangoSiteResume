# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('pledge', models.CharField(max_length=140)),
                ('name', models.CharField(default=b'Anonymous', max_length=128, null=True, help_text=b'Leave NAME blank to remain anonymous', blank=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
