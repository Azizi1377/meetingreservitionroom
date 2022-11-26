# Generated by Django 4.1.3 on 2022-11-21 07:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('departmen', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=255)),
                ('applicant', models.CharField(max_length=255, null=True)),
                ('owner', models.CharField(max_length=255)),
                ('date', models.DateField(max_length=30)),
                ('start_time', models.TimeField(default=datetime.time(10, 41, 57, 376762), max_length=30)),
                ('end_time', models.TimeField(max_length=30)),
                ('is_period', models.BooleanField()),
                ('week', models.IntegerField(default=0, null=True)),
                ('is_verifed', models.CharField(choices=[('درحال بررسی', 'درحال بررسی'), ('تایید', 'تایید'), ('نپذیرفتن', 'نپذیرفتن')], default='درحال بررسی', max_length=20)),
                ('meeting_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.meetingroom')),
            ],
        ),
    ]