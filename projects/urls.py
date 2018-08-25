from django.urls import path,include
from .views import  (HomePageView,
                    ProjectListView)

app_name='projects'

urlpatterns = [
    path('',ProjectListView.as_view(),name='projects'),
    path('amort/',include('amort.urls',namespace='amort')),
]
