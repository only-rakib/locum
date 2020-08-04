
from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_view, name='locum_apply'),
    path('contact/', views.contact_us_view, name='contact_us'),
    path('job/', views.job_search_view, name='job_search'),
    path('resourse/', views.resourse_view, name='resourse'),
]
