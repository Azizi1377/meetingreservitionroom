from django.db import models
import datetime
from jalali_date import date2jalali, datetime2jalali
from django.contrib import messages
from datetime import timedelta

from django_jalali.db import models as jmodels


now = datetime.datetime.now()
time_now = now.time()


class MeetingRoom(models.Model):
    class Meta:
        verbose_name = 'اتاق جلسه'
        verbose_name_plural = 'اتاق جلسات'
        
    name = models.CharField(max_length=255, verbose_name='نام اتاق')
    departmen = models.CharField(max_length=255, verbose_name='نام ساختمان')

    def __str__(self) -> str:
        return self.departmen + ":" + self.name


class Reservation(models.Model):
    class Meta:
        verbose_name = 'رزرو اتاق'
        verbose_name_plural = 'رزرو کردن'
        
    objects = jmodels.jManager()    ##
    
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE, verbose_name=' اتاق جلسه')
    titel = models.CharField(max_length=255, verbose_name=' عنوان') 
    applicant = models.CharField(max_length=255, null=True, verbose_name=' مسئول') 
    owner = models.CharField(max_length=255, verbose_name=' نام درخواست کننده')  
    date = jmodels.jDateField(max_length=30, verbose_name=' تاریخ')    # models.DateField 
    start_time = models.TimeField(max_length=30, default=time_now, verbose_name=' زمان شروع') 
    end_time = models.TimeField(max_length=30, verbose_name=' زمان پایان') 
    is_period = models.BooleanField(verbose_name=' این رزرو تکرار شود ') 
    week = models.IntegerField(null=True, default=0, verbose_name=' تعداد هفته ')

    IN_PROGRESS = 'درحال بررسی'
    SUCCESSFUL = 'تایید'
    FAILED = 'نپذیرفتن'
    STATE_CHOICE = [
        (IN_PROGRESS, 'درحال بررسی'),
        (SUCCESSFUL, 'تایید'),
        (FAILED, 'نپذیرفتن'),
    ]
    is_verifed = models.CharField(max_length=20, choices=STATE_CHOICE, default=IN_PROGRESS, verbose_name=' وضعیت درخواست ')
    
    
    def save(self, *args, **kwargs):
        print("---------------------------------")
        print(self)
        print(args)
        print(kwargs)
        print("---------------------------------")
        super(Reservation, self).save(*args, **kwargs) 

        




    # def clean_repeat_Reservation(self):
  
    #     list7 = [self.cd['date'] + timedelta(days=7*i) for i in range(0, self.cd['week'])]
    #     l = len(list7)
    #     for i in range(l):  
    #         Reservation.objects.create(
    #             meeting_room=self.cd['meeting_room'],
    #             titel=self.cd['titel'],
    #             applicant=self.cd['applicant'],
    #             owner=self.cd['owner'],
    #             date=list7[i],        
    #             start_time=self.cd['start_time'],
    #             end_time=self.cd['end_time'],
    #             is_period=self.cd['is_period'],
    #             week=self.cd['week']
    #         )   
    #     return messages.success(self.request, 'درخواست های شما برای رزرو اتاق جلسات با موفقیت ثبت شدند', 'success')
    
    
    def __str__(self):
        return "%s, %s" % (self.date)
    
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return str(self.meeting_room)
    
    def get_jalali_date(self):
        return date2jalali(self.date)
    get_jalali_date.short_description = "تاریخ"
    
    