from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	name = models.CharField(max_length=50)
	price = models.IntegerField()
	def __unicode__(self):
		return self.name

class Customer(models.Model):
	user = models.OneToOneField(User)
	products = models.ManyToManyField(Product, through='Buyings')
	def __unicode__(self):
		return self.user.username

class Buyings(models.Model):
	customer = models.ForeignKey(Customer)
	product = models.ForeignKey(Product)
	amount = models.IntegerField(default=0)