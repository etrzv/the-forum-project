# Generated by Django 4.1.3 on 2022-11-24 15:03

import core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='username',
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=1, max_length=25, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=1, max_length=15, validators=[django.core.validators.MinLengthValidator(2), core.validators.validate_only_letters]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=1, max_length=15, validators=[django.core.validators.MinLengthValidator(2), core.validators.validate_only_letters]),
            preserve_default=False,
        ),
    ]