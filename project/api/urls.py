import api.views as views
from django.urls import path

app_name = 'api'
urlpatterns = [
    path('email/', views.ForwardEmail.as_view(), name='email'),
]
