import main.views as views
from django.urls import path

urlpatterns = [
    path('works/<int:pk>', views.WorksDetailView.as_view(), name='works_detail'),
    path('works', views.WorksView.as_view(), name='works'),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('', views.HomeView.as_view(), name='home'),
]
