# Generated by Django 5.0.6 on 2024-06-07 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0008_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(error_messages={'blank': 'This field cannot be blank. First name is required'}, max_length=150, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(error_messages={'blank': 'This field cannot be blank. Last name is required'}, max_length=150, null=True, verbose_name='last name'),
        ),
    ]