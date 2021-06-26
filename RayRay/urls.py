'''from django.conf.urls import url, include
from django.contrib import admin
from bosrayList import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.homepage, name='homepage'),                        
    url(r'^new_profile$', views.new_profile, name='new_profile'),
    url(r'^(\d+)/addpart_id$', views.addpart_id, name='addpart_id'),
    url(r'^(\d+)/view_profile$', views.view_profile, name='view_profile'),
    ]'''





from django.conf.urls import url, include
from django.contrib import admin
from bosrayList import views 

urlpatterns = [    
    url('admin/', admin.site.urls),
    url(r'^$', views.home_page, name='home_page'),
    #url(r'^bosrayList/new$', views.new_list, name='new_list'),    
    #url(r'^bosrayList/(\d+)/$', views.view_list, name='view_item'),    
    #url(r'^bosrayList/(\d+)/add_item$', views.add_item, name='add_item'),
    url(r'^regis$', views.registrate, name='registrate'),
    url(r'^model3$', views.modelsss, name='modelsss'),
    url(r'^model4$', views.modelssss, name='modelssss'),
    url(r'^model5$', views.modelsssss, name='modelsssss'),
    url(r'^contact$', views.contacts, name='contacts'),
    url(r'^about$', views.abouts, name='abouts'),
    ]    

'''
    url(r'^$', views.MainPage, name='mainpage'), #1st model    
    url(r'^bosrayList/new_name$', views.new_ibrgy, name='new_ibrgy'),  ), # 1st model      
    url(r'^bosrayList/(\d+)/$', views.view_ibrgy, name='view_ibrgy'),    #2nd model
    url(r'^bosrayList/(\d+)/add_info$', views.add_info, name='add_info') ,] #2nd model

1st page html action
<form method="POST" action="/new_residents">

1st page html pang view ng data sa table
<tr> {% for ibrgy in ibrgys %}
            
                <td> <a href=bosrayList/{{ibrgy.id}}>{{ibrgy.bID}}</a></td>
                <td>{{ibrgy.bnamer}}</td>
            <td>{{ibrgy.mncplty}}</td>
        </tr> {% endfor %}
2nd page html action

<form method="POST" action="/{{ ibrgy.id }}/add_info">
2nd  page html pang view ng data sa table
{% for bresidents in ibrgy.bresidents_set.all %}
        <tr>
            <!{{ forloop.counter }}:  -->
            <td>{{ forloop.counter }} : {{bresidents.rlname }}</td>
            <td>{{ brsidents.rfname }}</td>
            <td>{{ bresidents.rmname }}</td>
            <td>{{ bresidents.rrelation }}</td>
            <td>{{ bresidents.rjob }}</td>
            <td>{{ bresidents.rnumber }}</td>
            <td>{{ bresidents.radd }}</td>
        
        </tr> {% endfor %} </table>

'''