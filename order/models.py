from django.db import models
from user.models import User
from merch.models import Merch

class Order(models.Model):
    class PaymentMethod(models.TextChoices):
        GCASH = 'gcash'
        BANK_TRANSFER = 'bank_transfer'

    class OrderStatus(models.TextChoices):
        PENDING = 'pending'
        PAID = 'paid'
        DELIVERED = 'delivered'
        CANCELLED = 'cancelled'

    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255, choices=PaymentMethod.choices)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_paid = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    
    def __str__(self):
        return f"Order {self.id} - {self.buyer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    merch = models.ForeignKey(Merch, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"OrderItem {self.id} - {self.merch.name}"
