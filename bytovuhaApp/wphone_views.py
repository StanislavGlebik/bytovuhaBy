# encoding=utf-8

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
import csv
import views

from django.contrib.auth.models import User
from models import Customer, Product, Buyings

def login_action(request, username, password):

	try:
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(str(user.customer.id)+'<br>'+username+'<br>'+password)
			else:
				return HttpResponse(str(-1)+'<br>'+username+'<br>'+password)
		else:
			return HttpResponse(str(-1)+'<br>'+username+'<br>'+password)
	except Exception:
		return HttpResponse(str(-1)+'<br>'+username+'<br>'+password)

def wpproducts(request):
	products = Product.objects.filter()
	resstr = ''
	splitter = '|'
	for product in products:
		resstr = resstr + str(product.id) + splitter
		resstr = resstr + product.name + splitter
		resstr = resstr + str(product.price) + splitter
		resstr = resstr + product.category + splitter
		resstr = resstr + product.image_url + splitter
		resstr = resstr + product.description + splitter
		resstr = resstr + '<br>'
		
	return HttpResponse(resstr)
	
def wpbuyings(request):
	buyings = Buyings.objects.filter()
	resstr = ''
	splitter = '|'
	for b in buyings:
		resstr = resstr + str(b.customer_id) + splitter
		resstr = resstr + str(b.product_id) + splitter
		resstr = resstr + str(b.amount) + splitter
		resstr = resstr + '<br>'
	return HttpResponse(resstr)	
	
def wpbuy(request, customerid, productid):
	product = get_object_or_404(Product, id=productid)
	customer = get_object_or_404(Customer, id=customerid)
	views.helper_add_to_basket(customer, product)
	return HttpResponse('')
	
def wppay(request, customerid):
	customer = get_object_or_404(Customer, id=customerid).products.clear()
	views.send_mail("Спасибо за покупку", "Бытовуха.by поздравляет вас с покупкой!", User.objects.get(id = request.user.id).email)
	return HttpResponse('')