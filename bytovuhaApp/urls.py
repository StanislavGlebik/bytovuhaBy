from django.conf.urls import patterns, url
from bytovuhaApp import views

urlpatterns = patterns("",
	url(r'^$', views.index),
	url(r'login/$', views.login_action),
	url(r'logout/$', views.logout_action),
	url(r'basket/$', views.show_basket),		
	url(r'pay/$', views.pay_for_products),
	url(r'buy/(?P<product_id>\d+)/$', views.add_to_basket, name='buy'),	
	url(r'remove/(?P<product_id>\d+)/$', views.remove_product_from_basket, name='remove'),		
	url(r'all_products/', views.all_products),
	url(r'product/(?P<product_id>\d+)/$', views.product, name="product_description"),
)