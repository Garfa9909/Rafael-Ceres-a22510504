from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(max_length = 100)
    number = models.IntegerField()
    postal_code = models.IntegerField()
    def __str__(self):
        return f"{self.street}, {self.number}, {self.postal_code}"

class Product(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "products")
    def __str__(self):
        return self.name      

class User(models.Model):
    name = models.CharField(max_length = 100)
    address = models.OneToOneField(Address, on_delete = models.CASCADE, related_name = "user")
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "orders")

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "order_items")
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = "order_items")
    amount = models.IntegerField()
    def __str__(self):
        return f"{self.product}: {self.amount}"
