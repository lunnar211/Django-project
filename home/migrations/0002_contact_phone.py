# Generated by Django 4.2.2 on 2023-06-30 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=datetime.datetime(2023, 6, 30, 12, 36, 31, 738349, tzinfo=datetime.timezone.utc), max_length=22),
            preserve_default=False,
        ),
    ]
