# Generated by Django 4.0.4 on 2022-06-13 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_jobseeker_company_remove_jobseeker_skills_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='experience',
        ),
    ]
