# Generated by Django 2.2.12 on 2020-05-20 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locations',
            old_name='phome',
            new_name='phone',
        ),
    ]
