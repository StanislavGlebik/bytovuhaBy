#encoding=utf-8

from bytovuhaApp.models import *

from django.contrib.auth.models import User

#user = User.objects.create_user('Cristopher Nolan')
#user.set_password('The Dark Knight')
#user.save()

#customer = Customer(user=user)
#customer.save()

user = User.objects.create_user('Andrew', 'andrew414414@gmail.com')
user.set_password('111111')
user.save()

customer = Customer(user=user)
customer.save()

user = User.objects.create_user('Nastya', 'anastasiya.koloskova@gmail.com')
user.set_password('111111')
user.save()

customer = Customer(user=user)
customer.save()


product = Product(name="Стиральная машина LG W201", price=1000, category='Washing_machines', image_url='/static/washMach.jpg')
product.save()

product = Product(name="Стиральная машина Samsung R861", price=1300, category='Washing_machines', image_url='/static/washMachSams.jpg')
product.save()

product = Product(name="Стиральная машина Zvezda", price=1300, category='Washing_machines', image_url='/static/washMachZvezda.jpg')
product.save()

product = Product(name="Ноутбук Acer a35", price=320, category="Electronics", image_url="/static/acer.jpg")
product.save()

product = Product(name="Ноутбук Asus 345", price=420, category="Electronics", image_url="/static/asus.jpg")
product.save()

product = Product(name="Ноутбук Dell Latitude 345", price=1200, category="Electronics", image_url="/static/laptop.jpg")
product.save()

product = Product(name="Чайник Vitek W2", price=12, category="Pots", image_url="/static/teapot.jpg")
product.save()

product = Product(name="Чайник Bosch B5", price=22, category="Pots", image_url="/static/teapot_white.jpg")
product.save()

product = Product(name="Тостер Vitek T6", price=22, category="Tosters", image_url="/static/toster.jpg")
product.save()

product = Product(name="Тостер Shmoster", price=22, category="Tosters", image_url="/static/toster_white.jpg")
product.save()
