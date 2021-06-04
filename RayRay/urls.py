from django.conf.urls import url, include
from django.contrib import admin
from bosrayList import views 

urlpatterns = [    
    url('admin/', admin.site.urls),
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^bosrayList/new$', views.new_list, name='new_list'),    
    url(r'^bosrayList/(\d+)/$', views.view_list, name='view_item'),    
    url(r'^bosrayList/(\d+)/add_item$', views.add_item, name='add_item'),]
    

