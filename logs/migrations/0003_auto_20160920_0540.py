# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_entry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name_plural': '\u4e3b\u9898'},
        ),
    ]
