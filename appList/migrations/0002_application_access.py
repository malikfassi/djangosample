# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='access',
            field=models.CharField(default=b'PU', max_length=2, choices=[(b'PU', b'Public'), (b'PR', b'Private')]),
        ),
    ]
