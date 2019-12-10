from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView

from . import models

class HomeView(TemplateView):
    models=models.Project
    template_name = 'main/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = models.Project.objects.all().order_by('-date_created')
        context['projects'] = projects

        return context

class ProjectView(DetailView):
    models=models.Project
    template_name = 'main/projects_detail.html'

    def get(self, request, pk):
        project = get_object_or_404(
            models.Project,
            pk=pk)

        return render(request, self.template_name, {
            'project': project})
