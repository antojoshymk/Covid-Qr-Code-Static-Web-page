# Generated by Django 3.2.7 on 2022-01-29 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdataqrexe2',
            name='todaydate',
            field=models.DateField(default=datetime.date(2022, 1, 29)),
        ),
    ]