# Generated by Django 4.1 on 2022-09-04 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0028_techer_resume_alter_user_special_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='techer',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 13, 11, 7, 300214, tzinfo=datetime.timezone.utc)),
        ),
    ]