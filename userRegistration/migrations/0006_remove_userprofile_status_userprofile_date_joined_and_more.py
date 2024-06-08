# Generated by Django 5.0.6 on 2024-06-01 00:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0005_alter_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='status',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(error_messages={'blank': 'This field cannot be blank. First name is required'}, max_length=150, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(error_messages={'blank': 'This field cannot be blank. Last name is required'}, max_length=150, null=True, verbose_name='last_name'),
        ),
    ]
