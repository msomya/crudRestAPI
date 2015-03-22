from django.conf.urls import url
from dashboard import views

urlpatterns = [
    url(r'^production/$', views.product_list),
    url(r'^production/search/$', views.production_detail),
    url(r'^production/modify/$',views.production_modify),
]
