# Generated by Django 2.2.12 on 2020-05-20 15:19
from django.conf import settings
from django.db import migrations


def create_admin(apps, schema_editor):
    try:
        from authapp.models import User
        User.objects.create_superuser("admin", "", "admin", age="29")
        User.save()
    except:
        print("Failed to create superuser")


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [migrations.RunPython(create_admin)]

