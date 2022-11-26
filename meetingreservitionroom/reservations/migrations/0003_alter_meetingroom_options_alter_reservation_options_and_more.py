# Generated by Django 4.1.3 on 2022-11-25 12:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_alter_reservation_start_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetingroom',
            options={'verbose_name': 'اتاق جلسه', 'verbose_name_plural': 'اتاق جلسات'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'رزرو اتاق', 'verbose_name_plural': 'رزرو کردن'},
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='departmen',
            field=models.CharField(max_length=255, verbose_name='نام ساختمان'),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام اتاق'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='applicant',
            field=models.CharField(max_length=255, null=True, verbose_name=' مسئول'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=django_jalali.db.models.jDateField(max_length=30, verbose_name=' تاریخ'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='end_time',
            field=models.TimeField(max_length=30, verbose_name=' زمان پایان'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='is_period',
            field=models.BooleanField(verbose_name=' این رزرو تکرار شود '),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='is_verifed',
            field=models.CharField(choices=[('درحال بررسی', 'درحال بررسی'), ('تایید', 'تایید'), ('نپذیرفتن', 'نپذیرفتن')], default='درحال بررسی', max_length=20, verbose_name=' وضعیت درخواست '),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='meeting_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.meetingroom', verbose_name=' اتاق جلسه'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='owner',
            field=models.CharField(max_length=255, verbose_name=' نام درخواست کننده'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_time',
            field=models.TimeField(default=datetime.time(15, 42, 31, 42826), max_length=30, verbose_name=' زمان شروع'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='titel',
            field=models.CharField(max_length=255, verbose_name=' عنوان'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='week',
            field=models.IntegerField(default=0, null=True, verbose_name=' تعداد هفته '),
        ),
    ]