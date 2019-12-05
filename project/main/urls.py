import main.views as views
from django.urls import path, include

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/<int:pk>', views.ProjectView.as_view(), name='project'),
]
