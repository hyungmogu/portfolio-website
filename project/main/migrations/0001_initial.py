# Generated by Django 3.0 on 2019-12-05 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('url_demo', models.URLField()),
                ('url_source_code', models.URLField()),
                ('challenges', models.TextField()),
                ('result', models.TextField()),
                ('image_main', models.URLField()),
            ],
        ),
    ]
