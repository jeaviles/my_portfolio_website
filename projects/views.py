from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView)
from .models import Project

class HomePageView(ListView):
    model = Project
    template_name = 'projects/home.html'

    def get_queryset(self):
        return Project.objects.order_by('-pk')[:2]

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects_list.html'

    def get_queryset(self):
        return Project.objects.order_by('-pk')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/projects_detail.html'
