# Generated by Django 4.2.16 on 2024-12-06 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='username',
            new_name='email',
        ),
    ]
