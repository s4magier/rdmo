# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='text_de',
            field=models.TextField(help_text='The German text for this task.', verbose_name='Text (de)'),
        ),
        migrations.AlterField(
            model_name='task',
            name='text_en',
            field=models.TextField(help_text='The English text for this task.', verbose_name='Text (en)'),
        ),
    ]
