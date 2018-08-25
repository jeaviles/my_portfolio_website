from django.urls import path
from .views import amort_view

app_name='amort'

urlpatterns = [
    path('',amort_view,name='amort'),
]
