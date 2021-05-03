from django.conf.urls import url, include
from django.contrib import admin
from mypage import views 

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^LMList/new$', views.new_list, name='new_list'),    
    url(r'^LMList/(\d+)/$', views.view_list, name='view_item'),    
    url(r'^LMList/(\d+)/add_item$', views.add_item, name='add_item'),]
    
