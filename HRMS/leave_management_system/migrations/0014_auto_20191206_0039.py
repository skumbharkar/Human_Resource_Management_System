# Generated by Django 2.2.7 on 2019-12-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_management_system', '0013_employee_info_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_info',
            name='photo',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
