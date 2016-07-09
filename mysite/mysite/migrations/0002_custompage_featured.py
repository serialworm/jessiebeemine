# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custompage',
            name='featured',
            field=models.ImageField(default=b'', upload_to=b'uploads'),
        ),
    ]
