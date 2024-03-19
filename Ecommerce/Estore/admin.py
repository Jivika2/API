from django.contrib import admin

# Register your models here.
from .models import Category, Book, Product
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Product)
#admin.site.register(Cart)