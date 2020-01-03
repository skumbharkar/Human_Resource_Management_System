"""leave_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views,views_admin

urlpatterns =[
    path('', views.homepage),
    path('admin_login',views.admin_login,name='admin_login'),
    path('emp_homepage',views.display_emp_homepage,name='emp_homepage'),
    path('emp_profile', views.emp_profile, name='emp_profile'),
    path('validate_employee',views.validate_employee),
    path('homepage_main',views.homepage,name='homepage'),
    path('log_out',views.log_out,name='log_out'),
    path('change_pwd_request',views.change_pwd_request,name='change_pwd_request'),
    path('change_password',views.change_password),
    path('leave_request',views.leave_request,name='leave_request'),
    path('validate_leaves_details',views.validate_leaves_details),
    path('leave_history',views.emp_leaves_history,name='emp_leaves_history'),
    path('cancel_leave_request',views.cancel_leave_request,name='cancel_leave_request'),
    path('cancel_leave',views.cancel_leave),
    path('reschedule_leave_request',views.reschedule_leave_request,name='reschedule_leave'),
    path('check_leave_id',views.check_leave_id,name='check_leave_id'),
    path('reschedule_leave',views.reschedule_leave),
    #path('forgot_password',views.forgot_password,name='forgot_password'),

    path('validate_admin',views_admin.validate_admin),
    path('show_all_leaves',views_admin.show_all_leaves),
    path('display_dashboard',views_admin.display_dashboard,name='display_dashboard'),
    path('leave_details',views_admin.leave_details),
    path('take_action_request',views_admin.take_action_request,name='take_action_request'),
    path('take_action',views_admin.take_action),
    path('show_approved_leaves',views_admin.show_approved_leaves),
    path('show_NA_leaves',views_admin.show_NA_leaves),
    path('add_department',views_admin.add_department,name='add_department'),
    path('delete_department',views_admin.delete_department,name='delete_department'),
    path('show_departments',views_admin.show_departments,name='show_departments'),
    path('add_employee',views_admin.add_employee,name='add_employee'),
    path('modify_employee',views_admin.modify_employee,name='modify_employee'),
    path('admin_change_pwd',views_admin.admin_change_pwd,name='admin_change_pwd'),


]
