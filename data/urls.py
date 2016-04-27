from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.employee_list, name='employee_list'),
    url(r'^sort/$', views.sort, name='sort'),
    url(r'^search/$', views.search, name='search'),
]
