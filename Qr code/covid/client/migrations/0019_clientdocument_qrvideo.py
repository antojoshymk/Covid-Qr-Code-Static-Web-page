# Generated by Django 4.0 on 2022-02-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0018_alter_clientdataqrexe2_todaydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdocument',
            name='qrvideo',
            field=models.ImageField(blank=True, null=True, upload_to='qrvideodata'),
        ),
    ]
