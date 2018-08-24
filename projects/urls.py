from django.urls import path
from .views import HomePageView,ProjectListView
urlpatterns = [
    path('',ProjectListView.as_view(),name='projects'),
]
