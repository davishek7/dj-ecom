from django.contrib import admin
from .models import Category,Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','price','in_stock','created','updated']
    list_filter=['in_stock','is_active']
    list_editable=['price','in_stock']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)

