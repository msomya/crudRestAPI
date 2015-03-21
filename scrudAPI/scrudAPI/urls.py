from django.conf.urls import patterns, include, url
from rest_framework.authtoken.views import obtain_auth_token

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scrudAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/token', obtain_auth_token),
)
