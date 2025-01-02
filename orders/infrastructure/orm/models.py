from django.db import models

from shop.infrastructure.orm.models import Product
from client.infrastructure.orm.models import Address
from account.infrastructure.orm.models import CustomUser


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'), 
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(CustomUser, related_name='orders', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')

    class Meta:
        ordering = ('-created_at',)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        return f"Order #{self.id} - {self.status}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity