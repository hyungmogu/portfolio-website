from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView

from django.core.mail import send_mail #this is temporary

from . import models


class HomeView(TemplateView):
    template_name = 'main/home.html'

class WorksView(TemplateView):
    models=models.Project
    template_name = 'main/works.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     projects = models.Project.objects.all().order_by('-date_created')
    #     context['projects'] = projects

    #     return context

class WorksDetailView(DetailView):
    models=models.Project
    template_name = 'main/works_detail.html'

    def get(self, request, pk):
        project = get_object_or_404(
            models.Project,
            pk=pk)

        return render(request, self.template_name, {
            'project': project})

class AboutView(DetailView):
    template_name = 'main/about.html'

    def get(self, request):
        return render(request, self.template_name)

class ContactView(DetailView):
    template_name = 'main/contacts.html'

    def get(self, request):
        return render(request, self.template_name)