from re import template
from unicodedata import name
from django.contrib import admin
from django.urls import path, reverse_lazy
from home import views
from .forms import MyPasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("registration", views.registration, name = 'registration'),
    path("admin_login", views.admin_login, name = 'admin_login'),
    path("admin_home", views.admin_home, name = 'admin_home'),
    path("admin_logout", views.admin_logout, name = 'admin_logout'),
    path("contact", views.contact, name = 'contact'),
    path("change_password", PasswordChangeView.as_view(
        template_name = 'admin_zone/change_password.html', 
        form_class=MyPasswordChangeForm, 
        success_url=('change_password')),
        name='change_password'
    ),
    path("city", views.city, name = 'city'),
    path("contact_view", views.contact_view, name = 'contact_view'),
    path("emp_reg", views.emp_reg, name = 'emp_reg'),
    path("update_emp", views.update_emp, name = 'update_emp'),
    path("del_emp", views.del_emp, name = 'del_emp'),
    path("del_city", views.del_city, name = 'del_city'),
    path("del_qual", views.del_qual, name = 'del_qual'),
    path("del_js", views.del_js, name = 'del_js'),
    path("del_contact", views.del_contact, name = 'del_contact'),
    path("emp_manage", views.emp_manage, name = 'emp_manage'),
    path("email_handler", views.email_handler, name = 'email_handler'),
    path("generate_mail", views.generate_mail, name = 'generate_mail'),
    path("contact_mail", views.contact_mail, name = 'contact_mail'),
    path("jobseeker", views.jobseeker, name = 'jobseeker'),
    path("qualification", views.qualification, name = 'qualification'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)