# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import PdaChangesListView, PdaChangesDetailView, PdaChangesRegisterView, PdaChangesCreateView, listing_by_date #, listing
from django.core.urlresolvers import reverse_lazy


urlpatterns = patterns('',
    #url(r'^$', PdaChangesListView.as_view(), name='index'),
    url(r'^$',listing_by_date , name='index'),

    url(r'^(?P<pk>[0-9]+)/$', PdaChangesDetailView.as_view(), name='detail'),
    url(r'^login/$', 'django.contrib.auth.views.login',
          {"template_name" : "japp/login.html"}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
          {"next_page" : reverse_lazy('japp:login')}, name="logout"),
    url(r'^register/$', PdaChangesRegisterView.as_view(), name='register'),
    url(r'^add/$', PdaChangesCreateView.as_view(), name='add'),
)
