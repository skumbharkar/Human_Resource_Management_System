# Generated by Django 2.2.7 on 2019-11-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_management_system', '0006_employee_leaves_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_leaves_details',
            name='leave_id',
            field=models.IntegerField(default=0),
        ),
    ]
