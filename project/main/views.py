from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = models.projects.objects.all()
        context['projects'] = projects

        return context
