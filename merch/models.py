from django.db import models


class MerchType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Merch(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)
    merch_type = models.ForeignKey(MerchType, on_delete=models.CASCADE, related_name='merches')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MerchSize(models.Model):
    merch_type = models.ForeignKey(MerchType, on_delete=models.CASCADE, related_name='sizes')
    name = models.CharField(max_length=255)
    description = models.TextField( blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.merch_type.name})"


class MerchVariant(models.Model):
    merch = models.ForeignKey(Merch, on_delete=models.CASCADE, related_name='variants')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True)
    variant = models.CharField(max_length=255)
    is_bestseller = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    is_limited = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)
    size = models.ForeignKey(MerchSize, on_delete=models.CASCADE, related_name='variants')
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.merch.name} - {self.variant} - {self.size.name}"


class Bundle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True)
    merch = models.ManyToManyField(Merch, related_name='bundles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
