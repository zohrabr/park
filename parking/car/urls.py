 
from django.conf.urls import  patterns, url
from car import views



urlpatterns=patterns('', 
	url(r'^inscription/$', views.register , name='inscription'),# create account
	url(r'^merci/$', views.merci , name='merci'), #apres ajout du parking
	url(r'^$', views.accueil , name='accueil'), #home page
	url(r'^login/$', views.user_login , name='login'),
	url(r'^logout/$', views.user_logout , name='logout'),
	url(r'^add_parking/$', views.add_parking , name='ajout'), #parking owner --> add parking
)
