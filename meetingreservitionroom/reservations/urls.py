from django.urls import path
from . import views

urlpatterns = [
    path('', views.statusroom, name='statusroom'),
    path('reservation/', views.staffreservation, name='reservation'),
    path('change_week', views.change_week, name='change_week'),
]