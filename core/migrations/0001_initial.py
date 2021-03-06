# Generated by Django 2.2.7 on 2019-11-14 14:30

import core.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('E', 'Employer'), ('S', 'Seeker'), ('P', 'Partner'), ('O', 'Others')], max_length=1)),
                ('phone', models.CharField(max_length=10, unique=True, validators=[core.auth.validators.phone_number_validator])),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('alternate_phone', models.CharField(blank=True, max_length=10, null=True, validators=[core.auth.validators.phone_number_validator])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('otp', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancies', models.IntegerField()),
                ('min_experience', models.IntegerField(choices=[(0, '0 to 6 months'), (1, '6 months to 1 year'), (2, '1 year to 2 year'), (3, '2 year to 3 year'), (4, '3 year to 4 year'), (5, 'Four year to 5 year'), (6, 'Above 5')])),
                ('location', models.CharField(max_length=255)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1, null=True)),
                ('educational_qualification', models.CharField(choices=[('BELOW 5th Class', 'BELOW 5th Class'), ('Class 5th to 9th', 'Class 5th to 9th'), ('10th pass', '10th pass'), ('12th pass', '12th pass'), ('ITI', 'ITI'), ('Polytechnic', 'Polytechnic'), ('Diploma', 'Diploma'), ('Graduate (B.Sc., B.A., B.Com.)', 'Graduate (B.Sc., B.A., B.Com.)'), ('Other Graduate (Any Stream)', 'Other Graduate (Any Stream)'), ('B.Tech. (Any Stream)', 'B.Tech. (Any Stream)'), ('M.Tech. (Any Stream)', 'M.Tech. (Any Stream)'), ('Post graduate (Any stream)', 'Post graduate (Any stream)'), ('MBA/PGDM (Any Stream)', 'MBA/PGDM (Any Stream)')], max_length=255)),
                ('salary_range', models.CharField(blank=True, max_length=255, null=True)),
                ('salary_range_in_hand', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('V', 'Verified'), ('B', 'Not Verified')], max_length=1)),
                ('questions', models.TextField(blank=True, null=True)),
                ('eligibility', models.TextField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('reporting_location', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('apply_till', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Pending'), ('S', 'Seen'), ('D', 'Selected'), ('R', 'Rejected'), ('J', 'Joined'), ('B', 'Blacklisted')], max_length=1)),
                ('answer', models.TextField(blank=True, null=True)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('status_changed', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Job')),
            ],
        ),
    ]
