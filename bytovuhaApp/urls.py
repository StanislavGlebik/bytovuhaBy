from django.conf.urls import patterns, url
from bytovuhaApp import views
from bytovuhaApp import wphone_views

urlpatterns = patterns("",
	url(r'^$', views.index),
	url(r'login/$', views.login_action),
	url(r'logout/$', views.logout_action),
	url(r'basket/$', views.show_basket),		
	url(r'contacts/$', views.contacts),
	url(r'send/$', views.send_mail),	
	url(r'register/$', views.register),	
	url(r'wplogin/(?P<username>\w*)/(?P<password>\w*)', wphone_views.login_action),
	url(r'wpproducts/$', wphone_views.wpproducts),
	url(r'wpbuyings/$', wphone_views.wpbuyings),
	url(r'wpbuy/(?P<customerid>\d+)/(?P<productid>\d+)', wphone_views.wpbuy),
	url(r'wppay/(?P<customerid>\d+)', wphone_views.wppay),
	url(r'products_for_category/(?P<category>\w*)/(?P<page>\d+)/$', views.products_for_category, name='products_for_category'),
	url(r'pay/$', views.pay_for_products),
	url(r'buy/(?P<product_id>\d+)/$', views.add_to_basket, name='buy'),	
	url(r'remove/(?P<product_id>\d+)/$', views.remove_product_from_basket, name='remove'),		
	url(r'product/(?P<product_id>\d+)/$', views.product, name="product_description"),
)