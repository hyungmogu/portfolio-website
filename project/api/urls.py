import api.views as views
from django.urls import path

urlpatterns = [
    path('email/', views.HomeView.as_view(), name='email'),
]
