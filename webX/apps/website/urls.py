from django.conf.urls.defaults import *

urlpatterns = patterns('',
		url(r'^$', 'website.views.home', name='websiteHome'),
		)
