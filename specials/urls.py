
from django.urls import path
from . import views

app_name = 'specials'

urlpatterns = [
  path('', views.index, name='index'),
  path('print/', views.print, name='print')
]
