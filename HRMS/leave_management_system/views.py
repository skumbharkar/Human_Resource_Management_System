


from django.shortcuts import render,redirect
from .models import employee_info,employee_leaves_details,leave_count,admin_info
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from datetime import datetime

def homepage(request):

    return render(request,'homepage_main.html')

def admin_login(request):

    return render(request,'admin_login.html')

def display_emp_homepage(request):
    return render(request,'employee_homepage.html')

def emp_profile(request):

    emp = employee_info.objects.get(employee_id=request.session['emp_id'])
    return render(request,'employee_profile.html',{'employee':emp})

def validate_employee(request):

    email_id = request.POST.get('email')
    pwd = request.POST.get('password')

    try:
        emp = employee_info.objects.get(email=email_id, password=pwd)
    except employee_info.DoesNotExist:
        messages.error(request,"Invalid username or password")
        return redirect('homepage')
    else:
        request.session['emp_id']=emp.employee_id
        return render(request, 'employee_homepage.html', {'employee': emp})


def log_out(request):

    del request.session['emp_id']
    request.session.flush()
    return redirect('homepage')

def change_pwd_request(request):

    emp = employee_info.objects.get(employee_id=request.session['emp_id'])
    return render(request,'emp_change_pwd.html',{'employee':emp})

def change_password(request):


    current_pwd=request.POST['current_pwd']
    new_pwd=request.POST['new_pwd']
    confirm_pwd=request.POST['confirm_pwd']

    emp = employee_info.objects.get(employee_id=request.session['emp_id'])

    if current_pwd!=emp.password:
        messages.error(request,'Invalid Current Password')
        return redirect('change_pwd_request')
    elif new_pwd!=confirm_pwd:
        messages.error(request,'New password doesnt match with confirmed password')
        return redirect('change_pwd_request')
    else:
        emp.password=new_pwd
        emp.save()
        messages.info(request,'Password Changed Successfully...')
        return redirect('change_pwd_request')


def leave_request(request):
    emp = employee_info.objects.get(employee_id=request.session['emp_id'])
    leaves_taken=employee_leaves_details.objects.filter(employee_id=request.session['emp_id']).count()
    leave_id=str(emp.employee_id)+str(leaves_taken+1)

    leave_count_record=leave_count.objects.filter(employee_id=request.session['emp_id'])
    if leave_count_record.count() == 0:
        remaining_leaves=0
    else:
        remaining_leaves=leave_count_record[0].remaining_leaves
    return render(request, 'apply_for_leave.html', {'employee': emp,'leave_id':leave_id,'remaining_leaves':remaining_leaves})

def validate_leaves_details(request):


    leave_id=request.POST['leave_id']
    remaining_leaves=request.POST['remaining_leaves']
    leave_type=request.POST['leave_type']
    leave_start_date=request.POST['from_date']
    leave_end_date=request.POST['to_date']
    total_days=request.POST['total_days']
    description=request.POST['desc']



    if int(total_days)>int(remaining_leaves):
        messages.info(request, 'Please enter valid total days. Total days is grater than remaining leaves.')
        return redirect('leave_request')

    else:
        emp = employee_info.objects.get(employee_id=request.session['emp_id'])
        record=employee_leaves_details(employee_id=emp.employee_id,leave_id=leave_id,first_name=emp.first_name,last_name=emp.last_name,email=emp.email,leave_type=leave_type,leave_start_date=leave_start_date,leave_end_date=leave_end_date,total_days=total_days,description=description,applied_date=datetime.today().strftime('%Y-%m-%d'),status='NA')
        record.save()

        messages.info(request, 'Leaves applied successfully...!!!')
        return redirect('leave_request')

def emp_leaves_history(request):

    emp = employee_info.objects.get(employee_id=request.session['emp_id'])
    leaves=employee_leaves_details.objects.filter(employee_id=request.session['emp_id']).order_by('-applied_date')
    total_leaves=leaves.count()

    return render(request, 'emp_leave_history.html', {'employee': emp,'leaves':leaves,'count':total_leaves})


def cancel_leave_request(request):
    emp = employee_info.objects.get(employee_id=request.session['emp_id'])
    return render(request, 'cancel_leave.html', {'employee': emp})

def cancel_leave(request):

    leave_id=request.POST['leave_id']
    leave_type=request.POST['leave_type']
    leave = employee_leaves_details.objects.filter(employee_id=request.session['emp_id'],leave_id=leave_id,leave_type=leave_type)
    count=leave.count()
    if count==0:
        messages.error(request,'Invalid Leave Id or Leave Type')
        return redirect('cancel_leave_request')

    elif leave[0].status=='Approved':
        messages.error(request, 'Leave is approved so u cant cancel now.')
        return redirect('cancel_leave_request')

    else:
        employee_leaves_details.objects.filter(employee_id=request.session['emp_id'], leave_id=leave_id,leave_type=leave_type).delete()
        messages.error(request, 'Leave Cancelled Successfully....!!')
        return redirect('cancel_leave_request')

def reschedule_leave_request(request):
    emp = employee_info.objects.get(employee_id=request.session['emp_id'])

    return render(request, 'reschedule_leave_request.html', {'employee': emp,'flag': 0})

def check_leave_id(request):

    leave_id=request.POST['leave_id']
    emp_id=request.POST['emp_id']
    leave=employee_leaves_details.objects.filter(employee_id=emp_id,leave_id=leave_id)
    count=leave.count()

    if count!=1:
        messages.error(request, 'Please enter correct leave id.')
        return redirect('reschedule_leave')
    elif leave[0].status == 'Approved':
        messages.error(request, 'Your leave is already approved.')
        return redirect('reschedule_leave')
    else:
        emp = employee_info.objects.get(employee_id=request.session['emp_id'])
        leave_count_record = leave_count.objects.filter(employee_id=request.session['emp_id'])
        if leave_count_record.count() == 0:
            remaining_leaves = 0
        else:
            remaining_leaves = leave_count_record[0].remaining_leaves
        leave_dict={'leave_id':leave_id,'remaining_leaves':remaining_leaves,'leave_type':leave[0].leave_type}
        return render(request,'reschedule_leave_request.html',{'employee': emp,'flag': 1,'leave':leave_dict})


def reschedule_leave(request):

    leave_id = request.POST['leave_id']
    remaining_leaves = request.POST['remaining_leaves']
    leave_type = request.POST['leave_type']
    leave_start_date = request.POST['from_date']
    leave_end_date = request.POST['to_date']
    total_days = request.POST['total_days']
    description = request.POST['desc']


    emp = employee_info.objects.get(employee_id=request.session['emp_id'])
    leave={'leave_id':leave_id,'leave_type':leave_type,'remaining_leaves':remaining_leaves}


    if int(total_days) > int(remaining_leaves):

        messages.error(request, 'Please enter valid total days. Total days is grater than remaining leaves.')
        return render(request, 'reschedule_leave_request.html', {'employee': emp, 'flag': 1, 'leave': leave})

    else:
        leave = employee_leaves_details.objects.get(leave_id=leave_id)
        leave.leave_start_date=leave_start_date
        leave.leave_end_date=leave_end_date
        leave.total_days=total_days
        leave.description=description
        leave.save()
        messages.info(request, 'Leaves applied successfully...!!!')
        return redirect('reschedule_leave')







