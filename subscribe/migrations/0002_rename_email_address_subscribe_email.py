# Generated by Django 4.0.1 on 2022-01-09 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribe',
            old_name='email_address',
            new_name='email',
        ),
    ]
