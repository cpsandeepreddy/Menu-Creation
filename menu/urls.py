from django.conf.urls import patterns, include, url
#from card.views import *
from card import views
from card.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Card.as_view(), name='card'),
    url(r'^show/(?P<id>\w+)/$', Show.as_view(),name='show'),
    url(r'^delete/(?P<id>\w+)/$', Delete.as_view(),name='Delate'),
    url(r'^add/$', Add.as_view(),name='add'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
