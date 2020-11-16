from django.urls import path

from . import views


app_name = 'slack_app'

urlpatterns = [
    path('events/', views.events, name='events'),
]
