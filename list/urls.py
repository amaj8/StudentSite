from django.conf.urls import url
from . import views

app_name = 'list'

urlpatterns =[
    url(r'^$',views.HomeView,name='home'),
    url(r'^record/$',views.RecordView,name='record'),
]