from django.urls import path

from . import views

urlpatterns = [
    path('slack/events/', views.events, name='events'),
]
