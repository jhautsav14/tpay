# Generated by Django 4.0.4 on 2022-08-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_fluidbooking_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fluidbooking',
            name='fluid',
            field=models.CharField(max_length=50),
        ),
    ]
