from django.conf.urls import url, include
from django.contrib import admin
from bosrayList import views 

urlpatterns = [    
    url('admin/', admin.site.urls),
    url(r'^$', views.home_page, name='home_page'),    
    #url(r'^bosrayList/new$', views.new_list, name='new_list'),    
    #url(r'^bosrayList/(\d+)/$', views.view_list, name='view_item'),    
    #url(r'^bosrayList/(\d+)/add_item$', views.add_item, name='add_item'),]
    url(r'regis/', views.registrate, name='registrate'),
    url(r'model3/', views.modelsss, name='modelsss'),
    url(r'model4/', views.modelssss, name='modelssss'),
    url(r'model5/', views.modelsssss, name='modelsssss'),
    url(r'contact/', views.contacts, name='contacts'),
    url(r'about/', views.abouts, name='abouts'),







    ]    

