# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('banner', models.ImageField(upload_to=b'banners')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
    ]
