# Generated by Django 4.0.4 on 2022-05-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
