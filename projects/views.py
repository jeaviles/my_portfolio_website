from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView

class HomePageView(TemplateView):
    template_name = 'projects/home.html'

class ProjectListView(TemplateView):
    template_name = 'projects/projects_list.html'
