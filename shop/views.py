from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Product, Category


class ProductListView(ListView):
	model = Product
	template_name='index.html'
	context_object_name='products'
	paginate_by=8

	def get_queryset(self):
		return Product.products.all()

class ProductDetailView(DetailView):
	model=Product
	template_name='shop/product.html'
	context_object_name='product'


class CategoryProductView(ListView):
	model = Category
	template_name = 'shop/category.html'
	paginate_by=8

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
		context["category"] = category
		context["products"] = Product.products.filter(category=category) 
		return context
	
	

	
