from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='home'),
	url(r'^about',views.about,name='about'),
	url(r'^service$',views.service,name='service'),
	url(r'^contact$',views.contact,name='contact'),
	url(r'^login',views.loginUser,name='login'),
	url(r'^logout',views.logoutUser,name='logout'),

]
