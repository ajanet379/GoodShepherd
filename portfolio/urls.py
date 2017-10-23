
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^client/$', views.client_list, name='client_list'),
    url(r'^client/(?P<pk>\d+)/delete/$', views.client_delete, name='client_delete'),
    url(r'^client/(?P<pk>\d+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^client/create/$', views.client_new, name='client_new'),
    url(r'^item/$', views.item_list, name='item_list'),
    url(r'^item/(?P<pk>\d+)/delete/$', views.item_delete, name='item_delete'),
    url(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^item/create/$', views.item_new, name='item_new'),
    url(r'^employee/$', views.employee_list, name='employee_list'),
    url(r'^employee/(?P<pk>\d+)/delete/$', views.employee_delete, name='employee_delete'),
    url(r'^employee/(?P<pk>\d+)/edit/$', views.employee_edit, name='employee_edit'),
    url(r'^employee/create/$', views.employee_new, name='employee_new'),
    url(r'^donor/$', views.donor_list, name='donor_list'),
    url(r'^donor/(?P<pk>\d+)/delete/$', views.donor_delete, name='donor_delete'),
    url(r'^donor/(?P<pk>\d+)/edit/$', views.donor_edit, name='donor_edit'),
    url(r'^donor/create/$', views.donor_new, name='donor_new'),


]
