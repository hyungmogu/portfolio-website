import main.views as views
from django.urls import path
from django.views.generic.base import RedirectView

domain_name = 'hyungmogu.com'

urlpatterns = [
    path('works/<int:pk>', views.WorksDetailView.as_view(), name='works_detail'),
    path('works', views.WorksView.as_view(), name='works'),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('blogs', RedirectView.as_view(url='http://blog.{}'.format(domain_name)), name='blogs'),
    path('', views.HomeView.as_view(), name='home'),
]
