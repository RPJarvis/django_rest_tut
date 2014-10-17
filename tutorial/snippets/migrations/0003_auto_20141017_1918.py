# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_highlighted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='owners',
            new_name='owner',
        ),
    ]
