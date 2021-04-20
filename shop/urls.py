from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('products/<slug:slug>/',views.ProductDetailView.as_view(),name='product-detail'),
    path('category/<slug:category_slug>/',views.CategoryProductView.as_view(),name='category-list'),
]
