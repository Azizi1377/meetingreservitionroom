from django.shortcuts import render, redirect
from .form import ReservationForm, PostSerchForm
from .models import Reservation
from django.contrib import messages
from .filters import ReservationFilter
from datetime import datetime, timedelta, date
import pandas as pd
import time

# from jalali_date import datetime2jalali, date2jalali




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



# def logic_input_start_time(cd):
#     input_start = list(str(cd['start_time']))
#     input_start.remove(':')
#     del  input_start[4:6]
#     del  input_start[4]
#     input_start = [''.join(input_start)]
#     input_start = int(input_start[0])
#     return input_start


# def logic_input_end_time(cd):
#     input_end = list(str(cd['end_time']))
#     input_end.remove(':')
#     del  input_end[4:6]
#     del  input_end[4]
#     input_end = [''.join(input_end)]
#     input_end = int(input_end[0])
#     return input_end


# def logic_input_date(cd):
#     list6 = []
#     input_date = list(str(cd['date']))
#     input_date.remove('-')
#     input_date.remove('-')
#     input_date = [''.join(input_date)]
#     list6 = list6.__add__(input_date)
#     list6 = int(list6[0])
#     return list6


# def create_week_period(date, period):
#     output = [date + timedelta(days=7*i) for i in range(0, period)]
#     return output
    


# def repeat_Reservation(request, cd):
#     list7 = create_week_period(date=cd['date'], period=cd['week'])
#     l = len(list7)
#     for i in range(l):  
#         Reservation.objects.create(
#             meeting_room=cd['meeting_room'],
#             titel=cd['titel'],
#             applicant=cd['applicant'],
#             owner=cd['owner'],
#             date=list7[i],        
#             start_time=cd['start_time'],
#             end_time=cd['end_time'],
#             is_period=cd['is_period'],
#             week=cd['week']
#         )   
#     return messages.success(request, 'درخواست های شما برای رزرو اتاق جلسات با موفقیت ثبت شدند', 'success')



def create_one_request(request, cd):
    Reservation.objects.create(
        meeting_room=cd['meeting_room'],
        titel=cd['titel'],
        applicant=cd['applicant'],
        owner=cd['owner'],
        date=cd['date'],
        start_time=cd['start_time'],
        end_time=cd['end_time'],
        is_period=cd['is_period'],
        week=cd['week']
    )  
    return messages.success(request, 'درخواست شما برای رزرو اتاق جلسه با موفقیت ثبت شد', 'success')


def staffreservation(request): 
    if request.user.is_authenticated:
        if request.method == 'POST':             
            form = ReservationForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                
                # logic_start = logic_start_time()   
                # logic_end = logic_end_time()   
                # logic_status = logic_verifed()  
                # logic_reped = logic_period()   
                # logic_date = logic_history()
                # logic_input_start = logic_input_start_time(cd) 
                
                
                # logic_input_end = logic_input_end_time(cd)   
                # logic_input_history = logic_input_date(cd)   
                            
                # for x in range(0, len(logic_start)):
                #     if logic_status[x] != 'failed':
                #         if logic_start[x] <= logic_input_start <= logic_end[x] and logic_input_history == logic_date[x]:
                #             date=cd['date']
                #             messages.error(request, f'در تاریخ {date} این زمان قبلا رزرو شده است', 'error')
                #             return redirect('statusroom')
                #         elif logic_start[x] <= logic_input_end <= logic_end[x] and logic_input_history == logic_date[x]:
                #             messages.error(request, f'در این تاریخ زمان مورد نظر قبلا رزرو شده است', 'error')
                #             return redirect('statusroom')
                #         else:
                #             x = x + 1
                    
                    
                    
                    
                        
                # count = Reservation.objects.count()  
                # print(count)             
                # mydata = Reservation.objects.values_list('date')
                # print(mydata)
                # if mydata:
                #     l_date = []
                #     for i in range(count):
                #         print(i)
                #         y = mydata[i][0].year
                #         m = mydata[i][0].month
                #         d = mydata[i][0].day
                        
                #         l_date.append([y, m, d]) 
                                 
                #     print(l_date)
                
                
               
    
                
                
                
                      
                      
                      
                      
                      
                      
                             
 
                
                # if cd['start_time'] == cd['end_time']:
                #     messages.error(request, 'زمان شروع و پایان نباید یکی باشد', 'error')
                #     return redirect('statusroom')  
                
                # if cd['start_time'] > cd['end_time']:
                #     messages.error(request, 'زمان شروع نباید بیشتر از زمان پایان باشد', 'error')
                #     return redirect('statusroom')               
                
                
                # max_time = timedelta(hours=4)   
                # start_time = datetime.strptime(cd['start_time'].strftime("%H:%M"), "%H:%M")
                # end_time = datetime.strptime(cd['end_time'].strftime("%H:%M"), "%H:%M")
                # datea = end_time - start_time
                
                # if datea >= max_time:
                #     messages.error(request, 'زمان جلسه نباید بیشتراز 4 ساعت باشد', 'error')
                #     return redirect('statusroom')
                
                
                
                
                
                repeat = bool(cd['is_period'])
                # if repeat:
                #     repeat_Reservation(request, cd)
                #     return redirect(statusroom)
                # else:
                    # create_one_request(request, cd)  
                    # return redirect(statusroom) 
                                   
        else:
            user = request.user.username         
            form = ReservationForm(initial={'owner':user })       
    else:
        messages.error(request, 'برای درخواست اتاق جلسه ابتدا لاگین کنید', 'error')
        return redirect('user_login')  
             
    return render(request, 'reservations.html', {'form':form})



def statusroom(request): 
    CurrentDay = datetime.today().weekday()
    if CurrentDay<5:
        CurrentDay+=2
    else:
        CurrentDay%=5
          
    #Current Week 
    todaydate = date.today()
    startdate = todaydate - timedelta(days=CurrentDay)
    enddate = todaydate + timedelta(days=6-CurrentDay)
       
    Current_Week = Reservation.objects.filter(date__range=[startdate, enddate])

    if request.GET.get('search'):
        Current_Week = Current_Week.filter(titel__contains=request.GET['search'])
    form_class = PostSerchForm

    return render(request, 'rooms.html', {'statusroom':Current_Week, 'Filter':form_class})  



def change_week(request, *args, **kwargs): 
    current =  int(time.time()) if not request.GET.get("current_date") else int(request.GET.get("current_date"))

    action = request.GET.get("action", None)
    today = datetime.fromtimestamp(current)
    
    if action == "next":
        today = today + timedelta(days=7)
    elif action == "last":
        today = today - timedelta(days=7)
    
    CurrentDay = today.weekday()
    if CurrentDay<5:
        CurrentDay+=2    
    else:
        CurrentDay%=5

    todaydate = today
    startdate = todaydate - timedelta(days=CurrentDay)
    enddate = todaydate + timedelta(days=6-CurrentDay)
      
    next_Week = Reservation.objects.filter(date__range=[startdate, enddate])
    if request.GET.get('search'):
        next_Week = next_Week.filter(titel__contains=request.GET['search'])
    form_class = PostSerchForm
    
    return render(request, 'rooms.html', {'statusroom':next_Week, "startdate":int(startdate.timestamp()), 'Filter':form_class}) 


# def persian_number(mystr):
#     numbers = {
#         "0":"۰",
#         "1":"۱",
#         "2":"۲",
#         "3":"۳",
#         "4":"۴",
#         "5":"۵",
#         "6":"۶",
#         "7":"۷",
#         "8":"۸",
#         "9":"۹",
#     }
#     for e, p in numbers.items():
#         mystr = mystr.replace(e, p)
#     return mystr