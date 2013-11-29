from django.conf.urls import patterns, url
from bytovuhaApp import views

urlpatterns = patterns("",
	url(r'^$', views.index),
	url(r'products/', views.all_products),
	url(r'product/(?P<product_id>\d+)/$', views.product),
	url(r'users/', views.all_users),
	url(r'user/(?P<user_id>\d+)/name/$', views.user),		
)