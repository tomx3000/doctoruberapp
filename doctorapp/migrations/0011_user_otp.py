# Generated by Django 3.0.4 on 2020-03-09 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0010_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]