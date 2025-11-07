from datetime import datetime
import email
from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from home.models import Contact, JobSeeker, City, Qualification, Employee
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.core.mail import send_mail
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        city = request.POST.get('city')
        contactno = request.POST.get('contactno')
        email = request.POST.get('email')
        qualification = request.POST.getlist('qualification')
        file = request.POST.get('file')
        jobseeker = JobSeeker(name=name, gender=gender, address=address, city=city, contactno=contactno, email=email, qualification=qualification, file=file, date=datetime.today())
        # reCaptcha 
        clientKey = request.POST['g-recaptcha-response']
        secretKey = '6LfXwWggAAAAAHorSSLbBTHEs_sof0NUSS65CEO8'
        captchaData = {
            'secret': secretKey,
            'response': clientKey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data= captchaData)
        response = json.loads(r.text)
        verify = response['success']
        if verify:
            jobseeker.save()
            messages.success(request, 'Your request has been sent!')
            return HttpResponseRedirect(reverse('registration'))
        else:
            messages.error(request, 'Tick the Captcha')
            return HttpResponseRedirect(reverse('registration'))
    cities = City.objects.all()
    qualification = Qualification.objects.all()
    return render(request, 'registration.html', {'cities': cities, 'qualification': qualification})

def admin_login(request):
    # admin@gmail.com | pwd: Qazwsx@@123
    if request.method=="POST":
        admin_email = request.POST.get('admin_email')
        admin_pwd = request.POST.get('admin_pwd')
        #Check if credentials are correct
        user = authenticate(username = admin_email, password = admin_pwd)
        if user is not None:
            login(request, user)
            return redirect("admin_home")
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect("admin_login")
    return render(request, 'admin_login.html')

def admin_logout(request):
    logout(request)
    return render(request, 'admin_login.html')

def admin_home(request):
    if request.user.is_anonymous:
        return redirect("admin_login")

    return render(request, "admin_zone/admin_home.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        contactno = request.POST.get('contactno')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, gender=gender, address=address, contactno=contactno, email=email, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        return HttpResponseRedirect(reverse('contact'))
    return render(request, 'contact.html')

def change_password(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your password has been changed!')
            update_session_auth_hash(request, fm.user)
            return HttpResponseRedirect('change_password')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'admin_zone/change_password.html', {'form': fm})

def city(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    if request.method == "POST":
        city = request.POST.get('city')
        cityob = City(city=city)
        cityob.save()
        messages.success(request, city + ' has been added!')
        return HttpResponseRedirect(reverse('city'))
    cities = City.objects.all()
    return render(request, 'admin_zone/city.html', {'cities': cities})

def contact_view(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    contacts = Contact.objects.all()
    return render(request, 'admin_zone/contact_view.html', {'contacts': contacts})

def emp_manage(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    employees = Employee.objects.all()
    return render(request, 'admin_zone/emp_manage.html', {'employees': employees})

def update_emp(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    emp_id = request.GET.get('empid')
    if request.method == "POST":
        name = request.POST['name']
        fname = request.POST['fname']
        mname = request.POST['mname']
        gender = request.POST['gender']
        address = request.POST['address']
        city = request.POST['city']
        contactno = request.POST['contactno']
        email = request.POST['email']
        department = request.POST['department']
        designation = request.POST['designation']
        dob = request.POST['dob']
        doj = request.POST['doj']
        salary = request.POST['salary']
        Employee.objects.filter(empid=emp_id).update(name=name, fname=fname, mname=mname, gender=gender, address=address, city=city, contactno=contactno, email=email, department=department, designation=designation, dob=dob, doj=doj, salary=salary)
        messages.success(request,  name +' has been updated!')
        return HttpResponseRedirect(reverse('emp_manage'))
    employee = Employee.objects.get(empid=emp_id)
    cities = City.objects.all()
    return render(request, 'admin_zone/update_emp.html', {'employee':employee, 'cities': cities})

def emp_reg(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    if request.method == "POST":
        empid = request.POST.get('empid')
        name = request.POST.get('name')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        city = request.POST.get('city')
        contactno = request.POST.get('contactno')
        email = request.POST.get('email')
        department = request.POST.get('department')
        designation = request.POST.get('designation')
        dob = request.POST.get('dob')
        doj = request.POST.get('doj')
        salary = request.POST.get('salary')
        if Employee.objects.filter(empid=empid).exists():
            messages.success(request,'Employee ID: ' + empid + ' already exists.')
            return HttpResponseRedirect(reverse('emp_reg'))
        else:
            Employee.objects.create(empid=empid, name=name, fname=fname, mname=mname, gender=gender, address=address, city=city, contactno=contactno, email=email, department=department, designation=designation, dob=dob, doj=doj, salary=salary)
            JobSeeker.objects.filter(email=email).delete()
            messages.success(request,  name + ' has been registered!')
            send_mail(
            "Electrotech Recruitment",
            "Congralutions!!!!! \nDear " + name + ",\nYour application has been accepted.\nWe will contact you shortly :D",
            'REDACTED_EMAIL',
            [email],
            fail_silently=False        
            )
            messages.success(request,'Mail has been sent to ', name)
            return HttpResponseRedirect(reverse('emp_reg'))
    cities = City.objects.all()
    jobseeker = JobSeeker.objects.all()
    return render(request, 'admin_zone/emp_reg.html',{'jobseeker': jobseeker, 'cities': cities})

def jobseeker(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    jobseekers = JobSeeker.objects.all()
    return render(request, 'admin_zone/jobseeker.html', {'jobseekers': jobseekers})

def qualification(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    if request.method == "POST":
        qualification = request.POST.get('qualification')
        qual = Qualification(qualification=qualification)
        qual.save()
        messages.success(request, qualification + ' has been added!')
        return HttpResponseRedirect(reverse('qualification'))
    qualification = Qualification.objects.all()
    return render(request, 'admin_zone/qualification.html', {'qualification': qualification})

def del_emp(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    emp_id = request.GET.get('empid')
    name = request.GET.get('name')
    email = request.GET.get('email')
    Employee.objects.filter(empid=emp_id).delete()
    send_mail(
        "Electrotech Recruitment",
        "Hello \nDear " + name + ",\nYour job has been terminated.\nWe wish you all the luck for you future.",
        'REDACTED_EMAIL',
        [email],
        fail_silently=False        
    )
    messages.success(request,'Mail has been sent to ' + name + " about termination of job.")
    return HttpResponseRedirect(reverse('emp_manage'))

def del_city(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    id = request.GET.get('id')
    City.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('city'))

def del_qual(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    id = request.GET.get('id')
    Qualification.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('qualification'))

def del_js(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    id = request.GET.get('id')
    name = request.GET.get('name')
    email = request.GET.get('email')    
    JobSeeker.objects.filter(id=id).delete()
    send_mail(
            "Electrotech Recruitment",
            "Hi " + name + "\nUnfortunately your application has been rejected.\nBetter Luck Next Time.",
            'REDACTED_EMAIL',
            [email],
            fail_silently=False        
        )
    return HttpResponseRedirect(reverse('jobseeker'))

def del_contact(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    id = request.GET.get('id')
    Contact.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('contact_view'))

def email_handler(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    emp_id = request.GET.get('empid')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            subject,
            message,
            'REDACTED_EMAIL',
            [email],
            fail_silently=False        
        )
        messages.success(request, 'Mail has been sent to ' + name)
        return HttpResponseRedirect(reverse('emp_manage'))
    employee = Employee.objects.get(empid=emp_id)
    return render(request, 'admin_zone/email_handler.html', {'employee':employee})

def generate_mail(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            subject,
            message,
            'REDACTED_EMAIL',
            [email],
            fail_silently=False        
        )
        messages.success(request, 'Mail has been sent to ' + name)
        return HttpResponseRedirect(reverse('generate_mail'))
    return render(request, 'admin_zone/generate_mail.html')

def contact_mail(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    id = request.GET.get('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            subject,
            message,
            'REDACTED_EMAIL',
            [email],
            fail_silently=False        
        )
        messages.success(request, 'Mail has been sent to ' + name)
        return HttpResponseRedirect(reverse('contact_view'))
    contact = Contact.objects.get(id=id)
    return render(request, 'admin_zone/contact_mail.html', {'contact': contact})