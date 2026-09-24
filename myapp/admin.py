from django.contrib import admin
# from .models import Products
from .models import *

admin.site.register(Products)
admin.site.register(UserCart)
admin.site.register(CartItems)
# Register your models here.
