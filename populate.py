import os
import django
from datetime import datetime, timedelta
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Training_Project.settings')
django.setup()

from home.models import Employee, JobSeeker, Contact, City, Qualification

# Sample Data
DEPARTMENTS = ['IT', 'HR', 'Finance', 'Marketing', 'Operations', 'Sales']
DESIGNATIONS = ['Manager', 'Team Lead', 'Executive', 'Senior Executive', 'Associate']
GENDERS = ['Male', 'Female']
CITIES_LIST = ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Kolkata', 'Ahmedabad']
QUALIFICATIONS_LIST = ['B.Tech', 'M.Tech', 'MBA', 'BCA', 'MCA', 'B.Sc', 'M.Sc', 'B.Com', 'M.Com']

FIRST_NAMES = ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram', 'Anjali', 'Arjun', 'Pooja', 'Rohan', 'Divya',
               'Karan', 'Neha', 'Aditya', 'Riya', 'Sanjay', 'Kavita', 'Manish', 'Shreya', 'Rajesh', 'Meera']
LAST_NAMES = ['Sharma', 'Kumar', 'Singh', 'Verma', 'Gupta', 'Patel', 'Rao', 'Iyer', 'Nair', 'Reddy']

print("🚀 Starting bulk data population...")

# 1. Add Cities
print("\n📍 Adding Cities...")
for city in CITIES_LIST:
    City.objects.get_or_create(city=city)
print(f"✓ Added {len(CITIES_LIST)} cities")

# 2. Add Qualifications
print("\n🎓 Adding Qualifications...")
for qual in QUALIFICATIONS_LIST:
    Qualification.objects.get_or_create(qualification=qual)
print(f"✓ Added {len(QUALIFICATIONS_LIST)} qualifications")

# 3. Add Employees (Employee has fname, mname, dob)
print("\n👥 Adding Employees...")
for i in range(1, 51):  # Add 50 employees
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    name = f"{first_name} {last_name}"
    
    employee_data = {
        'empid': f'EMP{i:04d}',
        'name': name,
        'fname': f"{random.choice(FIRST_NAMES)} {last_name}",
        'mname': f"{random.choice(FIRST_NAMES)} {last_name}",
        'gender': random.choice(GENDERS),
        'address': f'{random.randint(1, 999)} Street, Area {random.randint(1, 10)}',
        'city': random.choice(CITIES_LIST),
        'contactno': random.randint(7000000000, 9999999999),
        'email': f'{first_name.lower()}.{last_name.lower()}{i}@electrotech.com',
        'department': random.choice(DEPARTMENTS),
        'designation': random.choice(DESIGNATIONS),
        'dob': datetime.now().date() - timedelta(days=random.randint(8000, 15000)),
        'doj': datetime.now().date() - timedelta(days=random.randint(100, 3650)),
        'salary': random.randint(30000, 150000)
    }
    
    Employee.objects.get_or_create(empid=employee_data['empid'], defaults=employee_data)

print(f"✓ Added 50 employees")

# 4. Add Job Seekers (JobSeeker does NOT have fname, mname, dob)
print("\n🎯 Adding Job Seekers...")
for i in range(1, 31):  # Add 30 job seekers
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    name = f"{first_name} {last_name}"
    
    # FIXED: Only use fields that JobSeeker model actually has
    jobseeker_data = {
        'name': name,
        'gender': random.choice(GENDERS),
        'address': f'{random.randint(1, 999)} Street, Area {random.randint(1, 10)}',
        'city': random.choice(CITIES_LIST),
        'contactno': random.randint(7000000000, 9999999999),
        'email': f'{first_name.lower()}.{last_name.lower()}{i}@gmail.com',
        'qualification': random.choice(QUALIFICATIONS_LIST),
        'date': datetime.now()
    }
    
    JobSeeker.objects.create(**jobseeker_data)

print(f"✓ Added 30 job seekers")

# 5. Add Contact Messages
print("\n💬 Adding Contact Messages...")
MESSAGES = [
    "I would like to inquire about job openings in your company.",
    "Could you please provide information about employee benefits?",
    "I am interested in the HR Manager position.",
    "When will the recruitment drive begin?",
    "Please share details about the interview process.",
    "I have a query regarding my application status.",
    "Thank you for considering my application.",
    "I would like to schedule an interview.",
]

for i in range(1, 21):  # Add 20 messages
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    
    contact_data = {
        'name': f"{first_name} {last_name}",
        'gender': random.choice(GENDERS),
        'address': f'{random.randint(1, 999)} Street, Area {random.randint(1, 10)}',
        'contactno': random.randint(7000000000, 9999999999),
        'email': f'{first_name.lower()}{i}@gmail.com',
        'message': random.choice(MESSAGES),
        'date': datetime.now() - timedelta(days=random.randint(0, 30))
    }
    
    Contact.objects.create(**contact_data)

print(f"✓ Added 20 contact messages")

print("\n✅ Bulk data population completed successfully!")
print("\n📊 Summary:")
print(f"   Cities: {City.objects.count()}")
print(f"   Qualifications: {Qualification.objects.count()}")
print(f"   Employees: {Employee.objects.count()}")
print(f"   Job Seekers: {JobSeeker.objects.count()}")
print(f"   Contact Messages: {Contact.objects.count()}")