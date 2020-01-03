from django.db import models

# Create your models here.

class admin_info(models.Model):

    employee_id = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=10)
    mobile_no = models.IntegerField()
    address_1 = models.CharField(max_length=80)
    address_2 = models.CharField(max_length=80)
    pan_card = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    dept_code = models.CharField(max_length=20)
    aadhar_no = models.IntegerField()
    dob = models.DateField()
    photo = models.ImageField(upload_to='images')

class employee_info(models.Model):
    employee_id = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    department = models.CharField(max_length=20,default='NA')
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=10)
    mobile_no = models.IntegerField()
    city_town = models.CharField(max_length=80,default='NA')
    state = models.CharField(max_length=80,default='NA')
    country = models.CharField(max_length=80,default='NA')
    pan_card = models.CharField(max_length=20)
    aadhar_no = models.IntegerField()
    dob = models.DateField()
    photo = models.ImageField(upload_to='images')
    status = models.CharField(max_length=20,default='NA')

class employee_leaves_details(models.Model):

    employee_id = models.IntegerField()
    leave_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    leave_type = models.CharField(max_length=30)
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    total_days = models.IntegerField()
    description = models.CharField(max_length=200)
    applied_date = models.DateField()
    status = models.CharField(max_length=5,default='NA')
    comments = models.CharField(max_length=200,default='')

class leave_count(models.Model):
    employee_id = models.IntegerField()
    total_eligible_leaves = models.IntegerField(default=24)
    leaves_taken = models.IntegerField(default=0)
    remaining_leaves = models.IntegerField(default=0)

class department(models.Model):
    dept_code = models.CharField(max_length=20,default='')
    dept_name = models.CharField(max_length=20,default='')
    created_date = models.DateField()




