# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createstudent',
            name='other',
            field=models.CharField(max_length=100, verbose_name=b'other'),
            preserve_default=True,
        ),
    ]
