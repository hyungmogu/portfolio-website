import main.views as views
from django.urls import path

urlpatterns = [
    path('projects/<int:pk>', views.ProjectView.as_view(), name='project'),
]
