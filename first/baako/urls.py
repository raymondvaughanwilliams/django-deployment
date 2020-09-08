from django.conf.urls import url
from baako import views


urlpatterns =[
url(r'^$',views.index,name='index'),
url(r'^$',views.jitsi,name='jitsi'),

]
