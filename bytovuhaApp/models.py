from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=50)
	price = models.IntegerField()
	def __unicode__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=50)
	products = models.ManyToManyField(Product)
	def __unicode__(self):
		return self.name
