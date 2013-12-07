# encoding=utf-8

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.models import User
from django.db import IntegrityError

from models import Customer, Product, Buyings

#TODO: remove hardcode from urls!!!

#Dirty hack
def helper_add_to_basket(customer, product):
	amount = customer.products.filter(id=product.id).count() + 1
	Buyings.objects.filter(customer=customer, product=product).delete()	

	buying = Buyings(customer=customer, product=product, amount=amount)
	buying.save()

def helper_remove_from_basket(customer, product):
	byings_to_delete = Buyings.objects.filter(customer=customer, product=product)	
	byings_to_delete.delete()

#TODO: I think, we can do it without this method. We need to check this
def index(request):	
	return render(request, 'bytovuhaApp/index.html')

#TODO: to think about decorator for login_action and register
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

def register(request):
	if request.POST.has_key('username') and request.POST.has_key('pass'):
		try:
			user = User.objects.create_user(request.POST['username'], request.POST['email'])
		except IntegrityError:
			return render(request, 'bytovuhaApp/registration.html', {'message':'', 'alert':True})
		user.set_password(request.POST['pass'])
		user.save()

		customer = Customer(user=user)
		customer.save()
		
		send_mail("Регистрация на Бытовуха.by", "Добро пожаловать в увлекательный мир Бытовухи!", request.POST['email'])
		
		return redirect("/login/")
	else:
		return render(request, 'bytovuhaApp/registration.html', {'message':'Регистрация', 'alert':False})

def logout_action(request):
	logout(request)
	return redirect("/")

def contacts(request):
	return render(request, 'bytovuhaApp/contacts.html')

def show_basket(request):
	if request.user.is_authenticated():
		customer = User.objects.get(id = request.user.id).customer
		buyings = Buyings.objects.select_related().filter(customer=customer)
		#products = User.objects.get(id = request.user.id).customer.products.all()	

		context = {'buyings': map(lambda x: (x.product.name, x.product.price, x.amount, x.product.id), buyings), 'heading': 'Корзина'}
		return render(request, 'bytovuhaApp/basket.html', context)
	else: 
		# TODO: change to normal next url
		return redirect_to_login("/")

def add_to_basket(request, product_id):
	if request.user.is_authenticated():
		product = get_object_or_404(Product, id=product_id)
		customer = User.objects.get(id = request.user.id).customer
		helper_add_to_basket(customer, product)
		return redirect('products_for_category//0')
	else:
		# TODO: change to normal next url
		return redirect_to_login("/")

def remove_product_from_basket(request, product_id):
	if request.user.is_authenticated():
		product = get_object_or_404(Product, id=product_id)
		customer = User.objects.get(id = request.user.id).customer
		helper_remove_from_basket(customer, product)
		return redirect('basket/')
	else:
		# TODO: change to normal next url
		return redirect_to_login("/")	

def pay_for_products(request):
	if request.user.is_authenticated():
		User.objects.get(id = request.user.id).customer.products.clear()
		send_mail("Спасибо за покупку", "Бытовуха.by поздравляет вас с покупкой!", User.objects.get(id = request.user.id).email)
		return render(request, 'bytovuhaApp/thank_you.html')
	else:
		# TODO: change to normal next url
		return redirect_to_login("/")	

def products_for_category(request, category, page):

	if len(category) == 0:
		products = Product.objects.filter()
		heading=u"Все наши продукты"
	else:
		for cat in Product.CATEGORIES:
			if cat[0]==category:
				heading=cat[1]
		products = Product.objects.filter(category=category)

	page = int(page)
	if page < 0:
		page = 0

	prev_page = page-1
	if prev_page<0:
		prev_page=0

	context = {'products': products[page*5:(page+1)*5], 'heading': heading, 'category': category, 'prev_page':prev_page, 'next_page': page+1}
	return render(request, 'bytovuhaApp/products_list.html', context)

def product(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	return render(request, 'bytovuhaApp/product_description.html', {'product': product})

def personalpage(request):
	if request.user.is_authenticated():
		customer = User.objects.get(id = request.user.id).customer
		#context = {'products': , 'heading': "All our products", 'category': category, 'prev_page':prev_page, 'next_page': page+1}
		return render(request, 'bytovuhaApp/personal_page.html', {'name': customer.name})
	else:
		return redirect_to_login("/")

#Debug
def send_mail(subject, text, to):
	from django.core.mail import send_mail
	send_mail(subject, text, "bytovuhaBy@gmail.com", [to], fail_silently=False)
