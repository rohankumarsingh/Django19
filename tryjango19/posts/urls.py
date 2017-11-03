from django.conf.urls import url
from django.contrib import admin
#from posts import views as post_view

#from posts import views
from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete
)

urlpatterns = [

url(r'^$',post_list),
url(r'^create/$',post_create),
url(r'^detail/$',post_detail),
url(r'^update/$',post_update),
url(r'^delete/$',post_delete),

  # url(r'^$',post_view.post_list),
   # url(r'^create/$',post_view.post_create),
    #url(r'^detail/$',post_view.post_detail),
    #url(r'^update/$',post_view.post_update),
    #url(r'^delete/$',post_view.post_delete),
   
    #url(r'^admin/', "<appname>.views.<function_name>"),
]