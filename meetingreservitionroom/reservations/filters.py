import django_filters
from django_filters import DateFilter
from .models import Reservation


class ReservationFilter(django_filters.FilterSet):
    
    titel = django_filters.CharFilter(label='عنوان')
    date =DateFilter(field_name="date", lookup_expr='gte', label='تاریخ')
    meeting_room = django_filters.CharFilter(label='اتاق')
    
    class Meta:
        model = Reservation
        fields = [
            'titel',
            'date',
            'meeting_room'
        ]
    
            