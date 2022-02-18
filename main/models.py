from distutils.command.upload import upload
from django.db import models

class About(models.Model):
	img = models.ImageField(upload_to='About/')
	phone = models.CharField(max_length=255)
	phone2 = models.CharField(max_length=255)
	email = models.EmailField()
	text = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	map = models.CharField(max_length=255)

class Slider(models.Model):
	img = img = models.ImageField(upload_to='Slider/')
	title = models.CharField(max_length=255)
	text = models.CharField(max_length=255)

class Category(models.Model):
	name = models.CharField(max_length=255)

class Info(models.Model):
	img = models.ImageField(upload_to='Slider/')
	title = models.CharField(max_length=255)
	text = models.CharField(max_length=255)

class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	describtion = models.CharField(max_length=255)
	info = models.ManyToManyField(Info)
	img1 = models.ImageField(upload_to='Product')
	img2 = models.ImageField(upload_to='Product', null=True, blank=True)
	img3 = models.ImageField(upload_to='Product', null=True, blank=True)
	img4 = models.ImageField(upload_to='Product', null=True, blank=True)
	new = models.BooleanField(default=True)

class Ad(models.Model):
	img = models.ImageField(upload_to='Advertisement/')
	title = models.CharField(max_length=255)
	text = models.CharField(max_length=255)

class Feedback(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	subject = models.CharField(max_length=255)
	msg = models.CharField(max_length=255)