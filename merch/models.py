from django.db import models

class Merch(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class MerchVariant(models.Model):
    class MerchType(models.TextChoices):
        SHIRT = 'shirt'
        HOODIE = 'hoodie'
        CAP = 'cap'
        STICKER = 'sticker'
        OTHER = 'other'
        
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    type = models.CharField(max_length=255, choices=MerchType.choices, default=MerchType.OTHER)
    variant = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    quantity = models.IntegerField()
    merch = models.ForeignKey(Merch, on_delete=models.CASCADE)
    is_limited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.merch.name} - {self.variant} - {self.size}"
    
class Bundle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    merch = models.ManyToManyField(Merch)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
