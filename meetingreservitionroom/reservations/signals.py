from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from datetime import timedelta

from .models import Reservation

from django.http import HttpResponseBadRequest
from django.core.exceptions import BadRequest
from datetime import datetime, timedelta, date

list7 = []
@receiver(post_save, sender=Reservation)
def handle_repeated_reservation(sender, instance, created, **kwargs):
    if created:
        if instance.is_period:
            list7 = [instance.date + timedelta(days=7*i) for i in range(0, instance.week)]
            l = len(list7)
            for i in range(1,l):  #for i in range(instance.week):
                Reservation.objects.create(
                    meeting_room=instance.meeting_room,
                    titel=instance.titel,
                    applicant=instance.applicant,
                    owner=instance.owner,
                    date=list7[i], # instance.date,
                    start_time=instance.start_time,
                    end_time=instance.end_time,
                    is_period=False,
                    week=0,
                )

@receiver(pre_save, sender=Reservation)
def handle_equalـtime_reservation(sender, instance, **kwargs):
    if instance.start_time == instance.end_time:
        raise BadRequest('زمان شروع و پایان نباید یکی باشد')
    

@receiver(pre_save, sender=Reservation)
def handle_equalـtime_reservation(sender, instance, **kwargs):
    if instance.start_time > instance.end_time:
        raise BadRequest('زمان شروع نباید بیشتر از زمان پایان باشد')



@receiver(pre_save, sender=Reservation)
def handle_equalـtime_reservation(sender, instance, **kwargs):
    max_time = timedelta(hours=4)   
    start_time = datetime.strptime(instance.start_time.strftime("%H:%M"), "%H:%M")
    end_time = datetime.strptime(instance.end_time.strftime("%H:%M"), "%H:%M")
    datea = end_time - start_time

    if datea >= max_time:
        raise BadRequest('زمان جلسه نباید بیشتراز 4 ساعت باشد')



# def logic_start_time():
#     list1 = []
#     Period = Reservation.objects.all()
#     for p in Period:                   
#         start = p.start_time
#         start = list(str(start))
#         start.remove(':')
#         del  start[4:6]
#         del  start[4]
#         start = [''.join(start)]
#         list1 = list1.__add__(start) 
#         for i in range(0, len(list1)):
#             list1[i] = int(list1[i])  
#     return list1


# def logic_end_time():
#     list2 = []
#     Period = Reservation.objects.all()
#     for p in Period:                     
#         end = p.end_time                           
#         end = list(str(end))                             
#         end.remove(':')      
#         del  end[4:6]  
#         del  end[4]           
#         end = [''.join(end)]                          
#         list2 = list2.__add__(end)                                       
#         for i in range(0, len(list2)):
#             list2[i] = int(list2[i])   
#     return list2


# def logic_verifed():
#     list3 = []
#     Period = Reservation.objects.all()
#     for p in Period:                  
#         verifed = p.is_verifed 
#         verifed = list(str(verifed))
#         verifed = [''.join(verifed)]
#         list3 = list3.__add__(verifed) 
#     return list3


# def logic_period():
#     list4 = []
#     Period = Reservation.objects.all()
#     for p in Period:                   
#         period = p.is_period
#         period = list(str(period))
#         period = [''.join(period)]
#         list4 = list4.__add__(period) 
#     return list4


# def logic_history():
#     list5 = []
#     Period = Reservation.objects.all()
#     for p in Period:                 
#         history = p.date 
#         history = list(str(history))
#         history.remove('-')
#         history.remove('-')
#         history = [''.join(history)]
#         list5 = list5.__add__(history)
#         for i in range(0, len(list5)):
#             list5[i] = int(list5[i]) 
#     return list5




# @receiver(pre_save, sender=Reservation)
# def logic_input_start_time(sender, instance, **kwargs):
#     input_start = list(str(instance.start_time))
#     input_start.remove(':')
#     del  input_start[4:6]
#     del  input_start[4]
#     input_start = [''.join(input_start)]
#     input_start = int(input_start[0])
#     return input_start



# @receiver(pre_save, sender=Reservation)
# def logic_input_end_time(sender, instance, **kwargs):
#     input_end = list(str(instance.end_time))
#     input_end.remove(':')
#     del  input_end[4:6]
#     del  input_end[4]
#     input_end = [''.join(input_end)]
#     input_end = int(input_end[0])
#     return input_end



# @receiver(pre_save, sender=Reservation)
# def logic_input_date(sender, instance, **kwargs):
#     list6 = []
#     input_date = list(str(instance.date))
#     input_date.remove('-')
#     input_date.remove('-')
#     input_date = [''.join(input_date)]
#     list6 = list6.__add__(input_date)
#     list6 = int(list6[0])
#     return list6


# logic_start = logic_start_time()   
# logic_end = logic_end_time()   
# logic_status = logic_verifed()  
# logic_reped = logic_period()   
# logic_date = logic_history()



# # logic_input_start = logic_input_start_time() 


# # logic_input_end = logic_input_end_time()   
# # logic_input_history = logic_input_date() 




# @receiver(pre_save, sender=Reservation)
# def handle_equalـtime_reservation(sender, instance, **kwargs): 
#     for x in range(0, len(logic_start)):
#         if logic_status[x] != 'failed':
#             if logic_start[x] <= logic_input_start_time(instance) <= logic_end[x] and logic_input_date(instance) == logic_date[x]:
#                 date=instance.date
#                 raise BadRequest(f'در تاریخ {date} این زمان قبلا رزرو شده است')
#             elif logic_start[x] <= logic_input_end_time(instance) <= logic_end[x] and logic_input_date(instance) == logic_date[x]:
#                 raise BadRequest('در این تاریخ زمان مورد نظر قبلا رزرو شده است')
#             else:
#                 x = x + 1
                