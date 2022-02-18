from django.shortcuts import render
from .models import*

def Index(requests):
	name_product = Product.objects.filter(new=True)
	reted = Product.objects.filter(reting__gte=3, reting__lte=4)
def Blog(requests):
	return

