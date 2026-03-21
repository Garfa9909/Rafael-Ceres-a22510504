from django.contrib import admin

from .models import Category
from .models import Address
from .models import Product
from .models import User
from .models import Order
from .models import OrderItem

admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)
