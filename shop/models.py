from django.db import models
from django.conf import settings
from django.urls import reverse
from PIL import Image

class ProductManager(models.Manager):
	def get_queryset(self):
		return super(ProductManager,self).get_queryset().filter(is_active=True)


class Category(models.Model):
	name=models.CharField(max_length=200,blank=True,null=True,db_index=True)
	slug=models.SlugField(max_length=200,unique=True,blank=True,null=True)

	class Meta:
		verbose_name_plural = 'categories'

	def get_absolute_url(self):
		return reverse('shop:category-list', args=[self.slug])

	def __str__(self):
		return self.name


class Product(models.Model):
	category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE,blank=True,null=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator', blank=True, null=True)
	title=models.CharField(max_length=200,blank=True,null=True)
	author=models.CharField(max_length=200,default='admin',blank=True,null=True)
	slug=models.SlugField(max_length=200,unique=True,blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	image=models.ImageField(upload_to='thumbnails/')
	price=models.DecimalField(max_digits=10,decimal_places=2)
	in_stock=models.BooleanField(default=True)
	is_active=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	objects = models.Manager()
	products = ProductManager()

	class Meta:
		ordering=['-created']
	
	def get_absolute_url(self):
		return reverse('shop:product-detail',args=[self.slug])

	def __str__(self):
		return self.title

