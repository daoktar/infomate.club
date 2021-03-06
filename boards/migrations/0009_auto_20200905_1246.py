# Generated by Django 2.2.13 on 2020-09-05 12:46

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0008_boardfeed_is_parsable'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardblock',
            name='view',
            field=models.CharField(default='blocks/three.html', max_length=256),
        ),
        migrations.AddField(
            model_name='boardfeed',
            name='mix',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='boardfeed',
            name='view',
            field=models.CharField(default='feeds/simple.html', max_length=256),
        ),
        migrations.AlterField(
            model_name='boardfeed',
            name='url',
            field=models.TextField(),
        ),
    ]
