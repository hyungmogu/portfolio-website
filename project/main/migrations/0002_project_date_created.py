# Generated by Django 2.1.1 on 2019-12-09 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]