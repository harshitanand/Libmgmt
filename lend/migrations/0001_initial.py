# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('copies', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issuebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('groupname', models.CharField(max_length=255)),
                ('issued', models.IntegerField(default=0)),
                ('can_issue', models.IntegerField(blank=True)),
                ('bookname', models.ForeignKey(to='lend.Books')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
