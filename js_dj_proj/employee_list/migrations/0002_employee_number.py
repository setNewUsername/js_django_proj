# Generated by Django 4.1.7 on 2023-02-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
