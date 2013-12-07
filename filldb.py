from bytovuhaApp.models import *

from django.contrib.auth.models import User

#user = User.objects.create_user('Cristopher Nolan')
#user.set_password('The Dark Knight')
#user.save()

#customer = Customer(user=user)
#customer.save()

user = User.objects.create_user('Andrew')
user.set_password('111111')
user.save()

customer = Customer(user=user)
customer.save()

user = User.objects.create_user('Nastya')
user.set_password('111111')
user.save()

customer = Customer(user=user)
customer.save()


product = Product(name="Washing machine LG", price=1000, category='Washing_machines', image_url='/static/washMach.jpg')
product.save()

product = Product(name="Washing machine Samsung", price=1300, category='Washing_machines', image_url='/static/washMachSams.jpg')
product.save()

product = Product(name="Washing machine Zvezda", price=1300, category='Washing_machines', image_url='/static/washMachZvezda.jpg')
product.save()

product = Product(name="Acer a35", price=320, category="Electronics", image_url="/static/acer.jpg")
product.save()

product = Product(name="Asus 345", price=420, category="Electronics", image_url="/static/asus.jpg")
product.save()

product = Product(name="Dell Latitude 345", price=1200, category="Electronics", image_url="/static/laptop.jpg")
product.save()

product = Product(name="Pot number one", price=12, category="Pots", image_url="/static/teapot.jpg")
product.save()

product = Product(name="Pot number two", price=22, category="Pots", image_url="/static/teapot_white.jpg")
product.save()

product = Product(name="Toster number one", price=22, category="Tosters", image_url="/static/toster.jpg")
product.save()

product = Product(name="Toster white", price=22, category="Tosters", image_url="/static/toster_white.jpg")
product.save()
