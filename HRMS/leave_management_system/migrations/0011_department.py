# Generated by Django 2.2.7 on 2019-12-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_management_system', '0010_employee_leaves_details_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_code', models.CharField(default='', max_length=20)),
                ('dept_name', models.CharField(default='', max_length=20)),
                ('created_date', models.DateField()),
            ],
        ),
    ]
