# Generated by Django 2.2.7 on 2019-11-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_management_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_credentials',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='admin',
        ),
    ]
