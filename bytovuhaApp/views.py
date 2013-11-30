from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

from models import User, Product

def index(request):
	return render(request, 'bytovuhaApp/index.html')

def user(request, user_id):
	user = get_object_or_404(User, id=user_id)
	return HttpResponse("user {0}".format(user.name))

def products_for_user(request, user_id):
	user = get_object_or_404(User, id=user_id)
	products = user.products.all()
	context = {'products': products, 'heading': "Your products, " + user.name}
	return render(request, 'bytovuhaApp/products_list.html', context)

def all_users(request):
	users = get_list_or_404(User)
	return HttpResponse(" ".join(map(lambda user: user.name, users)))

def all_products(request):
	products = get_list_or_404(Product)
	context = {'products': products, 'heading': "All our products"}
	return render(request, 'bytovuhaApp/products_list.html', context)

def product(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	return HttpResponse(u"Product: {0} Price: {1}".format(product.name, product.price))