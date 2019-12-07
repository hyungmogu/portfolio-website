import main.views as views
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
>>>>>>> fix: downgrade to django 2.1.1

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/<int:pk>', views.ProjectView.as_view(), name='project'),
]
