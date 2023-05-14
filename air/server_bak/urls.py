from django.contrib import admin
from django.urls import path
from user import views as user
from air import views as air
from flight import views as flight
from django.urls import path



urlpatterns = [
    path('save/', user.save, name='save'),
    path('update/', user.update, name='update'),
    path('login/', user.login, name='login'),
    path('list/', user.list, name='list'),
    path('info/', user.info, name='info'),
    path('save/', flight.save, name='save'),
    path('update/', flight.update, name='update'),
    path('list/', flight.list, name='list'),
    path('page/', flight.page, name='page'),
    path('page1/', flight.page1, name='page1'),
    path('delete/', air.delete, name='delete'),
    path('update/', air.update, name='update'),
    path('page/', air.page, name='page'),
    path('save/', air.save, name='save'),
    path('admin/', admin.site.urls),
    path('user/info',user.info,name='info'),
    path('user/delete',user.delete,name='delete'),
    path('user/list',user.list,name='list'),
    path('user/login',user.login,name='login'),#log
    path('user/registry',user.save,name='registry'),#log
    path('user/page',user.page,name='pag'),#log
    path('user/update',user.update,name='update'),#log
    path('air/info',air.info,name='info'),#detail
    path('air/delete',air.delete,name='delete'),#delete
    path('air/list',air.list,name='list'),#search all
    path('air/save',air.save,name='save'),#add
    path('air/update',air.update,name='update'),#modify
    path('air/page',air.page,name='pag'),#search page
    path('flight/info',flight.info,name='info'),#detail
    path('air/info1',air.info1,name='info1'),#detail
    path('flight/delete',flight.delete,name='delete'),#delete
    path('flight/list',flight.list,name='list'),#search all
    path('flight/save',flight.save,name='save'),#add
    path('flight/update',flight.update,name='update'),#edit
    path('flight/page',flight.page,name='pag'),#search page
    path('flight/page1',flight.page1,name='pag1'),#sear

]
