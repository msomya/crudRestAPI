from django.conf.urls import url
from dashboard import views

urlpatterns = [
    url(r'^dashboard/$', views.product_list),
    url(r'^dashbroad/(?P<pk>[0-9]+)/$', views.product_detail),
]
