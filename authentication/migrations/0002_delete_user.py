# Generated by Django 4.0.4 on 2022-06-05 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
