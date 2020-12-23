from django.contrib import admin
from .models import Product, Category

# Registered Category and Product Models for Admin View
admin.site.register(Product)
admin.site.register(Category)