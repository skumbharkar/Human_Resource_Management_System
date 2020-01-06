from django.shortcuts import render,redirect
from .models import admin_info,employee_info,employee_leaves_details,leave_count,department
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from datetime import datetime
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from HRMS.settings import EMAIL_HOST_USER

def validate_admin(request):

    email_id = request.POST['email']
    pwd = request.POST['password']

    try:
        emp = admin_info.objects.get(email=email_id, password=pwd)
    except admin_info.DoesNotExist:
        messages.error(request,"Invalid username or password")
        return redirect('admin_login')
    else:
        request.session['emp_id']=emp.employee_id
        return render(request, 'admin_homepage.html', {'employee': emp})


def show_all_leaves(request):

    all_leaves=employee_leaves_details.objects.all().order_by('-applied_date')
    paginator=Paginator(all_leaves,5)
    page=request.GET.get('page')

    emp = admin_info.objects.get(employee_id=request.session['emp_id'])

    try:
        leave=paginator.get_page(page)
    except PageNotAnInteger:
        leave=paginator.get_page(1)
    except EmptyPage:
        leave=paginator.get_page(paginator.num_pages)

    return render(request,'display_all_leaves.html',{'employee':emp,'leaves':leave})

def display_dashboard(request):

    leaves_for_approval = employee_leaves_details.objects.filter(status='NA').order_by('-applied_date')
    paginator = Paginator(leaves_for_approval, 5)
    page = request.GET.get('page')
    emp = admin_info.objects.get(employee_id=request.session['emp_id'])

    summary={}
    summary['total_leaves']=employee_leaves_details.objects.all().count()
    summary['approved_leaves']=summary['total_leaves'] - leaves_for_approval.count()
    summary['na_leaves']=leaves_for_approval.count()

    try:
        leave=paginator.get_page(page)
    except PageNotAnInteger:
        leave=paginator.get_page(1)
    except EmptyPage:
        leave=paginator.get_page(paginator.num_pages)

    return render(request,'display_dashboard.html',{'employee':emp,'leaves':leave,'summary':summary})

def leave_details(request):

    leave_id=request.GET.get('leave_id')
    caller_id=request.GET.get('caller_id')

    leave=employee_leaves_details.objects.get(leave_id=leave_id)
    emp = admin_info.objects.get(employee_id=request.session['emp_id'])
    return render(request,'leave_info.html',{'employee':emp,'leave':leave,'caller_id':caller_id})

def take_action_request(request):

    leave_id=request.GET.get('leave_id')
    emp = admin_info.objects.get(employee_id=request.session['emp_id'])
    return render(request,'take_action_request.html',{'employee':emp,'leave_id':leave_id})

def take_action(request):
    leave_id=request.POST['leave_id']
    status=request.POST['action']
    comments=request.POST['comments']

    if status=='Approved':
        leave=employee_leaves_details.objects.get(leave_id=leave_id)
        leave.status=status
        leave.comments=comments

        emp_id=leave.employee_id
        rec=leave_count.objects.get(employee_id=emp_id)
        rec.remaining_leaves=rec.remaining_leaves - leave.total_days
        rec.leaves_taken=rec.leaves_taken + leave.total_days
        rec.save()
        leave.save()
        print("Hi........."+EMAIL_HOST_USER)
        '''subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = ["mayurichidrawar111@gmail.com"]
        send_mail(subject,message, EMAIL_HOST_USER, recepient, fail_silently=False)'''
    else:
        leave = employee_leaves_details.objects.get(leave_id=leave_id)
        leave.status = status
        leave.comments = comments
        leave.save()

    messages.info(request,'Action applied successfully...!!')
    return redirect('take_action_request')

def show_approved_leaves(request):

    action=request.GET.get('action')
    emp = admin_info.objects.get(employee_id=request.session['emp_id'])

    if action == 'search' :
        leave_id = request.POST['leave_id']
        leaves = employee_leaves_details.objects.filter(leave_id=leave_id)
        return render(request, 'display_approved_leaves.html', {'employee': emp, 'leaves': leaves,'flag':0})

    else:
        all_approved_leaves = employee_leaves_details.objects.filter(status='Approved').order_by('-applied_date')
        paginator = Paginator(all_approved_leaves, 5)
        page = request.GET.get('page')

        try:
            leave = paginator.get_page(page)
        except PageNotAnInteger:
            leave = paginator.get_page(1)
        except EmptyPage:
            leave = paginator.get_page(paginator.num_pages)

        return render(request, 'display_approved_leaves.html', {'employee': emp, 'leaves': leave,'flag':1})

def show_NA_leaves(request):
    all_NA_leaves = employee_leaves_details.objects.filter(status='NA').order_by('-applied_date')
    paginator = Paginator(all_NA_leaves, 5)
    page = request.GET.get('page')

    emp = admin_info.objects.get(employee_id=request.session['emp_id'])

    try:
        leave = paginator.get_page(page)
    except PageNotAnInteger:
        leave = paginator.get_page(1)
    except EmptyPage:
        leave = paginator.get_page(paginator.num_pages)

    return render(request, 'display_NA_leaves.html', {'employee': emp, 'leaves': leave})

def add_department(request):

    action=request.GET.get('action')

    if action == 'add':
        dept_code=request.POST['dept_code']
        dept_name=request.POST['dept_name']
        creation_date=request.POST['creation_date']
        record=department(dept_code=dept_code,dept_name=dept_name,created_date=creation_date)
        record.save()

        messages.info(request,'Department Saved Successfully...!!!')
        return redirect('add_department')
    else:
        emp = admin_info.objects.get(employee_id=request.session['emp_id'])
        return render(request,'add_department.html',{'employee':emp})

def delete_department(request):

    action = request.GET.get('action')

    if action == 'delete':
        dept_code = request.POST['dept_code']
        dept_name = request.POST['dept_name']

        dept = department.objects.filter(dept_code=dept_code, dept_name=dept_name)

        if dept.count() == 1:
            dept.delete()
            messages.info(request, 'Department deleted successfully...!!!')
            return redirect('delete_department')
        else:
            messages.error(request, 'Invalid department code or department name')
            return redirect('delete_department')

    else:
        emp = admin_info.objects.get(employee_id=request.session['emp_id'])
        dept = department.objects.all()
        return render(request, 'delete_department.html', {'employee': emp,'dept':dept})

def show_departments(request):

    emp = admin_info.objects.get(employee_id=request.session['emp_id'])
    dept=department.objects.all()
    return render(request, 'show_departments.html', {'employee': emp,'dept':dept})

def add_employee(request):

    action = request.GET.get('action')

    if action == 'add':

        emp_id=request.POST['emp_id']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        dept=request.POST['dept']
        dob=request.POST['dob']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        mob=request.POST['mob']
        pan_card=request.POST['pan_card']
        aadhar=request.POST['aadhar_card']
        pwd=request.POST['pwd']
        photo=request.FILES['photo']
        status=request.POST['status']

        record=employee_info(employee_id=emp_id,first_name=first_name,last_name=last_name,email=email,department=dept,
                             dob=dob,city_town=city,state=state,country=country,mobile_no=mob,pan_card=pan_card,aadhar_no=aadhar,
                             password=pwd,status=status,photo=photo)
        record.save()
        messages.info(request,'Employee added successfully...!!!')
        return redirect('add_employee')
    else:
        emp = admin_info.objects.get(employee_id=request.session['emp_id'])
        dept= department.objects.all()
        new_emp_id=employee_info.objects.all().last().employee_id + 1
        return render(request, 'add_employee.html', {'employee': emp,'dept':dept,'new_emp_id':new_emp_id})

def modify_employee(request):
    action=request.GET.get('action')

    if action == 'check':
        emp_id=request.POST['emp_id']
        record=employee_info.objects.filter(employee_id=emp_id)

        if record.count()==0:
            messages.error(request, 'Invalid employee id')
            return redirect('modify_employee')
        else:
            emp = admin_info.objects.get(employee_id=request.session['emp_id'])
            dept = department.objects.all()
            return render(request,'modify_employee.html',{'employee': emp,'flag':1,'dept':dept,'record':record})

    elif action == 'modify':
        emp_id = request.POST['emp_id']
        dept=request.POST['dept']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        mob=request.POST['mob']
        status=request.POST['status']

        record=employee_info.objects.get(employee_id=emp_id)
        record.department=dept
        record.city_town=city
        record.state=state
        record.country=country
        record.mobile_no=mob
        record.status=status

        record.save()
        messages.info(request, 'Employee modified...!!!')
        return redirect('modify_employee')

    else:
        emp = admin_info.objects.get(employee_id=request.session['emp_id'])
        return render(request, 'modify_employee.html', {'employee': emp,'flag':0})

def admin_change_pwd(request):

    action = request.GET.get('action')
    emp = admin_info.objects.get(employee_id=request.session['emp_id'])

    if action == 'submit':

        current_pwd = request.POST['current_pwd']
        new_pwd = request.POST['new_pwd']
        confirm_pwd = request.POST['confirm_pwd']

        if current_pwd != emp.password:
            messages.error(request, 'Invalid Current Password')
            return redirect('admin_change_pwd')
        elif new_pwd != confirm_pwd:
            messages.error(request, 'New password doesnt match with confirmed password')
            return redirect('admin_change_pwd')
        else:
            emp.password = new_pwd
            emp.save()
            messages.info(request, 'Password Changed Successfully...')
            return redirect('admin_change_pwd')

    else:
        return render(request, 'admin_pwd_change.html', {'employee': emp})
