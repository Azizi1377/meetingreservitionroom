from django.contrib import admin
from .models import MeetingRoom, Reservation

from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('titel','applicant','owner', 'date', 'start_time', 'end_time', 'is_period', 'is_verifed')
    list_filter = ('titel','applicant', ('date', JDateFieldListFilter), 'start_time', 'end_time', 'is_verifed')
    search_fields = ('titel','applicant', 'date', 'start_time', 'end_time', 'is_verifed')
    ordering = ['-date']

admin.site.register(MeetingRoom)
admin.site.register(Reservation, ReservationsAdmin)



# get_jalali_date
