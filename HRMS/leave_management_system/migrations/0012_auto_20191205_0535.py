# Generated by Django 2.2.7 on 2019-12-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_management_system', '0011_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_info',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='employee_info',
            name='address_2',
        ),
        migrations.AddField(
            model_name='employee_info',
            name='city_town',
            field=models.CharField(default='NA', max_length=80),
        ),
        migrations.AddField(
            model_name='employee_info',
            name='country',
            field=models.CharField(default='NA', max_length=80),
        ),
        migrations.AddField(
            model_name='employee_info',
            name='department',
            field=models.CharField(default='NA', max_length=20),
        ),
        migrations.AddField(
            model_name='employee_info',
            name='state',
            field=models.CharField(default='NA', max_length=80),
        ),
    ]
