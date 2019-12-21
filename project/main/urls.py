import main.views as views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('works/<int:pk>', views.WorksView.as_view(), name='works'),
]
