from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.models import User

from models import Customer, Product

#TODO: remove hardcode from urls!!!

#TODO: I think, we can do it without this method. We need to check this
def index(request):
	return render(request, 'bytovuhaApp/index.html')

#TODO: I think, we can do it without this method. We need to check this
def login_action(request):
	if request.POST.has_key('username') and request.POST.has_key('pass'):
		user = authenticate(username=request.POST['username'], password=request.POST['pass'])
		if user is not None:
		    if user.is_active:
		    	login(request, user)
		    	return render(request, 'bytovuhaApp/index.html')
		    else:
	    		context = {'message': 'User '}
		else:
			context = {'message': "The username and password were incorrect."}

		return render(request, 'bytovuhaApp/login.html', context)
	else:
		return render(request, 'bytovuhaApp/login.html')

def logout_action(request):
	logout(request)
	return redirect_to_login("/")

def show_basket(request):
	products = User.objects.get(id = request.user.id).customer.products.all()	
	context = {'products': products, 'heading': 'Your basket'}
	return render(request, 'bytovuhaApp/basket.html', context)

def add_to_basket(request, product_id):
	if request.user.is_authenticated():
		product = get_object_or_404(Product, id=product_id)
		User.objects.get(id = request.user.id).customer.products.add(product)
		return redirect('all_products/')
	else:
		# TODO: change to normal next url
		return redirect_to_login("/")

def remove_product_from_basket(request, product_id):
	if request.user.is_authenticated():
		product = get_object_or_404(Product, id=product_id)
		User.objects.get(id = request.user.id).customer.products.remove(product)
		return redirect('basket/')
	else:
		# TODO: change to normal next url
		return redirect_to_login("/")	

def pay_for_products(request):
	if request.user.is_authenticated():
		User.objects.get(id = request.user.id).customer.products.clear()
		return render(request, 'bytovuhaApp/thank_you.html')
	else:
		# TODO: change to normal next url
		return redirect_to_login("/")	

def all_products(request):
	products = get_list_or_404(Product)
	context = {'products': products, 'heading': "All our products"}
	return render(request, 'bytovuhaApp/products_list.html', context)

def product(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	return render(request, 'bytovuhaApp/product_description.html', {'product': product})
