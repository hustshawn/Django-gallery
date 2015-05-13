from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'trips.views.home', name='home'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'trips.views.hello_world'),
    url(r'^post/(?P<id>\d+)/$', 'trips.views.post_detail',name='post_detail'),
#	url(r'^hello/$', 'trips.views.hello_shawn'),

)