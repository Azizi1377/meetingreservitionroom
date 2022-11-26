from django import forms
from .models import Reservation
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from . import views



class ReservationForm(forms.ModelForm): 
    class Meta:
        model = Reservation
        fields = [
            'meeting_room',
            'titel',
            'applicant',
            'owner',
            'date',
            'start_time',
            'end_time',
            'is_period',
            'week'
        ] 
        
        widgets = {
            'start_time': forms.TimeInput(format='%H:%M'),
            'end_time': forms.TimeInput(format='%H:%M'),
        } 
        
        labels = {
            "meeting_room": "اتاق جلسه",
            "titel": "عنوان",
            "applicant": "مسئول جلسه",
            "owner": "نام درخواست کننده",
            "start_time": "زمان شروع جلسه",
            "end_time": "زمان پایان جلسه",
            "is_period": "آیا این رزرو تکرار شود",
            "week": "برای چند هفته" 
        }
        
        # def clean_is_period(self):
        #     data = self.clean_data.get('is_period')  
        #     if data == True:
        #         return views.repeat_Reservation()
                                       
       
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=('تاریخ'), widget=AdminJalaliDateWidget)




class PostSerchForm(forms.Form):
    search = forms.CharField()