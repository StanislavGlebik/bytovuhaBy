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


product = Product(name="Стиральная машина LG W201", price=1000, category='Washing_machines', image_url='/static/washMach.jpg', description='Автоматическая стиральная машина, фронтальная загрузка 6 кг, отжим 1000 об/мин, глубина 44 см, энергопотребление A+, прямой привод, защита от протечек, 13 программ')
product.save()

product = Product(name="Стиральная машина Samsung R861", price=1300, category='Washing_machines', image_url='/static/washMachSams.jpg', description='Автоматическая стиральная машина, фронтальная загрузка 6 кг, отжим 1200 об/мин, глубина 40 см, энергопотребление A+, защита от протечек, 12 программ')
product.save()

product = Product(name="Стиральная машина Zvezda", price=1300, category='Washing_machines', image_url='/static/washMachZvezda.jpg', description='Автоматическая стиральная машина, фронтальная загрузка 5 кг, отжим 800 об/мин, глубина 40 см, энергопотребление A, 15 программ')
product.save()

product = Product(name="Ноутбук Acer a35", price=320, category="Electronics", image_url="/static/acer.jpg", description='Бюджетная универсальная модель с 15.6" экраном. Построена на платформе Intel, снабжена глянцевым экраном, стандартным аккумулятором, базовым набором портов. Имеет классический универсальный дизайн с комбинацией глянца и зернистого пластика.')
product.save()

product = Product(name="Ноутбук Asus 345", price=420, category="Electronics", image_url="/static/asus.jpg", description='Универсальный аппарат от компании Asus потребительского класса. Аппарат построен на базе процессора Intel третьего поколения, имеет стандартный набор встроенных модулей и разъемов. В зависимости от модели, может поставляться как в плаcтиковом, так и в металлическом корпусе.')
product.save()

product = Product(name="Ноутбук Dell Latitude 345", price=1200, category="Electronics", image_url="/static/laptop.jpg", description='Модель начального уровня ноутбуков Dell 2013 года, предназначенная для ежедневного использования. Ноутбук построен на платформе Intel Chief River, оснащен стандартной матрицей 15.6" с разрешением 1366x768 точек, встроенной графикой, обыкновенным набором портов, за исключением VGA. Выпускается в черном цветовом решении.')
product.save()

product = Product(name="Чайник Vitek W2", price=12, category="Pots", image_url="/static/teapot.jpg", description='2800 Вт, 1.3 л, подставка: с возможность вращения, материал корпуса: керамика')
product.save()

product = Product(name="Чайник Bosch B5", price=22, category="Pots", image_url="/static/teapot_white.jpg", description='2400 Вт, 1.5 л, подставка: с возможность вращения, материал корпуса: пластик, металл')
product.save()

product = Product(name="Тостер Vitek T6", price=22, category="Tosters", image_url="/static/toster.jpg", description='Тостер, мощность: 850 Вт, материал корпуса: пластик и металл, количество тостов: 2')
product.save()

product = Product(name="Тостер Shmoster", price=22, category="Tosters", image_url="/static/toster_white.jpg", description='Тостер, мощность: 750 Вт, материал корпуса: пластик, количество тостов: 2 ')
product.save()
