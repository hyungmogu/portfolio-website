from django.shortcuts import render
from django.views.generic import TemplateView

from . import models

# Create your views here.

class HomeView(TemplateView):
    models=models.Project
    template_name = 'main/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = models.Project.objects.all()
        context['projects'] = projects

        return context