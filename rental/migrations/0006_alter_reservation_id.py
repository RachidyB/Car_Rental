# Generated by Django 4.0.4 on 2022-06-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_remove_car_rent_per_day_alter_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
