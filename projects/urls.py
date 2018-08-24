from django.urls import path
from .views import  (HomePageView,
                    ProjectListView,
                    ProjectDetailView)

app_name='projects'

urlpatterns = [
    path('',ProjectListView.as_view(),name='projects'),
    path('detail/<int:pk>/',ProjectDetailView.as_view(),name='detail'),
]
