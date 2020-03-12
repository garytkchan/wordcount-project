

from django.urls import path
from . import views # . means this directory

urlpatterns = [
    path('', views.home, name='home'),
    path('count_it/', views.count, name='count'), #urlName, defCount, match_form_Action 'count'
]
