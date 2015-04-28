# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lend', '0002_auto_20150427_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='bookname',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
